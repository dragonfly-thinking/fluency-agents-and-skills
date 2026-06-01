---
name: generate-image
description: >-
  Generate an image from a text description — a picture, illustration, icon,
  logo, hero image, or diagram-style art. Powered by Google's "Nano Banana"
  through a single OpenRouter key, so there's no separate image-service account
  to manage. Use whenever the user says "make an image", "generate a picture",
  "create an icon / logo / illustration", or "I need some art for…".
---

# Generate Image

Turn a text prompt into a real image file using Google's Nano Banana model,
called through one OpenRouter key. The heavy lifting lives in a small, shared,
pre-tested engine (`openrouter.py`) so you never hand-write API calls.

## The engine

The engine is shared between this skill and the `web-searcher` sub-agent, so it
lives in **one** place rather than inside either of them:

```
~/.fluency/bin/openrouter.py     # the shared engine
~/.fluency/openrouter.key        # the key (created during setup)
```

**Before the first call, make sure the engine is installed** (idempotent — safe
to run every time):

```bash
mkdir -p ~/.fluency/bin
[ -f ~/.fluency/bin/openrouter.py ] || cp "$(dirname "$0")/scripts/openrouter.py" ~/.fluency/bin/openrouter.py 2>/dev/null \
  || cp ~/.claude/skills/generate-image/scripts/openrouter.py ~/.fluency/bin/openrouter.py 2>/dev/null \
  || cp ~/.codex/skills/generate-image/scripts/openrouter.py ~/.fluency/bin/openrouter.py
```

If neither copy path resolves on the user's machine, just read this skill's
`scripts/openrouter.py` and write it to `~/.fluency/bin/openrouter.py` yourself.

## How to generate

```bash
python3 ~/.fluency/bin/openrouter.py image "a single dragonfly over still water at dawn, soft blue palette" -o dragonfly.png --aspect 16:9 --size 2K
```

- `--aspect` — `1:1` (default), `16:9`, `9:16`, `4:3`, `3:2`, `4:5` …
- `--size` — `0.5K`, `1K`, `2K` (default), `4K`
- `-o` — output file (defaults to `openrouter-image.png`)

Then **open it for the user** so they see it immediately (`open dragonfly.png` on
macOS) or tell them the exact path.

## Iterate — don't settle for the first result

The first image is a draft, not the answer. After showing it, invite changes and
run again with a revised prompt: *"warmer light", "remove the reeds", "flatter,
more icon-like", "use our brand blue #0563FA"*. Generating three variations and
picking the best is normal and cheap (~$0.04 each).

## First-time key setup

If any command prints **"No OpenRouter key found"**, set the user up once:

1. Get a key at **https://openrouter.ai/keys** (starts with `sk-or-`).
2. Add a few dollars at **https://openrouter.ai/settings/credits**, and **set a
   spend limit on the key** so it can never overspend.
3. Save it (never echo the key back afterwards):
   ```bash
   mkdir -p ~/.fluency && printf '%s' 'sk-or-THEIR-KEY' > ~/.fluency/openrouter.key && chmod 600 ~/.fluency/openrouter.key
   ```
4. Confirm with `python3 ~/.fluency/bin/openrouter.py check`.

## Common issues

- **"Out of OpenRouter credit"** — the #1 cause of failure. Add credit at
  https://openrouter.ai/settings/credits.
- **"No image returned"** — the prompt was too abstract; make it more concrete and retry.

## Pairs well with

- **`visual-explainer`** / **`slides`** — generate hero imagery, then drop it into a page or deck.
- **`canvas-design`** — for polished poster/PDF compositions.
