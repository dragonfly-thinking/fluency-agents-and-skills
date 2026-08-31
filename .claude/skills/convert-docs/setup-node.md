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

## First, work out which version they need

**On a Mac, check the OS version before anything else** — this decides which Node they get:

```bash
sw_vers -productVersion
```

- **macOS 13 or newer** → **Node 24** (the current Active LTS).
- **macOS 11 or 12** → **Node 22**. Node 24 requires macOS 13.5, so on a pre-2017 Mac it will not
  run. Node 22 is in maintenance until April 2027, which is fine for this purpose.
- **Windows or Linux** → **Node 24**. Both Node versions support Windows 10+ identically; there is
  no old-Windows problem, only an old-Mac one.

## Then check what's already installed

```bash
node --version
```

**At or above the version you just chose — you're done, nothing to install.**

> ⚠️ **Do not accept Node 20 or below.** Node 20 reached end-of-life on 30 April 2026. It also
> silently caps `agent-browser` (used by the `browser-agent` skill) at an old release, because npm
> quietly serves the newest version whose requirements the installed Node satisfies — with no error.
> Upgrade it rather than waving it through.
>
> ⚠️ **If they already have Node 22 on a macOS 13+ machine**, that's worth upgrading to 24 for the
> same reason. If they're on macOS 11/12, leave it — 22 is the correct answer there, and a future
> session should be told so (see *Finishing up*).

---

## macOS and Linux

**You can do this entire section yourself. The user does nothing and types no password.**

**Do NOT use `brew install node`.** The Homebrew `node` formula tracks the *Current* release,
not the LTS this skill wants. (Re-checked against the Node.js release schedule on 2026-09-01:
**24 "Krypton" is Active LTS, 26 is Current**, so `brew install node` gets you 26.) If Homebrew
is already installed, ask for the version explicitly:

```bash
brew install node@24     # or node@22 on macOS 11/12 — both formulae exist
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

# 3. Install the version chosen above — name it explicitly, don't use --lts
nvm install 24        # or: nvm install 22   on macOS 11/12

# 4. Confirm
node --version
```

> **Why not `nvm install --lts`?** It resolves to whatever is Active LTS on the day, which moves —
> Node 26 is due to take over from 24 in late October 2026. Two people installing a fortnight
> apart would end up on different runtimes, and a re-install would silently change the answer
> under someone who changed nothing. Name the version.

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

When they say it's done, run `hash -r` and check again — the installer puts Node in
`/usr/local/bin`, which is already on the PATH, so your shell just needs to stop caching the old
answer. **No restart required.** Only if it still isn't found should you ask them to reopen the app.

## Windows

```powershell
winget install OpenJS.NodeJS.LTS
```

Usually works with no prompt and no user involvement. That package tracks whichever line is
Active LTS, which is Node 24 today — fine on Windows either way, since there is no old-Windows
constraint. Check what landed with `node --version` and carry on.

If `winget` isn't recognised, send them to [nodejs.org](https://nodejs.org) for the Windows
installer to double-click — same hand-off wording as the macOS fallback above.

**Then add it to this session's PATH rather than asking them to restart anything.** Windows
updates the system PATH, which the terminal you're already in won't pick up — but you can point at
the install directly:

```bash
export PATH="$PATH:/c/Program Files/nodejs"
node --version
```

If that doesn't find it, look for `node.exe` under `/c/Program Files/nodejs` or
`$LOCALAPPDATA/Programs/nodejs` and add whichever exists. Only if none of that works should you
ask them to quit and reopen Claude Code or Codex — and say why, so it doesn't look like nothing
happened.

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

**If — and only if — you installed Node 22 because the Mac is too old for 24**, add one line to
their `CLAUDE.md` / `AGENTS.md` saying so. Everything else about the install (which version, where
it lives) a future session can rediscover in a second with `node --version` and `which node`, so
don't write that down. The *reason* is the part that isn't recoverable: without it, a future
session sees an old version number and offers to upgrade them to one their machine cannot run.

Once `node --version` reports the version you chose:

```bash
npm install -g @firecrawl/anydoc && anydoc --version
```

If the global install fails on permissions, don't chase it — `npx -y @firecrawl/anydoc` works
without installing anything, so just use that from now on and say nothing about it.

Then go back and do the conversion they originally asked for. **That was the point** — don't
finish setup and wait for further instructions.
