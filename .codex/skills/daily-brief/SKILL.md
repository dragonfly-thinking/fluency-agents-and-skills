---
name: daily-brief
description: Morning rundown — today's calendar, top emails, and one research item
  you care about. Use when you want to start the day oriented instead of reactive.
---

# Daily Brief

Your morning rundown. Run this once at the start of the day and walk away knowing what matters before the inbox pulls you in.

**When to use this skill:**
- "What's on for today?"
- "Give me my morning brief"
- "Brief me before I start"
- First thing in the morning, before opening email

---

## What you get

A short, scannable summary with three sections:

1. **Today's calendar** — meetings, conflicts, where you need to be
2. **Top inbox items** — anything that needs you (not a digest of everything)
3. **One thing worth knowing** — a research item from a topic you care about (news, market, a person, an industry)

Designed to fit on one screen. Less is the point.

---

## How it works

Under the hood this skill delegates to two subagents:

- **Vault Librarian** — finds your tracked topics, ongoing projects, and what you flagged yesterday
- **Web Searcher** — fetches today's relevant news on those topics
- **Inbox Triager** *(when MCP is wired)* — surfaces only the emails that need a response

It doesn't auto-send anything, doesn't auto-archive, doesn't act. It briefs you and stops.

---

## Customising the brief

The first time you run this, the skill asks:

- **What time zone?** — so "today" makes sense
- **What topics do you track?** — for the "one thing worth knowing" item
- **Calendar source** — Google Calendar, Outlook, or paste in
- **Email source** — Gmail, Outlook, or skip

These are saved so the next morning you just say "daily brief" and go.

---

## Examples

### "Daily brief"

```
Today — Tuesday 21 May

Calendar:
  09:00  Team standup (15 min)
  11:00  Client call — ACME (1 hr, prep doc attached)
  14:30  1:1 with Anthea (30 min, no agenda yet)

Inbox (3 need you):
  · Sarah — quote signoff, waiting since Friday
  · Legal — contract revision, asks for reply today
  · Conference organiser — speaker bio still missing

Worth knowing:
  · Bloomberg reports new tariff signals on EV imports — relevant to
    your "trade policy" topic. One paragraph summary attached.
```

### "Brief me, but skip the news today"

The skill runs without the research item — just calendar + inbox.

---

## Pairs well with

- **Weekly Review** — Friday afternoon equivalent of this skill
- **Research Brief** — go deeper on the one "worth knowing" item the brief surfaces
