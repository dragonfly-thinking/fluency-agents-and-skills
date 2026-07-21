---
name: proofread
description: >-
  Proofreads and improves a draft for clarity, grammar, structure, and tone by
  delegating to the writing-editor subagent. Use when the user asks to
  "proofread", "polish", "tidy up", "check", or "edit" a piece of writing —
  emails, briefing notes, abstracts, paragraphs, drafts of anything. Returns
  tracked-style suggestions plus a cleaned version. Does not check argument
  quality or facts.
version: 1.1.0
---

# Proofread

A light writing pass. Use this every time the user is about to send or publish something and wants the writing tightened.

## How to invoke

Delegate the work to the **writing-editor** subagent. Do not do the editing yourself in the main thread — the subagent has the right instructions for voice preservation, register matching, and output format.

```
Invoke writing-editor with:
- The draft (full text)
- The document type (email / briefing note / abstract / blog post / other)
- The audience (if known)
```

If the document type or audience isn't obvious, ask the user one question before invoking.

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

The writing-editor returns a structured edit list plus a cleaned version. Present the subagent's output to the user as-is. Do not summarise or filter — the writer needs to see the actual edits.

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

See [checklist.md](checklist.md) for the editing pass criteria the writing-editor applies.
