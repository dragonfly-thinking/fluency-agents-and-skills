# Fluency Agents and Skills — Codex kit

The Codex-side of the kit. Codex (0.130+) has a full skills system using the **same `SKILL.md` format** as Claude Code, **and** a first-class agent-role system — so this mirrors the sibling `.claude/` folder closely: skills are skills, and the subagents are real Codex agent roles.

## The mapping

| Claude Code | Codex equivalent here | Note |
|-------------|----------------------|------|
| `.claude/skills/<name>/SKILL.md` | `.codex/skills/<name>/SKILL.md` | Identical format: `name` + `description` frontmatter, markdown body. Codex reads only the frontmatter to decide when to trigger. |
| `.claude/agents/<name>.md` (subagent personas) | `[agents.<name>]` in **`.codex/config.toml`** → `config_file` → **`.codex/agents/<name>.toml`** | Codex agent roles are TOML, not markdown. `config.toml` registers each role (`description` + `config_file`); the role file holds `developer_instructions` (the persona), `model_reasoning_effort`, `sandbox_mode`. Role keys are snake_case (Dragonfly house convention); file names stay hyphenated. |
| `CLAUDE.md` | `AGENTS.md` (this file) | Codex reads `AGENTS.md` for project instructions. |

## Agent roles (`.codex/config.toml` + `.codex/agents/`)

| Role (`agent_role`) | Persona file | What it does |
|---------------------|--------------|--------------|
| `critical_friend` | `agents/critical-friend.toml` | Pressure-tests an argument/plan |
| `fact_checker` | `agents/fact-checker.toml` | Verifies claims via web search |
| `writing_editor` | `agents/writing-editor.toml` | Clarity / structure / voice edit pass |
| `project_planner` | `agents/project-planner.toml` | Goal → milestones, tasks, risks |
| `vault_librarian` | `agents/vault-librarian.toml` | Finds relevant local notes/files |
| `web_searcher` | `agents/web-searcher.toml` | Multi-query web research with citations |

In Codex, subagents are invoked **explicitly** — *"use the web_searcher agent to find sources on X"*. Skills that delegate name the role; Codex loads the persona from the role's TOML.

## Skills here

Same 15 skills as the Claude side. Skills that delegate to a role:

| Skill | Delegates to |
|-------|--------------|
| `proofread` | `writing_editor` |
| `critical-review` | `critical_friend` + `fact_checker` (in parallel) |
| `research-brief` | `web_searcher` |
| `discovery-interview` | `project_planner` |
| `new-project` | `project_planner` (and the `discovery-interview` skill) |
| `premortem` | `project_planner` |
| `weekly-review` | `vault_librarian` + `project_planner` |
| `daily-brief` | `vault_librarian` + `web_searcher` |

`setup-workspace` hands project creation to the `new-project` skill. Standalone (no
subagent): `visual-explainer`, `slides`, `canvas-design`, `pdf-create`, `here-now`,
`generate-image`.

```
.codex/
├── AGENTS.md
├── config.toml          ← [features] multi_agent + 6 [agents.*] registrations
├── agents/              ← 6 agent-role personas (.toml; the source of truth)
└── skills/              ← 15 skills (SKILL.md per folder)
```

## Discovery — read this before installing

- **Skills:** Codex auto-discovers skills in `$CODEX_HOME/skills` (`~/.codex/skills`). It also reads a **project config layer**, but if your build doesn't pick up project-local `.codex/skills/`, copy them: `cp -R .codex/skills/* ~/.codex/skills/`.
- **Agent roles:** registered in `.codex/config.toml` (`[agents.*]` → `config_file`), personas in `.codex/agents/*.toml`. Codex loads roles from the config layers (Managed / User / project). If your build only reads roles from `~/.codex/config.toml`, merge the `[features]` + `[agents.*]` blocks into that file and copy the `agents/` folder beside it. Verify with `codex` → `/status`, or check that a `spawn_agent` with `agent_role: "web_searcher"` resolves.

## Note on the fact-checker

The `fact_checker` role verifies claims via **web search** against authoritative primary sources (official statistical agencies, World Bank/OECD/WHO, primary documents). Make sure web search is enabled in the Codex session; if it isn't, the role marks claims "Unverifiable" rather than inventing a verification.
