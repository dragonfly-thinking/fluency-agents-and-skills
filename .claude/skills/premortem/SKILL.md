---
name: premortem
description: >-
  Identify failure modes before committing to a plan. Structured risk analysis
  that surfaces what could go wrong, what's a real threat vs. a paper threat,
  and what nobody wants to say out loud. Use before you commit, not after.
version: 1.0.0
---

# Premortem

> "Imagine it's three months from now and this project has failed badly. Why did it fail?"

A premortem is the cheapest insurance policy in decision-making. Five to ten minutes of structured "what could go wrong" before committing saves weeks of "why did this go wrong" afterwards.

**When to use this skill:**
- "Premortem on this plan"
- "Before I commit to this, what could go wrong?"
- "Run a risk check on this"
- Before a big decision, hire, launch, contract, or project kickoff

Based on Gary Klein's research and popularised by Shreyas Doshi (Stripe).

---

## The technique

The skill walks you through four risk categories:

| Category | What it is | Why it matters |
|----------|-----------|----------------|
| **Tiger** | A clear threat that will bite if you don't address it | These need mitigations *now* |
| **Paper Tiger** | Looks threatening but is actually fine | Calling these out reduces noise |
| **Elephant** | The thing nobody wants to talk about | Often the real risk |
| **Accepted Risk** | Real but you've chosen to carry it | Worth naming so it doesn't surprise you |

The point isn't paranoia. It's making the implicit explicit, so you decide consciously.

---

## How a session runs

### Step 1 — Set the context

You tell the skill what you're committing to. A plan doc, a decision, a hire, a launch. The skill asks:

- What's the goal?
- What's the timeline?
- What's already locked in vs. still negotiable?

### Step 2 — The "3 months later" question

The skill asks you to imagine the project has failed. Why? You brainstorm. The skill prompts in five risk areas:

- **Technical / capability** — what skills, tools, or resources might fall short?
- **People** — who needs to do what; what if they can't or won't?
- **Dependencies** — what's external; what if it slips or breaks?
- **Assumptions** — what are we taking for granted that might be wrong?
- **The thing nobody wants to say** — what's the elephant?

### Step 3 — Triage

Each risk gets sorted: Tiger, Paper Tiger, Elephant, or Accepted. The skill challenges you on the easy "accepted" calls — are you really fine with it, or are you ducking?

### Step 4 — Mitigations

For each Tiger and Elephant:

- What would have to be true for this to actually bite?
- What's the cheapest mitigation that meaningfully reduces the risk?
- Who owns it?
- When does it need to be in place by?

Mitigations get added to your plan. Not as a separate doc that gets forgotten — folded into the work.

---

## Calibration

The skill is opinionated about two things:

**False positives are real.** "Pattern matching for risks" without checking the actual plan produces noise. The skill insists on evidence — *where* in the plan is the risk, *what mitigation isn't there*, *what would actually fail*.

**Elephants are usually the real risk.** If everyone agrees on the Tigers, the Tigers probably aren't what kills you. The skill spends extra time hunting for what people aren't saying.

---

## Examples

### Premortem on a hire

```
Context: Hiring a senior PM, start date 4 weeks out.

TIGERS:
  · Onboarding plan doesn't exist. (Mitigation: Sam to draft by Fri.)
  · Existing PM is overloaded and can't onboard. (Mitigation: clear two
    days of his calendar in week 1.)

PAPER TIGERS:
  · "What if they're not technical enough?" — JD specified non-technical
    PM, this is by design.

ELEPHANTS:
  · Nobody's said it but the team is sceptical of more headcount.
    Need to address in the kickoff, not pretend the doubt isn't there.

ACCEPTED:
  · 4 weeks is tight for ramp-up. We're carrying that risk because
    the launch can't wait.
```

### Premortem on a product launch

The skill works through technical readiness, marketing readiness, support readiness, dependencies (vendors, contracts, integrations), and the "what would Shreyas Doshi say is the elephant?" question.

### Premortem on a personal decision

Yes, this works for big personal calls too — a job change, a move, taking on a big commitment. The framework is the same. The elephants are different.

---

## What it does *not* do

- Doesn't pretend to predict the future — it surfaces what *could* go wrong, not what will
- Doesn't make the decision for you
- Doesn't generate exhaustive lists — quality of risks, not quantity
- Doesn't replace expertise — if you need domain knowledge to assess a risk properly, the skill says so

---

## Pairs well with

- **Discovery Interview** — run the interview first to make the plan, then premortem on it
- **Research Brief** — when premortem surfaces "we don't actually know X", brief it
- **Weekly Review** — slipping patterns often reveal Tigers your premortem missed
- **Project Planner subagent** — fold mitigations into the actual plan, don't keep them in a separate doc
