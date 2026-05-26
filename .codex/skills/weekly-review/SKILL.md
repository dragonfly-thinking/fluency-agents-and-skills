---
name: weekly-review
description: End-of-week summary — what got done, what's stuck, what's slipping, what
  to consider for next week. Reads your calendar, processed meetings, and vault. Use
  Friday afternoon or first thing Monday.
---

# Weekly Review

Friday afternoon (or Monday morning), this skill produces a one-page review of the week — what happened, what didn't, and what's worth carrying forward.

**When to use this skill:**
- "Run my weekly review"
- "Where am I at?"
- Friday at 4pm, before logging off
- Monday at 8am, before the new week kicks in

---

## What you get

Five sections:

1. **Done** — meetings held, decisions made, things shipped or sent
2. **Open** — actions still in flight, with where each one is stuck
3. **Slipping** — things that were supposed to happen this week and didn't
4. **New** — things that landed mid-week and changed the picture
5. **Next week** — proposed focus areas, given what's open + what's coming up

Not a feed dump. The skill weighs what matters and skips what doesn't.

---

## How it builds it

The skill orchestrates several specialists:

- **Vault Librarian** — reads any meeting notes processed this week, any project files updated
- **Project Planner** — reads your active project files for what's open vs. closed
- **Inbox Triager** *(MCP)* — finds emails you flagged but didn't action
- The skill itself stitches these into a coherent review and weighs significance

It looks at *this week's signal*, not all-time history. Designed for habitual weekly use, not a one-off audit.

---

## What "slipping" means

Three thresholds:

| Severity | What it looks like | What the skill does |
|----------|---------------------|---------------------|
| Drift | Something has moved a few days | Flag, no fuss |
| Slip | Something missed a stated deadline | Flag with context — why? |
| Stall | Something hasn't moved in 2+ weeks | Flag prominently, ask if it's still worth pursuing |

The skill won't nag you about everything. It's looking for patterns worth your attention.

---

## Customisation

First time you run this, the skill asks:

- **Week start day?** (Default: Monday)
- **Working days?** (Default: Mon–Fri; relevant for the "slipping" calculation)
- **Where do projects live?** (Default: `projects/` in your vault)
- **Output destination?** (File in vault, email to self, Slack DM, or just print)

These save and the next review just runs.

---

## Examples

### "Weekly review"

```
Week of 19–23 May

Done (this week)
  · 4 client calls (ACME, Beta, Gamma, Delta)
  · SOW v2 sent to ACME — signed back Wed
  · New onboarding flow shipped to staging
  · 2 hires moved to final round

Open (in flight)
  · Q3 budget — waiting on Sarah at ACME (since Mon)
  · Onboarding handoff to CS — meeting booked for Jun 4
  · Pricing tier review — Sam owes draft by Tue 28

Slipping
  · Conference speaker bio — due Tue, still draft
  · Q2 retro doc — was for last week, hasn't moved

Stalling (2+ weeks)
  · Partnership exploration with Stripe — no movement since 7 May.
    Worth keeping alive or close?

Next week — proposed focus
  1. Ship the pricing tier draft (you owe Tue)
  2. Unblock Q3 budget conversation with ACME
  3. Process the 4 meeting transcripts sitting in your inbox
  4. Decide on the Stripe thread (don't let it just drift)
```

### "Weekly review, just the slipping items"

For a quick mid-week check, you can ask for one section only.

---

## Pairs well with

- **Daily Brief** — Monday's brief inherits "Next week" from Friday's review
- **Premortem** — when "Slipping" reveals a pattern, run a premortem on what's going wrong
