---
name: research-brief
description: >-
  Turns a topic or question into a synthesised, structured, cited brief — not a
  list of links. Spawns the web-searcher subagent, tiers each source by
  credibility, then writes the brief itself. Use for "brief me on X", "research X
  and give me the picture", "what do I need to know about [company / market /
  person] before my call", or "synthesise these sources for me". NOT for a raw
  link dump (spawn web-searcher directly) or checking one specific claim (use
  critical-review).
version: 1.1.0
metadata:
  short-description: Synthesised, cited brief on a topic
---

# Research Brief

Turn a topic or question into a brief the user can act on: a synthesised, structured, cited
read — not "here are 10 links". The searching is delegated; the **synthesis is yours**.

## How to invoke

Run three stages. Don't jump straight to searching — the plan step is what saves wasted briefs.

**Stage 1 — Plan (ask, then get a nod).** If the question is ambiguous, ask one or two
clarifying questions before searching — scope, depth, source type. Common asks:

- "When you say 'AI safety regulation' — global, US, or EU specifically?"
- "Academic literature, or industry/press sources?"
- "Is this for a decision you're about to make, or background reading?"

Then sketch the handful of queries you'll run and get the user's nod before spending the time.

**Stage 2 — Search (delegate).** Spawn a subagent with **agent_role: "web_searcher"**
(registered in `.codex/config.toml` as `[agents.web_searcher]`, persona in
`.codex/agents/web-searcher.toml`) — you spawn it by name and hand it the planned queries; it
can run several in parallel. For every source it returns, tag a credibility tier:

- **Primary** — original studies, official documents, on-record statements.
- **Reputable secondary** — established journalism, peer-reviewed reviews, analyst reports.
- **Weaker** — blog posts, opinion pieces, AI-generated summaries.

If a strand comes back thin, spawn web-searcher again for deeper or different sources rather
than synthesising from weak material. If subagent spawning is disabled in this session, follow
the web-searcher persona yourself (it's in `.codex/agents/web-searcher.toml`) — gather and cite
the sources, then continue to Stage 3.

**Stage 3 — Synthesise (yours, not the subagent's).** Do **not** paste web-searcher's
summaries. Weigh the sources against each other, surface where they disagree, and write the
brief in the structure below. Every claim carries a citation.

## Output

Write the brief with these exact sections, top-down so the user can stop after the bottom line:

```
## The question
[restated in plain terms so you're aligned]

## Bottom line
[the answer in <=3 sentences]

## Key findings
[4-7 points, each with its evidence and citation]

## What's contested
[where sources disagree, and why]

## What's missing
[what wasn't findable; what would need primary research]

## Sources
[every source, with its credibility tier]
```

**Hard rule:** if the brief rests mostly on *weaker* (tier-3) sources, say so in one line at
the very top, above the bottom line — before anything else. The user decides whether to send
you back for better sources or accept what's available. Never bury a thin evidence base.

## Gotchas

- **Don't paste the subagent's output.** web-searcher gathers and cites; the synthesis — the
  weighing, the tensions, the structure — is this skill's whole job. A brief that's just
  pasted search results has failed.
- **Cite every claim.** An uncited assertion in a brief is indistinguishable from a guess.
- **Flag a thin evidence base at the top, not in a footnote.** The tier-3 warning is
  load-bearing; it changes whether the user trusts the brief.
- **Sources-only mode is a different ask.** If the user just wants ranked links with one-line
  annotations, skip Stage 3 and return web-searcher's list — don't force a full synthesis.

## Reference

- **`.codex/agents/web-searcher.toml`** — the canonical persona Codex loads (registered via
  `[agents.web_searcher]` in `config.toml`).
- [references/web-searcher.md](references/web-searcher.md) — readable copy of the same persona.

## Pairs well with

- **web-searcher subagent** — the specialist this skill leans on to gather and cite sources.
- **visual-explainer** — turn the finished brief into a one-page explainer for someone else.
