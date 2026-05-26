# Extending Demo — Codex kit

This is the Codex-side version of the Session 3 "Extending" demo. It mirrors the capabilities in the sibling `.claude/` folder. Codex (0.130+) has a full skills system that uses the **same `SKILL.md` format** as Claude Code, **and** a first-class agent-role system — so this is a true 1:1 translation: skills are skills, and the three subagents are real Codex agent roles.

## The mapping

| Claude Code | Codex equivalent here | Note |
|-------------|----------------------|------|
| `.claude/skills/<name>/SKILL.md` | `.codex/skills/<name>/SKILL.md` | Identical format: `name` + `description` frontmatter, markdown body. Codex reads only the frontmatter to decide when to trigger. |
| `.claude/agents/<name>.md` (subagent personas) | `[agents.<name>]` in **`.codex/config.toml`** → `config_file` → **`.codex/agents/<name>.toml`** | Codex agent roles are TOML, not markdown. `config.toml` registers each role (`description` + `config_file`); the role file holds `developer_instructions` (the persona), `model_reasoning_effort`, `sandbox_mode`. Skills spawn them by `agent_role`. The `references/*.md` files are readable copies; the `.codex/agents/*.toml` files are the source of truth. |
| `CLAUDE.md` | `AGENTS.md` (this file) | Codex reads `AGENTS.md` for project instructions. |

## Agent roles (`.codex/config.toml` + `.codex/agents/`)

| Role (`agent_role`) | Persona file | Used by |
|---------------------|--------------|---------|
| `critical_friend` | `agents/critical-friend.toml` | `critical-review` |
| `fact_checker` | `agents/fact-checker.toml` | `critical-review` |
| `writing_editor` | `agents/writing-editor.toml` | `proofread` |

A skill spawns a role with the `spawn_agent` tool, e.g. `agent_role: "critical_friend"`, prompt = the draft. No brief-pasting — Codex loads the persona from the role's TOML. (Role keys are snake_case to match the Dragonfly house convention; file names stay hyphenated.)

## Skills here

| Skill | What it does | Agent roles it spawns |
|-------|--------------|----------------------|
| `critical-review` | Heavy pre-send review — challenges the argument **and** fact-checks the claims, in parallel | `critical-friend` + `fact-checker` |
| `proofread` | Light clarity/grammar/structure/tone pass, preserving the writer's voice | `writing-editor` |
| `visual-explainer` | Generates a self-contained HTML page that visually explains an idea, process, comparison, or dataset | — |
| `here-now` | Publishes a file/folder/HTML to a live shareable URL | — |

```
.codex/
├── AGENTS.md
├── config.toml                     ← [features] multi_agent + 3 [agents.*] registrations
├── agents/                         ← agent role personas (the source of truth)
│   ├── critical-friend.toml
│   ├── fact-checker.toml
│   └── writing-editor.toml
└── skills/
    ├── critical-review/
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── critical-friend.md   ← readable copy of agents/critical-friend.toml
    │   │   └── fact-checker.md      ← readable copy of agents/fact-checker.toml
    │   ├── checklist.md
    │   └── examples/before-after.md
    ├── proofread/
    │   ├── SKILL.md
    │   ├── references/writing-editor.md  ← readable copy of agents/writing-editor.toml
    │   └── checklist.md
    ├── visual-explainer/SKILL.md
    └── here-now/SKILL.md
```

## Discovery — read this before the session

- **Skills:** Codex auto-discovers skills in `$CODEX_HOME/skills` (`~/.codex/skills`). It also reads a **project config layer**, but if your build doesn't pick up project-local `.codex/skills/`, symlink them: `ln -s "$(pwd)/.codex/skills/<name>" ~/.codex/skills/<name>` (or `cp -R .codex/skills/* ~/.codex/skills/`).
- **Agent roles:** registered in the project `.codex/config.toml` (`[agents.*]` → `config_file`), with personas in `.codex/agents/*.toml`. Codex loads agent roles from the config layers (Managed / User / project). If your build only reads agent roles from `~/.codex/config.toml`, merge the `[features]` + `[agents.*]` blocks into that file and copy the `agents/` folder beside it. Verify with `codex` → `/status`, or check that a `spawn_agent` with `agent_role: "critical_friend"` resolves.

## Two things worth verifying for the session

1. **Agent roles loaded** — confirm Codex sees `critical-friend`, `fact-checker`, `writing-editor` (see discovery note above). If not, the skills fall back to running each persona in-thread.
2. **Web search** — the `fact-checker` role verifies claims via web search against authoritative primary sources. Make sure web search is enabled in the Codex session. If it isn't, the role marks claims "Unverifiable" rather than inventing a verification.
