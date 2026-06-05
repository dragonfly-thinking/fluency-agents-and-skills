---
name: research-brief
description: >-
  Structured brief on a topic. Orchestrates web search, source assessment, and
  synthesis. The "now synthesise it" follow-up to a raw Web Searcher run. Use
  when you want a real briefing, not just a list of links.
version: 1.0.0
---

# Research Brief

Turn a topic or question into a brief you can actually use. Not "here are 10 links" — a synthesised, structured read.

**When to use this skill:**
- "Brief me on [topic]"
- "Research X and give me the picture"
- "What do I need to know about [company / market / person]?"
- "Synthesise these sources for me"

---

## What you get

A structured brief, typically 1-2 pages, with:

1. **The question** — restated in plain terms so we're aligned
2. **Bottom line** — the answer in three sentences if you only read the top
3. **Key findings** — 4-7 points with evidence
4. **What's contested** — where sources disagree, and why
5. **What's missing** — what wasn't findable, what would need primary research
6. **Sources** — every claim tied to a citation

Designed to read top-down: stop after the bottom line if that's all you need.

---

## How it works

Three stages:

1. **Plan** — the skill asks one or two clarifying questions ("how deep?", "any sources to anchor on?"), then sketches what it'll search for. You approve before it runs.
2. **Search** — delegates to **Web Searcher** for multiple parallel queries, then evaluates each source for credibility (publication, date, primary vs secondary).
3. **Synthesise** — the skill itself does the writing. It doesn't paste in summaries — it weighs sources, finds the tensions, and writes a coherent brief.

Total time: 3-8 minutes for a real topic. Faster than you doing it yourself; slower than asking ChatGPT a vague question and getting a shallow answer.

---

## When it asks clarifying questions

The skill won't just dive in if the question is ambiguous. Common asks before it starts:

- "When you say 'AI safety regulation' — global, US, or EU specifically?"
- "Do you want academic literature or industry/press sources?"
- "Is this for a decision you're about to make, or background reading?"

This matters because "research on X" can mean six different things. Two questions up front saves you a wasted brief.

---

## Source discipline

The skill flags sources by tier:

- **Primary** — original studies, official documents, on-record statements
- **Reputable secondary** — established journalism, peer-reviewed reviews, analyst reports
- **Weaker** — blog posts, opinion pieces, AI-generated summaries

A brief that's mostly tier-3 sources gets flagged at the top. You decide whether to send the skill back for better sources or accept what's available.

---

## Examples

### "Brief me on Australia's critical minerals strategy"

The skill asks: "Recent (last 12 months) or historical context too?" You say recent. Off it goes — 4 minutes later you have a brief with the 2023 update, key minerals on the list, partnerships with Japan/US/EU, and the unresolved tensions around lithium processing.

### "What's the deal with this company before my call?"

Faster mode: company name + LinkedIn → one-page brief on what they do, recent news, who's investing, where the friction is. A fast way to prep before a call.

### "Just give me the sources, I'll read them"

You can ask for the sources-only mode. Skips the synthesis step. Returns a curated, ranked list with one-line annotations.

---

## Pairs well with

- **Daily Brief** — the "worth knowing" item often becomes a Research Brief
- **Visual Explainer** — turn the brief into a one-page explainer for someone else
- **Web Searcher subagent** — the specialist this skill leans on to gather and cite sources
