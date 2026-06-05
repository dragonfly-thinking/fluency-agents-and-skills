# Install guide — for the agent

**You are an AI coding agent (Claude Code or Codex). The user has asked you to set up this kit. Follow the steps for the user's runtime below.** This installs 6 specialist subagents and 15 skills into the user's environment so they're available in every session, not just this folder.

If you don't know which runtime you're in: you're **Claude Code** if you read `CLAUDE.md` and use `.claude/`; you're **Codex** if you read `AGENTS.md` and use `.codex/`. If unsure, ask the user.

---

## What gets installed

- **6 agents** (specialists a skill can delegate to): `critical-friend`, `fact-checker`, `writing-editor`, `project-planner`, `vault-librarian`, `web-searcher`
- **15 skills** (verbs the user invokes): `setup-workspace`, `new-project`, `proofread`, `critical-review`, `research-brief`, `discovery-interview`, `premortem`, `weekly-review`, `daily-brief`, `visual-explainer`, `slides`, `canvas-design`, `pdf-create`, `here-now`, `generate-image`

The repo ships both `.claude/` (Claude Code format) and `.codex/` (Codex format). Install the one matching the runtime. The repo also carries `course-notes/` (session key points) and `mcp/` (external-connection setup guides) — these stay in the repo rather than being installed; see the wrap-up step.

---

## Claude Code install

Copy the agents and skills into the user's home Claude directory:

```bash
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R .claude/agents/*  ~/.claude/agents/
cp -R .claude/skills/*  ~/.claude/skills/
```

That's it. Claude Code auto-discovers `~/.claude/agents/` and `~/.claude/skills/`. Restart the session (or start a new one) and the skills/agents are live. Skills route automatically when the user describes the task.

---

## Codex install

Codex needs three things: the skills, the agent role files, and the `[agents.*]` registrations merged into the user's config.

```bash
mkdir -p ~/.codex/skills ~/.codex/agents
cp -R .codex/skills/*  ~/.codex/skills/
cp -R .codex/agents/*  ~/.codex/agents/
```

Then **merge** the agent registrations into `~/.codex/config.toml`. Do NOT overwrite the file — the user may already have config. Ensure `[features] multi_agent = true` is present, then append any `[agents.*]` blocks from this repo's `.codex/config.toml` that aren't already there. The blocks look like:

```toml
[features]
multi_agent = true

[agents.critical_friend]
description = "..."
config_file = "agents/critical-friend.toml"
# ...and the other five agents
```

Read `.codex/config.toml` for the exact blocks and copy them verbatim. After merging, verify with `codex` → `/status`, or by spawning a sub-agent with `agent_role: "web_searcher"`. In Codex, subagents are invoked **explicitly** — e.g. *"use the web_searcher agent to find sources on X"*. See `.codex/AGENTS.md` for the full Codex mapping.

---

## The here-now skill (special)

`here-now` publishes files to a live URL. It ships with working scripts (`scripts/publish.sh`, `scripts/drive.sh`), so copying it as above is enough. Alternatively, install the always-current upstream version directly:

```bash
npx skills add heredotnow/skill --skill here-now -g
```

No API key is needed for anonymous publishing (URLs expire in 24h). For permanent URLs, the skill walks the user through an email sign-in to get a key — see `.codex/skills/here-now/SKILL.md`.

---

## After installing — verify

Tell the user it's done and give them something to try:

> "Installed 6 agents and 15 skills. **First time?** Run *`setup-workspace`* — it'll interview you and create your `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/`. Or try: *start a new project with `new-project`* (it opens by asking what you'd like to work on), *run `discovery-interview` on an idea you've been sitting on*, *build me slides on X*, *research-brief on Y*, or *publish something with here-now*."

Then two more things:

1. **Point at the course notes.** If the repo is on the user's machine, mention `course-notes/` — the key points from the four course sessions. Offer: *"Want me to read the course notes and suggest what's worth putting into action first?"* If the kit was installed from a URL and the repo is NOT on disk, offer to download it so `course-notes/` and `mcp/` (the external-connection setup guides) stay available.
2. **Tell them the kit is theirs to shape.** One line is enough: *"If a skill ever gets something wrong, just tell me — I can update the skill so it doesn't happen again. And if you notice a task you repeat, I can turn it into a new skill."*

## Runtime dependencies to mention

- **Web search** must be enabled for `fact-checker`, `web-searcher`, `research-brief`, and `daily-brief` to verify/retrieve from the web. If it's off, they'll say so rather than invent.
- **here-now** needs `curl`, `file`, and `jq` on PATH (standard on macOS/Linux).
- **pdf-create** uses an already-installed Chrome/Edge; if none is found it falls back to "open the HTML and Cmd/Ctrl+P → Save as PDF" — no installs.

---

For what each skill and agent does, see [`README.md`](README.md).
