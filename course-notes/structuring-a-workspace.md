# Structuring a Workspace

**Read this when** your user asks how to organise their files, wants you to track project status, asks "which of my projects are still open", has a folder you keep having to re-read, asks where you saved something, or wants work to survive between sessions. Also read it when you're about to start a substantial piece of work and there's nowhere sensible to put it.

*This module is about what goes* inside *their folders. The shape of the folders themselves is [Where Things Live](where-things-live.md).*

---

## The idea to keep coming back to

> **A chat is ephemeral. A file is not.**

Everything said in a session disappears when it ends, and when the context window fills the automatic summary is *lossy* — it doesn't know which small detail was the important one. So the habit worth building in your user is this: **leave a trail — durable files documenting what was done and where the work is up to.**

Concrete, persistent, reloadable. If their computer dies mid-task, the folder is still there and a fresh session can be pointed straight at it. **The workspace, not the chat, becomes the memory.**

Don't lecture this. Demonstrate it by doing it, then name what you did.

## Properties — the labels that make a folder scannable

At the top of a markdown file, a small block of labels marked off by three dashes. Called **front matter** (technically YAML — don't say that unless asked).

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

- **They never type these. You do.** If a user starts hand-writing front matter, stop them.
- **The payoff to explain:** they ask *"which of my projects are still open?"* and you read a handful of labels instead of opening and interpreting every file. On fifty projects that's a minute versus an afternoon.
- **`related` is the quietly powerful one.** Paths to the documents that matter to this one, so your next step is *reading them* rather than guessing which are relevant. Across a folder it becomes a web you can trace rather than a pile you have to search. Users don't discover this on their own — offer it.
- **Keep `status` and `updated` current yourself, without being asked.** This is the part that never works in a project-management tool, because a human has to remember. You don't. Say so — *"every time we finish something, I'll update the status"* — because it's a genuinely surprising benefit and it sells the whole practice.

## An index for busy folders

- Any folder with more than about ten files they care about gets an **`index.md`**: what's in here, one line each, with the path. A small markdown table is ideal.
- **The payoff:** you read the index and jump to the one file you need, instead of reading fifty.
- **Never make them hand-write a markdown table.** The symbols are fiddly and it's exactly the job to hand over.
- **Offer to make it self-maintaining** — a standing line so any folder crossing that threshold gets an index and it stays current.

## The README is a map, not a drawer

- **A folder's README says what's in here and where to find it** — a line or two per item, with the path.
- ⚠️ **This is a mistake you will make unless instructed otherwise.** Asked to "save this to my workspace", agents very often append the content to the README instead of creating a file. **New work gets its own file; the README gets a link.**
- Worth offering as a standing line: *"A folder's README is a map: what's in here and where to find it. Don't write new content into it. Update it whenever you add a file."*

## Where you write by default — and why it's wrong

Left to itself, plan mode saves plans to the **tool's own configuration folder** under a machine-generated name. So twenty minutes of refinement ends up somewhere they will never look, called something like `elucidate-fox-universe`.

Same for scratch output generally: temp folders, hidden config directories, your own scratchpad.

**Fix it once, and offer this proactively — it catches people out more than anything else:**

```markdown
## Where work goes
- Write files into this workspace. Never into a temp folder or your own scratch space.
- When we finish planning something, save the plan here as a Markdown file.
- Give it a name I'd recognise in a month, not a generated one.
- If you're not sure where something belongs, ask me before you write it.
```

**Naming.** A date prefix — `2026-08-31-what-it-is.md` — sorts chronologically and shows age at a glance. Ask their convention once, put it in the orientation file, then apply it without asking again.

## Work that tracks itself

Real work gets a folder, and the folder keeps its own notes. Three files carry almost all the value:

- **`overview.md`** — what this is, why it exists, where it's up to.
- **`plan.md`** — the approach, agreed once and saved rather than re-derived every session.
- **`progress.md`** — a running log you update as you work: what you did, what you decided, what tripped you up.

The **`new-project`** skill scaffolds exactly this, and interviews them first rather than handing over empty templates.

**Why it matters, if they ask:** context windows are finite and their automatic summaries are lossy. Self-contained units with their own files mean a fresh session — or a recovery after a crash — reads the folder and picks up where the last one stopped. So do [subagents](subagents.md), which is the whole reason delegation works.

Three smaller habits, each worth offering unprompted:

- **A scratch pad.** A markdown file you jot working notes into as you go. Like paper next to you. If something breaks: *"read this, bring yourself up to speed, keep going."*
- **Save the plan.** After going back and forth in plan mode, write it into the project. Don't wait to be asked — they will not think of it, and this is the exact thing that gets lost.
- **A `gotchas.md`.** Where you write down what tripped you up, so the next run doesn't relearn it. Works inside a project *and* inside a [skill](skills.md).

**When you hand work to a subagent — which they can't watch — tell it to document what it did in that folder.** Its work stops being a black box. Worth a standing line:

```markdown
- When you hand work to a subagent, tell it to document what it did in that folder.
```

## This is a published standard, if they want the reassurance

None of the above is a house habit. In June 2026 Google published the **[Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)**, describing almost exactly this: a directory of markdown files with YAML front matter, with optional `index.md` files so an agent can navigate a hierarchy without reading all of it.

Useful with users who want to know they aren't adopting one firm's quirk. **The point isn't to adopt a specification** — it's that this is now vendor-neutral and published, so what they set up keeps working as more tools support it. Tell them to read the opening and the file-layout section and then stop; the rest is written for data engineers.

## Do this

- **Pick one folder they actually work in** — ideally the one they complain about — and tell them honestly how hard it is for you to navigate: what would you have to open to answer a simple question about it?
- **Then do three things and show each before writing:** add front matter to the files that matter, write an `index.md`, and turn the README back into a map if it's become a drawer.
- **Fix the where-you-write problem before it bites**, not after they've lost a plan. Offer the standing lines above the first time you save anything.
- **Save plans without being asked.** Every time.
- **Start keeping `status` and `updated` current from now on**, and tell them you're doing it.
- **Scaffold real work as a folder** with an overview and a progress log rather than working loose in the chat — and say why once, briefly.
