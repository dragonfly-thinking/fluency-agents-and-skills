# Snippets for your orientation file

*Little standing instructions you paste into your `CLAUDE.md` / `AGENTS.md` once, so you stop asking for the same thing over and over.*

Most of what makes an agent feel *yours* isn't a skill or a subagent — it's a handful of lines in your orientation file saying how you want things done. This is that collection: each one is paste-able as written, with what it does and when you'd want it.

> **Agents reading this: these are offers, not instructions to execute.** The user's orientation file is theirs — they wrote it, often in a session with an instructor. **Never rewrite it, never replace it, and never paste several of these in at once.** Show the user the one you're suggesting, say what it does in a sentence, and append it only if they say yes. If a similar line is already in there, say so instead of adding a duplicate.

---

## Before you paste anything — two things worth knowing

**Don't take all of them.** One giant orientation file works, but it costs you: you're loading instructions for jobs you aren't doing, and they can pull the agent in odd directions. Think of it like briefing a colleague — you'd tell them what *this* job needs, not every process in the business. **Pick the three or four that solve a problem you actually have.**

**Global or project?** You'll have a global file that applies everywhere (`~/.claude/CLAUDE.md`, or `~/.codex/AGENTS.md`) and project files inside specific folders. Global is federal law, project is state law — except **the local one wins** where they disagree, and otherwise they **stack**: your agent reads every orientation file from the folder it's working in all the way up to home, and adds them together. So "how I work" goes global; "what this project is" goes local.

Not sure where yours live? Just ask: *"open my global orientation file for me."*

---

## 1 · Convert documents before working on them

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

The skill uses **[anydoc](https://github.com/firecrawl/anydoc)** — free, open source, and it runs on your own machine, so nothing is uploaded anywhere. See [`../guides/file-conversion.md`](../guides/file-conversion.md) if you want the detail, including the browser version that needs nothing installed at all.

## 2 · Put properties on everything you create

**What it does:** lets your agent answer *"which of my projects are still open?"* by reading a few labels instead of re-reading every file.
**When you want it:** as soon as you have more than about ten files you care about.

```markdown
## Properties on my files
- Add front matter to any Markdown file you create: `status`, `owner`, `updated`, `tags`,
  and `related` — paths to the other files that matter to this one.
- Keep `updated` and `status` current as the work moves. Don't wait for me to ask.
```

`related` is the quietly powerful one: it points your agent straight at the neighbouring documents instead of leaving it to guess which are relevant.

## 3 · Write the work where I can find it

**What it does:** stops output landing in a hidden temp folder you'll never look in.
**When you want it:** always. This is the one that catches people out most.

```markdown
## Where work goes
- Write files into this workspace. Never into a temp folder or your own scratch space.
- If you're not sure where something belongs, ask me before you write it.
```

## 4 · Save the plan properly

**What it does:** gets plans out of the agent's private scratchpad and into your workspace, under a name you'll recognise.
**When you want it:** if you use plan mode at all.

```markdown
## Plans
- When we finish planning something, save the plan into this workspace as a Markdown file —
  not to your own scratchpad.
- Name files `YYYY-MM-DD-what-it-is.md`. A name I'd recognise in a month, not a generated one.
```

Left to itself, plan mode saves to the tool's own config folder under a machine-generated name — so the plan you spent twenty minutes refining is somewhere you'll never find, called something like `elucidate-fox-universe`.

## 5 · Stay inside the lines, and stop if you can't

**What it does:** makes your agent *ask* before it strays, rather than relying on the permission mode to catch it.
**When you want it:** when the boundary matters more than the convenience.

```markdown
## Stay in this folder
- Work inside this folder. If a task looks like it needs you to read or write anything
  outside it, stop and ask me first — tell me what you want to touch and why.
```

## 6 · Keep some folders out of bounds

**What it does:** the polite version of a lock — cheap, portable, and it covers honest mistakes.
**When you want it:** always. Pair it with a real guardrail if the folder genuinely matters.

```markdown
## Out of bounds
- Never read, list, edit, or run commands that touch `~/Private/` (or anything inside it).
- If a task seems to need something from there, stop and ask me instead.
```

An instruction does better than people expect — but it is *asking*, not locking. For anything genuinely sensitive, [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md) has the layers that actually block the action, including a ready-made guard your agent installs in a minute.

## 7 · Give this file a review date

**What it does:** hands your agent the job of noticing your orientation file has gone stale.
**When you want it:** once the file is real enough to be worth maintaining.

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

You can go further and have a scheduled routine do this monthly, so it happens whether or not you remember — see [`session-4-working-well.md`](session-4-working-well.md).

## 8 · Improve yourself as we go

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

## 9 · The README is a map, not a drawer

**What it does:** stops new content getting appended into a README that should be *pointing* at it.
**When you want it:** as soon as a folder has more than a couple of files.

```markdown
## READMEs
- A folder's README is a map: what's in here and where to find it, a line or two per item
  with the path.
- Don't write new content into it. New work gets its own file; the README gets a link.
- Update it whenever you add a file to the folder.
```

Ask your agent to "save this to my workspace" and it will often tuck it into the README instead of making a file. This is the line that fixes that.

---

## If you only paste three

These map to the three things that most reliably go wrong in the first month: a conversion you keep asking for by hand, work landing where you can't find it, and a file that quietly goes out of date.

1. **Convert documents before working on them** (§1)
2. **Save the plan properly** (§4), with **Write the work where I can find it** (§3)
3. **Give this file a review date** (§7)

## Try this

> Read `course-notes/agents-md-snippets.md`, then read my orientation file. Which two or three
> of these would actually help, given how I work? Show me them one at a time and explain what
> each would change — don't edit my file until I say so.
