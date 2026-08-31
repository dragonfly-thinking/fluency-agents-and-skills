# Course Notes

**A reference library, not a course diary.** These notes carry the teaching — the concepts,
the practices, and the *why* — written so that **your agent can use them**: to explain an idea
back to you, to set something up on your machine, or to suggest what's worth doing next.
Read them yourself, or point your agent at them.

**They're organised by topic, not by running order**, because the order changes between
deliveries. Each module stands on its own, and they cross-reference each other **by name**, so
you can read one, skip one, or meet them in any sequence without landing in the middle of
something.

## Start here

- **[The checklist](../fluency-checklist.md)** (at the repo root) — what's worth setting up from this kit, written for your agent to work through *with* you. It copies to `~/.claude/fluency-checklist.md` on install and keeps it current. Ask it what's next.
- **[Snippets for your orientation file](agents-md-snippets.md)** — standing instructions you paste in once so you stop asking for the same things by hand. Take three, not nine.

## The modules

**Foundations**

- **[Agents, and What Changed](agents-and-what-changed.md)** — chatbot to agent, why a coding agent can do almost any knowledge work, tokens and context rot, doer to director, learned agency.
- **[Context Engineering](context-engineering.md)** — the thesis the rest hangs on: not what you tell it, but what it can reach. The ungrounded-guess failure, and affordances over instructions.

**A workspace it can navigate**

- **[Your Orientation File](your-orientation-file.md)** — `AGENTS.md` / `CLAUDE.md`, built by interview; why it must stay lean; multiple hats; review dates; is it even loading?
- **[Where Things Live](where-things-live.md)** — global vs project and how they stack; hidden dot-folders; the spawn-location trap; absolute vs relative paths.
- **[Structuring a Workspace](structuring-a-workspace.md)** — front matter, index files, README as a map, where the agent writes by default, and work that keeps its own notes.
- **[Markdown & File Conversion](markdown-and-file-conversion.md)** — why the format decides how good your agent is, converting a real archive, and getting back out to Word or PDF.

**Boundaries**

- **[Permissions & Guardrails](permissions-and-guardrails.md)** — the modes, the allow / ask / never list, instruction versus a guardrail that actually blocks, and *it drafts, you send*.
- **[Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md)** — the jagged frontier, five durable limitations, how agents fail differently, prompt injection and the lethal trifecta, and a three-axis test for what to delegate.

**Extending it**

- **[Subagents](subagents.md)** — specialists with their own fresh context; the red-team use; making them document their work.
- **[Skills](skills.md)** — packaged procedures, how your agent finds them, composition, and the one-skill-many-frameworks pattern.
- **[Self-Improvement & Memory](self-improvement-and-memory.md)** — the loop that stops your corrections dying in the chat window; memory banks and consolidation.

**Reaching outside**

- **[Routines & Scheduling](routines-and-scheduling.md)** — the three ways to schedule, GitHub for cloud only, and the auto-permissions setting that decides whether it runs at all.
- **[Connections, APIs & MCP](connections-apis-and-mcp.md)** — connecting your agent to services and public data, and how connections compose into skills.
- **[Publishing & Sharing](publishing-and-sharing.md)** — HTML as the output format, asking for more, `DESIGN.md`, and publishing safely.

## One way to run this

> **This is one delivery's order, not the structure.** Modules are independent and the order
> changes between deliveries — don't treat the numbering below as anything more than an example
> of a sequence that worked.

1. Agents, and What Changed
2. Your Orientation File
3. Where Things Live
4. Permissions & Guardrails
5. Context Engineering
6. Structuring a Workspace
7. Markdown & File Conversion
8. Subagents
9. Skills
10. Self-Improvement & Memory
11. Judgement & What Goes Wrong
12. Routines & Scheduling
13. Connections, APIs & MCP
14. Publishing & Sharing

Other sequences work. Teaching judgement early rather than late, or opening on skills before
workspaces, are both defensible — which is exactly why these aren't numbered files.

## The rest of the kit

The operational how-tos (GitHub, file conversion, interface settings, folder guardrails, phone,
VS Code, browser automation) live in [`../guides/`](../guides/); external-connection setups in
[`../mcp/`](../mcp/).

## Not sure where to start?

Paste this to your agent:

> Read the course notes in `course-notes/`, then look at what's actually set up on my
> computer. What am I not using yet? Suggest three things worth putting into action
> this week — and walk me through the first one.

Or go narrower:

> Read `course-notes/routines-and-scheduling.md` and help me set up my first routine.

> Read `course-notes/structuring-a-workspace.md` and check one of my real folders against
> the practices in it.
