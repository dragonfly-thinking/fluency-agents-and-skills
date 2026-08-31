# Structuring a Workspace

*Making a folder legible to a machine: labels, indexes, and work that keeps its own notes.*

[Where Things Live](where-things-live.md) covers the shape of your folders and where they sit. This is about what goes *inside* them — the small conventions that turn "read fifty files to answer that" into "read one".

The one idea underneath all of it:

> **A chat is ephemeral. A file is not.**

Everything you say to an agent disappears when the session ends, and when the context window fills the automatic summary is *lossy* — it doesn't know which small detail was the important one. So the best habit you can build is this: **get your agents to leave a trail — durable files that document what they did and where the work is up to.** Concrete, persistent, reloadable. If your computer dies mid-task, the folder is still there, and any fresh session can be pointed straight at it. **The workspace, not the chat, becomes the memory.**

---

## Properties — the labels that make a folder scannable

At the top of a markdown file you can add a small block of labels, marked off by three dashes. It's called **front matter** (technically YAML; you never need to know that).

```markdown
---
status: in-progress
owner: me
updated: 2026-08-31
tags: [client-work, q3]
related:
  - projects/q3-launch/plan.md
  - background/company-overview.md
---
```

- **You never type these.** Ask: *"add front matter to this file to help us track it — suggest sensible properties for the kind of work I do."*
- **What it buys you:** ask *"which of my projects are still open?"* and the agent reads a handful of labels instead of opening and interpreting every file. On a folder of fifty projects that is the difference between a minute and an afternoon.
- **`related` is the quietly powerful one.** List the paths of the documents that matter to this one and the agent's next step is *reading them*, not guessing which are relevant. Do it across a folder and you have a web of connected documents it can trace rather than a pile it has to search.
- **Keep `status` and `updated` current** — and make that the agent's job, not yours. This is the part that never works in a project-management tool, because a human has to remember. An agent doesn't: *"every time we finish something, update the status."* It just does it.

## An index for busy folders

- Any folder with more than about ten files you care about gets an **`index.md`**: what's in here, one line each, with the path. A small markdown table is ideal.
- **The payoff:** instead of reading fifty project files to work out what's going on, the agent reads the index and jumps straight to the one it needs.
- **You will never hand-write a markdown table.** The symbols are fiddly and it is exactly the job to hand over. Agents render them perfectly.
- Make it a standing instruction so it maintains itself: *"any folder with more than about ten files gets an `index.md`; update it when you add something."*

## The README is a map, not a drawer

- **A folder's README says what's in here and where to find it** — a line or two per item, with the path. That's it.
- **Don't let new content be written into it.** Ask an agent to "save this to my workspace" and it will very often append it to the README instead of making a file. New work gets its **own file**; the README gets a **link**.
- The rule, worth pasting into your orientation file: *"A folder's README is a map: what's in here and where to find it. Don't write new content into it. Update it whenever you add a file."*

## Where the agent writes by default — and why it's wrong

Left to itself, plan mode saves your plan to the **tool's own configuration folder** under a machine-generated name. So the plan you spent twenty minutes refining ends up somewhere you will never look, called something like `elucidate-fox-universe`.

Same for scratch output generally: temp folders, hidden config directories, its own scratchpad.

**Fix it once, in your orientation file:**

```markdown
## Where work goes
- Write files into this workspace. Never into a temp folder or your own scratch space.
- When we finish planning something, save the plan here as a Markdown file.
- Give it a name I'd recognise in a month, not a generated one.
- If you're not sure where something belongs, ask me before you write it.
```

**Name things so you can find them.** A date prefix — `2026-08-31-what-it-is.md` — sorts chronologically and tells you at a glance how old something is. Put your convention in the orientation file and stop thinking about it.

## Work that tracks itself

Real work gets a folder, and the folder keeps its own notes. Three files carry almost all of the value:

- **`overview.md`** — what this is, why it exists, where it's up to.
- **`plan.md`** — the approach, agreed once and saved rather than re-derived every session.
- **`progress.md`** — a running log the agent updates as it works: what it did, what it decided, what tripped it up.

The kit's **`new-project`** skill scaffolds exactly this, and interviews you first rather than handing you empty templates.

Why it matters: **context windows are finite and their automatic summaries are lossy.** Break work into self-contained units with their own files and a fresh session — or a recovery after a crash — reads the folder and picks up exactly where the last one left off. So do subagents, which is the whole reason [Subagents](subagents.md) work at all.

Three related habits, each small:

- **A scratch pad.** Just a markdown file the agent jots working notes into as it goes. Like having paper next to you. If something goes wrong, you say *"read this, bring yourself up to speed, and keep going."*
- **Save the plan.** After going back and forth in plan mode, ask for it as a file in the project. Future sessions read it instead of re-deriving it.
- **A `gotchas.md`.** Somewhere the agent writes down what tripped it up, so the next run doesn't relearn it. Works inside a project *and* inside a [skill](skills.md).

And when you hand work to a subagent — which you can't watch — **tell it to document what it did in that folder.** Its work stops being a black box. Worth a standing line: *"when you invoke a subagent, tell it to document its work in a folder."*

## This is now a published standard

None of the above is a house habit any more. In June 2026 Google published the **[Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)**, and it describes almost exactly this: a directory of markdown files with YAML front matter, with optional `index.md` files so an agent can navigate a hierarchy without reading all of it.

The point isn't to adopt a specification. It's that **this way of working is now vendor-neutral and published**, so the structure you set up will keep working as more tools support it. Read the opening and the file-layout section, then stop — the rest is written for data engineers.

## Try this

> Look at one folder I actually work in. Tell me honestly how hard it is for you to navigate:
> what would you have to open to answer a simple question about it? Then do three things —
> add front matter to the files that matter, write an `index.md`, and turn the README into a
> map if it has become a drawer. Show me each before you write it.
