# Subagents

*Specialists your main agent dispatches work to — each with a fresh context window, its own instructions, and no loyalty to what you just wrote.*

A subagent is just another agent — same underlying model — that your main agent can hand a job to. It runs in **its own fresh context window** with **its own focused instructions**, does the work somewhere else, and returns the distilled result.

You never talk to a subagent directly. You brief your main agent; it spawns, instructs, and collects. That is why subagents suit **bounded jobs with a clear result to hand back**, not tasks that need a lot of back-and-forth.

---

## Why dispatch at all

**1 · Context isolation — the big one.** A dispatched subagent does **not** inherit your session's context. It starts clean, does the heavy reading in its own window, and returns only the answer. Your main conversation stays sharp instead of filling up and drifting into lossy compaction.

This is the payoff for every habit in [Structuring a Workspace](structuring-a-workspace.md). A subagent that arrives with no memory of your session can still be effective — *if* the workspace is navigable and the project folder documents itself. If it isn't, the subagent is as lost as any stranger. **A well-organised workspace is what makes delegation work.**

**2 · A different perspective.** A subagent gets tailored instructions you'd never want cluttering your everyday agent — a role, a tone, a narrow toolset. Your main agent is *general-purpose by design*; every fresh session loads the same broad orientation. A new chat is just another general-purpose agent reading the same generic map. A subagent is where the job-specific instructions go.

**3 · Scoped tools and models.** Restrict or specialise what it can reach — no web, no file edits — and pick a cheaper or heavier model to match the job.

**4 · Parallelism.** Run several at once. *"Fan out subagents to read these ten papers, one each"* spins up a whole set simultaneously. You don't write them; the main agent creates them with tailored instructions and you review what comes back.

**When to skip them:** when you need all the resulting context kept in the main thread, or when the task depends on everything you've already done together.

## The highest-leverage use: a fresh-eyes red team

Because a subagent starts from a blank context with its own instructions, **it isn't invested in what your main agent just produced**. Point a deliberately critical reviewer at a plan or a draft and it nearly always comes back with a real issue. This holds even on the most capable models — a clean-context adversarial pass still finds things.

Two refinements worth knowing:

- **Don't tell it the work is yours.** Ask it to tear the piece apart without mentioning that you wrote it. Then compare that with what your main agent said about the same work. The gap between the two answers is the most instructive five minutes in this whole kit — see *sycophancy* in [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md).
- **Bias doesn't disappear; you choose its direction.** A subagent isn't neutral, it's *differently* biased — and that is the useful property. Run several with different framings and you get the blind-men-and-the-elephant coverage one reviewer can't give you.

*(The kit ships `critical-friend` and the `critical-review` skill for exactly this: "use the critical-review skill to red-team this plan.")*

## What they look like

They are **files in a folder** — `.claude/agents/<name>.md` for Claude, `.codex/agents/<name>.toml` for Codex, registered in `.codex/config.toml`. The formats differ slightly; your agent handles that.

A subagent file is short: a **name**, a **description** of when it should be used, optionally which tools and model it gets, and then the instructions themselves — the role, the standards, what to return.

**Never write one by hand.** Describe the specialist you want and let the agent write the file:

> *"Create a subagent for [the role]. It should [what it does], and it must [what it must never do]. Write the file for me and show me the result."*

**Where they live decides whether you can use them.** Global means everywhere; project means only inside that folder — and there is a trap in it. See [Where Things Live](where-things-live.md).

## How it decides to use one

- **Claude** picks a subagent automatically, based on its **name and description**. Write those two lines carefully — they are the entire basis on which it chooses.
- **Codex** uses one **only when you explicitly ask for it**. Name it.
- **Being explicit works in both**: *"use the writing-editor subagent for this."* When in doubt, say the name.

The same name-and-description mechanic governs [skills](skills.md), where it's worth understanding properly — it's the reason a big library of tools doesn't slow your agent down.

## Make them document their work

You can't easily watch a subagent run. So tell it to leave a trail: a folder with an `overview.md` and a running `progress.md`. The folder is concrete and **persistent** — it survives the chat, and any future session (or a recovery after a crash) can be pointed straight at it.

Worth a standing line in your orientation file:

```markdown
- When you hand work to a subagent, tell it to document what it did in that folder.
```

## Subagents versus running several sessions

Two different things, easily blurred:

- **Subagents** are spawned *by your main agent* and run inside one session, each in its own fresh window. You don't open windows for them or talk to them.
- **Multiple sessions** are separate chats *you* open and manage. Genuinely useful — running the same fact-checker over the same material in two sessions and comparing the outputs will surface inconsistencies a single pass hides.

**The one hard rule for multiple sessions: don't let two of them edit the same file at once.** They can't see each other; each sees phantom changes appearing and gets confused about whether it's overwriting something. Separate outputs are completely fine — files and folders persist across sessions and every session sees the latest version on disk. It's simultaneous edits to *one* file that cause trouble.

**Sequencing turns this into a workflow.** Chain agents in a set order — research, then draft, then critique — and you have built a workflow. That's the seed of [routines](routines-and-scheduling.md).

## The kit's six

The kit installs six generally-useful subagents:

| Subagent | What it does |
|---|---|
| **critical-friend** | Pressure-tests an argument or plan — pushbacks, steel-manned counter-position, blind spots |
| **fact-checker** | Verifies factual and statistical claims against authoritative primary sources |
| **writing-editor** | Heavy editorial pass — clarity, structure, voice, cuts — without replacing your voice |
| **project-planner** | Turns a goal into milestones, tasks, dependencies, and honest estimates |
| **vault-librarian** | Reads your local notes and surfaces what's relevant to the task |
| **web-searcher** | Routes a query to the best available source and returns a sourced answer with citations |

These are a starting crew, not a fixed set. **Find what you have** by asking, or by looking in your `.claude` / `.codex` folder under `agents`. **Edit them** by giving feedback in the chat and letting the agent make the change — the files are hidden by default, so most editors won't show them without a nudge.

## A note on time estimates

Agents have **no sense of effort or duration**. They're trained on human estimates, so they'll announce "about a month of work" and finish before lunch — or the reverse. Ignore the estimate. What's worth asking for instead is a **plan before it executes**, which stops it over-delivering to impress you and lets you see the scope before committing.

## Try this

> Think about the kinds of work I keep asking you for. Which one or two would genuinely be
> better done by a specialist with its own instructions? Propose them — name, description,
> what they'd do, what they'd never do. Then write the first one, and use it on something
> real so I can see the difference.
