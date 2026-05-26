# Fluency Agents and Skills

A working example of **agents and skills** from the Dragonfly Thinking **AI Fluency** course — the "Extending your Agent" session. Open it in [Claude Code](https://claude.ai/download) or [OpenAI Codex](https://developers.openai.com/codex/cli) and you have a small, real multi-agent setup to learn from and adapt.

One piece of work walked all the way through: take a messy draft → **proofread** it (a skill that calls a specialist subagent) → **visually explain** it (a skill) → **publish** it to a live URL (a skill). Optionally, **critically review** it (a skill that fans out to two subagents in parallel).

## What's inside

```
.
├── briefing-note-draft.md     # the draft we work on (a policy briefing note, with deliberate flaws)
├── .claude/                   # the Claude Code kit
│   ├── agents/                #   subagents (specialists)
│   │   ├── writing-editor.md
│   │   ├── critical-friend.md
│   │   └── fact-checker.md
│   └── skills/                #   skills (the verbs you invoke)
│       ├── proofread/             → delegates to writing-editor
│       ├── visual-explainer/      → turns content into a shareable HTML page
│       ├── here-now/              → publishes to a live {slug}.here.now URL
│       └── critical-review/       → fans out to critical-friend + fact-checker
└── .codex/                    # the Codex kit (same capabilities, Codex-native)
    ├── AGENTS.md
    ├── config.toml            #   registers the 3 agent roles (multi_agent = true)
    ├── agents/                #   agent role personas (TOML)
    │   ├── critical-friend.toml
    │   ├── fact-checker.toml
    │   └── writing-editor.toml
    └── skills/                #   the same 4 skills, SKILL.md format
```

## Skills vs. agents — the lesson

- A **skill** is a *verb* you invoke ("proofread this"). It's instructions + optional bundled files.
- A **subagent** is a *specialist* a skill can delegate to — its own focused context and persona.
- `proofread` is a skill that hands the work to the **writing-editor** subagent. `critical-review` fans out to **critical-friend** + **fact-checker** in parallel. `visual-explainer` and `here-now` are skills with no subagent — not everything needs a specialist.

## Claude Code vs. Codex

Both runtimes have skills and subagents, configured differently:

| | Claude Code | Codex |
|---|---|---|
| Skills | `.claude/skills/<name>/SKILL.md` | `.codex/skills/<name>/SKILL.md` (same format) |
| Subagents | `.claude/agents/<name>.md` (markdown) | `.codex/agents/<name>.toml` registered in `.codex/config.toml` |
| Subagent routing | automatic | explicit — *"use the critical_friend agent to…"* |

See [`.codex/AGENTS.md`](.codex/AGENTS.md) for the full Codex mapping and setup notes.

## Getting started

1. Clone this repo and open the folder in Claude Code or Codex.
2. Open `briefing-note-draft.md` and read it.
3. Ask your agent to **proofread** it — watch the skill hand off to the writing-editor specialist.
4. Ask it to turn the cleaned draft into a **visual one-pager**, then **publish** it.
5. (Optional) Ask for a **critical review** to stress-test the argument and fact-check its claims.

---

Part of the **AI Fluency** course by [Dragonfly Thinking](https://github.com/dragonfly-thinking). This is the AI Fluency tier — a starter scaffold, not a methodology-license deployment.
