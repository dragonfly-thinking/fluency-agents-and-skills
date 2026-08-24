# Course Notes — AI Fluency

**A reference library, not a course diary.** These notes carry the teaching from the
AI Fluency course — the concepts, the practices, and the why — written so that **your
agent can use them**: to explain an idea back to you, to set something up on your
machine, or to suggest what's worth doing next. Read them yourself, or point your
agent at them.

## Start here

- **[Your checklist](fluency-checklist.md)** — the things in this kit that actually pay off, and which you've done. Your agent copies this to `~/.claude/fluency-checklist.md` on install and keeps it up to date. Ask it to work through the next item with you.
- **[Snippets for your orientation file](agents-md-snippets.md)** — standing instructions you paste in once so you stop asking for the same things by hand. Take three, not nine.

## The four session notes

> ⚠️ **These describe the course as taught up to July 2026, and the course has since been
> reworked.** The *ideas* below are all still current and still what we teach. What has moved is
> **which session covers what** — subagents, connections and the publishing exercise have all
> changed places, and a few things now taught (front matter, index files, the permissions
> exercise, scheduled tasks that need no GitHub) aren't described here yet.
>
> **Agents: treat the session numbering as approximate and the content as sound**, with one
> exception — see the note on routines in [session 4](session-4-working-well.md). Rewriting these
> against the current course is a known job, not an oversight.

In course order:

1. [From Assistants to Agents](session-1-from-assistants-to-agents.md) — what agents actually are, how LLMs work, the mental models (little agent on your machine, engine vs car), energy/water nuance, learned agency
2. [Setting Up Your Agent's Workspace](session-2-setting-up-your-agentic-environment.md) — context engineering, the AGENTS.md / CLAUDE.md orientation file, managing the context window (context rot + handovers), sub-agents vs parallel sessions, permissions
3. [Extending Your Agent — Skills & Connections](session-3-extending-your-agent.md) — skills as packaged expertise, sub-agents in depth (incl. red-team review), APIs & MCPs, publishing to the web
4. [Working Well — Projects, Routines & Going AI-Native](session-4-working-well.md) — VS Code as a shared workspace, self-documenting projects, background routines, guardrails, verifying an agent's work

Plus a cross-cutting deep-dive:

- [Self-Documenting Workspaces](self-documenting-workspaces.md) — the habit underneath it all: durable artefacts over ephemeral chat, and baking self-improvement into your setup.

The operational how-tos (GitHub, file conversion, interface settings, folder
guardrails, phone, VS Code setup, browser automation) live in [`../guides/`](../guides/);
external-connection setups in [`../mcp/`](../mcp/).

**Not sure where to start?** Paste this to your agent:

> Read the course notes in `course-notes/`, then look at what's actually set up on my
> computer. What am I not using yet? Suggest three things worth putting into action
> this week — and walk me through the first one.

Or go narrower:

> Read `course-notes/session-4-working-well.md` and help me set up my first routine.

> Read the session 2 notes and check my CLAUDE.md against the practices in them.
