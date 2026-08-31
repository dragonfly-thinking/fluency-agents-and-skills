# Skills

*Packaged standard operating procedures — the way you codify how *you* want a job done, once, so you stop explaining it.*

A skill is a **folder your agent reads on demand**. Inside it, a `SKILL.md` file says what the job is, when to use it, and how you want it done. That's the whole requirement. Everything else — checklists, examples, reference files, scripts — is optional and loaded only when the instructions call for it.

If a subagent is a *specialist*, a skill is a *verb*: "proofread this", "build me a deck", "run a premortem". Skills are how your agent gets meaningfully better at the specific work you actually do.

---

## How your agent knows a skill exists

This is worth understanding properly, because it explains why you can install dozens of skills without slowing anything down.

**Your agent pre-loads only each skill's name and description.** That's it — a line or two per skill, sitting in context. When it decides one is relevant to what you're doing, *then* it loads the full `SKILL.md` and whatever that file points at.

This is true on both runtimes. OpenAI's documentation puts it plainly: *"ChatGPT and Codex start with each skill's name and description, then load the full SKILL.md instructions when they decide to use that skill."*

Two consequences:

- **The description is the most important line in the file.** It is the entire basis on which the skill gets chosen. Write it as *when to use this*, not *what this is*.
- **A big library is cheap.** Twenty unused skills cost you twenty lines of context, not twenty documents.

The same mechanic drives [subagent](subagents.md) selection on Claude. Where the skill has to *sit* for any of this to work — and the trap that catches everyone — is in [Where Things Live](where-things-live.md).

## What's in a `SKILL.md`

- **Front matter** with a `name` and a `description` — the two lines above.
- **The instructions**: what the job is, the steps, the standards, the shape of the output.
- **Optionally, anything else in the folder** — a checklist, worked examples, a style reference, a script. Referenced from the instructions, loaded when needed.

**Point a skill at your files.** This is the move that turns a generic skill into yours: put your actual materials in the folder, or point at paths in your workspace. Two or three examples of the documents you typically produce will do more for output quality than any amount of describing.

## Composition — skills, subagents, and skills again

Skills can **dispatch subagents**, and subagents can invoke skills. That layering is where the real capability sits.

The clearest example is in the kit: run **`/proofread`** and open its `SKILL.md`, and you'll see it does **not** do the editing itself. It delegates to the **`writing-editor`** subagent, with an explicit instruction not to do the work directly. A skill as the standard operating procedure; a subagent as the worker it hands off to.

Worth running once on your own writing, then running the same piece *without* the skill and comparing. The contrast is the point.

## Calling one

- Type **`/`** and pick it from the list, or just mention it by name.
- **Add context inline:** `/visual-explainer make it pirate-themed`.
- Or don't name it at all. Describe the job and let the agent choose — that's the name-and-description mechanic above doing its work, and watching it pick the right skill unprompted is the moment the whole thing clicks.
- **Skill not showing when you type `/`?** Almost always placement, and occasionally a session that started before the skill was installed. [Where Things Live](where-things-live.md) has both fixes.

## Making your own

**The simplest way is to just ask**, right after you've done something you'll do again:

> *"Turn what we just did into a skill. Write the `SKILL.md` for me, and put it somewhere I'll be able to use it everywhere."*

For a more guided build, **`skill-creator`** interviews you, scaffolds the folder, and validates the result. Claude Code users get it from this kit; Codex ships its own.

**Never hand-write one.** If your agent offers you a template to fill in, tell it to write the file itself and show you the result. Worth a standing line:

```markdown
## Write it for me
- When I ask for a skill, a subagent, a settings file or a config change, write the file
  yourself and show me the result. Don't hand me a template to fill in or a block to paste.
```

**Good candidates**, in rough order of payoff:

- A **formatting skill**, fed two or three examples of what you actually produce.
- A skill that knows your **brand colours, logo and house style**, so visual outputs come out consistent instead of randomly themed.
- Any procedure you have now explained to your agent **twice**. The second time is the signal.

## ⚠️ One skill covering many frameworks — not one skill per framework

This is the design mistake that catches people who have real methodology to encode, and it is worth getting right the first time.

If your organisation has ten analytical frameworks, the instinct is ten skills. Don't. **Build one skill that covers all of them, with a process for selecting which ones apply.** The selection logic is the valuable part — it's the judgement an experienced practitioner applies before they start, and it is exactly what a per-framework skill throws away. Ten separate skills also means your agent has to pick correctly from ten similar descriptions, which is precisely the situation where it picks wrong.

The same problem shows up as **over-delivery**: you ask for "a review of this document" and get back far more than the task warranted, even with a house style already defined. Three fixes, and they stack:

- **Set the shape up front** — work stage by stage, cap the length, ask for a plan first.
- **Keep a running list of the jargon it over-reaches for**, fed back to it as a reference file so it can self-correct.
- **Put the selection process in the skill**, so "which framework applies here" is a decision the skill makes explicitly rather than a guess it makes silently.

## Give a skill a memory of its own

Add a **`gotchas.md`** (or `tips.md`) inside the skill's folder — somewhere the agent jots notes to itself as it runs, so the next run avoids whatever tripped up the last one. Small habit, compounds fast. More on this in [Self-Improvement & Memory](self-improvement-and-memory.md).

## What's in the kit

Sixteen skills ship with this kit (fifteen on Codex, which brings its own `skill-creator`). Full table in the [repo README](../README.md). The ones worth knowing by name:

| Skill | What it does |
|---|---|
| **setup-workspace** | Interviews you and builds your orientation file, `context/` and `projects/` |
| **new-project** | Interviews you, then scaffolds a tracked project — overview, plan, progress log |
| **proofread** | Clarity / grammar / structure / tone pass, via `writing-editor` |
| **critical-review** | Stress-tests an argument and fact-checks its claims, in parallel |
| **verify-work** | Checks finished work against what was actually asked, using fresh adversarial subagents |
| **convert-docs** | Word / PowerPoint / Excel / PDF / EPUB → clean markdown, locally |
| **visual-explainer** | Turns content into a shareable HTML one-pager |
| **here-now** | Publishes a file or folder to a live URL |
| **daily-brief** | A morning brief from your notes and the web |
| **premortem** | Surfaces how a plan could fail before you commit |
| **research-brief** · **slides** · **canvas-design** · **pdf-create** · **browser-agent** · **skill-creator** | See the README |

**They are a starting point, not a product.** Trim the ones you never use, adjust defaults, add your own examples to a skill's folder. When one gets something wrong, say so — *"that wasn't quite right; update the proofread skill so it keeps my heading style next time"* — and it fixes itself.

## Try this

> Run `/proofread` on something I actually wrote. Then open its `SKILL.md` and show me what
> it's doing — I want to see that it hands the work to a subagent rather than doing it
> itself. Then run the same piece again *without* the skill, and tell me what's different.
