---
name: verify-work
description: >-
  Check a finished piece of agent (or human) work against what was actually
  asked for, using fresh adversarial sub-agents that had no part in producing
  it. Use after a task completes — "verify this", "check the agent did what I
  asked", "did this meet the brief?" — before you rely on or send the result.
version: 1.0.0
---

# Verify Work

> An agent should never mark its own homework. Get a fresh one to tear it apart.

At the end of the day *you're* responsible for what the agent produces — so build
verification into the workflow instead of hoping. This skill takes the original
request and the finished work, then spins up **fresh adversarial reviewers** whose
only job is to find where the work falls short. They weren't involved in producing
it, they have no stake in it looking good, and they're told to be sceptical.

**When to use this skill:**
- "Verify this against what I asked for"
- "Did the agent actually do everything in the brief?"
- After any sub-agent or background routine finishes a substantial piece of work
- Before sending a deliverable to someone whose opinion matters

---

## How a run works

### Step 1 — Pin down the requirements

The skill first establishes what "done" was supposed to mean. It looks for, in order:

1. The **original request** — the prompt, brief, plan file, or task file that kicked
   the work off. If it's in the conversation, use that; if it's in a project folder
   (an `overview.md`, `plan.md`, or task file), read it.
2. Anything the requirements **imply but don't state** — e.g. "summarise each
   document" implies *every* document got summarised, not most of them.

If no clear requirements exist, the skill asks the user one question — *"what did
you ask for, in your own words?"* — rather than inventing a standard.

Write the requirements out as a **numbered checklist** before reviewing anything.
That checklist is the contract the reviewers verify against.

### Step 2 — Send in the adversarial reviewers

Spin up **one to three fresh sub-agents** depending on the size of the work. Each
gets: the requirements checklist, the finished work (or paths to it), and an
explicitly adversarial brief:

> *"You did not produce this work and you should assume it has problems. For each
> requirement, hunt for evidence it was NOT met — things skipped, done partially,
> done differently from what was asked, or claimed but not actually done. Check the
> files themselves, don't trust any summary. Report concrete evidence, not
> impressions."*

Useful reviewer lenses when running more than one:

| Lens | What it hunts for |
|------|-------------------|
| **Completeness** | Requirements skipped or half-done; the item quietly dropped from a list of ten |
| **Correctness** | Claims that don't match the source; numbers, names and quotes that don't check out (delegates well to the **fact-checker** agent) |
| **Fitness** | It's complete and accurate — but is it actually what was *asked for*? Right format, right audience, right length? |

### Step 3 — The verdict

Report back as a table — one row per requirement:

```
| # | Requirement            | Verdict     | Evidence                              |
|---|------------------------|-------------|---------------------------------------|
| 1 | Summarise all 12 docs  | ⚠️ Partial   | 11 summaries found; doc 07 missing     |
| 2 | Cite sources           | ✅ Met       | Every claim carries a working link     |
| 3 | Under two pages        | ❌ Not met   | Output is 4 pages                      |
```

Three verdicts only: **Met** (with where the evidence is), **Partial / Not met**
(with the concrete gap), or **Can't verify** (say what would be needed to check —
never round "couldn't check" up to "fine").

End with a one-line overall call: *safe to use as-is*, *usable after these fixes*,
or *needs a redo* — and offer to fix the gaps.

---

## Calibration

- **Evidence, not vibes.** A reviewer saying "looks good" is worthless. Every
  verdict points at something checkable — a file, a line, a count.
- **The gaps hide in the middle.** Agents rarely botch the first or last item in a
  list; they drop item 7 of 12. Completeness reviewers should count.
- **Don't gold-plate.** The standard is the *requirements*, not perfection. If the
  work meets the brief, say so and stop — a verifier that always finds something
  trains you to ignore it.

## What it does *not* do

- Doesn't verify subjective quality ("is this insightful?") — it verifies the work
  against what was asked
- Doesn't replace your judgement on whether the *requirements themselves* were right
- Doesn't fix anything without asking first

## Pairs well with

- **critical-friend** — for pressure-testing the *argument* in a piece of work, not
  just its compliance with the brief
- **fact-checker** — the correctness lens for factual/statistical claims
- **new-project** — task files written by `new-project` make ideal requirement
  checklists to verify against
