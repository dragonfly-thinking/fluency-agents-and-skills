#!/usr/bin/env python3
"""
openrouter.py — one key, many superpowers.

A tiny, dependency-free engine so an AI agent can use a single OpenRouter API
key to generate images and run live, cited web search (including X/social).
Built for the Dragonfly AI Fluency course. No pip installs required — only the
Python standard library.

Commands:
    python3 openrouter.py check
    python3 openrouter.py image  "<prompt>" [-o out.png] [--aspect 16:9] [--size 2K]
    python3 openrouter.py search "<question>" [--model perplexity/sonar] [--max-results 4]
    python3 openrouter.py xsearch "<question>" [--handles a,b] [--from 2026-01-01]

Key lookup order:
    1. $OPENROUTER_API_KEY
    2. ~/.fluency/openrouter.key   (plain text file, just the key)
    3. macOS Keychain item "My OpenRouter Key"

Design notes (these are deliberate, see the course best-practices research):
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
X_MODEL = "x-ai/grok-4.3"                          # current Grok with x_search (4.1-fast deprecated)

KEY_FILE = Path.home() / ".fluency" / "openrouter.key"
ATTRIB = {  # attribution only — affects OpenRouter rankings, nothing functional
    "HTTP-Referer": "https://dragonflythinking.com",
    "X-Title": "AI Fluency Course",
}
RETRYABLE = {408, 429, 500, 502, 503}


# --- key + http --------------------------------------------------------------

def find_key():
    env = os.environ.get("OPENROUTER_API_KEY")
    if env:
        return env.strip()
    if KEY_FILE.exists() and KEY_FILE.read_text().strip():
        return KEY_FILE.read_text().strip()
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
        "  1. Get a key at https://openrouter.ai/keys (starts with 'sk-or-')\n"
        "  2. Add a few dollars at https://openrouter.ai/settings/credits and\n"
        "     set a SPEND LIMIT on the key (so nothing can ever overspend).\n"
        "  3. Save it:  mkdir -p ~/.fluency && "
        "printf %s 'sk-or-...' > ~/.fluency/openrouter.key && chmod 600 ~/.fluency/openrouter.key\n\n"
        'If you are talking to an AI agent, just say: '
        '"Save my OpenRouter key sk-or-... to ~/.fluency/openrouter.key".'
    )


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
                sys.exit("Out of OpenRouter credit. Top up at "
                         "https://openrouter.ai/settings/credits and try again. "
                         "(Tip: an image is ~$0.04, a search ~$0.001.)")
            if e.code in (401, 403):
                sys.exit(f"OpenRouter auth/permission error {e.code}: {body[:200]}")
            if e.code in RETRYABLE and attempt < 3:
                retry_after = e.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else (1.5 ** attempt + 0.3 * attempt)
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
    print(f"Key OK. Credit remaining: ${remaining:.2f} "
          f"(${d['total_usage']:.2f} used of ${d['total_credits']:.2f}).")
    if remaining < 1:
        print("⚠️  Low credit — top up at https://openrouter.ai/settings/credits")


def cmd_image(key, a):
    payload = {
        "model": IMAGE_MODEL,
        "messages": [{"role": "user", "content": a.prompt}],
        "modalities": ["image", "text"],
        "image_config": {"aspect_ratio": a.aspect, "image_size": a.size},
    }
    r = request("/chat/completions", key, payload, "POST")
    imgs = r["choices"][0]["message"].get("images") or []
    if not imgs:
        sys.exit("No image returned — try a more concrete prompt.")
    b64 = imgs[0]["image_url"]["url"].split(",", 1)[1]
    out = a.out or "openrouter-image.png"
    Path(out).write_bytes(base64.b64decode(b64))
    print(f"Saved image to {out}  ({a.aspect}, {a.size})")


def _render_search(r):
    msg = r["choices"][0]["message"]
    print((msg.get("content") or "").strip())
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
    pi.add_argument("--size", default="2K", help="0.5K, 1K, 2K, 4K")

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
