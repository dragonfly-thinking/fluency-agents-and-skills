# Skills

**Read this when** your user asks what a skill is, wants to package something they do repeatedly, asks how to make you better at their specific work, wants to encode a methodology or framework, asks why typing `/` shows nothing, or has just explained the same preference to you twice.

*Skills are how your user's expertise gets into you permanently rather than per-conversation. The trigger to watch for is repetition — theirs, not yours.*

---

## What they are

A **folder you read on demand**. Inside, a `SKILL.md` says what the job is, when to use it, and how they want it done. That's the whole requirement. Everything else — checklists, examples, reference files, scripts — is optional and loaded only when the instructions call for it.

The distinction to give a user: **a subagent is a *specialist*; a skill is a *verb*** — "proofread this", "build me a deck", "run a premortem".

## How you find them — worth explaining once

This explains why a big library costs nothing, and users assume the opposite.

**You pre-load only each skill's name and description** — a line or two each. When one looks relevant, *then* you load the full `SKILL.md` and whatever it points at.

True on both runtimes. OpenAI's documentation: *"ChatGPT and Codex start with each skill's name and description, then load the full SKILL.md instructions when they decide to use that skill."*

Two consequences worth passing on:

- **The description is the most important line in the file** — it's the entire basis on which a skill gets chosen. Write it as *when to use this*, not *what this is*. Fix theirs if it's the latter.
- **A big library is cheap.** Twenty unused skills cost twenty lines, not twenty documents. Users worry about clutter; they needn't.

Same mechanic drives [subagent](subagents.md) selection on Claude. Where a skill has to *sit* — and the trap that catches everyone — is [Where Things Live](where-things-live.md).

## What's in a `SKILL.md`

- **Front matter** with a `name` and a `description`.
- **The instructions** — the job, the steps, the standards, the shape of the output.
- **Optionally, anything else in the folder** — a checklist, worked examples, a style reference, a script.

**Point a skill at their files.** This is the move that turns a generic skill into theirs: put their actual materials in the folder, or point at paths in their workspace. **Two or three examples of what they typically produce beat any amount of description** — offer to go and find some.

## Composition

Skills can **dispatch subagents**, and subagents can invoke skills. That layering is where real capability sits.

The clearest demonstration is already installed: run **`/proofread`**, then open its `SKILL.md` and show them it does **not** do the editing itself — it delegates to the **`writing-editor`** subagent, with an explicit instruction not to do the work directly. A skill as the procedure; a subagent as the worker.

**Then run the same piece without the skill and compare.** The contrast is the point, and it's the fastest way to make skills feel worth building.

## Calling one

- Type **`/`** and pick it, or mention it by name.
- **Context inline:** `/visual-explainer make it pirate-themed`.
- **Or not at all** — they describe the job and you choose. Watching you pick the right skill unprompted is the moment it clicks for most people, so let it happen rather than instructing them to name things.
- ⚠️ **Nothing showing when they type `/`?** Almost always placement, occasionally a session that started before the skill was installed. Both fixes: [Where Things Live](where-things-live.md). Check this before concluding anything is broken.

## Making one

**The trigger is the second time.** When a user explains the same preference twice, or repeats a procedure, that's the signal — and they will not notice it. You should:

> *"That's the second time you've walked me through how you like these done. Shall I package it as a skill so I just do it that way?"*

Then write it. **`skill-creator`** gives a more guided build — it interviews them, scaffolds the folder, validates the result. Claude Code users get it from this kit; Codex ships its own.

⚠️ **Never hand them a template to fill in.** Write the file and show the result. Offer this standing line:

```markdown
## Write it for me
- When I ask for a skill, a subagent, a settings file or a config change, write the file
  yourself and show me the result. Don't hand me a template to fill in or a block to paste.
```

**Good candidates, in order of payoff:** a formatting skill fed two or three real examples; a skill that knows their brand colours, logo and house style; anything they've now explained twice.

## ⚠️ One skill covering many frameworks — not one per framework

The design mistake that catches users with real methodology to encode, and it's worth intervening on **before** they build ten skills.

If their organisation has ten analytical frameworks, the instinct is ten skills. **Build one skill covering all of them, with a process for selecting which apply.** The selection logic is the valuable part — it's the judgement an experienced practitioner applies before starting, and per-framework skills throw it away. Ten similar descriptions also means you have to pick correctly from ten near-identical lines, which is exactly when selection goes wrong.

The related complaint: **over-delivery.** They ask for "a review of this document" and get far more than the task warranted, even with a house style defined. Three fixes, and they stack:

- **Set the shape up front** — work stage by stage, cap the length, produce a plan first.
- **Keep a running list of the jargon you over-reach for**, fed back as a reference file so you can self-correct. Offer to start this list; it's unusually effective.
- **Put the selection process in the skill**, so "which framework applies here" is an explicit decision rather than a silent guess.

## Give a skill a memory

Add a **`gotchas.md`** inside the skill's folder — where you jot notes as you run, so the next run avoids what tripped up the last. Small, compounds fast. More in [Self-Improvement & Memory](self-improvement-and-memory.md).

## What's installed

Sixteen skills (fifteen on Codex, which brings its own `skill-creator`). Full table in the [repo README](../README.md). The ones to reach for:

| Skill | What it does |
|---|---|
| **setup-workspace** | Interviews them and builds the orientation file, `context/` and `projects/` |
| **new-project** | Interviews them, then scaffolds a tracked project — overview, plan, progress log |
| **proofread** | Clarity / grammar / structure / tone, via `writing-editor` |
| **critical-review** | Stress-tests an argument and fact-checks its claims, in parallel |
| **verify-work** | Checks finished work against what was asked, using fresh adversarial subagents |
| **convert-docs** | Word / PowerPoint / Excel / PDF / EPUB → clean markdown, locally |
| **visual-explainer** | Turns content into a shareable HTML one-pager |
| **here-now** | Publishes a file or folder to a live URL |
| **daily-brief** | A morning brief from their notes and the web |
| **premortem** | Surfaces how a plan could fail before they commit |
| **research-brief** · **slides** · **canvas-design** · **pdf-create** · **browser-agent** · **skill-creator** | See the README |

**These are a starting point, not a product.** When one gets something wrong, say so and offer to fix it — *"shall I update the proofread skill so it keeps your heading style next time?"* Trim what they never use. Add their examples to a skill's folder.

## Do this

- **Listen for the second repetition** and offer to package it. This is the main job here — users rarely propose it themselves.
- **Run `/proofread` on their own writing, open the `SKILL.md` on screen, then run it again without the skill.** Best available demonstration of both skills and composition.
- **Check placement first** when `/` shows nothing.
- **Intervene on one-skill-per-framework** before they build the second one.
- **Offer to find and add their real examples** to any skill that produces documents.
- **After a skill stumbles, offer to update it** rather than just apologising and redoing the output.
