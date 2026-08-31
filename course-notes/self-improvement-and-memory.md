# Self-Improvement & Memory

*The mechanic that stops your corrections evaporating — so the setup gets better as you use it, rather than only when you remember to improve it.*

Here is the problem, stated plainly. **Right now, every correction you give lands in a chat window and dies there.** You tell your agent it used the wrong heading style. It fixes it. The session ends. Next week you tell it again. Nothing accumulates, and a setup that doesn't accumulate slowly decays while feeling fine.

The fix is small and it is the highest-compounding thing in this kit: **write the correction into a file, and give the agent standing permission to propose those files itself.**

---

## The loop

1. **You correct something.**
2. **The agent notices it's a correction**, not a one-off — because you've told it to watch for that.
3. **It proposes the change to the relevant file** — your orientation file, or the skill you were running.
4. **You approve it.** Or you don't. Either way you saw it, and you can open the file and read exactly what changed.

Step 4 is the part that makes this safe rather than alarming. **Propose, then approve. You stay in the driver's seat.** Nothing is edited behind your back, and the change is a plain text file you can read, edit, or undo.

## The standing instruction

Paste this into your orientation file. It is the single line most worth having:

```markdown
## Keep making this better
- If you notice something about how I work that isn't written down here, say so and offer
  to add it. Don't wait for me to ask.
- If I correct you on the same thing twice, propose a line for this file that stops it
  happening a third time.
- If my setup is making your job harder — missing context, a folder you can't navigate,
  something in here that's gone stale — tell me plainly rather than working around it.
- After running a skill, suggest how it could be improved. If I repeat a task with no
  skill, propose one.
- When something trips you up here, write it into a `gotchas.md` so we don't relearn it.
```

**Why this is a standing line and not just a question you could ask.** You *can* ask *"how could my setup be better?"* any time — but you won't, because nothing reminds you, and you can't ask about the things you haven't noticed. Baking it in means the agent raises them **at the moment it hits them**, which is the only moment anyone actually knows what they are.

The first three lines improve **your setup**; the last two improve **your tools**. Same habit pointed at different things — and the setup half is the one people miss.

## Do the same for a skill

The same mechanic works one level down. Add a short instruction at the end of a skill's `SKILL.md` saying: *if the user corrects the output, treat that as a signal their preference has shifted — propose an edit to this file and ask before applying it.*

Then the next time you correct a proofread, the skill improves rather than just that one output. Reactive becomes proactive, and you still review.

A worked progression to run once:

1. **Correct a skill by hand.** Change `/proofread` to your own preferences, then re-run it on something new to confirm the change actually took.
2. **Add the standing instruction** to that skill, then correct it again — and watch it propose the edit itself.
3. **Do the same for your orientation file**, save something to memory, open a fresh session, and ask what it remembers.

## Agent memory

Both Claude and Codex now ship their own memory systems, and they're worth exploring — but understand what memory *is* before you lean on it. It's a set of files the agent writes and reads. Nothing magic. Which means the ordinary rules apply: it can get long, it can go stale, and it can quietly mislead.

**A memory bank** is just a deliberate version of this: a folder of small notes, each one fact or preference, that the agent adds to as it learns things about how you work. The value is that it survives sessions and tools. The risk is accumulation.

**Three habits keep it useful:**

- **Consolidate.** Once notes accumulate, ask for a merge-and-trim pass — by recency, by project, or by topic. *"Read through my memory files. Merge the duplicates, cut anything that's no longer true, and tell me what you removed."* Do this rather than letting a memory folder grow to a hundred fragments that contradict each other.
- **Keep a progress log of the changes.** Ask the agent to record how it has altered your memories, in a separate file. Then you can review the *history* without reading the memory files themselves — which is what you actually want, because you care about what changed, not about re-reading things you already knew.
- **Know when to review.** The signal is behavioural: **if performance degrades, or it starts missing things it used to get right, go and look at your orientation file and your accumulated memory.** Something in there is probably wrong, stale, or crowding out something that matters. The fix is usually a line *removed*, not a line added.

A nice thing that happens once people get this: an agent asked to add a self-improvement instruction to *one* skill sometimes writes it into its memory system instead, so it applies to every skill. The tools are occasionally a step ahead of the instruction — let them be.

## `gotchas.md` — hard-won lessons that stay won

The smallest version of all of this, and the one to start with.

A `gotchas.md` is a file the agent writes notes to itself in when something trips it up. It lives **inside a skill's folder** (so that skill stops repeating a mistake) or **inside a project folder** (so future sessions on that project don't relearn it). One line per lesson.

You don't maintain it. The standing instruction above does.

## Have it review itself on a schedule

The standing instruction catches things **in the moment**. A **review date** catches whatever slipped past:

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

**The review date is the backstop, not the substitute.** If you take only one, take the standing instruction — but the review date is what stops a file quietly rotting for six months. Better still, hand it to a [routine](routines-and-scheduling.md) so it happens monthly whether or not you remember: *"review what's been going on in this workspace and tell me what needs updating."*

That is the same weekly "tidy and document my workspace" pass that keeps [Structuring a Workspace](structuring-a-workspace.md) honest without you remembering to.

## What this looks like when it's working

- Your orientation file gets **shorter as often as it gets longer**, because pruning is part of the loop.
- You stop explaining the same preference. It's written down.
- Skills improve after they stumble instead of stumbling identically forever.
- When something goes wrong, there's a file explaining why — and the next session doesn't repeat it.

The tracking habits make the workspace **document itself**; this loop makes it **improve itself**. Together that's a setup that gets better the more you use it, with no extra effort from you.

## Try this

> Look at how I'm working with you right now. Where am I relying on the chat as memory
> instead of leaving a trail in files? Suggest two small changes — then add a "Keep making
> this better" section to my orientation file that bakes them in. Show it to me before you
> write it.
