---
name: discovery-interview
description: Deep interview process that turns a vague idea into a detailed spec.
  The agent asks structured, non-obvious questions — one at a time — until the shape
  of what you want is clear. Use when you can feel the idea but can't write it down
  yet.
---

# Discovery Interview

You have an idea. You can't quite write it down. You don't know what questions to ask yourself. This skill is the interviewer who pulls the spec out of you.

**When to use this skill:**
- "Help me figure out what I actually want"
- "Interview me about this idea"
- "I want to build/start/run X but I don't know where to begin"
- "Turn this vague thing into a spec"

Works for technical, business, creative, and personal projects.

---

## The principle

Most "what do you want?" conversations fail because they ask the obvious questions. This skill asks the **non-obvious** ones.

Three rules the skill follows:

1. **One question at a time** — batched questions tank completion and produce shallow answers.
2. **Open first, structured later** — start wide, narrow based on what comes back.
3. **Surface tradeoffs explicitly** — most ambiguity is unresolved tension, not missing detail.

The skill won't just write down what you say. It pushes back, asks "what if", and offers genuine alternatives where it sees them.

---

## How a session runs

### Phase 1 — Orient (2-3 questions)

Just enough to know what shape this is.

> "In one sentence, what problem are you trying to solve?"
> "Who's it for — and is that the same person who'll pay for it?"
> "If this works perfectly, what changes?"

### Phase 2 — Deep dive (10-30 questions, depending on complexity)

The skill works through whatever angles matter for your idea. Common areas:

- **Scope** — what's in, what's out, what's deliberately not version-1
- **Users** — who, in what context, with what existing alternatives
- **Tradeoffs** — speed vs. polish, flexibility vs. constraint, etc.
- **Constraints** — time, money, capability, dependencies
- **Failure modes** — what would make this a waste of effort
- **Success signals** — how would you know it's working

Each question is informed by your previous answers. The skill won't ask a generic checklist.

### Phase 3 — Validate

Before writing the spec, the skill says:

> "Here's what I think I heard. Where am I wrong?"

Negative framing on purpose. "Does this look right?" gets weak answers. "Where am I wrong?" surfaces real objections.

### Phase 4 — Write the spec

Only after the validation pass. The output is a structured document — usually a markdown file in your vault — that someone else (or another agent) could pick up and act on.

---

## What the spec includes

Depending on the kind of project:

- The problem in plain language
- Who it's for and what they're doing instead today
- What "done" looks like for v1
- Explicit non-goals (just as important)
- Tradeoffs you've decided on
- Open questions you haven't resolved (named, not hidden)
- Next concrete steps

---

## Examples

### "I want to start a newsletter"

The skill spends 20 minutes interviewing. By the end you have:
- The reader you're writing for, specifically
- Why this newsletter exists when 50 others on similar topics already do
- Cadence you can actually sustain
- Three concrete pieces you'd write in the first month
- What success looks like at 100 subscribers vs. 1,000
- The tools you'll use (or research separately)

### "I want to build an AI tool for my team"

The interview surfaces:
- What problem the tool solves vs. what's just "AI is cool"
- Who'd actually use it daily vs. monthly vs. never
- Build-it vs. buy-it tradeoffs
- The smallest thing you could test in 2 weeks
- Why this might fail

### "I want to switch jobs"

Yes, this works for personal decisions too. The skill interviews on what you're optimising for, what you're avoiding, what tradeoffs you're willing to make, and what would change if the answer is "yes" or "no".

---

## What it does *not* do

- Doesn't push you toward a particular answer
- Doesn't make the decision for you
- Doesn't claim to know your domain — it's an interviewer, not a domain expert
- Doesn't skip the validation pass — half-formed specs cause downstream pain

If the interview surfaces gaps it can't fill from the conversation (e.g. "you need market data on X"), the skill names them as next steps, not as answers.

---

## Pairs well with

- **Research Brief** — when the interview surfaces something you'd need to research before deciding
- **Premortem** — run on the spec the discovery produces, before you commit
- **Project Planner subagent** — turn the spec into an actionable plan
