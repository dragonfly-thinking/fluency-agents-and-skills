---
name: critical-review
description: Stress-tests a draft argument or position by delegating in parallel to the critical-friend subagent (challenges the thinking) and the fact-checker subagent (verifies factual and statistical claims against authoritative primary sources via web search). Use when the user is about to commit to an argument, publish a policy memo, send a briefing note, or otherwise wants their reasoning and evidence pressure-tested before it goes out. Returns a synthesised review: pushbacks, counter-position, what would have to be true to be wrong, and per-claim fact-check verdicts.
---

# Critical Review

A heavy review pass. Use this at milestones — before sending the briefing, before publishing the argument, before committing to a position.

This skill **orchestrates two subagents in parallel** because the two jobs are independent:

- **critical-friend** challenges the argument (reasoning, assumptions, missing voices)
- **fact-checker** verifies the claims (statistics, facts, named figures)

Running them in parallel halves the wall-clock time and keeps each subagent's context focused on its own job.

## How to invoke

```
Step 1 — Confirm scope with the user (one question if needed):
  "What's the audience and stakes for this draft? Internal note, public memo, ministerial briefing?"

Step 2 — Spawn both subagents in parallel (single message, two Task tool calls):

  Invocation A: critical-friend
    Input: the full draft + audience/stakes
    Returns: pushbacks, steel-manned counter-position, hidden assumptions, missing voices

  Invocation B: fact-checker
    Input: the full draft
    Returns: per-claim verdicts (verified / incorrect / unverifiable)

Step 3 — Synthesise the two outputs (see Output section below).
```

**Critical:** spawn them in parallel, not sequentially. The skill's whole advantage is the fan-out.

## Output

Present the two subagent outputs side-by-side under clear headings. Do **not** collapse them — the user needs to see which findings came from which lens.

```
# Critical Review

## What the Critical Friend found
[critical-friend's full output]

## What the Fact-checker found
[fact-checker's full output]

## Summary
- Strongest pushback: [one line]
- Most significant factual issue: [one line]
- Recommendation: [proceed / revise / rethink]
```

The summary at the bottom is short — two lines and a recommendation. Don't bury the headline.

## What this skill is for

- Pre-send check on policy memos, briefing notes, formal arguments
- Stress-testing recommendations before they're committed
- Catching wrong statistics and weak reasoning in the same pass
- Any "before this goes out" moment

## What this skill is NOT for

- **Light grammar/clarity pass** → use the `proofread` skill instead (much faster)
- **Doing the rewrite for the user** → this skill identifies issues; the user (or a follow-up `proofread` call) handles the fix
- **Pure fact-checking with no argument review** → invoke fact-checker directly

## Sequencing with proofread

The natural workflow is:

1. Draft something
2. Run `proofread` (light, fast)
3. Apply the cleaned version
4. Run `critical-review` (heavy, slower)
5. Decide what to do with the pushbacks and fact-check findings

Running `critical-review` before `proofread` works too — but the writing should be coherent enough that the critical-friend isn't tripping on grammar.

## Reference

- [checklist.md](checklist.md) — the lenses the two subagents apply
- [examples/before-after.md](examples/before-after.md) — a worked example
