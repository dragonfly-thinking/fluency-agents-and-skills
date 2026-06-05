---
name: proofread
description: >-
  Proofreads and improves a draft for clarity, grammar, structure, and tone by
  delegating to the writing-editor subagent. Use when the user asks to
  "proofread", "polish", "tidy up", "check", or "edit" a piece of writing —
  emails, briefing notes, abstracts, paragraphs, drafts of anything. Returns
  tracked-style suggestions plus a cleaned version. Does not check argument
  quality or facts.
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
- **Rewriting from scratch** → just ask the writing-editor directly with that brief

## Output

The writing-editor returns a structured edit list plus a cleaned version. Present the subagent's output to the user as-is. Do not summarise or filter — the writer needs to see the actual edits.

## Reference

See [checklist.md](checklist.md) for the editing pass criteria the writing-editor applies.
