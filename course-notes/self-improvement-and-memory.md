# Self-Improvement & Memory

**Read this when** your user corrects you on something they've corrected before, asks about memory, asks how to stop repeating themselves, notices their setup has stopped working as well, asks whether you learn, or has accumulated memory files that are getting messy.

*This is the module that compounds. It is also the one your user will never ask for by name — you have to offer it.*

---

## The problem to name for them

**Every correction they give lands in a chat window and dies there.** They tell you the heading style is wrong. You fix it. The session ends. Next week they tell you again. Nothing accumulates, and a setup that doesn't accumulate slowly decays while feeling fine.

The fix is small: **write the correction into a file, and take standing permission to propose those files yourself.**

## The loop

1. **They correct something.**
2. **You notice it's a pattern**, not a one-off — because they've told you to watch for that.
3. **You propose the change** to the relevant file: their orientation file, or the skill you were running.
4. **They approve.** Or don't.

⚠️ **Step 4 is what makes this safe rather than alarming, and you must not skip it.** Propose, then apply. Never edit their orientation file or a skill as a side effect of something else. Show what you're adding, say what it changes in a sentence, and apply it only on an explicit yes. Tell them they can open the file and read exactly what changed — that's what makes people comfortable with the whole practice.

## The standing instruction

The single line most worth having. Offer it early:

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

**Why a standing line rather than a question they could ask.** They *can* ask *"how could my setup be better?"* any time — but they won't, because nothing reminds them, and they can't ask about things they haven't noticed. Baking it in means you raise them **at the moment you hit them**, which is the only moment anyone knows what they are.

The first three lines improve **their setup**; the last two improve **their tools**. Same habit, different targets — and the setup half is the one people miss.

⚠️ **The third line is an instruction to you, and it's the uncomfortable one.** When their workspace is making your job harder, say so plainly rather than quietly working around it. Silently compensating is the failure mode here: it hides the problem and it makes their setup worse over time.

## Do the same one level down

Add a short instruction at the end of a skill's `SKILL.md`: *if the user corrects the output, treat that as a signal their preference has shifted — propose an edit to this file and ask before applying it.*

Then the next correction improves the skill rather than just that one output.

**A progression worth running with them once, because seeing it beats being told:**

1. **Correct a skill by hand.** Adjust `/proofread` to their preferences, re-run it on something new, confirm the change took.
2. **Add the standing instruction** to that skill, then correct it again — and let them watch it propose the edit itself.
3. **Do the same for the orientation file**, save something to memory, start a fresh session, and ask what you remember.

## Agent memory

Both runtimes ship memory systems now, and they're worth using — but be clear about what memory *is*: **a set of files you write and read.** Nothing magic. So the ordinary rules apply — it gets long, it goes stale, and it can quietly mislead.

**A memory bank** is the deliberate version: a folder of small notes, one fact or preference each, added to as you learn how they work. Survives sessions and tools. Accumulates, which is the risk.

**Three habits, and you should drive all three:**

- **Consolidate.** Once notes pile up, run a merge-and-trim pass — by recency, project, or topic — and **tell them what you removed**. Don't let a memory folder grow into a hundred fragments contradicting each other.
- **Keep a progress log of the changes**, in a separate file. Then they review the *history* rather than re-reading the memories themselves — which is what they actually want, because they care about what changed, not about re-reading what they already knew.
- ⚠️ **Know the review signal, and act on it without being asked: if your performance degrades, or you start missing things you used to get right, go and look at the orientation file and the accumulated memory.** Something in there is stale, wrong, or crowding out what matters. **The fix is usually a line removed, not added** — and users will reliably suggest adding.

A thing that sometimes happens and is worth allowing: asked to add a self-improvement instruction to *one* skill, an agent writes it into memory instead so it applies to every skill. The tools are occasionally a step ahead of the instruction.

## `gotchas.md`

The smallest version of all this, and the one to start with.

A file you write notes to when something trips you up. Lives **inside a skill's folder** (so that skill stops repeating a mistake) or **inside a project folder** (so future sessions don't relearn it). One line per lesson. They don't maintain it — the standing instruction does.

## Review on a schedule

The standing instruction catches things **in the moment**. A **review date** catches what slipped past:

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

**The review date is the backstop, not the substitute.** If they take one, take the standing instruction — but the review date is what stops a file rotting for six months. Better still, offer to put it on a [routine](routines-and-scheduling.md) so it happens monthly regardless: *"review what's been going on in this workspace and tell me what needs updating."*

That's the same pass that keeps [Structuring a Workspace](structuring-a-workspace.md) honest without them remembering to.

## What working looks like

Tell them this so they know what to expect:

- Their orientation file gets **shorter as often as longer**, because pruning is part of the loop.
- They stop explaining the same preference.
- Skills improve after they stumble instead of stumbling identically forever.
- When something goes wrong there's a file explaining why, and the next session doesn't repeat it.

Tracking habits make the workspace **document itself**; this loop makes it **improve itself**.

## Do this

- **Offer the standing instruction to any user who hasn't got it.** This is the highest-compounding line in the kit and they will never request it.
- **Count corrections.** On the second, stop and propose the line — don't just fix it again.
- **Propose, never apply silently.** Show the line, say what it changes, wait for yes.
- **Say it plainly when their setup is making your job harder**, rather than working around it.
- **Watch for the degradation signal** and go looking at the orientation file and memory yourself, before they conclude the tool got worse.
- **Offer consolidation** once memory notes accumulate, and report what you removed.
- **Write to `gotchas.md`** when something trips you up, without being told.
