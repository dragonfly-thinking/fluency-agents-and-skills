---
name: handoff
description: >-
  Capture the current conversation as a handover document a fresh session can
  pick up from — what we were doing, what's decided, what's done, what's next,
  and exactly which files matter. Use when a chat is getting long, before
  stopping for the day, or any time you want work to survive a new session.
version: 1.0.0
---

# Handoff

> The chat is ephemeral. The handover file is what survives.

Every new session starts as a blank slate, and the automatic summaries agents make
when a conversation gets long are lossy — they don't know which small detail was
the crucial one. This skill writes the handover *deliberately*, as a file in your
workspace, so the next session (or a colleague, or you in three weeks) can pick up
exactly where this one left off.

**When to use this skill:**
- "Write a handoff" / "hand this over to a fresh session"
- The context is filling up and you want to continue in a new chat
- End of a work block on something you'll come back to
- Before handing the same task to a different agent (or person)

---

## What it writes

One Markdown file — `handoff.md` in the relevant project folder (or
`handoffs/YYYY-MM-DD-topic.md` if one already exists there). A few labels at the
top (`status`, `updated`), then five short sections:

1. **What this is** — the task/project in two sentences, and *why* it's being done.
2. **State of play** — what's been completed (with file paths to the outputs),
   what's in progress, what hasn't started.
3. **Decisions made** — anything agreed in conversation that isn't visible in the
   files, each with its one-line *why*. This is the section most handovers miss —
   and the reason the next session re-litigates settled questions.
4. **Next steps** — the concrete next actions, in order, starting with the very
   next thing to do.
5. **Read these first** — the 3–6 files a fresh session should open, in order,
   with a word on why each matters.

Keep it to about a page. A handover nobody reads is as useless as no handover.

## How to resume from one

In the new session, just point at the file:

> *"Read `handoff.md` in this folder and pick up where it leaves off."*

If the project has an orientation file (`CLAUDE.md` / `AGENTS.md`), the skill also
offers to add one line to it — *"if a `handoff.md` exists here, read it before
starting work"* — so future sessions find it without being told.

## Calibration

- **Write for a stranger.** The next session knows nothing this conversation knew.
  Codenames, shorthand, and "the approach we discussed" all need spelling out.
- **Decisions beat narrative.** Skip the story of how we got here; record what was
  *decided* and why. That's what stops the next session undoing it.
- **Paths, not descriptions.** "The draft" is useless; `projects/report/draft-v2.md`
  is a handover.

## Pairs well with

- **new-project** — projects set up with `new-project` already have a `progress.md`;
  the handoff complements it with the conversation-level state
- **weekly-review** — a week's worth of handoffs makes the review write itself
