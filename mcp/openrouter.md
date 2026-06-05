# Add OpenRouter — for the agent

**You are an AI coding agent (Claude Code or Codex). The user wants to set up
OpenRouter — one API key that unlocks capabilities this kit can't do on its own:
image generation (the `generate-image` skill), live web search with real
citations, and X/social search (the premium lanes of the `web-searcher` agent).**

One key powers all of it, pay-as-you-go, no extra subscriptions. Rough costs: an
image ≈ $0.04, a search ≈ $0.001 — $10 of credit lasts a long time.

Explain each step to the user in plain English before you run it, and ask them to
approve any command. Steps 1–3 happen in the user's browser — guide them; don't
try to do these yourself.

---

## Step 1 — Create the account (user, in browser)

Send the user to **https://openrouter.ai** to sign up (Google sign-in is fine).

## Step 2 — Add credit, and cap it (user, in browser)

1. At **https://openrouter.ai/settings/credits**, add **$10**.
2. **Have them set a spend limit.** This is the important bit: with a cap, nothing
   can ever overspend — if something goes wrong, it just stops. Say this to the
   user explicitly; it's what makes the setup safe.

## Step 3 — Create the key (user, in browser)

At **https://openrouter.ai/keys** → **Create Key** → name it (e.g. "Fluency") →
copy it. It starts with `sk-or-`. Tell the user to treat it like a password.

## Step 4 — Install the engine and save the key (you)

The kit's OpenRouter capabilities run through one small, pre-tested engine script
that ships inside the `generate-image` skill. Put it in place:

```bash
mkdir -p ~/.fluency/bin
[ -f ~/.fluency/bin/openrouter.py ] || cp ~/.claude/skills/generate-image/scripts/openrouter.py ~/.fluency/bin/openrouter.py 2>/dev/null \
  || cp ~/.codex/skills/generate-image/scripts/openrouter.py ~/.fluency/bin/openrouter.py
```

(If neither path exists, the kit isn't installed globally yet — install it first
per [`AGENTS.md`](../AGENTS.md), or copy `scripts/openrouter.py` from this repo's
`generate-image` skill folder.)

Then save the key the user gives you — and **never echo it back afterwards**:

```bash
mkdir -p ~/.fluency && printf '%s' 'sk-or-THEIR-KEY' > ~/.fluency/openrouter.key && chmod 600 ~/.fluency/openrouter.key
```

> ⚠️ Never write the key into `CLAUDE.md` / `AGENTS.md`, a skill file, or any
> file inside a synced or git-tracked folder. `~/.fluency/` is the one place it
> lives.

## Step 5 — Verify

```bash
python3 ~/.fluency/bin/openrouter.py check
```

This confirms the key works and shows remaining credit. Then give the user a
taste — run:

```bash
python3 ~/.fluency/bin/openrouter.py image "a single dragonfly over still water at dawn, soft blue palette" -o dragonfly.png --aspect 16:9
```

…and open the result for them. From now on the `generate-image` skill and the
`web-searcher` agent's premium/social lanes work automatically.

---

## If something goes wrong

- **"No OpenRouter key found"** — the key didn't save; redo Step 4.
- **"Out of OpenRouter credit"** — top up at https://openrouter.ai/settings/credits.
  This is the most common failure, and it's the spend cap doing its job.
- **`python3: command not found` (Windows)** — try `python` instead of `python3`.

## Notes

- This is an API key + engine script, not an MCP server — nothing to add to MCP
  configs, and no restart needed.
- Siblings in this folder: [`paper-search.md`](paper-search.md) (academic
  literature, free, no key) and [`data-commons.md`](data-commons.md) (public
  statistics, free key) — together they fill out all of `web-searcher`'s lanes.
