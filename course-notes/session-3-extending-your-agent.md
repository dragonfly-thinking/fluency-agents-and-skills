# Extending Your Agent — Skills & Connections

*Part 3 of the AI Fluency course notes.*

Your agent becomes far more useful in two directions: with **skills** (reusable instructions it runs on demand — packaged standard operating procedures) and with **connections** to external tools (APIs, MCPs) that let it reach the software and data you already use. Both push more of the work *outside* the chat window: the agent runs procedures, talks to other services, and can publish the result to the live web. This note covers sub-agents, skills, connections, and a worked workflow that ties them together — so you or your agent can pull the concepts and put them into action. Sibling notes: [Setting Up Your Agent's Workspace](session-2-setting-up-your-agentic-environment.md) and [Going AI-Native — Working Well](session-4-working-well.md).

---

## Sub-agents — a closer look

- A **sub-agent** is a specialist your main agent can dispatch to. It runs in its own fresh context window and has its own focused instructions.
- They live as **files in a folder**: `.claude/agents/<name>.md` for Claude, `.codex/agents/<name>.toml` for Codex. Format differs slightly between runtimes; the AI handles the setup either way.
- **Two main reasons to use them**:
  1. **Conserve context.** Offload exploratory work (big searches, file reads, reasoning steps) so the main thread doesn't fill up.
  2. **Specialise behaviour.** Give the agent a focused role, tone, or set of tools different from the main agent.
- **Why not just open a new main agent instead?** Because your main agent is *general-purpose by design* — every fresh session only loads your top-level AGENTS.md / CLAUDE.md, so it stays deliberately broad. A new chat is just another general-purpose agent reading the same generic map. A sub-agent is where you put the *tailored*, job-specific instructions — a role, a tone, a narrow toolset — that you'd never want cluttering your everyday agent.
- **The highest-leverage use — a fresh-eyes red-team review.** Because a sub-agent starts from a blank context with its own instructions, it isn't invested in whatever your main agent just produced — so it reliably catches gaps. Point a deliberately critical reviewer (or hand the job across to Codex) at a plan or a draft and it *nearly always* comes back with a real issue. This holds even when you're on the most powerful model: a clean-context adversarial pass still finds things. Great practice on any plan before you act on it. *(The kit ships `critical-friend` and `critical-review` for exactly this — try: "use the critical-review skill to red-team this plan.")*
- **Invocation**: Claude usually picks the right sub-agent automatically based on its description. Codex needs you to name it explicitly *(sub-agent invocation in Codex is changing fast — ask your agent what's current)*. Either way, you can always be explicit: *"use the writing-editor subagent to..."*
- **Never write these by hand.** Tell the agent what kind of specialist you want and it'll write the file for you.
- **Get sub-agents to document their work.** You can't easily watch a sub-agent run — so tell it to leave a trail: a folder with an `overview.md` (what it's doing and why) and a `progress.md` (a running log). The folder is concrete and *persistent* — it survives the chat, and any future session (or a recovery after a crash) can be pointed straight at it. Worth a standing line in your router file: *"when you invoke a sub-agent, tell it to document its work in a folder."* (More on this pattern in [Self-Documenting Workspaces](self-documenting-workspaces.md).)

## Skills — the new evolution of prompts

- A **skill** is a *prompt pack*: a folder on your computer the agent reads on demand. Effectively a packaged standard operating procedure.
- **Required**: a `SKILL.md` file with the instructions (the "what to do, when to do it, how to do it").
- **Optional**: anything else inside that folder — reference files, checklists, examples, scripts. The agent loads them only when the prompt says it needs them.
- Skills can also **dispatch sub-agents** as part of their instructions (e.g. the `proofread` skill hands off to the `writing-editor` sub-agent). And sub-agents can in turn invoke skills.
- **Why this matters**: skills are a way to *codify your expertise* — the way you like a task done, the conventions you follow, the format of the output. They make your agent meaningfully better at the specific work you do.
- Invoked by typing `/` in the chat and choosing the skill, or by mentioning it by name. You can add extra context inline (e.g. `/visual-explainer make it pirate-themed`).
- **Making your own**: the simplest way is to just ask — *"turn what we just did into a skill; write the SKILL.md for me"* — and the agent writes the folder. For a more guided build there's **`skill-creator`**: Claude Code users get it from this kit (adapted from Anthropic's public one); Codex ships its own first-party version — either way, it interviews you, scaffolds the folder, and validates the result.

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
- **Concrete examples**:
  - A formatting skill: give it 2–3 examples of the documents you typically produce, then run it on new content to apply the template.
  - A skill that knows your brand colours and logos, so visual outputs come out on-brand instead of randomly themed.
- **Give a skill a memory of its own.** Add a `gotchas.md` (or `tips.md`) file inside the skill's folder — somewhere the agent jots notes to itself as it runs, so the next run avoids whatever tripped up the last one.
- **The bigger idea — a self-improving, evolving workspace.** This isn't just for skills. The move is to *bake proactive self-improvement in* so you don't have to remember to do it: decide what upkeep you'd like the agent doing in the background (suggesting fixes, keeping notes, flagging repeated tasks) and put it in your router file once. The workspace then gets better as you use it — see [Self-Documenting Workspaces](self-documenting-workspaces.md).

## A worked workflow: polish → visualise → publish

A reusable recipe you (or your agent) can run today on any piece of content — something you've written, or text pulled from a link. Three skills in sequence:

1. **`/proofread`** → invokes the **writing-editor** sub-agent. Returns grammar/clarity/structure suggestions plus a cleaned version. Notice the layering: a skill (the verb) handing off to a sub-agent (the specialist).
2. **`/visual-explainer`** → turns the cleaned-up text into a self-contained HTML one-pager with diagrams (e.g. mermaid flowcharts). **What's an HTML file?** Just *code* — the scaffolding everything on the web is built from. The agent writes the code; your browser reads it and renders the page you see. And because it's real code, these pages can be genuinely *interactive* (flowcharts, toggles, tabs — the course slides themselves are HTML files). One striking example: a 1,300-word text-only magazine article, with no charts of its own, that the agent rendered into charts and timelines purely from the data buried in the prose.
3. **`/here-now`** → publishes the HTML page to a live URL at `{slug}.here.now`. **Why this step exists:** up to now your page is a *file on your own computer* — opening it looks like a web page and even shows a file address, but it isn't on the internet; email that link and no one else can open it. `here.now` takes the local file and puts it on a real, shareable web address. Free tier keeps the page live for 24 hours; a free account keeps it longer. You can also **pin/password-gate** a page — a code you hand to specific recipients, effectively a proxy for email — and, on a paid account, **attach your own domain** so links look professional (`insights.yourcompany.com`) instead of a random subdomain.

Run end to end, this walks **a real piece of work from messy draft to a polished page anyone can open — without leaving the chat.** That's skills + connections working together.

- **Watch the AI "tells."** Generated visuals have a recognisable default look — everything in shades of blue, an "oatmeal" beige aesthetic, and the giveaway title-then-*italicised-coloured-emphasis* pattern. Name it, then steer it: point the agent at your brand colours and logo, or ask for a specific style (e.g. brown da Vinci-style line drawings instead of blue). A skill that knows your brand keeps this consistent — see *Self-improving skills* above.
- **Replacing a confidential Word/PDF workflow.** Text-heavy, confidential documents can move to gated HTML: publish behind a pin, attach your own domain, and convert **HTML → PDF** whenever you need the document form. Build and iterate as HTML first, export to PDF at the end (see [`../guides/file-conversion.md`](../guides/file-conversion.md)). A strong first-draft combo: use **NotebookLM** for a fast first pass (a deck or visual), then hand it to your agent to iterate — NotebookLM is great at the first pass but weak at iterating.

## APIs, API Keys, and MCPs

The conceptual core of connecting your agent to the outside world:

- **API** = the way one piece of software talks to another. Like a restaurant with two doors: humans walk in and order at the counter; software calls the kitchen directly through the side window.
- **API key** = your account identifier. Tells the service who's calling, what they're allowed to access, and who to bill. Many services require one; some don't.
- **MCP (Model Context Protocol)** = a newer standard *on top of* APIs that makes it easier for agents specifically to discover and use external tools. You'll see this acronym a lot. You don't need to understand the protocol — your agent does.
- **Finding a connector.** To hook up a tool, search *"[tool name] MCP"* (or *"[tool name] API"*). The API is the plumbing underneath; the MCP sits on top and is the agent-friendly path — prefer it where it exists.
- **Connections compose into skills** (just like sub-agents do). A general research skill can bake in *"when researching, pull from these data sources I've already connected"* — so the connection fires automatically as part of the recipe.
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

## Practical Notes / Troubleshooting

- **Installing the kit** — paste the repo link into your agent and ask it to install. Common roadblocks:
  - **"Provenance restriction" error** — some agents refuse to fetch raw files from URLs; falling back to a terminal command worked.
  - **"Can't find the folder"** — the `.claude` folder is hidden; ask the agent to open it for you.
  - **Cowork limitations** — Cowork (Claude Desktop's safer mode) has some restrictions Claude Code doesn't. If something doesn't work in Cowork, try switching to the Code tab in the same app.
  - **New session** — after installing new skills or sub-agents, start a New Session so the agent picks them up.
  - **Skill not showing when you type `/`?** The most common cause: the skills were installed into a *project's* `.claude/skills/` folder instead of the *global* `~/.claude/skills/` one — so they only exist inside that one folder. Ask your agent: *"check whether the kit's skills are installed globally or just locally, and move them to global."* Then start a new session. (Same logic for Codex with `~/.codex/skills/`.)
- **Auto mode** — at the bottom of Claude Code, you can switch from "Ask permission" to "Auto" mode so it doesn't pause on every action. Recommended once you've built up trust.
- **You don't need the terminal.** The terminal (Terminal on Mac, PowerShell on Windows) is a window "under the hood" of your computer — it's how coding agents actually do their work, a throwback to how computers ran in the 80s. For everyday use you can live entirely in the chat/session view. It only surfaces occasionally: when the agent is *blocked* (e.g. it isn't allowed to delete a folder and asks you to run the command yourself), or to wire up a tool with no first-class connector.
- **Security** — APIs and external connections introduce some risk (notably *prompt injection*: malicious instructions embedded in a page the agent reads). For highly sensitive data (health records, HIPAA-protected info, etc.), don't expose it to coding agents yet. Back up your computer regardless — **Backblaze** is a simple full-machine backup service.

## The kit

You're reading this from inside the kit: sub-agents (`writing-editor`, `critical-friend`, `fact-checker`, `project-planner`, `vault-librarian`, `web-searcher`) plus a library of skills (`proofread`, `visual-explainer`, `here-now`, `critical-review`, `premortem`, `slides`, `canvas-design`, and more — see the repo README for the full list), in both `.claude/` and `.codex/` variants. Repo: **[github.com/dragonfly-thinking/fluency-agents-and-skills](https://github.com/dragonfly-thinking/fluency-agents-and-skills)**.

## Resources

### Tools
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

## Put this into action

- **Take a real piece of writing** — a memo, a report, a draft — and walk it through the workflow above: `/proofread`, then `/visual-explainer`, then `/here-now`. Get a URL.
- **Try another skill** — `canvas-design` for a polished PDF, `premortem` for a project you're about to start, or `new-project` to scope and scaffold something new.
- **Add a self-improvement line** to your AGENTS.md / CLAUDE.md file: *"After running any skill, suggest improvements. If you notice a repeated task, propose a new skill."*
- **Add a "leave a trail" line** too: *"When you do real work — especially anything you hand to a sub-agent — document it in a folder (an overview + a running progress log) so it survives the chat."*
