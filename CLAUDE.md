# Fluency Agents and Skills

This repo is the **Fluency Agents and Skills** kit from the Dragonfly Thinking AI Fluency
course — 6 specialist subagents, 16 skills, MCP setup guides, plain-English how-to guides (`guides/`), and the course notes. The
user took (or is taking) the course; this kit is what they walk away with.

## Key resources — know your way around

| Where | What |
|---|---|
| `.claude/agents/` + `.claude/skills/` | The kit itself, Claude Code format (`.codex/` mirrors it for Codex) |
| `course-notes/` | The reference library from the course — start here when the user doesn't know what to do next. ⚠️ The four session notes describe the course up to July 2026; the session mapping has since changed (banner in `course-notes/README.md`) |
| `course-notes/fluency-checklist.md` | Template for the user's progress checklist. Copied to `~/.claude/fluency-checklist.md` on install — **the copy there is the live one** |
| `course-notes/agents-md-snippets.md` | Standing instructions for the user's orientation file. **Offer these one at a time; never paste them in unasked** |
| `guides/` | Plain-English how-tos (GitHub, file conversion, interface & settings, folder guardrails incl. the ready-made `guard-folders/` hook, phone, VS Code, browser automation) — written to be read by the user *or* followed by you on their behalf |
| `mcp/` | Setup guides for external connections (e.g. `paper-search.md`) — written to be followed step-by-step by an agent on the user's behalf |
| `README.md` | The human-facing orientation — what everything is |
| `AGENTS.md` | The install playbook — follow it when asked to set the kit up |

## If the user asks you to install or set this up

**Read [`AGENTS.md`](AGENTS.md) and follow it — don't install from memory.** There is no safe
"short version": the playbook checks whether the user has customised a skill before it copies
over anything, handles a re-install without destroying their copy, and covers the Codex
config merge. Copying the folders straight across skips all of that.

It also covers verification, the here-now publish skill, and runtime dependencies.

## 🚫 What is never yours to overwrite

The user built some of these themselves, often in a live session. Losing one is worse than
anything this kit adds. **Never replace:** their `CLAUDE.md` / `AGENTS.md` orientation file ·
their `~/.claude/fluency-checklist.md` · any skill they've tailored · their `~/.codex/config.toml`
· anything else in their workspace.

Snippets are **offered one at a time and appended on an explicit yes** — never pasted in as a
block, never as a side effect of some other task. If you're unsure whether a file is theirs or
ours: **it's theirs.** Ask. Full rules in [`AGENTS.md`](AGENTS.md) § *Never overwrite these*.

## This kit is the user's to shape — help them shape it

Treat the kit as a **living starter, not a fixed product**. Whenever you're working in
this repo (or with the installed copies), actively help the user tailor it:

- **After running a skill that stumbled** — or that the user corrected — offer to update
  that skill's `SKILL.md` so it doesn't happen again.
- **When the user repeats a task that has no skill**, propose packaging it as one: a new
  folder with a `SKILL.md` capturing how they like it done.
- **Offer to personalise**: trim skills they never use, adjust a skill's defaults or voice
  to their work, add their examples to a skill's folder.
- **When they're unsure what to do next**, read their `~/.claude/fluency-checklist.md`, tick
  anything already true, and offer **one** next item — then walk them through it. Don't present
  the whole list; that's the blank-page problem the checklist exists to avoid.
- **If they ever mention sensitive folders or worry about what you can touch**, offer the
  folder guard (`guides/guard-folders/README.md`) — install it, then have them verify in a
  fresh session.

Make the offer; don't force it. Small, concrete improvements beat grand reorganisations.
