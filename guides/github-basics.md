# GitHub, Explained — backup, sharing, and history for your workspace

**Who this is for:** your work now lives in folders of Markdown files, and you keep
hearing "GitHub" — from your agent, from colleagues, and from the cloud-routines
setup screen. This is the plain-English version
of what it is and how to start using it, with steps written so **your agent can do
the setup for you**.

---

## What GitHub actually is

GitHub is an **online store for folders of files** — originally built so software
developers around the world could work on the same code without overwriting each
other. You don't need to be a developer: Dragonfly's own team (mostly
non-developers) runs on it daily. For a knowledge worker with an agent workspace,
it does three things:

1. **Backup.** Your workspace lives on GitHub as well as your computer. Laptop
   dies, gets stolen, coffee incident — you restore everything.
2. **Collaboration.** Share a workspace with your team. Someone makes a change and
   "pushes" it; everyone else "pulls" it down. No emailing versions around.
3. **Version history.** Every saved change is kept forever. You (or your agent) can
   see exactly what changed when, and roll back a mistake — the ultimate undo.

It also unlocks two agent features: **cloud routines** (Claude's scheduled tasks
that run without your laptop being awake work by pulling your files from GitHub,
processing them in the cloud, and writing results back) and **working from
anywhere** (any machine — or a cloud session — can pull your workspace down).

## The five words you'll hear

| Word | What it means |
|------|---------------|
| **Repository ("repo")** | One folder-of-files stored on GitHub — e.g. your whole workspace |
| **Commit** | A saved snapshot of your changes, with a one-line note of what changed |
| **Push** | Send your commits up to GitHub |
| **Pull** | Bring down changes from GitHub (yours from another machine, or a teammate's) |
| **Clone** | Copy a repo from GitHub onto a computer for the first time |

That's genuinely most of it. Your agent handles the mechanics; you just need to
recognise the words.

## ⚠️ Two things to get right before you start

- **Private, not public.** A repo can be **public** (anyone on the internet can
  read it) or **private** (only people you invite). Your workspace almost certainly
  contains things that shouldn't be public — **always choose private** unless you
  have a specific reason not to.
- **Never commit secrets.** API keys and passwords don't belong in tracked files,
  even in a private repo. Keep them where the setup guides in `mcp/` put them
  (config files outside the repo, or environment variables).

  **And if one slips through: rotate it, don't just delete it.** Git keeps every
  version forever — that's the feature. Deleting a key from a file in a later
  commit leaves it sitting in the history, still readable. The fix is to go to
  wherever the key came from, delete it there, and issue a new one. Takes a
  minute and costs nothing. Ask your agent to scan the folder for anything
  key-shaped *before* the first push, when it's still easy.

---

## Setup — point your agent at this section

**You are an AI coding agent (Claude Code or Codex). The user wants their workspace
backed up to GitHub.** Explain each step in plain English before you run it, and
ask them to approve commands. Adapt to what's already installed.

1. **Account.** Have the user create a free account at
   [github.com](https://github.com) if they don't have one (they do this part —
   it's an email signup).
2. **Check for git** (the underlying tool): `git --version`. On macOS, accept the
   developer-tools prompt if one appears; on Windows, install from
   [git-scm.com](https://git-scm.com) or `winget install Git.Git`.
3. **Install and authenticate the GitHub CLI** — easiest path for non-developers:
   `gh` from [cli.github.com](https://cli.github.com) (`brew install gh` /
   `winget install GitHub.cli`), then `gh auth login` — the user follows the
   browser prompts. Afterwards run `gh auth status` and check it names the
   account they expect: if they have both a personal and a work GitHub login,
   `gh` can be signed into the wrong one, and the only symptom later is a
   confusing "repository not found".
4. **Turn the workspace into a repo and push it.** From the workspace folder:
   initialise (`git init`), write a sensible `.gitignore` first (exclude `.DS_Store`,
   any folders of huge binary files, and anything containing keys), commit, then
   `gh repo create <name> --private --source=. --push`. **Confirm with the user
   that the repo should be private before creating it.**
5. **Set the habit.** Offer to add one line to their `CLAUDE.md` / `AGENTS.md`:
   *"At the end of a work session, offer to commit and push the day's changes with
   a clear message."* From then on, backup is something the agent proposes, not
   something the user remembers.
6. **Verify.** Open `github.com/<username>/<name>` in the browser — the user should
   see their files. That page is the backup.

## Everyday use (after setup)

You don't need to learn commands. Say to your agent:

- *"Commit and push today's changes"* — backup.
- *"What changed in this folder in the last two weeks?"* — history.
- *"Restore yesterday's version of `report.md`"* — the undo.
- *"Pull the latest changes"* — when you (or a teammate) worked from elsewhere.

## Using a second computer (or your whole team)

On the other machine: install the same tools (steps 2–3), then *"clone my
`<name>` repo from GitHub into my Documents folder."* From then on it's **pull
when you sit down, push when you finish** — on both machines. Your agent will
happily manage this rhythm if you ask it to.

> **iCloud / OneDrive instead?** They *can* sync a workspace between your own
> machines, but they sync every half-saved change instantly (no snapshots, no
> history, no "roll back to Tuesday"), and syncing the hidden `.claude` / `.codex`
> config folders is patchy. Fine for casual use on your own devices; GitHub is the
> proper tool the moment history or teammates matter.

## If your work computer is locked down

Can't install anything at work? The pattern flips: keep the repo on GitHub as the
home of the files, and let the agent work on them **in the cloud** (Claude's
cloud/GitHub-connected sessions and routines run on GitHub-hosted files without
touching the local machine). Check what your IT policy actually permits before
putting work content anywhere — but mechanically, this is the standard answer for
"my machine is locked down."

---

*A mild learning curve is normal. Your agent knows git deeply — when anything
looks weird ("merge conflict", "detached HEAD"), paste the message in and ask.
The one rule that avoids most trouble: **pull before you start, push when you
stop.***
