# AI Fluency Session 2 — Key Points

**Session 2: Setting Up Your Agent's Workspace**

Last week we installed our agents (Claude / Codex). This week was about *configuring the environment* they work in, so they can accomplish tasks with as little hand-holding as possible. The core shift: from **prompt engineering** (crafting clever instructions) to **context engineering** (building the workspace — files, folders, and an orientation file — so the agent can find what it needs itself). The centrepiece is the `AGENTS.md` / `CLAUDE.md` orientation file, plus a first look at **sub-agents**. This session traded some content time for a hands-on activity and an open Q&A.

---

## From Prompt Engineering to Context Engineering

- **Prompt engineering** mattered a lot in the early days because output quality swung wildly on phrasing. It still matters, but far less — the models are now intelligent enough to understand intent.
- The new lever is **context engineering**: not *what you tell it to do*, but *what's in the agent's environment* that lets it accomplish the goal.
- Less about instructions, more about **affordances** — the right files, folders, and references being available.

## Context & Tokens (Recap + Extension)

- Context = the agent's "working memory." Once the bucket is full, anything outside it is simply not referenced.
- Measured in **tokens** (~¾ of a word). Everything — text, images, audio, video, files, and the whole conversation history — gets converted to tokens.
- Context windows have grown from ~3,000 words (early ChatGPT) to ~**1 million tokens** today. Most people's entire written life's work would fit.
- **Searches and tool use eat tokens too** — a big search task can silently burn 100k–200k tokens. This is *why* sub-agents and good workspace design matter.
- **Coding agents don't read everything** — they use search tools to find the relevant lines/files on demand, which keeps them context-efficient. "Your context window is finite, but your workspace doesn't have to be."
- The 1% that's critical (the one file/paragraph that matters most) is what *you* still need to point them to.

## The Orientation File: `AGENTS.md` / `CLAUDE.md`

- A plain-text (markdown) file that is **automatically loaded at the start of every session** — the first thing a "blank slate" agent sees.
- `AGENTS.md` (Codex) and `CLAUDE.md` (Claude) are functionally interchangeable. If your tool makes the wrong one, just ask it to rename.
- Think of it like onboarding a new hire: who you are, how you work, your conventions (e.g. British English), and — crucially — **where to find more information**.
- **Signpost, don't dump.** Keep it lean (a few hundred words). Rather than pasting 3,000 words, point to files/folders via their **file paths**; the agent will search them when needed. Dumping everything just wastes context.
- It's a **living document** — your context changes, so should the file. Build in an instruction like *"if you notice my priorities have changed, suggest updates / ask me questions."*
- **Multiple files, hierarchical.** You can have a global one (root of your computer) plus project-level ones in specific folders. All files up the folder chain are included; the **closest one wins** on conflicts.

## Hands-On Activity

- Paste the provided **setup prompt** into Claude Cowork or Codex. It runs a short interview (~10 min) and generates your `AGENTS.md`/`CLAUDE.md` plus starter background-context files.
- Helpful to have your LinkedIn, company website, etc. handy to feed it.
- The agent **creates the files for you** — no manual saving. Just confirm: *"please make sure you've created the file in our workspace."*
- "Workspace" = just a folder on your computer. Files land either in the folder you opened, or in the hidden `.claude` / `.codex` config folder (the dot = hidden).
- **Tip:** on Mac, right-click a file → *Copy as Pathname* to get its address; in Windows, copy from the address bar. Or just ask the agent to open/locate things for you.

## Best Practices for the Orientation File

- **Show, don't tell.** Examples are the single biggest lever on output quality. Provide references rather than describing what you want — but give **several** examples (e.g. a `writing-style.md` with 10 samples) so it doesn't over-imitate a single one.
- **Make it self-improving.** Ask the agent to proactively suggest improvements, flag when info looks stale, and maintain a `gotchas.md` / "mistakes to avoid" file it re-reads each message.
- **Do as little manual work as possible** — collaborate with the agent to write and update these files; don't sit there hand-writing them.

## Common Failures

- **Too much information** stuffed into the file (wastes context).
- **Empty filler** instructions ("do a good job") — low value; they're already trying to.
- **Stale / old information** (biggest one) — agents have no memory of "before"; outdated details = wrong company names, wrong style, etc.
- **Never store secrets** (passwords, keys) — these tools read text files instantly and *will* surface them.

## Meeting Recordings (High-Leverage Tip)

- Record your meetings and export the transcripts into your workspace — transcription is now very accurate and there's "so much gold" in meetings.
- Then ask the agent to extract action items, write notes, or turn a transcript into a branded presentation. Tools mentioned: **Zoom built-in**, **Otter.ai**, and other note-takers.

## Sub-Agents

- A sub-agent is just another agent (same as Claude/Codex) that your **main agent can invoke** and delegate work to. Instructions live in a hidden `.claude/agents` (or `.codex`) folder.
- **Why use them:**
  1. **Save context** — offload big search/research tasks so they don't bloat the main conversation (each sub-agent gets a *fresh* context window).
  2. **Custom perspective** — give them tailored instructions (e.g. a *Critical Friend* that tears your draft apart instead of being sycophantic).
  3. **Scoped tools** — restrict or specialise their tools (no web, no file edits), and even pick a cheaper/faster or heavier model.
  4. **Parallelism** — run several at once (e.g. read 10 papers through one lens).
- **When to skip:** when you need all the resulting context kept in the main thread, or the task needs everything you've already done.
- **Claude vs Codex behaviour:** Claude will often invoke sub-agents automatically (based on their descriptions); **Codex only uses them when you explicitly ask.** Either way, saying *"use a sub-agent for this"* is the reliable move.
- **Cowork caveat:** custom sub-agents may not run in Cowork mode at all — only in **Claude Code** (the Code tab of the same app). If your installed sub-agents aren't being invoked in Cowork, switch to Code.
- A **starter pack** of generally-useful sub-agents was provided (Claude zip / Codex zip) — e.g. web researcher, writing editor, critical friend. Install by dragging the folder into your workspace and asking the agent to set it up. Scope them **globally** (available everywhere) or **per-project** as appropriate.
- *(Microsoft Copilot "Cowork" users — e.g. WWF — already have a suite of built-in sub-agents and tenant context, so may not need the pack.)*

## Other Q&A Worth Noting

- **Org-wide context?** No one-click sync for local tools like Cowork (they live on your machine). For fairly stable material, have one person create the **canonical context folder** and distribute it; teams like Dragonfly use **GitHub** to sync docs across computers. We're partly "regressing" from cloud-synced apps back to local — possibly temporary, but worth learning now.
- **Opus vs Sonnet?** Default to **Sonnet** for nearly everything — Opus is expensive and burns through usage limits fast (especially on the $20/mo plan).
- **Agent vs Skill?** Teased for next week — an agent is the "person"; skills are recipes/SOPs that the agent can run.

## Resources Mentioned

### Tools used in the session
- **[Claude Desktop / Cowork / Claude Code](https://claude.com/download)** — Anthropic's desktop app. Cowork is the simpler tab; Code is more powerful. Same app, two modes.
- **[OpenAI Codex CLI](https://developers.openai.com/codex/cli)** — OpenAI's terminal-based coding agent; the Codex equivalent used by participants on the OpenAI side.

### The orientation-file standard
- **[AGENTS.md](https://agents.md)** — The cross-tool convention for the agent orientation file. Works across Codex, Cursor, Aider, GitHub Copilot and others. `CLAUDE.md` is Claude's near-identical equivalent.
- **[Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents)** — Official docs on how subagents work, where they live, and how to dispatch them.

### Session 2 starter kit
- **[`setup-workspace` skill](https://github.com/dragonfly-thinking/fluency-agents-and-skills/tree/main/.claude/skills/setup-workspace)** — the setup-interview, now packaged as a skill in the kit. Install the kit, then run `setup-workspace` — it'll detect whether you already have a workspace and route to init, add-project, refresh-context, or add-guardrail mode.
- **[Session 2 Practical Resources (Notion)](https://dragonflythinking.notion.site/Session-2-Practical-Resources-364e541fefe3806e825bc5affb7e5951)** — the live page Sam shared in-session. Still hosts the original paste-prompt version of the interview.
- **[github.com/dragonfly-thinking/fluency-agents-and-skills](https://github.com/dragonfly-thinking/fluency-agents-and-skills)** — The same starter pack as a public repo: six subagents (writing-editor, critical-friend, fact-checker, project-planner, vault-librarian, web-searcher) plus skills, in both `.claude/` and `.codex/` variants. Paste the link into your agent and ask it to install.

### Meeting-recording / transcription tools (raised in the "meetings as context" tip)
- **[Zoom](https://www.zoom.com)** — Built-in cloud recording + transcript (`.vtt` / `.txt`).
- **Google Meet** — Captions and auto-transcript that lands in Google Docs (no single canonical URL beyond Workspace).
- **Microsoft Teams** — Built-in transcription via the meeting controls.
- **[Otter.ai](https://otter.ai)** — Dedicated transcription app; works alongside any meeting tool.
- **[Granola](https://www.granola.ai)** — Mac-only meeting note-taker that captures everything automatically.
- **[Fireflies.ai](https://fireflies.ai)** — Team-oriented AI note-taker with CRM integrations.

### Also surfaced in Q&A
- **[Cursor](https://www.cursor.com)** — AI-first code editor; mentioned by a participant as the interface he uses to see his `.claude/` folder and run Claude Code with a file tree visible.

## How the Course Unfolded

| Session | Focus |
|---------|-------|
| **3** | **Skills** (standard operating procedures the agent can invoke) + extending capabilities — connecting to external tools and publishing to the web |
| **4** | Working Well — consolidation: projects set up properly, planning mode, progress logs, and background routines |

The running metaphor: Session 1 *planted the seed* (created the agent), Session 2 *built the house and gave it a map* (the workspace + orientation file), Session 3 gives it *recipes and a phone line* (skills + tool connections).

## Next Steps

Go away and actually **set up your workspace environment** — this matters more than sub-agents:

- Create a folder and run the setup prompt to generate your `CLAUDE.md` / `AGENTS.md`.
- Seed it with context files/folders: writing-style guide, company overview, key people/birthdays (for personal use), reference docs, etc. — let the agent create them.
- Build in instructions that make it an **evolving workspace** (so it updates itself as things change and when you give feedback).
- Optionally, create your own sub-agents for repeatable tasks where you want a specific *perspective* — but never hand-write them; ask Claude/Codex to draft, then tweak.
- Above all: **the agent is only as useful as the information it can access.** Focus there.
