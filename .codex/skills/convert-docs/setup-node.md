# Setting up Node — so `convert-docs` can use the fast local converter

**Read this only when the skill sends you here.** It is not part of the kit install, and it is
never required — `convert-docs` works without it (Route 1b), just more slowly and using more of
your context on long documents.

**You are an AI agent doing this for a non-technical user.** They have very likely never opened a
terminal. Don't explain package managers. Say what you're doing in one sentence, do it, and tell
them when it's done.

## Before you start — three rules

1. **Ask first, and say how long.** *"This takes about two minutes and installs Node.js, a
   standard tool your agent uses to run small programs. Want me to?"* If they say no, drop it,
   use Route 1b, and don't ask again this session.
2. **Prefer the routes that need nothing from them.** On macOS and Linux you can do the whole
   thing yourself — no password, no installer, no restart. Only the last-resort fallbacks need
   the user, because **you cannot type an administrator password**. When that happens, hand the
   step over with a clear instruction, and never ask them to paste a password to you.
3. **Never leave them worse off.** If any step fails, stop, say plainly that the fast converter
   isn't available, and carry on with Route 1b. A failed setup must not cost them their task.

## First, check it isn't already there

```bash
node --version
```

Anything `v20.x` or higher — you're done, nothing to install. Below v20, or "command not found",
continue. (An old Node is common; it needs upgrading, not just installing.)

---

## macOS and Linux

**You can do this entire section yourself. The user does nothing and types no password.**

**If Homebrew is already installed** (`command -v brew` succeeds) — use it, it's their machine's
normal way of doing things and needs no password:

```bash
brew install node
```

**Otherwise use nvm**, which installs Node inside the user's own home folder. No administrator
rights, no password prompt, no installer to double-click. **Do NOT install Homebrew** to get
around this — Homebrew needs admin rights and pulls in Apple's developer tools, which is far too
much for what we're doing here.

```bash
# 1. Install nvm (pinned version, into ~/.nvm — nothing system-wide, no sudo)
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 2. Load it into THIS shell — without this, `nvm` and `node` won't be found yet
export NVM_DIR="$HOME/.nvm"; . "$NVM_DIR/nvm.sh"

# 3. Install the current LTS
nvm install --lts

# 4. Confirm
node --version
```

> **Step 2 matters.** nvm adds itself to the user's shell profile, which only takes effect in
> *new* terminals. Sourcing it as above makes Node usable immediately, in the session you're
> already in — so you can go straight on and do their conversion rather than asking them to
> restart anything.

Verified end to end on macOS: nvm installs with no password, Node LTS installs, and
`npx -y @firecrawl/anydoc` then converts correctly.

**Only if both of those fail** — fall back to the official installer, which does need the user:

```bash
V=$(curl -fsL https://nodejs.org/dist/index.json | python3 -c "import sys,json; print([r for r in json.load(sys.stdin) if r.get('lts')][0]['version'])")
curl -fL "https://nodejs.org/dist/$V/node-$V.pkg" -o ~/Downloads/node-installer.pkg && echo "Saved to ~/Downloads/node-installer.pkg"
```

> *"I've put an installer in your Downloads folder called **node-installer.pkg**. Double-click it
> and click Continue through the steps — it'll ask for your Mac password near the end, which is
> normal. Tell me when it's finished and I'll carry on."*

Then they must quit and reopen Claude Code or Codex before `node --version` will find it.

## Windows

```powershell
winget install OpenJS.NodeJS.LTS
```

Usually works with no prompt and no user involvement. If `winget` isn't recognised, send them to
[nodejs.org](https://nodejs.org) for the Windows installer to double-click — same hand-off wording
as the macOS fallback above.

Either way Node won't appear until a **new** terminal is opened, so have them restart Claude Code
or Codex before you re-check. (Windows is the one platform where there's no reliable
no-restart path — say so plainly rather than leaving them wondering why nothing happened.)

---

## When it's blocked

On a managed work laptop, installing software is often disabled, or `winget`/`brew` are absent and
the installer refuses to run. **This is a normal outcome, not a failure to debug.** Say so once,
without jargon:

> *"Your work laptop won't let me install that — no problem, I'll convert your documents the other
> way. It's a bit slower but the result is the same."*

Then use Route 1b and don't raise it again. Don't suggest they email IT; that's their call, not a
step in your task.

## Finishing up

Once `node --version` reports v20 or higher:

```bash
npm install -g @firecrawl/anydoc && anydoc --version
```

If the global install fails on permissions, don't chase it — `npx -y @firecrawl/anydoc` works
without installing anything, so just use that from now on and say nothing about it.

Then go back and do the conversion they originally asked for. **That was the point** — don't
finish setup and wait for further instructions.
