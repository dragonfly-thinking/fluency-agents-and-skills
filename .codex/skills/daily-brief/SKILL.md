---
name: daily-brief
description: >-
  Morning rundown — today's calendar, top emails, and one research item the user
  cares about. Use when the user says "what's on for today?", "give me my morning
  brief", "brief me before I start", or wants to start the day oriented instead of
  reactive. Runs once at the start of the day and stops — it briefs, it doesn't act.
version: 1.1.0
---

# Daily Brief

The user's morning rundown. Run it once at the start of the day so they know what matters before the inbox pulls them in.

**When to use this skill:**
- "What's on for today?"
- "Give me my morning brief"
- "Brief me before I start"
- First thing in the morning, before opening email

---

## What to produce

A short, scannable summary with three sections:

1. **Today's calendar** — meetings, conflicts, where the user needs to be
2. **Top inbox items** — only what needs the user (not a digest of everything)
3. **One thing worth knowing** — a research item from a topic the user tracks (news, market, a person, an industry)

Keep it to one screen. Less is the point. Never auto-send, auto-archive, or take any action — brief and stop.

---

## How to assemble it

Delegate the research legs to subagents, then compose the three sections yourself:

- **Vault Librarian** (subagent) — finds the user's tracked topics, ongoing projects, and anything flagged yesterday
- **Web Searcher** (subagent) — fetches today's relevant news on those topics for the "one thing worth knowing" item

For the inbox section, read the user's email through a connected email MCP (Gmail, Outlook) if one is available, and surface only messages that need a response. If no email MCP is connected, say so and produce the brief without the inbox section rather than inventing items.

---

## First-run setup

The brief needs a little context to be useful. On the first run, if `config.json` does **not** exist in this skill directory, ask the user four things and save them (use the `AskUserQuestion` tool to present the choices cleanly):

1. **Time zone** — so "today" resolves correctly
2. **Tracked topics** — for the "one thing worth knowing" item
3. **Calendar source** — Google Calendar, Outlook, or paste-in
4. **Email source** — Gmail, Outlook, or skip

Save to `config.json` in this skill directory:

```json
{
  "timezone": "Europe/Madrid",
  "topics": ["trade policy", "AI regulation", "EV market"],
  "calendar_source": "google",
  "email_source": "gmail"
}
```

On every subsequent run, read `config.json` first and skip the questions — the user just says "daily brief" and goes. If they ask to change a tracked topic or a source, update the file.

---

## Example

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

Run without the research item — just calendar + inbox.

---

## Gotchas

- **Don't invent inbox items.** If no email MCP is connected, the inbox section has no data — omit it and say why. A fabricated "3 emails need you" is worse than no inbox section.
- **One research item, not a digest.** The "worth knowing" section is a single item tied to a tracked topic. If nothing relevant surfaced today, say "nothing notable on your topics" rather than padding with generic headlines.
- **Respect the time zone.** "Today" is meaningless without `config.json`'s `timezone` — a brief built in the wrong zone shows yesterday's or tomorrow's calendar. Read the config before resolving dates.
- **Brief, don't act.** No replying, archiving, accepting invites, or sending. This skill surfaces; the user decides.

---

## Pairs well with

- **Research Brief** — go deeper on the one "worth knowing" item the brief surfaces
