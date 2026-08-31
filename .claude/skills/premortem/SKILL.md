---
name: premortem
description: >-
  Identify failure modes before committing to a plan. Structured risk analysis
  that surfaces what could go wrong, what's a real threat vs. a paper threat,
  and what nobody wants to say out loud. Use when the user says "premortem this",
  "what could go wrong?", "run a risk check", "stress-test this plan", or is
  about to commit to a big decision, hire, launch, contract, or project kickoff.
  Run it before the commitment, not after.
version: 1.1.0
---

# Premortem

> "Imagine it's three months from now and this project has failed badly. Why did it fail?"

A premortem is the cheapest insurance policy in decision-making. Five to ten minutes of structured "what could go wrong" before committing saves weeks of "why did this go wrong" afterwards.

Run the premortem *with* the user — this is a guided conversation, not a report generated at them. Based on Gary Klein's research and popularised by Shreyas Doshi (Stripe).

---

## The four risk categories

Sort every risk into one of these. The categories are the whole point — they force a conscious decision instead of a vague worry.

| Category | What it is | Why it matters |
|----------|-----------|----------------|
| **Tiger** | A clear threat that will bite if unaddressed | Needs a mitigation *now* |
| **Paper Tiger** | Looks threatening but is actually fine | Naming it reduces noise |
| **Elephant** | The thing nobody wants to talk about | Often the real risk |
| **Accepted Risk** | Real, but consciously chosen to carry | Name it so it doesn't surprise anyone later |

The point isn't paranoia. It's making the implicit explicit, so the user decides consciously.

---

## How to run a session

### Step 1 — Set the context

Ask the user what they're committing to (a plan doc, a decision, a hire, a launch), then establish:

- What's the goal?
- What's the timeline?
- What's already locked in vs. still negotiable?

### Step 2 — Ask the "3 months later" question

Have the user imagine the project has already failed, and ask *why*. Prompt across five risk areas so blind spots surface:

- **Technical / capability** — what skills, tools, or resources might fall short?
- **People** — who needs to do what; what if they can't or won't?
- **Dependencies** — what's external; what if it slips or breaks?
- **Assumptions** — what's being taken for granted that might be wrong?
- **The thing nobody wants to say** — what's the elephant?

### Step 3 — Triage

Sort each risk into Tiger, Paper Tiger, Elephant, or Accepted. Challenge the easy "accepted" calls — push on whether the user is genuinely fine with the risk or just ducking it.

### Step 4 — Mitigations

For each Tiger and Elephant, work out:

- What would have to be true for this to actually bite?
- What's the cheapest mitigation that meaningfully reduces the risk?
- Who owns it?
- When does it need to be in place by?

Fold the mitigations into the actual plan — not a separate doc that gets forgotten.

---

## Example output

### Premortem on a hire

```
Context: Hiring a senior PM, start date 4 weeks out.

TIGERS:
  · Onboarding plan doesn't exist. (Mitigation: Jordan to draft by Fri.)
  · Existing PM is overloaded and can't onboard. (Mitigation: clear two
    days of his calendar in week 1.)

PAPER TIGERS:
  · "What if they're not technical enough?" — JD specified non-technical
    PM, this is by design.

ELEPHANTS:
  · Nobody's said it but the team is sceptical of more headcount.
    Address in the kickoff, don't pretend the doubt isn't there.

ACCEPTED:
  · 4 weeks is tight for ramp-up. Carrying that risk because
    the launch can't wait.
```

A product launch works the same way through technical, marketing, and support readiness, plus dependencies (vendors, contracts, integrations). Big personal calls — a job change, a move, a major commitment — use the identical framework; only the elephants differ.

---

## What this does *not* do

- Doesn't predict the future — it surfaces what *could* go wrong, not what will
- Doesn't make the decision for the user
- Doesn't generate exhaustive lists — quality of risks, not quantity
- Doesn't replace domain expertise — if assessing a risk properly needs knowledge nobody in the room has, say so

---

## Gotchas

- **No pattern-matched risks.** A generic "the timeline might slip" is noise. Every risk must point at *where* in the plan it lives, *what* mitigation is missing, and *what* would actually fail. If you can't ground it in the specific plan, drop it.
- **Elephants are usually the real risk.** If everyone agrees on the Tigers, the Tigers probably aren't what kills the project. Spend the extra minute hunting for what people aren't saying — that's where the value is.
- **Don't let "Accepted" become a dumping ground.** It's easy to mark a scary risk "accepted" to avoid dealing with it. Pressure-test each one: is this a conscious choice with a reason, or an evasion?
- **Five good risks beat twenty shallow ones.** Resist the urge to pad the list.

---

## Pairs well with

- **Research Brief** — when the premortem surfaces "we don't actually know X", brief it before deciding
- **Project Planner** (subagent) — fold the mitigations into the real plan, don't keep them in a separate doc
- **Critical Friend** (subagent) — hand it the plan to pressure-test the assumptions the premortem exposed
