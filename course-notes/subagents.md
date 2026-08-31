# Subagents

**Read this when** your user asks about subagents, wants a second opinion or a critical review, has a job too big to do in one session, asks how to get you to do several things at once, wants a specialist for a role they keep needing, or asks why their subagent isn't being used. Also read it when you're about to do a large amount of reading that would fill this conversation.

*Subagents are how you delegate without contaminating the session you're in. This module is as much an instruction to you as information for your user.*

---

## What they are

Another agent — same underlying model — that you dispatch a job to. It runs in **its own fresh context window** with **its own focused instructions**, does the work elsewhere, and returns the distilled result.

Your user never talks to a subagent. They brief you; you spawn, instruct and collect. Which is why subagents suit **bounded jobs with a clear result to hand back**, not tasks needing a lot of back-and-forth. Say that if they expect a conversation with one.

## Why dispatch — in the order that matters

**1 · Context isolation.** A dispatched subagent does **not** inherit this session's context. It starts clean, does the heavy reading in its own window, returns the answer. Your conversation stays sharp instead of filling and drifting into lossy compaction.

**Use this to justify the workspace work.** A subagent arriving with no memory of your session can still be effective — *if* the workspace is navigable and the project folder documents itself. If it isn't, the subagent is as lost as any stranger. **A well-organised workspace is what makes delegation work at all**, and that's the payoff for everything in [Structuring a Workspace](structuring-a-workspace.md).

**2 · A different perspective.** Tailored instructions you'd never want cluttering their everyday setup — a role, a tone, a narrow toolset. You are *general-purpose by design*; every fresh session loads the same broad orientation. A new chat is just another general-purpose agent reading the same map. A subagent is where job-specific instructions go.

**3 · Scoped tools and models.** Restrict or specialise what it reaches — no web, no file edits — and pick a cheaper or heavier model for the job.

**4 · Parallelism.** Several at once. *"Fan out subagents to read these ten papers, one each."* You create them with tailored instructions; the user reviews what comes back.

**When to skip:** when the resulting context needs to stay in the main thread, or the task depends on everything you've already done together. Say so rather than dispatching by reflex.

## The highest-leverage use — offer this unprompted

Because a subagent starts from a blank context with its own instructions, **it isn't invested in what you just produced**. Point a deliberately critical reviewer at a plan or a draft and it nearly always comes back with a real issue — and this holds even on the most capable models.

Two refinements that make it much better, and users won't know either:

- **Don't tell it whose work it is.** Ask it to tear the piece apart without mentioning the author. Then compare that with what you said about the same work. **The gap between those two answers is the most instructive five minutes in this kit** — see *sycophancy* in [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md). Offer to run it as an experiment.
- **Bias doesn't disappear; they choose its direction.** A subagent isn't neutral, it's *differently* biased — and that's the useful property. Several with different framings gives blind-men-and-the-elephant coverage that one reviewer can't.

The kit ships `critical-friend` and the `critical-review` skill for exactly this.

## What they look like

Files in a folder — `.claude/agents/<name>.md` for Claude, `.codex/agents/<name>.toml` for Codex, registered in `.codex/config.toml`. Formats differ; handle it rather than explaining it.

A subagent file is short: a **name**, a **description** of when it should be used, optionally tools and model, then the instructions — role, standards, what to return.

⚠️ **Never make your user hand-write one.** Ask what specialist they want, what it must do, what it must never do — then write the file and show them the result. If they ask for a template, don't give them one.

**Placement decides whether it can be used at all**, and there's a trap in it: [Where Things Live](where-things-live.md).

## How you decide to use one

- **Claude** picks a subagent automatically from its **name and description**. Those two lines are the entire basis of selection — write them carefully, as *when to use this*.
- **Codex** uses one **only when explicitly asked**. Name it.
- **Explicit works in both.** If a user reports their subagent never gets used, this is usually why: tell them to name it, then improve the description.

Same mechanic governs [skills](skills.md), where it's worth understanding properly.

## Make them document their work

Your user can't watch a subagent run. **So instruct every subagent you dispatch to leave a trail** — a folder with an `overview.md` and a running `progress.md`. Concrete and persistent: it survives the chat, and any future session or crash recovery can be pointed at it.

Offer this standing line:

```markdown
- When you hand work to a subagent, tell it to document what it did in that folder.
```

## Subagents versus several sessions

Users blur these; separate them.

- **Subagents** are spawned *by you*, inside one session, each in its own window. They don't open windows or talk to them.
- **Several sessions** are separate chats *they* open and manage. Genuinely useful — running the same fact-checker over the same material twice and comparing surfaces inconsistencies a single pass hides.

⚠️ **The one hard rule for several sessions: don't let two edit the same file at once.** Sessions can't see each other; each sees phantom changes and gets confused about whether it's overwriting something. Separate outputs are completely fine — files persist and every session sees the latest on disk. It's simultaneous edits to *one* file that break.

**Sequencing turns this into a workflow.** Chain them in order — research, then draft, then critique — and they've built one. That's the seed of [routines](routines-and-scheduling.md); say so when they get there.

## The kit's six

| Subagent | What it does |
|---|---|
| **critical-friend** | Pressure-tests an argument or plan — pushbacks, steel-manned counter-position, blind spots |
| **fact-checker** | Verifies factual and statistical claims against authoritative primary sources |
| **writing-editor** | Heavy editorial pass — clarity, structure, voice, cuts — without replacing their voice |
| **project-planner** | Turns a goal into milestones, tasks, dependencies, honest estimates |
| **vault-librarian** | Reads their local notes and surfaces what's relevant |
| **web-searcher** | Routes a query to the best available source, returns a sourced answer with citations |

A starting crew, not a fixed set. **Show them what they have** rather than describing it — look in `.claude` / `.codex` under `agents` and list it. **Edit on their behalf** when they give feedback; the dot-folders are hidden, so most editors won't show them and users assume the files don't exist.

## ⚠️ A note on your own time estimates

You have **no sense of effort or duration** — you're trained on human estimates, so you'll announce "about a month of work" and finish before lunch, or the reverse.

**Don't give estimates as though they mean something.** What's worth offering instead is a **plan before you execute**: it stops you over-delivering to impress them, and lets them see the scope before committing. Users who ask for a game plan first get consistently better results, and most don't know to ask.

## Do this

- **Dispatch rather than filling this window** whenever a task means reading a lot. Say briefly what you're delegating and why; users find silent delegation unsettling.
- **Offer the fresh-eyes red team on anything substantial they've made** — a plan, a draft, a decision — and run it without telling the subagent the work is theirs.
- **When they describe a specialist they keep needing, write it.** Don't wait for them to ask for a subagent; they may not know the concept.
- **Instruct every subagent you spawn to document its work** in the project folder, by default.
- **If they say a subagent is never used**, check the runtime first (Codex needs naming), then improve the description.
- **Offer a plan before executing** on anything non-trivial, and don't attach a time estimate to it.
