# Fluency Agents and Skills

This repo is the **Fluency Agents and Skills** starter kit — 6 specialist subagents and 12 skills for Claude Code and Codex.

## If the user asks you to install or set this up

Follow [`AGENTS.md`](AGENTS.md) — it's the full install playbook. For Claude Code, the short version is:

```bash
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R .claude/agents/*  ~/.claude/agents/
cp -R .claude/skills/*  ~/.claude/skills/
```

Then start a new session — Claude Code auto-discovers `~/.claude/agents/` and `~/.claude/skills/`. See `AGENTS.md` for verification, the here-now publish skill, and runtime dependencies (web search, etc.).

For what each skill and agent does, see [`README.md`](README.md).
