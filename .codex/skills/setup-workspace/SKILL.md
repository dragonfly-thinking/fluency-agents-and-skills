---
name: setup-workspace
description: Sets up the user's agentic workspace — a router file (CLAUDE.md or AGENTS.md) plus context/ and projects/ subfolders. Smart-detects current state: if nothing is set up anywhere, runs the full init interview to create the workspace from scratch. If a workspace already exists, helps scope a new project, refresh the context files, or update guardrails. Use when the user says any of "set me up", "init my workspace", "create my agents.md", "set up claude for me", "add a new project to my setup", "refresh my context files", or similar.
---

# Setup Workspace

Detect whether the user has an agentic workspace, then route to the right mode.

## Step 1 — Detect the user's current state

Before doing anything else, look for an existing workspace. Check **both** scopes:

**Global scope:**
- `~/.claude/CLAUDE.md` (Claude Code / Desktop user)
- `~/.codex/AGENTS.md` (Codex user)
- `~/.claude/context/` or `~/.codex/context/` folder
- `~/.claude/projects/` or `~/.codex/projects/` folder

**Project scope (current working directory):**
- `./CLAUDE.md` or `./AGENTS.md`
- `./.claude/CLAUDE.md` or `./.codex/AGENTS.md`
- `./context/` folder
- `./projects/` folder

Use `ls` and `Read` to check — never assume from memory.

## Step 2 — Decide which mode to run

Based on what you found:

| Found | Default mode |
|---|---|
| Nothing anywhere | **INIT** (no question — just run it) |
| Workspace exists, no explicit user direction | **ASK** the user which mode they want |
| Workspace exists, user named a mode (e.g. "add a project for X") | Run that mode |

When you need to ASK, use this exact prompt:

> *"I can see you already have a workspace set up. What would you like to do?*
> *1. **Add a new project** — scope a current piece of work into `projects/<name>/`*
> *2. **Refresh your context files** — update `bio.md` / `work.md` based on what's changed*
> *3. **Add a guardrail** — append a new "always remember" rule to the router file*
> *4. **Re-run init from scratch** — start over (I'll back up the current files first)*
> *Or describe what you actually want."*

## Mode A — INIT (no workspace anywhere)

The user has nothing set up. Run the **full setup interview** to produce their first workspace.

**Read and follow exactly:** [`references/init-interview.md`](references/init-interview.md)

Do not paraphrase or shorten — that file is the canonical interview. It enforces 5-question max, one-question-at-a-time, and a single-code-block output. Follow it verbatim.

When finished, tell the user where to save the files:
- **Claude Code:** workspace root or `~/.claude/`. Save router as `CLAUDE.md`.
- **Codex:** workspace root or `~/.codex/`. Save router as `AGENTS.md`.
- **Claude Desktop (Cowork):** paste files into Custom Instructions, or upload to a Claude Project.

## Mode B — ADD PROJECT (workspace exists)

The user wants to scope a new piece of work into their existing setup. **Hand this off to
the `new-project` skill** — that's the dedicated tool for it.

`new-project` runs a light interview (goal, constraints, what's out of scope), proposes the
structure, and scaffolds `projects/<slug>/` with `overview.md`, `plan.md`, and `progress.md`,
then adds a one-line entry to the router file.

Don't scaffold the project inline here — `new-project` produces the richer, self-tracking
structure rather than a single `index.md`, and keeps project setup in one place.

## Mode C — REFRESH CONTEXT (workspace exists)

The user wants to update `bio.md` and/or `work.md`.

1. **Read the current files** first so you know what's there.
2. **Ask one question:** *"What's changed since you last wrote these? New role, new audience, new working pattern, something else?"*
3. **Show a diff before saving:** quote what would change. Use negative framing — *"What's wrong with this?"* — not *"Look right?"*.
4. **Save the updates** only after the user approves.

## Mode D — ADD A GUARDRAIL (workspace exists)

User wants to add an "always remember" rule to the router file.

1. Ask: *"What's the rule?"* — capture verbatim.
2. Append it to the router file's "Always remember" section. Don't reorder existing rules.
3. Show the updated section back to the user.

## Composition notes

- **To scaffold a project**, hand off to `new-project` — it writes the overview/plan/progress structure and updates the router.
- **For deep scoping of a vague idea** before scaffolding, hand off to `discovery-interview`.
- **For project planning** after a project is scoped, suggest the user run `project-planner` (subagent) on the new `overview.md` / `plan.md`.
- **Never run multiple modes in one invocation.** One mode per session — keep it focused.

## Anti-patterns

- **Don't assume the workspace doesn't exist.** Always check first. Overwriting a real workspace is destructive.
- **Don't batch questions.** One at a time, always — same rule as the init interview.
- **Don't invent answers.** If you don't have info, ask or leave it blank with a `<TODO: ...>` marker.
- **Don't move files between scopes silently.** If a file already exists at global scope and the user wants project scope, ask before duplicating or moving.
- **Don't auto-detect "the user is on Claude vs Codex" by guessing.** If unclear, ask: *"Are you using Claude Code, Claude Desktop / Cowork, or Codex?"*
