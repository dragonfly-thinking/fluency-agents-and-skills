# Add OpenRouter — for the agent

**You are an AI coding agent (Claude Code or Codex). The user wants to set up
OpenRouter — one API key that unlocks capabilities this kit can't do on its own:
image generation, live web search with real
citations, and X/social search (the premium lanes of the `web-searcher` agent).
The same key also unlocks PDF→Markdown conversion including true OCR — that one
isn't part of the engine script below; it's a separate recipe in
[`../guides/file-conversion.md`](../guides/file-conversion.md).**

One key powers all of it, pay-as-you-go, no extra subscriptions. Rough costs: an
image ≈ **$0.04**, a cited web search ≈ **$0.005**, an X/social search ≈
**$0.015**. So $10 is roughly 250 images or 1,800 searches — it lasts a long time.
*(Checked against `openrouter.ai/api/v1/models` on 2026-07-27.)*

Explain each step to the user in plain English before you run it, and ask them to
approve any command. Steps 1–3 happen in the user's browser — guide them; don't
try to do these yourself.

---

## Step 1 — Create the account (user, in browser)

Send the user to **https://openrouter.ai** to sign up (Google sign-in is fine).

## Step 2 — Add credit (user, in browser)

At **https://openrouter.ai/settings/credits**, add **$10**.

**Do not turn on auto top-up.** Pre-paid credit that never refills itself is the
single thing that makes this safe: $10 in means $10 is the most it can ever cost,
whatever goes wrong. Auto top-up removes that ceiling.

## Step 3 — Create the key, and cap it (user, in browser)

At **https://openrouter.ai/keys** → **Create Key** → name it (e.g. "Fluency") →
**set a credit limit of $10, with no reset** → copy it. It starts with
`sk-or-v1-`. Tell the user to treat it like a password.

> **The cap lives here, on the key — not on the credits page.** This is the step
> people skip, because it's a small optional-looking field on the create-key
> screen. Set it while you're there.
>
> Be accurate about what it buys, though: a cap set to **reset** daily or monthly
> is not a ceiling — a $5 daily cap permits about $150 a month. Choose *no reset*.
> The real backstop is the pre-paid balance from Step 2 with auto top-up off; the
> key cap is a second belt, not the only one.

## Step 4 — Install the engine and save the key (you)

The kit's OpenRouter capabilities run through one small, pre-tested engine script
that ships in this repo at `mcp/scripts/openrouter.py`. Put it in place:

Run this **from inside the cloned kit repo** (`cd` there first if you aren't):

```bash
mkdir -p ~/.fluency/bin
cp "$(git rev-parse --show-toplevel)/mcp/scripts/openrouter.py" ~/.fluency/bin/openrouter.py
```

Two deliberate choices there: `git rev-parse --show-toplevel` finds the repo root
from any subdirectory, so the command works wherever in the kit you happen to be;
and it **always overwrites**. The script is a kit artifact, not your data — so
re-running this step is how you pick up the latest version. Worth doing whenever
you `git pull` the kit.

Then save the key the user gives you — and **never echo it back afterwards**:

```bash
mkdir -p ~/.fluency && printf '%s' 'sk-or-THEIR-KEY' > ~/.fluency/openrouter.key && chmod 600 ~/.fluency/openrouter.key
```

> ⚠️ Never write the key into `CLAUDE.md` / `AGENTS.md`, a skill file, or any
> file inside a synced or git-tracked folder. `~/.fluency/` is the one place it
> lives.
>
> **And know where else it ends up.** If the user pastes the key into this chat,
> it's saved in the session transcript on their machine and in their AI
> provider's history. That's normal and usually fine — but it means the key is
> only as private as their machine and their transcripts. Tell them: *if you ever
> share a transcript, or the key stops feeling private, delete it at
> https://openrouter.ai/keys and make a new one.* Rotation takes ten seconds and
> costs nothing — that's more useful to know than another prohibition.

> **Windows:** the block above is macOS/Linux shell. In PowerShell the `chmod`
> step doesn't exist, so the file-permission protection simply doesn't happen —
> use WSL or Git Bash if you have it. Otherwise set the key as an environment
> variable (`OPENROUTER_API_KEY`) instead; the script reads that first.

## Step 5 — Verify

```bash
python3 ~/.fluency/bin/openrouter.py check
```

This confirms the key works and shows remaining credit. Then give the user a
taste — run:

```bash
python3 ~/.fluency/bin/openrouter.py image "a single dragonfly over still water at dawn, soft blue palette" -o dragonfly.png --aspect 16:9
```

…and open the result for them. From now on image generation and the
`web-searcher` agent's premium/social lanes work automatically — just ask your
agent to "generate an image of …" and it runs the engine directly.

> **On Codex, verify there too — passing on Claude Code proves nothing.** Codex
> runs agents in a sandbox that **blocks outbound network by default**, so the
> key can be perfect and every call still fail. The kit's `.codex/config.toml`
> sets `network_access = true` under `[sandbox_workspace_write]` to prevent this;
> if you merged your own config rather than using the kit's, add that block. To
> confirm, ask the Codex agent to run a search and check it actually cites live
> sources rather than quietly answering from memory.

---

## If something goes wrong

- **"No OpenRouter key found"** — the key didn't save; redo Step 4.
- **"Out of OpenRouter credit"** — top up at https://openrouter.ai/settings/credits.
  This is the most common failure, and it's the spend cap doing its job.
- **`auth/permission error 401: "User not found"`** — this is OpenRouter's
  wording for *the key wasn't accepted*, **not** "your account is gone". Usually
  a mistyped or truncated key, or stray quotes around it. It should start
  `sk-or-v1-`. Recreate it at https://openrouter.ai/keys and redo Step 4.
- **Network error reaching OpenRouter (on Codex)** — likely the sandbox blocking
  outbound network, not your key. See the Codex note in Step 5.
- **`python3: command not found` (Windows)** — try `python` instead of `python3`.

## Notes

- This is an API key + engine script, not an MCP server — nothing to add to MCP
  configs, and no restart needed.
- Siblings in this folder: [`paper-search.md`](paper-search.md) (academic
  literature, no key to start) and [`data-commons.md`](data-commons.md) (public
  statistics, free key) — together they fill out `web-searcher`'s lanes.
