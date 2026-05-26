---
name: critical-review
description: Stress-tests a draft argument or position by spawning two subagents in parallel — one that challenges the thinking (the critical-friend brief) and one that verifies statistical and factual claims via web search against authoritative sources (the fact-checker brief). Use when the user is about to commit to an argument, publish a policy memo, send a briefing note, or otherwise wants their reasoning and evidence pressure-tested before it goes out. Returns a synthesised review — pushbacks, counter-position, what would have to be true to be wrong, and per-claim fact-check verdicts.
metadata:
  short-description: Pressure-test an argument and fact-check its claims
---

# Critical Review

A heavy review pass. Use this at milestones — before sending the briefing, before publishing the argument, before committing to a position.

This skill **spawns two subagents in parallel** because the two jobs are independent:

- **critical-friend** challenges the argument (reasoning, assumptions, missing voices)
- **fact-checker** verifies the claims (statistics, facts, named figures)

Running them in parallel halves the wall-clock time and keeps each subagent's context focused on its own job.

## How to invoke

```
Step 1 — Confirm scope with the user (one question if needed):
  "What's the audience and stakes for this draft? Internal note, public memo, ministerial briefing?"

Step 2 — Spawn both subagents in parallel (spawn_agent, two calls in one go):

  Subagent A — agent_role: "critical_friend"
    Input prompt: the full draft + audience/stakes
    Returns: pushbacks, steel-manned counter-position, hidden assumptions, missing voices

  Subagent B — agent_role: "fact_checker"
    Input prompt: the full draft
    Returns: per-claim verdicts (verified / incorrect / unverifiable)

Step 3 — Synthesise the two outputs (see Output section below).
```

Both roles are registered in `.codex/config.toml` (`[agents.critical_friend]` and `[agents.fact_checker]`), with their personas in `.codex/agents/critical-friend.toml` and `.codex/agents/fact-checker.toml`. You spawn them by name; you do not need to paste a brief.

**Critical:** spawn them in parallel, not sequentially. The skill's whole advantage is the fan-out. Pass each subagent only the draft (plus audience/stakes for the critical-friend) — don't leak one lens's conclusions into the other.

If subagent spawning is disabled in this session, fall back to running both roles yourself sequentially in one context, switching hats — the persona text is in `.codex/config.toml`. Keep the two lenses' outputs strictly separate.

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
- **Pure fact-checking with no argument review** → use only the fact-checker brief

## Sequencing with proofread

The natural workflow is:

1. Draft something
2. Run `proofread` (light, fast)
3. Apply the cleaned version
4. Run `critical-review` (heavy, slower)
5. Decide what to do with the pushbacks and fact-check findings

Running `critical-review` before `proofread` works too — but the writing should be coherent enough that the critical-friend isn't tripping on grammar.

## The two agent roles

Registered in **`.codex/config.toml`**, with personas in **`.codex/agents/`** — that's what Codex loads:

- `[agents.critical_friend]` → `agents/critical-friend.toml` — challenges the argument
- `[agents.fact_checker]` → `agents/fact-checker.toml` — verifies claims via web search

The `references/*.md` files are human-readable copies for browsing; the `.codex/agents/*.toml` files are the source of truth.

## Reference

- [references/critical-friend.md](references/critical-friend.md) — readable copy of the critical-friend persona
- [references/fact-checker.md](references/fact-checker.md) — readable copy of the fact-checker persona
- [checklist.md](checklist.md) — the lenses the two subagents apply
- [examples/before-after.md](examples/before-after.md) — a worked example
