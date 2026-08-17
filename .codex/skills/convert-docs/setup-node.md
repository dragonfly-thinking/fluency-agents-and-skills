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
2. **You cannot type an administrator password.** Some routes below need one. When that happens,
   hand the step to the user with a clear instruction — don't try to work around it, and never
   ask them to paste their password to you.
3. **Never leave them worse off.** If any step fails, stop, say plainly that the fast converter
   isn't available, and carry on with Route 1b. A failed setup must not cost them their task.

## First, check it isn't already there

```bash
node --version
```

Anything `v20.x` or higher — you're done, nothing to install. Below v20, or "command not found",
continue. (An old Node is common; it needs upgrading, not just installing.)

---

## macOS

**If Homebrew is installed** (`command -v brew` succeeds) — this is the clean path, no password:

```bash
brew install node
```

**If Homebrew is not installed, do NOT install it.** It's a large install that needs an
administrator password and pulls in Apple's developer tools — far too much for this. Use the
official installer instead: you download it, the user double-clicks it.

```bash
# Look up the current LTS release rather than hard-coding a version
V=$(curl -fsL https://nodejs.org/dist/index.json | python3 -c "import sys,json; print([r for r in json.load(sys.stdin) if r.get('lts')][0]['version'])")
curl -fL "https://nodejs.org/dist/$V/node-$V.pkg" -o ~/Downloads/node-installer.pkg && echo "Saved to ~/Downloads/node-installer.pkg"
```

Then tell them, in these words or close to them:

> *"I've put an installer in your Downloads folder called **node-installer.pkg**. Double-click it
> and click Continue through the steps — it'll ask for your Mac password near the end, which is
> normal. Tell me when it's finished and I'll carry on."*

When they say it's done, **they must open a new terminal session** for it to be visible — in
practice, quit and reopen Claude Code or Codex. Then re-check `node --version`.

## Windows

```powershell
winget install OpenJS.NodeJS.LTS
```

Usually works without a prompt. If `winget` isn't recognised, send them to
[nodejs.org](https://nodejs.org) to download the Windows installer and double-click it — same
hand-off wording as the Mac route above.

Either way, Node won't appear until a **new** terminal is opened, so have them restart Claude Code
or Codex before you re-check.

## Linux

`sudo apt install nodejs npm` (Debian/Ubuntu) or the distro equivalent. This needs a password the
user must type themselves — hand it over rather than attempting it.

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
