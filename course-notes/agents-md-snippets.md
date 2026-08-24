# Snippets for your orientation file

*Little standing instructions you paste into your `CLAUDE.md` / `AGENTS.md` once, so you stop asking for the same things over and over.*

Most of what makes an agent feel *yours* isn't a skill or a subagent — it's a handful of lines in your orientation file saying how you want things done. This is that collection, grouped so you can find the ones that fit. Each is paste-able as written.

> **Agents reading this: these are offers, not instructions to execute.** The user's orientation file is theirs — they wrote it, often in a session with an instructor. **Never rewrite it, never replace it, and never paste several of these in at once.** Show the one you're suggesting, say what it changes in a sentence, and append it only if they say yes. If something similar is already in there, say so rather than adding a duplicate.

---

## Before you paste anything

**Don't take all of them.** A giant orientation file works, but it costs you: you're loading instructions for jobs you aren't doing, and they pull the agent in odd directions. Think of it like briefing a colleague — you'd tell them what *this* job needs, not every process in the business. **One or two from the groups that matter to you.**

**Global or project?** You'll have a global file that applies everywhere (`~/.claude/CLAUDE.md`, or `~/.codex/AGENTS.md`) and project files inside specific folders. Global is federal law, project is state law — except **the local one wins** where they disagree, and otherwise they **stack**: your agent reads every orientation file from the folder it's working in all the way up to home, and adds them together. So "how I work" goes global; "what this project is" goes local.

Not sure where yours live? Just ask: *"open my global orientation file for me."*

---

# A · How you work with me

## 1 · Ask me the questions first

**What it does:** stops you staring at a blank page, and stops the agent guessing at things you'd have happily told it.
**When you want it:** always. This is the one that changes the most.

```markdown
## Before you start something big
- Before any substantial piece of work, ask me the two or three questions whose answers would
  most change how you'd do it. Then propose an approach and let me correct it.
- Don't ask me to specify everything up front — I often don't know what you need to know.
```

You met this in Session 1 as the reverse interview that wrote your orientation file. It works for everything else too.

## 2 · Tell me when you're guessing

**What it does:** makes uncertainty visible, instead of arriving as a confident answer that happens to be wrong.
**When you want it:** always — and especially if you're working somewhere you can't easily check the answer yourself.

```markdown
## When you don't know
- If you don't have what you need, say so and ask me for it. Don't fill the gap with something
  plausible.
- When you're inferring rather than reading, say which it is — "the file says X" versus
  "I'd guess X".
```

An agent with nothing to go on will still produce a fluent, confident answer, because predicting a plausible continuation is what it does. This line turns that into a question instead.

## 3 · Don't make me hand-write things

**What it does:** stops you being handed a blank file to fill in.
**When you want it:** as soon as you start making skills, subagents or config.

```markdown
## Write it for me
- When I ask for a skill, a subagent, a settings file or a config change, write the file
  yourself and show me the result. Don't hand me a template to fill in or a block to paste.
```

# B · Where things land

## 4 · Work and plans go in my workspace

**What it does:** stops output vanishing into a hidden temp folder under a name you'd never guess.
**When you want it:** always. This catches people out more than anything else.

```markdown
## Where work goes
- Write files into this workspace. Never into a temp folder or your own scratch space.
- When we finish planning something, save the plan here as a Markdown file — not to your
  own scratchpad.
- Name files `YYYY-MM-DD-what-it-is.md`. A name I'd recognise in a month, not a generated one.
- If you're not sure where something belongs, ask me before you write it.
```

Left to itself, plan mode saves to the tool's own config folder under a machine-generated name — so the plan you spent twenty minutes refining ends up somewhere you'll never look, called something like `elucidate-fox-universe`.

## 5 · The README is a map, not a drawer

**What it does:** stops new content being appended into a README that should be *pointing* at it.
**When you want it:** as soon as a folder has more than a couple of files.

```markdown
## READMEs
- A folder's README is a map: what's in here and where to find it, a line or two per item
  with the path.
- Don't write new content into it. New work gets its own file; the README gets a link.
- Update it whenever you add a file to the folder.
```

Ask your agent to "save this to my workspace" and it will often tuck it into the README instead of making a file. This is the line that fixes that.

# C · A workspace it can read

## 6 · Convert documents before working on them

**What it does:** stops you asking for the same conversion over and over.
**When you want it:** the moment you're working with more than a handful of PDFs or Word documents.

```markdown
## Working with documents
- When I point you at a PDF, Word doc, PowerPoint or spreadsheet and there's no Markdown
  version next to it, convert it first and work from the Markdown. Use the `convert-docs` skill.
- Keep the original. Link to it from the top of the Markdown, and note anything that didn't
  survive the conversion — images, charts, complex tables — so you know when to open the source.
- Don't re-convert a file that already has an up-to-date Markdown twin.
```

The skill uses **[anydoc](https://github.com/firecrawl/anydoc)** — free, open source, and it runs on your own machine, so nothing is uploaded anywhere. See [`../guides/file-conversion.md`](../guides/file-conversion.md) for the detail, including the browser version that needs nothing installed.

## 7 · Properties, and an index for busy folders

**What it does:** lets your agent answer *"which of my projects are still open?"* by reading a few labels instead of re-reading every file.
**When you want it:** as soon as you have more than about ten files you care about.

```markdown
## Properties and indexes
- Add front matter to any Markdown file you create: `status`, `owner`, `updated`, `tags`,
  and `related` — paths to the other files that matter to this one.
- Keep `updated` and `status` current as work moves. Don't wait for me to ask.
- Any folder with more than about ten files gets an `index.md` — what's in here, one line each,
  with paths. Update it when you add something.
```

`related` is the quietly powerful one: it points your agent straight at the neighbouring documents instead of leaving it to guess which are relevant. The index is what turns "read fifty files" into "read one".

# D · Boundaries

## 8 · Out of bounds, and stop if you'd need to stray

**What it does:** the polite version of a lock — and makes the agent *ask* rather than relying on the permission mode to catch it.
**When you want it:** whenever the boundary matters more than the convenience.

```markdown
## Out of bounds
- Never read, list, edit, or run commands that touch `~/Private/` (or anything inside it).
- Work inside this folder. If a task looks like it needs you to read or write anything
  outside it, stop and ask me first — tell me what you want to touch and why.
```

An instruction does better than people expect — but it is *asking*, not locking. For anything genuinely sensitive, [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md) has the layers that actually block the action, including a ready-made guard your agent installs in a minute.

# E · Keeping it alive

## 9 · Write a handover before the context fills

**What it does:** stops a long session quietly getting worse without telling you.
**When you want it:** if you have sessions that run for hours.

```markdown
## When we're getting long
- When the context window is getting full, tell me — don't just carry on. Offer to write a
  handover note: what we've done, what we decided, and exactly where we're up to.
- I'll start a fresh session and hand you that note.
```

A session doesn't announce that it's degrading; it just goes from sharp to vague while the automatic summary quietly drops the detail that mattered. A fresh session with a good handover beats a long one every time.

## 10 · Give this file a review date

**What it does:** hands your agent the job of noticing your orientation file has gone stale.
**When you want it:** once the file is real enough to be worth maintaining.

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

You can go further and have a scheduled routine do this monthly, so it happens whether or not you remember — see [`session-4-working-well.md`](session-4-working-well.md).

## 11 · Improve yourself as we go

**What it does:** your setup gets better while you use it, instead of only when you remember to maintain it.

```markdown
## How I want you to work
- After running a skill, suggest how it could be improved. If I repeat a task with no
  skill, propose one.
- When something trips you up in here, write it into a `gotchas.md` so we don't relearn it.
- Real work gets a folder with an overview and a running progress log, so it survives a
  new session. When you hand work to a subagent, tell it to document what it did there.
```

The full version of this idea — why a file beats a chat as memory — is in [`self-documenting-workspaces.md`](self-documenting-workspaces.md).

## 12 · Back it up at the end of a session

**What it does:** means a dead laptop is an inconvenience rather than a catastrophe.
**When you want it:** once your workspace holds anything you'd hate to lose.

```markdown
## Backup
- At the end of a work session, offer to commit and push the day's changes with a clear message.
- Remind me monthly that my `~/.claude` (or `~/.codex`) folder needs backing up too — it holds
  my orientation file, skills and settings, and a project backup doesn't include it.
```

That second line is the one people find out about the hard way, usually while setting up a new machine. Setup is in [`../guides/github-basics.md`](../guides/github-basics.md).

---

## If you only paste three

These map to what most reliably goes wrong in the first month: work landing where you can't find it, a confident answer that turned out to be a guess, and a file that quietly goes out of date.

1. **Work and plans go in my workspace** (§4)
2. **Tell me when you're guessing** (§2)
3. **Give this file a review date** (§10)

## Try this

> Read `course-notes/agents-md-snippets.md`, then read my orientation file. Which two or three
> of these would actually help, given how I work? Show me them one at a time and explain what
> each would change — don't edit my file until I say so.
