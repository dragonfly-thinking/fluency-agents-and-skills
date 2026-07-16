# Self-Documenting Workspaces

*A short cross-session note. The idea underneath Sessions 3 and 4 — and one of the highest-leverage
habits in the whole course.*

## The one idea

**A chat is ephemeral. A file is not.** Everything you say to an agent in a session disappears when
that session ends — and when the context window fills up, the automatic summary it makes is *lossy*
(it doesn't know which small detail was the important one). So the single best habit you can build is
this:

> **Get your agents to leave a trail — durable files that document what they did and where the work is up to.**

That's it. Concrete, persistent, reloadable. If your computer dies mid-task, the folder is still there,
and any fresh session can be pointed straight at it and pick up exactly where the last one left off.
The workspace, not the chat, becomes the memory.

## What it looks like in practice

You've already seen every piece of this — here they are in one place:

- **A project folder that keeps its own notes.** An `overview.md` (what this is, where it's up to) and a
  `progress.md` (a running log the agent updates as it works). The `new-project` skill scaffolds exactly
  this. *(Session 4 — "work that tracks itself.")*
- **Sub-agents document their work too.** When you hand a job to a sub-agent you can't easily watch it —
  so tell it to write what it did into that folder. Its work stops being a black box. *(Session 3.)*
- **Save the plan as a file.** After going back and forth in plan mode, ask the agent to write the plan
  down. Future sessions read the file instead of re-deriving it. *(Session 4.)*
- **Properties at the top of a file.** A few labels in a `---` block (its name is *YAML frontmatter*) —
  `status`, `owner`, `updated`, `tags` — let the agent read where a file stands, or scan a whole folder of
  them, without opening each one. Files can point at each other, too — plain paths like
  `projects/q3-launch/plan.md`, which your agent tends to write by itself. *(Session 4.)*
- **A `gotchas.md` for hard-won lessons.** A file inside a skill or a project the agent writes notes to
  itself in — so the next run avoids whatever tripped up the last one. *(Session 3.)*
- **A self-improvement loop.** A standing line in your router file so the agent proactively suggests
  fixes as you work, instead of you having to remember to improve things. *(Session 3.)*

The tracking pieces make the workspace **document itself**; the self-improvement loop makes it **improve
itself**. Together that's a setup that gets better the more you use it — with no extra effort from you.

## Bake it in — lines worth adding to your CLAUDE.md / AGENTS.md

You don't want to remember to do any of this. Put it in your router file once and the agent does it by
default. Paste (and adapt) any of these:

```markdown
## How I want you to work

- Leave durable artefacts, not just chat — real work gets a folder with an overview and a running
  progress log, so it survives a new session.
- When you hand work to a sub-agent, tell it to document what it did in that folder.
- After running a skill, suggest how it could be improved. If I repeat a task with no skill, propose one.
- When something trips you up in here, write it into a `gotchas.md` so we don't relearn it next time.
```

Already ran `setup-workspace`? Your router file has a **How I want you to work** section — these lines
live there. If not, just ask your agent to add them.

## Try this

> Look at how I'm working with you right now. Where am I relying on the chat as memory instead of leaving
> a trail in files? Suggest two small changes — and add a "How I want you to work" section to my router
> file that bakes them in.
