# Fluency Agents and Skills

The **agents and skills** starter kit from the Dragonfly Thinking **AI Fluency** course. Open it in [Claude Code](https://claude.ai/download) or [OpenAI Codex](https://developers.openai.com/codex/cli) and you have a real multi-agent setup — specialist subagents plus a library of user-facing skills — to learn from and adapt.

A skill is a *verb* you invoke ("proofread this", "build me a deck"). A subagent is a *specialist* a skill can hand work to. Several skills delegate to the base agents below.

## Install (let your agent do it)

Clone the repo, open it in Claude Code or Codex, and just say:

> **"Read AGENTS.md and install this kit for me."**

The agent follows [`AGENTS.md`](AGENTS.md) — copying the 6 agents and 12 skills into `~/.claude/` or `~/.codex/` (and, for Codex, merging the agent registrations into `config.toml`). Or do it by hand:

```bash
# Claude Code
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R .claude/agents/* ~/.claude/agents/ && cp -R .claude/skills/* ~/.claude/skills/

# Codex (then merge .codex/config.toml's [agents.*] blocks into ~/.codex/config.toml)
mkdir -p ~/.codex/agents ~/.codex/skills
cp -R .codex/agents/* ~/.codex/agents/ && cp -R .codex/skills/* ~/.codex/skills/
```

Start a new session and the skills/agents are live. See [`AGENTS.md`](AGENTS.md) for verification and runtime notes.

## The agents (specialists)

| Agent | What it does |
|-------|--------------|
| **critical-friend** | Pressure-tests an argument or plan — pushbacks, steel-manned counter-position, blind spots |
| **fact-checker** | Verifies factual/statistical claims against authoritative primary sources via web search |
| **writing-editor** | Heavy editorial pass — clarity, structure, voice, cuts — without replacing your voice |
| **project-planner** | Turns a goal into milestones, tasks, dependencies, and honest estimates |
| **vault-librarian** | Reads your local notes/vault and surfaces what's relevant to the task |
| **web-searcher** | Multi-query web research, returns a sourced answer with inline citations |

## The skills (verbs you invoke)

| Skill | What it does | Delegates to |
|-------|--------------|--------------|
| **proofread** | Clarity / grammar / structure / tone pass | writing-editor |
| **critical-review** | Stress-test an argument and fact-check its claims, in parallel | critical-friend + fact-checker |
| **research-brief** | Sourced briefing on a topic | web-searcher |
| **discovery-interview** | Interviews you to turn a vague idea into a spec | project-planner |
| **premortem** | Surfaces how a plan could fail before you commit | project-planner |
| **weekly-review** | Pulls the week together into a review | vault-librarian + project-planner |
| **daily-brief** | A morning brief from your notes and the web | vault-librarian + web-searcher |
| **visual-explainer** | Turns content into a shareable HTML one-pager | — |
| **slides** | Builds an HTML slide deck | — |
| **canvas-design** | Designs canvas/poster-style visual layouts | — |
| **pdf-create** | Produces a polished PDF | — |
| **here-now** | Publishes a file/folder to a live `{slug}.here.now` URL | — |

## What's inside

```
.
├── after-automation.md        # a sample draft to try the skills on
├── .claude/                   # Claude Code kit
│   ├── agents/                #   6 subagents (.md)
│   └── skills/                #   12 skills (SKILL.md per folder)
└── .codex/                    # Codex kit (same capabilities, Codex-native)
    ├── AGENTS.md
    ├── config.toml            #   registers the agent roles (multi_agent = true)
    ├── agents/                #   6 agent-role personas (.toml, via config_file)
    └── skills/                #   the same 12 skills, SKILL.md format
```

## Claude Code vs. Codex

Both runtimes have skills and subagents, configured differently:

| | Claude Code | Codex |
|---|---|---|
| Skills | `.claude/skills/<name>/SKILL.md` | `.codex/skills/<name>/SKILL.md` (same format) |
| Subagents | `.claude/agents/<name>.md` (markdown) | `.codex/agents/<name>.toml`, registered in `.codex/config.toml` |
| Subagent routing | automatic | explicit — *"use the web_searcher agent to…"* |

See [`.codex/AGENTS.md`](.codex/AGENTS.md) for the full Codex mapping and setup notes.

## Getting started

1. Clone this repo and open the folder in Claude Code or Codex.
2. Try the demo flow on the sample draft: **proofread** `after-automation.md` (watch the hand-off to writing-editor), then **critical-review** it, then turn it into a **visual-explainer** one-pager and **here-now** publish it.
3. Or just invoke any skill on your own work — *"build me slides on X"*, *"research-brief on Y"*, *"run a premortem on this plan"*.
4. To install the kit globally: copy `.claude/` into `~/.claude/` (Claude Code) or merge `.codex/config.toml` + `agents/` into `~/.codex/` and the skills into `~/.codex/skills/` (Codex).

---

Part of the **AI Fluency** course by [Dragonfly Thinking](https://github.com/dragonfly-thinking). This is the AI Fluency tier — a starter scaffold, not a methodology-license deployment.
