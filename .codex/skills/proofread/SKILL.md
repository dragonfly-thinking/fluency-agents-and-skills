---
name: proofread
description: >-
  Proofreads and improves a draft for clarity, grammar, structure, and tone by
  spawning the writing-editor subagent. Use when the user asks to "proofread",
  "polish", "tidy up", "check", or "edit" a piece of writing — emails, briefing
  notes, abstracts, paragraphs, drafts of anything. Returns tracked-style
  suggestions plus a cleaned version. Does not check argument quality or facts.
version: 1.1.0
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
- **Rewriting from scratch** → that's a rewrite, not a proofread; brief the writing-editor with that explicit instruction instead

## Output

The writing-editor returns a structured edit list plus a cleaned version. Present its output to the user as-is. Do not summarise or filter — the writer needs to see the actual edits.

Expect this shape (pass it straight through):

```
## Edits
### Grammar & typos — quote → fix → one-line reason if non-obvious
### Clarity — quote → rewrite → reason
### Structure — merge / split / transition notes
### Tone — only if there's a real issue

## Cleaned version
[the full draft with edits applied; structural moves footnoted]
```

## Gotchas

- **Don't re-edit the writing-editor's output in the main thread.** Running it through a second voice undoes the voice-preservation the subagent just did — present its edits and cleaned version as-is.
- **Don't fire this on a fact-check or argument request.** "Is this true?" or "is this convincing?" is `critical-review`, not proofread — this pass only touches the writing, never the thinking or the facts.

## Reference

- **`.codex/agents/writing-editor.toml`** — the canonical persona Codex loads (registered via `[agents.writing_editor]` in `config.toml`)
- [references/writing-editor.md](references/writing-editor.md) — readable copy of the same persona
- [checklist.md](checklist.md) — the editing pass criteria the writing-editor applies
