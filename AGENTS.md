# Install guide — for the agent

**You are an AI coding agent (Claude Code or Codex). The user has asked you to set up this kit. Follow the steps for the user's runtime below.** This installs 6 specialist subagents and 15 skills into the user's environment so they're available in every session, not just this folder.

If you don't know which runtime you're in: you're **Claude Code** if you read `CLAUDE.md` and use `.claude/`; you're **Codex** if you read `AGENTS.md` and use `.codex/`. If unsure, ask the user.

---

## What gets installed

- **6 agents** (specialists a skill can delegate to): `critical-friend`, `fact-checker`, `writing-editor`, `project-planner`, `vault-librarian`, `web-searcher`
- **15 skills** (verbs the user invokes): `setup-workspace`, `new-project`, `proofread`, `critical-review`, `research-brief`, `discovery-interview`, `premortem`, `weekly-review`, `daily-brief`, `visual-explainer`, `slides`, `canvas-design`, `pdf-create`, `here-now`, `generate-image`

The repo ships both `.claude/` (Claude Code format) and `.codex/` (Codex format). Install the one matching the runtime. The repo also carries `course-notes/` (session key points) and `mcp/` (external-connection setup guides) — these stay in the repo rather than being installed; see the wrap-up step.

---

## Step 0 — get the repo onto disk

You may have been given only this repo's **URL**. The install commands below assume the repo's files are on the user's machine, so get them there first. **Do not install by fetching files one at a time over the web** — you'll miss scripts and subfolders.

No GitHub account is needed for any of this; the repo is public.

- **If the repo is already on disk** (you're reading this file locally): it's ready to install — **but the kit gets updated between sessions, so if this might be an older copy from a previous course session, re-download the current version first** (see below) and install that, not stale files.
- **If the user downloaded it themselves** (e.g. they say "I downloaded it"): look for `fluency-agents-and-skills-main` — usually in `~/Downloads`, possibly still zipped. Unzip if needed, then **move it somewhere durable** before installing, e.g. `mv ~/Downloads/fluency-agents-and-skills-main ~/fluency-agents-and-skills`. Downloads folders get purged, and `course-notes/` + `mcp/` need to live on after install. (If their download is from an earlier session, prefer re-fetching the latest as below.)
- **Otherwise, fetch it yourself — don't assume `git` is installed.** Most course participants won't have it (on a fresh Mac, even running `git` triggers an install prompt that can hang you). Default to the plain **ZIP download** — no git, no account. This is also the **update path**: re-downloading always gets the latest and replaces an older copy.

```bash
# No git needed — also the update path; replaces any existing copy
curl -L https://github.com/dragonfly-thinking/fluency-agents-and-skills/archive/refs/heads/main.zip -o /tmp/fluency-kit.zip
rm -rf ~/fluency-agents-and-skills && unzip -q /tmp/fluency-kit.zip -d ~ && mv ~/fluency-agents-and-skills-main ~/fluency-agents-and-skills
```

Only if `git` is *already* installed, cloning is a fine alternative (and makes later updates a `git pull`):

```bash
git clone https://github.com/dragonfly-thinking/fluency-agents-and-skills.git ~/fluency-agents-and-skills
```

Use `~/fluency-agents-and-skills` as the standard location — the course materials assume the repo lives somewhere predictable. Run the install commands below from inside it.

---

## Claude Code install

Copy the agents and skills into the user's home Claude directory:

```bash
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R .claude/agents/*  ~/.claude/agents/
cp -R .claude/skills/*  ~/.claude/skills/
```

That's it. Claude Code auto-discovers `~/.claude/agents/` and `~/.claude/skills/`. Restart the session (or start a new one) and the skills/agents are live. Skills route automatically when the user describes the task.

**Verify:** in the new session, have the user type `/` — the installed skills (`proofread`, `slides`, `new-project`, …) should appear in the list — and run `/agents` to confirm the six subagents are registered. If they don't appear, check the files actually landed (`ls ~/.claude/skills ~/.claude/agents`) and that the session was fully restarted.

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

> "Installed 6 agents and 15 skills. **First time?** Run *`setup-workspace`* — it'll interview you and create your `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/` for you. **Been here before?** Run *`setup-workspace`* again — it'll spot what's missing from your setup and fill just those gaps. Or try: *start a new project with `new-project`* (it opens by asking what you'd like to work on), *run `discovery-interview` on an idea you've been sitting on*, *build me slides on X*, *research-brief on Y*, or *publish something with here-now*."

Then two more things:

1. **Point at the course notes.** Tell the user where the repo lives on their machine (normally `~/fluency-agents-and-skills` — see Step 0) and that `course-notes/` there holds the key points from the four course sessions, with `mcp/` holding the external-connection setup guides. Offer: *"Want me to read the course notes and suggest what's worth putting into action first?"*
2. **Tell them the kit is theirs to shape.** One line is enough: *"If a skill ever gets something wrong, just tell me — I can update the skill so it doesn't happen again. And if you notice a task you repeat, I can turn it into a new skill."*

## Runtime dependencies to mention

- **Web search** must be enabled for `fact-checker`, `web-searcher`, `research-brief`, and `daily-brief` to verify/retrieve from the web. If it's off, they'll say so rather than invent.
- **here-now** needs `curl`, `file`, and `jq` on PATH (standard on macOS/Linux).
- **pdf-create** uses an already-installed Chrome/Edge; if none is found it falls back to "open the HTML and Cmd/Ctrl+P → Save as PDF" — no installs.

---

For what each skill and agent does, see [`README.md`](README.md).
