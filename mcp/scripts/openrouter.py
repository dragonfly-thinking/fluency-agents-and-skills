#!/usr/bin/env python3
"""
openrouter.py — one key, many superpowers.

A tiny, dependency-free engine so an AI agent can use a single OpenRouter API
key to generate images and run live, cited web search (including X/social).
Built for the Dragonfly AI Fluency course. No pip installs required — only the
Python standard library.

Commands:
    python3 openrouter.py check
    python3 openrouter.py image  "<prompt>" [-o out.png] [--aspect 16:9]
    python3 openrouter.py search "<question>" [--model perplexity/sonar] [--max-results 4]
    python3 openrouter.py xsearch "<question>" [--handles a,b] [--from 2026-01-01]

Key lookup order:
    1. $OPENROUTER_API_KEY
    2. ~/.fluency/openrouter.key   (plain text file, just the key)
    3. macOS Keychain item "My OpenRouter Key"

Design notes — all four are deliberate, and the reason is given inline:
  * Always sends an explicit max_tokens — OpenRouter reserves credit against
    max_tokens before running, so a huge default 402s on a low balance.
  * 402 (out of credit) is a HARD STOP, never retried — retrying just burns money.
  * Transient errors (429/500/502/503/408) get a short jittered backoff retry.
  * Model IDs are constants up top so a provider rename is a one-line edit.
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://openrouter.ai/api/v1"

# --- Model constants (preview slugs drift; change here, not inline) ----------
IMAGE_MODEL = "google/gemini-2.5-flash-image"     # "Nano Banana" (tested working)
SEARCH_MODEL = "perplexity/sonar"                  # native cited web search
X_MODEL = "~x-ai/grok-latest"                      # tilde-alias: auto-tracks current Grok
# Why the alias only here: the X lane wants "whatever Grok is current", and that
# family deprecates versions quickly, so an alias is the stable choice. The other
# two stay PINNED on purpose: neither has a ~latest alias, and both are
# price-sensitive, so silently jumping a generation would change what a call costs.
# Models re-checked against openrouter.ai on 2026-09-01 — perplexity/sonar and
# google/gemini-2.5-flash-image both still live; the grok tilde-alias resolves.

KEY_FILE = Path.home() / ".fluency" / "openrouter.key"
ATTRIB = {  # attribution only — affects OpenRouter rankings, nothing functional
    "HTTP-Referer": "https://dragonflythinking.com",
    "X-Title": "AI Fluency Course",
}
RETRYABLE = {408, 429, 500, 502, 503}


# --- key + http --------------------------------------------------------------

def _clean_key(raw):
    # Strip whitespace AND surrounding quotes: an agent writing the key with
    # echo "'$KEY'" produces a quoted file, and the resulting 401 is baffling.
    return raw.strip().strip("'\"").strip()


def find_key():
    env = os.environ.get("OPENROUTER_API_KEY")
    if env:
        return _clean_key(env)
    if KEY_FILE.exists():
        from_file = _clean_key(KEY_FILE.read_text())
        if from_file:
            return from_file
    try:
        out = subprocess.run(
            ["security", "find-generic-password", "-s", "My OpenRouter Key", "-w"],
            capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return None


def die_no_key():
    sys.exit(
        "No OpenRouter key found.\n\n"
        "Set one up:\n"
        "  1. Get a key at https://openrouter.ai/keys (starts with 'sk-or-v1-')\n"
        "  2. Add a few dollars at https://openrouter.ai/settings/credits and\n"
        "     set a SPEND LIMIT on the key (so nothing can ever overspend).\n"
        "  3. Save it:  mkdir -p ~/.fluency && "
        "printf %s 'sk-or-...' > ~/.fluency/openrouter.key && chmod 600 ~/.fluency/openrouter.key\n\n"
        'If you are talking to an AI agent, just say: '
        '"Save my OpenRouter key sk-or-... to ~/.fluency/openrouter.key".'
    )


def _retry_wait(retry_after, attempt):
    """Seconds to wait before a retry.

    Retry-After is allowed to be either a number of seconds or an HTTP-date
    (RFC 9110), and float() on the date form crashes. It can also be very large
    — an honest '3600' would otherwise park the terminal for an hour per retry
    with nothing on screen — so the wait is clamped to something a person will
    sit through.
    """
    wait = 1.5 ** attempt + 0.3 * attempt
    if retry_after:
        try:
            wait = float(retry_after)
        except ValueError:
            try:
                from email.utils import parsedate_to_datetime
                from datetime import datetime, timezone
                target = parsedate_to_datetime(retry_after)
                if target.tzinfo is None:
                    target = target.replace(tzinfo=timezone.utc)
                wait = (target - datetime.now(timezone.utc)).total_seconds()
            except Exception:
                pass
    return max(1.0, min(wait, 20.0))


def _payload_error(r):
    """OpenRouter can return an error object with HTTP 200. Surface it plainly
    instead of letting a KeyError on 'choices' surface as a traceback."""
    err = r.get("error")
    if isinstance(err, dict) and err.get("message"):
        sys.exit(f"OpenRouter returned an error: {err['message']}")
    if not r.get("choices"):
        sys.exit("OpenRouter returned no result. Try again, or rephrase the request.")
    return r


def request(path, key, payload=None, method="GET"):
    data = json.dumps(payload).encode() if payload is not None else None
    headers = {"Authorization": f"Bearer {key}"}
    if data is not None:
        headers["Content-Type"] = "application/json"
        headers.update(ATTRIB)
    req = urllib.request.Request(f"{API}{path}", data=data, headers=headers, method=method)

    last_err = None
    for attempt in range(4):  # 1 try + 3 retries on transient failures
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 402:
                sys.exit("Out of OpenRouter credit — or this key's spend cap is "
                         "used up. Check both at https://openrouter.ai/settings/credits "
                         "and https://openrouter.ai/keys, then try again. "
                         "(Tip: an image is ~$0.04, a web search ~$0.005, "
                         "an X search ~$0.015.)")
            if e.code in (401, 403):
                sys.exit(
                    f"OpenRouter didn't accept the key ({e.code}). Note that "
                    f"\"User not found\" is their wording for an invalid key — it does "
                    f"NOT mean your account is gone. Check the key starts with "
                    f"'sk-or-v1-' and has no quotes or spaces around it; recreate it "
                    f"at https://openrouter.ai/keys if unsure.\n\nDetail: {body[:200]}"
                )
            if e.code in RETRYABLE and attempt < 3:
                wait = _retry_wait(e.headers.get("Retry-After"), attempt)
                print(f"Rate limited or busy; retrying in {wait:.0f}s…", file=sys.stderr)
                time.sleep(wait)
                last_err = f"{e.code}: {body[:160]}"
                continue
            sys.exit(f"OpenRouter error {e.code}: {body[:300]}")
        except urllib.error.URLError as e:
            if attempt < 3:
                time.sleep(1.5 ** attempt)
                last_err = str(e)
                continue
            sys.exit(f"Network error reaching OpenRouter: {e}")
    sys.exit(f"OpenRouter request failed after retries: {last_err}")


# --- commands ----------------------------------------------------------------

def cmd_check(key, _):
    d = request("/credits", key)["data"]
    remaining = d["total_credits"] - d["total_usage"]
    print(f"Key OK. Account credit remaining: ${remaining:.2f} "
          f"(${d['total_usage']:.2f} used of ${d['total_credits']:.2f}).")
    if remaining < 1:
        print("⚠️  Low credit — top up at https://openrouter.ai/settings/credits")

    # The account balance is not the only thing that can stop a call: a per-key
    # spend cap runs out independently, and hitting it also 402s. Reporting only
    # the account balance made "Credit remaining: $10.00" appear next to calls
    # that were already being refused.
    try:
        k = request("/key", key).get("data") or {}
    except SystemExit:
        return
    if k.get("limit") is not None:
        left = k.get("limit_remaining")
        reset = k.get("limit_reset")
        left_txt = f"${left:.2f}" if isinstance(left, (int, float)) else "unknown"
        print(f"This key's spend cap: {left_txt} left of ${k['limit']:.2f}"
              + (f", resets {reset}." if reset else " (no reset — a true ceiling)."))
        if reset:
            print("   Note: a cap that resets is not a ceiling. A $5 daily cap "
                  "allows ~$150/month. Prefer no reset.")
    else:
        print("This key has NO spend cap set. Your only limit is the pre-paid "
              "balance above — set a cap at https://openrouter.ai/keys")


def cmd_image(key, a):
    payload = {
        "model": IMAGE_MODEL,
        "messages": [{"role": "user", "content": a.prompt}],
        "modalities": ["image", "text"],
        "image_config": {"aspect_ratio": a.aspect},
        # OpenRouter reserves credit against max_tokens before running, so an
        # unbounded default can 402 on a low balance. This is the priciest
        # command, so it needs the bound most.
        "max_tokens": 4096,
    }
    r = _payload_error(request("/chat/completions", key, payload, "POST"))
    imgs = r["choices"][0]["message"].get("images") or []
    if not imgs:
        sys.exit("No image returned — try a more concrete prompt.")
    url = imgs[0].get("image_url", {}).get("url", "")
    out = a.out or "openrouter-image.png"
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    if url.startswith("data:"):
        Path(out).write_bytes(base64.b64decode(url.split(",", 1)[1]))
    elif url.startswith("http"):
        with urllib.request.urlopen(url, timeout=120) as resp:
            Path(out).write_bytes(resp.read())
    else:
        sys.exit("The image came back in a format this script doesn't recognise.")
    print(f"Saved image to {out}  ({a.aspect})")


def _render_search(r):
    _payload_error(r)
    msg = r["choices"][0]["message"]
    content = (msg.get("content") or "").strip()
    if not content:
        print("The model returned no answer — try rephrasing the question.")
    else:
        print(content)
    cites = msg.get("annotations") or []
    urls = []
    for c in cites:
        u = (c.get("url_citation") or {}).get("url")
        if u and u not in urls:
            urls.append(u)
    if urls:
        print("\nSources:")
        for i, u in enumerate(urls, 1):
            print(f"  [{i}] {u}")


def cmd_search(key, a):
    payload = {
        "model": a.model,
        "max_tokens": 1200,
        "messages": [{"role": "user",
                      "content": a.query + "\n\nAnswer concisely and cite source URLs."}],
    }
    # Non-native-search models need the web plugin turned on explicitly.
    if ":online" not in a.model and not a.model.startswith("perplexity/"):
        payload["plugins"] = [{"id": "web", "max_results": a.max_results}]
    elif a.model.startswith("perplexity/"):
        # Perplexity does its own search, so the `web` plugin (and its
        # max_results) doesn't apply to it. Map the intent onto the knob
        # Perplexity does have, so --max-results still means something here.
        payload["web_search_options"] = {
            "search_context_size": "low" if a.max_results <= 3
            else "medium" if a.max_results <= 8 else "high"
        }
    _render_search(request("/chat/completions", key, payload, "POST"))


def cmd_xsearch(key, a):
    xf = {}
    if a.handles:
        xf["allowed_x_handles"] = [h.strip().lstrip("@") for h in a.handles.split(",")][:10]
    if getattr(a, "from_date", None):
        xf["from_date"] = a.from_date
    if a.to_date:
        xf["to_date"] = a.to_date
    payload = {
        "model": X_MODEL,
        "max_tokens": 1200,
        "plugins": [{"id": "web", "max_results": a.max_results}],
        "messages": [{"role": "user",
                      "content": a.query + "\n\nSummarise what people are saying and cite the posts."}],
    }
    if xf:
        payload["x_search_filter"] = xf
    _render_search(request("/chat/completions", key, payload, "POST"))


def main():
    p = argparse.ArgumentParser(description="OpenRouter: one key, many superpowers.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("check", help="verify the key and show remaining credit")

    pi = sub.add_parser("image", help="generate an image")
    pi.add_argument("prompt")
    pi.add_argument("-o", "--out")
    pi.add_argument("--aspect", default="1:1", help="1:1, 16:9, 9:16, 4:3, 3:2 …")
    # --size is accepted for backwards compatibility but ignored: the image model
    # advertises aspect_ratio and n, not a size/resolution parameter, so sending
    # one changed nothing. Better a documented no-op than a knob that silently
    # does nothing.
    pi.add_argument("--size", default=None, help=argparse.SUPPRESS)

    ps = sub.add_parser("search", help="live cited web search")
    ps.add_argument("query")
    ps.add_argument("--model", default=SEARCH_MODEL)
    ps.add_argument("--max-results", type=int, default=4, dest="max_results")

    px = sub.add_parser("xsearch", help="X/social search via Grok")
    px.add_argument("query")
    px.add_argument("--handles", help="comma-separated handles to restrict to")
    px.add_argument("--from", dest="from_date", help="ISO date, e.g. 2026-01-01")
    px.add_argument("--to", dest="to_date", help="ISO date")
    px.add_argument("--max-results", type=int, default=6, dest="max_results")

    a = p.parse_args()
    key = find_key()
    if not key:
        die_no_key()
    {"check": cmd_check, "image": cmd_image,
     "search": cmd_search, "xsearch": cmd_xsearch}[a.cmd](key, a)


if __name__ == "__main__":
    main()
