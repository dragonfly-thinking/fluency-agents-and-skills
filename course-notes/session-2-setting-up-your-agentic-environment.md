# AI Fluency Session 2 — Key Points

**Session 2: Setting Up Your Agent's Workspace**

Last week we installed our agents (Claude / Codex). This week was about *configuring the environment* they work in, so they can accomplish tasks with as little hand-holding as possible. The core shift: from **prompt engineering** (crafting clever instructions) to **context engineering** (building the workspace — files, folders, and an orientation file — so the agent can find what it needs itself). The centrepiece is the `AGENTS.md` / `CLAUDE.md` orientation file, plus a first look at **sub-agents**. This session traded some content time for a hands-on activity and an open Q&A.

---

## From Prompt Engineering to Context Engineering

- **Prompt engineering** mattered a lot in the early days because output quality swung wildly on phrasing. It still matters, but far less — the models are now intelligent enough to understand intent.
- The new lever is **context engineering**: not *what you tell it to do*, but *what's in the agent's environment* that lets it accomplish the goal.
- Less about instructions, more about **affordances** — the right files, folders, and references being available.
- **Why the lever moved.** The models now understand what you *mean*, so cleverly-worded prompts buy you less. The bottleneck isn't comprehension any more — it's **access**. Prompt engineering was learning to talk to a genius cleverly; context engineering is handing that genius the keys to your filing cabinet.
- **The failure it fixes: ungrounded guessing.** Think of an agent as a world-class consultant with total amnesia about you — brilliant, has read everything, but has never met *you*, doesn't know your standards. What you get back is capped by how well you brief it. With nothing to anchor on, it does the one thing these models always do — predict a **plausible continuation** — and a plausible continuation with no grounding is a guess. (That's all "hallucination" really is: plausible-sounding filler where a fact should be, not lying.) Context is the briefing that makes it swap guessing for reading. Ask *"what do you think of my analysis?"* with no file attached and a well-set-up agent will go hunting through your workspace, find *a* previous analysis, and confidently comment on it — impressive reach, but maybe the wrong file. Point it at the right one and the guessing stops.

## Context & Tokens (Recap + Extension)

- Context = the agent's "working memory." Once the bucket is full, anything outside it is simply not referenced.
- Measured in **tokens** (~¾ of a word). Everything — text, images, audio, video, files, and the whole conversation history — gets converted to tokens.
- Context windows have grown from ~3,000 words (early ChatGPT) to ~**1 million tokens** today. Most people's entire written life's work would fit.
- **Searches and tool use eat tokens too** — a big search task can silently burn 100k–200k tokens. This is *why* sub-agents and good workspace design matter.
- **Coding agents don't read everything** — they use search tools to find the relevant lines/files on demand, which keeps them context-efficient. "Your context window is finite, but your workspace doesn't have to be."
- The 1% that's critical (the one file/paragraph that matters most) is what *you* still need to point them to.

## Managing the Context Window — Context Rot & Handover Notes

The window doesn't just fill; it **degrades**. As it gets full, quality quietly drops *before* you hit the limit — reasoning gets worse, and the agent starts forgetting things you told it a few turns ago. This is **context rot**, and the tell is that the agent won't announce it: it just goes from sharp to "brain dead," and you're left wondering why you're suddenly talking to a dumber assistant.

- **Compaction helps, but it's lossy.** When the window is nearly full the tools auto-summarise the conversation to make room — and that summary drops detail, without knowing which small detail was the load-bearing one. A fresh session beats a compacted one every time.
- **The remedy — a handover note.** *Before* the window fills, ask the agent to write a **handover note**: a short file capturing what this session did, decided, and is up to. Then start a fresh session and hand it that note as the new foundation. Think of it like going on leave — you write the handover so whoever picks up the work isn't lost. A concrete prompt: *"We're getting long. Write a handover note to `handover.md` — what we've done, key decisions, and exactly where we're up to — so a fresh session can continue."*
- **Watch the meter, don't wait for the redline.** Both tools show how full the window is; where to find that indicator (and the rest of the interface) is in [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

This is one instance of a bigger habit: leave a durable trail in files instead of trusting the chat to remember. That habit is its own note — **[`self-documenting-workspaces.md`](self-documenting-workspaces.md)**.

## The Orientation File: `AGENTS.md` / `CLAUDE.md`

- A plain-text (markdown) file that is **automatically loaded at the start of every session** — the first thing a "blank slate" agent sees.
- `AGENTS.md` (Codex) and `CLAUDE.md` (Claude) are functionally interchangeable. If your tool makes the wrong one, just ask it to rename.
- Think of it like onboarding a new hire: who you are, how you work, your conventions (e.g. British English), and — crucially — **where to find more information**.
- **Signpost, don't dump.** Keep it lean (a few hundred words). Rather than pasting 3,000 words, point to files/folders via their **file paths**; the agent will search them when needed. Dumping everything just wastes context.
- It's a **living document** — your context changes, so should the file. Build in an instruction like *"if you notice my priorities have changed, suggest updates / ask me questions."*
- **Multiple files, and they stack.** You can have a **global** file plus **project-level** ones in specific folders. The global file lives in a hidden folder in your home directory — exactly `~/.claude/CLAUDE.md` (Codex: `~/.codex/AGENTS.md`). "Hidden" doesn't mean temporary: it's permanent, it's yours, and you can open and edit it directly like any other file. Nothing clears it.
- **Global vs project — they layer, they don't replace.** Everything up the folder chain is loaded together, so the files *stack*: the global file carries the high-level, always-true stuff (who you are, preferences, British English), and each project file adds its own specifics on top. Put "I live in Spain, use British English" in the global file once and you never repeat it in a project file. (If two files ever *directly* conflict, the closest, most specific one wins — but stacking, not overriding, is the everyday case.)

### Why this is the hard part

Writing the orientation file is harder than it sounds, because so much of how you work is **tacit** — never written down, just in your head. The agent can't guess what you never say. The fix is to not write it cold: let the agent **interview you** (*"interview me, then draft my `CLAUDE.md`"*). A good reverse-questionnaire pulls the tacit stuff out of you and onto the page — which is exactly what the setup activity below does.

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
- **Keep a separate profile file, and link to it.** The setup interview usually creates two files: the orientation file (`CLAUDE.md` / `AGENTS.md`) *and* a `user.md` profile (who you are, how you work). The orientation file **links** to `user.md` rather than embedding it — because the orientation file loads on *every* message and must stay lean, while `user.md` is read only when a task actually calls for it. The link in the always-loaded file is what guarantees the agent knows the profile exists, at no standing context cost.
- **Point, don't copy — a copy goes stale, a pointer can't.** To reuse context that lives elsewhere (a file in another folder, a shared doc), reference it by its **file path** or an **`@import`** rather than pasting a duplicate in. A path is read fresh on demand; an `@import` is pulled from the live file when the session starts. Either way you always get the current version. Paste a copy and it silently rots the moment the original changes.

## Common Failures

- **Too much information** stuffed into the file (wastes context).
- **Empty filler** instructions ("do a good job") — low value; they're already trying to.
- **Stale / old information** (biggest one) — agents have no memory of "before"; outdated details = wrong company names, wrong style, etc.
- **Never store secrets** (passwords, keys) — these tools read text files instantly and *will* surface them.

## Permissions & Modes

The moment you do real work, the agent asks permission a lot — every web fetch, every file edit, every download. Unmanaged, this is maddening (one task can throw 30 prompts). Two ways to tame it:

- **Ask the agent to set safe permissions for you.** Say *"I keep getting permission prompts and I'm not a technical user — I don't want to allow anything risky. Which permissions are safe to always allow?"* It proposes a sensible list and writes it into your settings so it stops re-asking. The usual safe-to-allow culprits are **web search / web fetch** and **`curl`** (that last one shows up constantly because agents use it to pull text out of PDFs).
- **Use the right mode for file edits.** The permission mode sits at the bottom of the Claude Code screen: **Manual** asks before every edit (safe, slow); **Accept Edits** stops asking for file edits (a good default once you trust the setup); **Auto** approves more for hands-off runs; **Bypass permissions** approves everything, for unattended tasks you don't want to babysit.
- **Model wrinkle:** **Haiku has no Auto mode** — on Haiku, use **Accept Edits**; on **Sonnet**, Auto is available. Nothing is more annoying than kicking off a long task, walking away, and returning to find it never started because it was waiting on a permission click. (Fuller map of modes and safe defaults: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).)

## Meeting Recordings (High-Leverage Tip)

- Record your meetings and export the transcripts into your workspace — transcription is now very accurate and there's "so much gold" in meetings.
- Then ask the agent to extract action items, write notes, or turn a transcript into a branded presentation. Tools mentioned: **Zoom built-in**, **Otter.ai**, and other note-takers.
- **Voice is context too.** You don't need a meeting to feed it your thinking. Voice notes on the go, or a voice *call* with your agent, get transcribed into text it can use — and a call has the bonus that the agent can ask clarifying questions and push back while you talk it out. A low-friction way to get what's in your head into the workspace.

## Sub-Agents

- A sub-agent is just another agent (same as Claude/Codex) that your **main agent can invoke** and delegate work to. Instructions live in a hidden `.claude/agents` (or `.codex`) folder.
- **Why use them:**
  1. **Save context** — offload big search/research tasks so they don't bloat the main conversation. Each sub-agent starts with a *fresh* context window, does the heavy reading in there, and returns **just the distilled result** — so the main agent's window stays clean and dodges the lossy compaction that sets in when it fills (see *context rot*, above). This is the biggest reason to reach for them.
  2. **Custom perspective** — give them tailored instructions (e.g. a *Critical Friend* that tears your draft apart instead of being sycophantic).
  3. **Scoped tools** — restrict or specialise their tools (no web, no file edits), and even pick a cheaper/faster or heavier model.
  4. **Parallelism** — run several at once (e.g. read 10 papers through one lens).
- **When to skip:** when you need all the resulting context kept in the main thread, or the task needs everything you've already done.
- **Claude vs Codex behaviour:** Claude will often invoke sub-agents automatically (based on their descriptions); **Codex only uses them when you explicitly ask.** Either way, saying *"use a sub-agent for this"* is the reliable move.
- **"Fan out."** In Claude, *"fan out sub-agents to…"* is a keyword that spins up a whole swarm at once — e.g. *"fan out sub-agents to read these 10 PDFs, one each."* You don't hand-write them: the main agent creates them with tailored instructions, and you review what comes back. You also never talk to a sub-agent directly — you brief the main agent; it spawns, instructs, and collects. That's why sub-agents suit *bounded* jobs with a clear result to hand back, not tasks that need lots of back-and-forth.
- **Cowork caveat:** custom sub-agents may not run in Cowork mode at all — only in **Claude Code** (the Code tab of the same app). If your installed sub-agents aren't being invoked in Cowork, switch to Code.
- A **starter pack** of generally-useful sub-agents was provided (Claude zip / Codex zip) — e.g. web researcher, writing editor, critical friend. Install by dragging the folder into your workspace and asking the agent to set it up. Scope them **globally** (available everywhere) or **per-project** as appropriate.
- *(Microsoft Copilot "Cowork" users — e.g. WWF — already have a suite of built-in sub-agents and tenant context, so may not need the pack.)*

## Sub-Agents vs Running Parallel Sessions

There are **two** different ways to run work in parallel, and they're easy to blur:

- **Sub-agents** are spawned *by your main agent* and run **inside one session**, each in its own fresh context window. You don't open windows for them or talk to them — the main agent does.
- **Multiple sessions** are separate chats *you* open and manage yourself. Handy for, say, running the same fact-checker over the same material in two sessions and comparing the outputs to surface hallucinations or inconsistencies.
- **The one hard rule for multiple sessions:** don't let two of them edit the **same file** at once. That's the single thing that reliably causes confusion — otherwise, parallel sessions are fine.
- **Sequencing turns this into a workflow.** Chain agents and sub-agents in a set order — research, then draft, then critique — and you've built a *workflow*. That's the seed of routines and scheduled tasks (Session 4). You can even keep one session running as an **orchestrator** that watches for files written elsewhere in your workspace and synthesises them as they land.

## Other Q&A Worth Noting

- **Org-wide context?** No one-click sync for local tools like Cowork (they live on your machine). For fairly stable material, have one person create the **canonical context folder** and distribute it; teams like Dragonfly use **GitHub** to sync docs across computers. We're partly "regressing" from cloud-synced apps back to local — possibly temporary, but worth learning now.
- **Which model?** Default to a mid-tier model (**Sonnet**) for nearly everything — the top tier is pricier and burns usage limits faster. There's a wrinkle that interacts with permissions (Haiku has no Auto mode) — see *Permissions & Modes* above.
- **Can you trust the agent's description of what it's doing?** Partly. For Claude, the *extended thinking* you can switch on is the model's real reasoning, not a story told after the fact. But an agent's running prose — *"now I'm reviewing the file…"* — is generated text, and it is **not** a reliable audit trail of what actually happened. The trustworthy record is the **tool calls it made and the files that actually changed.** Judge by outputs and diffs, not by the narration.
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
