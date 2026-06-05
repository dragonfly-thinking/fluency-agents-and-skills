# AI Fluency Session 3 — Key Points

**Session 3: Extending Your Agent**

We extended our agent's capabilities in two directions: with **skills** (reusable instructions the agent can run on demand) and with **connections** to external tools (APIs, MCPs). The big shift compared to earlier sessions: more of the work happens *outside* the chat window — your agent runs procedures, talks to other software, and at the end of this session, publishes the result to the live web. The teaching arc was a hands-on journey: take a real piece of writing → proofread it via a skill that delegates to a subagent → turn it into a visual one-pager via another skill → publish it on the web with a third skill. By the end, most participants had a shareable URL with their own polished page on it.

---

## The Story So Far

- **Session 1** — got an agent installed and pointed at a folder.
- **Session 2** — built its workspace and gave it a map (AGENTS.md / CLAUDE.md, context files, sub-agents).
- **Session 3 (this one)** — gave the agent skills it can run, and connected it out to your other tools.
- **Session 4** — Working Well: consolidating everything — projects set up properly, planning mode, progress logs, and background routines.

## Sub-agents — a closer look

- A **sub-agent** is a specialist your main agent can dispatch to. It runs in its own fresh context window and has its own focused instructions.
- They live as **files in a folder**: `.claude/agents/<name>.md` for Claude, `.codex/agents/<name>.toml` for Codex. Format differs slightly between runtimes; the AI handles the setup either way.
- **Two main reasons to use them**:
  1. **Conserve context.** Offload exploratory work (big searches, file reads, reasoning steps) so the main thread doesn't fill up.
  2. **Specialise behaviour.** Give the agent a focused role, tone, or set of tools different from the main agent.
- **Invocation**: Claude usually picks the right sub-agent automatically based on its description. Codex needs you to name it explicitly. Either way, you can always be explicit: *"use the writing-editor subagent to..."*
- **Never write these by hand.** Tell the agent what kind of specialist you want and it'll write the file for you.

## Skills — the new evolution of prompts

- A **skill** is a *prompt pack*: a folder on your computer the agent reads on demand. Effectively a packaged standard operating procedure.
- **Required**: a `SKILL.md` file with the instructions (the "what to do, when to do it, how to do it").
- **Optional**: anything else inside that folder — reference files, checklists, examples, scripts. The agent loads them only when the prompt says it needs them.
- Skills can also **dispatch sub-agents** as part of their instructions (e.g. the `proofread` skill hands off to the `writing-editor` sub-agent). And sub-agents can in turn invoke skills.
- **Why this matters**: skills are a way to *codify your expertise* — the way you like a task done, the conventions you follow, the format of the output. They make your agent meaningfully better at the specific work you do.
- Invoked by typing `/` in the chat and choosing the skill, or by mentioning it by name. You can add extra context inline (e.g. `/visual-explainer make it pirate-themed`).

## Where Skills and Sub-agents Live: Global vs Project

This is one of the most confusing bits, but the rule is simple:

- **Global** — `~/.claude/agents/` and `~/.claude/skills/` in your home folder. Available everywhere, in every project. Best for your default crew of specialists and your everyday skills.
- **Project-specific** — `.claude/agents/` and `.claude/skills/` inside the project folder. Only available when you're working in that project. Best for skills that only matter to a particular piece of work (e.g. a cookbook-formatting skill doesn't need to follow you into your day job).
- Same logic applies to Codex (`~/.codex/` vs `.codex/`).
- The dot at the start (`.claude`) makes the folder hidden by default. You can't see it in Finder without showing hidden files — but **just ask your agent**: *"open up the .claude folder for me"* and it'll do it.

## Self-improving skills

A small but high-leverage habit:

- Add an instruction to your AGENTS.md / CLAUDE.md file that says: *"whenever you execute a skill, suggest improvements; if you notice a repeated task, propose a new skill."*
- This way your toolkit gets better automatically as you work — you don't have to remember to update things.
- **Concrete examples** raised in the room:
  - A formatting skill: give it 2–3 examples of the documents you typically produce, then run it on new content to apply the template.
  - A skill that knows your brand colours and logos, so visual outputs come out on-brand instead of randomly themed.

## The Demo — Polish → Visualise → Publish

Three skills in sequence, on whatever piece of content participants brought (or pulled from a blog post link):

1. **`/proofread`** → invokes the **writing-editor** sub-agent. Returns grammar/clarity/structure suggestions plus a cleaned version. Notice the layering: a skill (the verb) handing off to a sub-agent (the specialist).
2. **`/visual-explainer`** → turns the cleaned-up text into a self-contained HTML one-pager with diagrams (e.g. mermaid flowcharts). Single file, opens in any browser.
3. **`/here-now`** → publishes the HTML page to a live URL at `{slug}.here.now`. Free tier keeps the page live for 24 hours; create an account for longer-lived links.

The arc: **a real piece of work, walked from messy draft to a polished page anyone can open — without leaving the chat.** That's the payoff of skills + connections together.

## APIs, API Keys, and MCPs

The conceptual core of the "connections" half of the session:

- **API** = the way one piece of software talks to another. Like a restaurant with two doors: humans walk in and order at the counter; software calls the kitchen directly through the side window.
- **API key** = your account identifier. Tells the service who's calling, what they're allowed to access, and who to bill. Many services require one; some don't.
- **MCP (Model Context Protocol)** = a newer standard *on top of* APIs that makes it easier for agents specifically to discover and use external tools. You'll see this acronym a lot. You don't need to understand the protocol — your agent does.
- **Don't be intimidated by either.** When you want to connect to something, just tell your agent *"set this up for me"* and it'll walk you through it.

## Connecting Your Agent to External Tools

In Claude Desktop / Cowork: **Customize → Connectors** in the sidebar. Browse, click "+" to add. Most are one-click after a login.

In Codex: **Plugins** menu. Similar experience, called "plugins" instead of "connectors", but functionally the same.

**Useful public-data MCPs mentioned** (all free, most without an API key):
- **Paper Search** — searches 20+ academic sources (arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed, SSRN). No API key.
- **ABS Statistics** — Australian Bureau of Statistics data.
- **World Bank Data360** — 1,000+ development indicators across 200+ countries.
- **Data Commons** — Google's harmonised aggregator across ~240 public datasets (World Bank, WHO, UN, OECD, US Census, ABS, NOAA). Free API key required.

## Other Skills Worth Exploring (from the kit)

- **`canvas-design`** — creates a polished PDF or image from content (good for posters, one-page summaries, branded outputs).
- **`premortem`** — before kicking off a project, anticipates what could go wrong and how to mitigate.
- **`slides`** — creates HTML slide decks.
- **`discovery-interview`** — interviews you to surface assumptions and context before you start a new project.

## Practical Notes / Troubleshooting

- **Installing the kit** — Sam shared a GitHub link with all skills and sub-agents. Most participants installed them by pasting the link into their agent and asking "install these for me." A few hit roadblocks:
  - **"Provenance restriction" error** — some agents refuse to fetch raw files from URLs; falling back to a terminal command worked.
  - **"Can't find the folder"** — the `.claude` folder is hidden; ask the agent to open it for you.
  - **Cowork limitations** — Cowork (Claude Desktop's safer mode) has some restrictions Claude Code doesn't. If something doesn't work in Cowork, try switching to the Code tab in the same app.
  - **New session** — after installing new skills or sub-agents, start a New Session so the agent picks them up.
- **Auto mode** — at the bottom of Claude Code, you can switch from "Ask permission" to "Auto" mode so it doesn't pause on every action. Recommended once you've built up trust.
- **Security** — APIs and external connections introduce some risk (notably *prompt injection*: malicious instructions embedded in a page the agent reads). For highly sensitive data (health records, HIPAA-protected info, etc.), don't expose it to coding agents yet. Backup your computer regardless — **Backblaze** was recommended as a simple full-machine backup service.

## The Session 3 Kit

The pack of subagents and skills shared in the session — six subagents (`writing-editor`, `critical-friend`, `fact-checker`, `project-planner`, `vault-librarian`, `web-searcher`) plus a full library of skills (`proofread`, `visual-explainer`, `here-now`, `critical-review`, `premortem`, `discovery-interview`, `slides`, `canvas-design`, and more — see the repo README for the complete list). Ships with both `.claude/` (for Claude Code / Desktop) and `.codex/` (for Codex) variants.

**[github.com/dragonfly-thinking/fluency-agents-and-skills](https://github.com/dragonfly-thinking/fluency-agents-and-skills)**

Paste this link into your agent and ask it to install — it'll set up the right files in the right place.

## Resources Mentioned

### Tools used in the demo
- **[Claude Desktop / Cowork / Claude Code](https://claude.com/download)** — Anthropic's desktop app. Cowork is the friendlier mode; Code is the more powerful tab.
- **[OpenAI Codex CLI](https://developers.openai.com/codex/cli)** — OpenAI's coding agent; the Codex equivalent of Claude Code.
- **[here.now](https://here.now)** — Free hosting that lets an agent publish files/HTML to a live `{slug}.here.now` URL. 24h free, longer with an account.

### MCPs and public data sources
- **[Paper Search MCP](https://github.com/openags/paper-search-mcp)** — Searches 20+ academic sources (arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed, SSRN). No API key.
- **[ABS Statistics MCP](https://github.com/seansoreilly/mcp-server-abs)** — Australian Bureau of Statistics: CPI, unemployment, GDP, etc. No API key.
- **[World Bank Data360 MCP](https://github.com/worldbank/data360-mcp)** — Official World Bank MCP. 1,000+ development indicators across 200+ countries. No API key.
- **[Data Commons MCP](https://github.com/datacommonsorg/agent-toolkit)** — Google's index of ~240 public datasets. Free API key required.
- **[Smithery](https://smithery.ai)** — The MCP installer; one-line install for most MCP servers.
- **[Model Context Protocol (MCP) spec](https://modelcontextprotocol.io)** — The open standard MCPs are built on.

### Documentation referenced
- **[Claude Code — Skills](https://code.claude.com/docs/en/skills)** — Official docs on `SKILL.md` format and invocation.
- **[Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents)** — Official docs on dispatching specialist subagents.
- **[Claude Desktop — Connectors](https://claude.com/docs/connectors)** — The Customize → Connectors menu (Gmail, Outlook, Google Drive, SharePoint, etc.).
- **[OpenAI Codex — Subagents](https://developers.openai.com/codex/subagents)** — Codex's parallel-subagent system.
- **[OpenAI Codex — Plugins](https://developers.openai.com/codex/plugins)** — Codex's MCP/skills/integrations system.

### Also worth knowing
- **[NotebookLM](https://notebooklm.google.com)** — Google's tool for working with very long documents and generating podcast/video overviews.
- **[Backblaze](https://www.backblaze.com/cloud-backup)** — Cheap full-computer cloud backup. Worth having when letting agents touch your filesystem.

## How the Course Ended

| Session | Focus |
|---|---|
| **4** | Working Well — consolidation: projects set up properly, planning mode, progress logs, and **routines** (background scheduled tasks, so you wake up and the work is already done). |

## Next Steps

- **Install the skills + sub-agents kit** if you didn't get it set up live — this repo is it; paste its link into your agent and ask it to install.
- **Take a real piece of writing** — a memo, a report, a draft — and walk it through the same arc: `/proofread`, then `/visual-explainer`, then `/here-now`. Get a URL. Share it.
- **Try one of the other skills** — `canvas-design` for a polished PDF, `premortem` for a project you're about to start, or `discovery-interview` for a project that needs scoping.
- **Add a self-improvement line** to your AGENTS.md or CLAUDE.md file: *"After running any skill, suggest improvements. If you notice a repeated task, propose a new skill."*
- **Stuck?** Office-hours and 15-minute one-on-one slots are bookable through the Resources hub.
- **For Microsoft Copilot / Cowork users**: your environment differs in real ways (OneDrive workspace, restricted installs) — reach out if Cowork is blocking you.
