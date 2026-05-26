---
name: proofread
description: Proofreads and improves a draft for clarity, grammar, structure, and tone by spawning the writing-editor subagent. Use when the user asks to "proofread", "polish", "tidy up", "check", or "edit" a piece of writing — emails, briefing notes, abstracts, paragraphs, drafts of anything. Returns tracked-style suggestions plus a cleaned version. Does not check argument quality or facts.
metadata:
  short-description: Light clarity, grammar, structure, and tone pass
---

# Proofread

A light writing pass. Use this every time the user is about to send or publish something and wants the writing tightened.

## How to invoke

Spawn a subagent with **agent_role: "writing_editor"** (registered in `.codex/config.toml` as `[agents.writing_editor]`, persona in `.codex/agents/writing-editor.toml`). You spawn it by name and don't paste a brief. Give it as the prompt:

- The draft (full text)
- The document type (email / briefing note / abstract / blog post / other)
- The audience (if known)

If the document type or audience isn't obvious, ask the user one question before spawning.

If subagent spawning is disabled in this session, follow the writing-editor persona yourself in the main thread (it's in `.codex/agents/writing-editor.toml`) — it's a single-pass task, so this works fine.

## What this skill is for

- Pre-send check on emails, briefing notes, drafts
- Cleaning up dictated text
- Sanding a paragraph the user is unsure about
- Catching typos and clarity issues in something near-final

## What this skill is NOT for

- **Stress-testing an argument** → use the `critical-review` skill instead
- **Fact-checking statistics** → use the `critical-review` skill (it includes fact-checking)
- **Rewriting from scratch** → just hand the writing-editor brief that explicit instruction

## Output

The writing-editor returns a structured edit list plus a cleaned version. Present its output to the user as-is. Do not summarise or filter — the writer needs to see the actual edits.

## Reference

- **`.codex/agents/writing-editor.toml`** — the canonical persona Codex loads (registered via `[agents.writing_editor]` in `config.toml`)
- [references/writing-editor.md](references/writing-editor.md) — readable copy of the same persona
- [checklist.md](checklist.md) — the editing pass criteria the writing-editor applies
