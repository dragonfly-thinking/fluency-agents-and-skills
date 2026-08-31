# Fluency Agents and Skills

Everything you take home from the Dragonfly Thinking **AI Fluency** course: the agents and skills we built and used, setup guides for the external connections we covered, and the teaching itself, written up as a reference library you can read in any order. Open it in [Claude Code](https://claude.ai/download) or [OpenAI Codex](https://developers.openai.com/codex/cli) and you have a real multi-agent setup — to use as-is, and to make your own.

A skill is a *verb* you invoke ("proofread this", "build me a deck"). A subagent is a *specialist* a skill can hand work to. Several skills delegate to the base agents below.

**Fresh from the course?** After installing, your agent starts you a **checklist** at `~/.claude/fluency-checklist.md` — the things in here that actually pay off, and which you've done. Ask it to work through the next one with you. Then browse [`course-notes/`](course-notes/) — the reference library, including [`agents-md-snippets.md`](course-notes/agents-md-snippets.md): standing instructions you paste into your orientation file once so you stop asking for the same things by hand.

## Install (let your agent do it)

No GitHub account needed — this page is public. Copy this page's link, paste it into Claude Code or Codex, and say:

> **"Read the AGENTS.md at this link and install the kit for me."**

Your agent does the rest: it downloads the kit, follows [`AGENTS.md`](AGENTS.md), and copies the 6 agents and 16 skills into your setup (15 on Codex — Codex ships its own first-party skill-creator, so the kit doesn’t duplicate it) (`~/.claude/` or `~/.codex/`) so they're available in every session. When it's done, it'll tell you what to try first.

Already downloaded the kit (the green **Code → Download ZIP** button)? Same idea — tell your agent: *"I've downloaded the fluency kit to my Downloads folder — install it for me."* (Took the course earlier and still have last time's copy? Just paste the link above instead — your agent grabs the current version, since the kit keeps improving.)

### Installing again? Nothing of yours gets overwritten

If you've installed before, this is safe to run again — and that's deliberate, because the kit keeps improving and re-installing is how you get the improvements.

**Your agent is instructed never to replace any of these:**

- **Your `CLAUDE.md` / `AGENTS.md`** — the orientation file you built. Snippets from [`course-notes/agents-md-snippets.md`](course-notes/agents-md-snippets.md) are *offered* one at a time and added only if you say yes. Never pasted in wholesale, never rewritten.
- **Your checklist** (`~/.claude/fluency-checklist.md`) — your ticks and notes stay; only genuinely new items get added.
- **Any skill you've tailored** — it checks contents before copying and asks you about anything you've actually changed, offering to back yours up first.
- **Your `~/.codex/config.toml`** — backed up, then merged. Never overwritten.
- **Everything else in your workspace** — your `context/`, your projects, your files. Untouched.

If you'd rather be certain, ask your agent to show you what it's about to change before it does anything.

<details>
<summary>Prefer to do it by hand? (terminal commands)</summary>

From inside the downloaded/cloned folder. ⚠️ **If you've installed before and customised any skill, back it up first** — these commands overwrite same-named files without asking. (Letting your agent install it, as above, avoids this: it checks and asks first.)

```bash
# Claude Code
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R .claude/agents/* ~/.claude/agents/ && cp -R .claude/skills/* ~/.claude/skills/

# Codex (then merge .codex/config.toml's [agents.*] blocks into ~/.codex/config.toml)
mkdir -p ~/.codex/agents ~/.codex/skills
cp -R .codex/agents/* ~/.codex/agents/ && cp -R .codex/skills/* ~/.codex/skills/
```

Start a new session and the skills/agents are live. See [`AGENTS.md`](AGENTS.md) for verification and runtime notes.

</details>

## The agents (specialists)

| Agent | What it does |
|-------|--------------|
| **critical-friend** | Pressure-tests an argument or plan — pushbacks, steel-manned counter-position, blind spots |
| **fact-checker** | Verifies factual/statistical claims against authoritative primary sources via web search |
| **writing-editor** | Heavy editorial pass — clarity, structure, voice, cuts — without replacing your voice |
| **project-planner** | Turns a goal into milestones, tasks, dependencies, and honest estimates |
| **vault-librarian** | Reads your local notes/vault and surfaces what's relevant to the task |
| **web-searcher** | Routes a query to the best backend — cited search, papers, public stats, or live X/social — and returns a sourced answer with inline citations |

## The skills (verbs you invoke)

| Skill | What it does | Delegates to |
|-------|--------------|--------------|
| **setup-workspace** | Sets up your `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/`, writing the files for you. Smart-detects what you've got: builds from scratch if there's nothing, fills the gaps if your setup is half-done, or adds a project / refreshes context / adds a guardrail if it's complete. | new-project |
| **new-project** | Interviews you to find and shape your next project — offers ideas if you're not sure what to work on — then scaffolds it as a tracked project: `overview.md` + `plan.md` + `progress.md` + a router entry. | project-planner |
| **proofread** | Clarity / grammar / structure / tone pass | writing-editor |
| **critical-review** | Stress-test an argument and fact-check its claims, in parallel | critical-friend + fact-checker |
| **research-brief** | Sourced briefing on a topic | web-searcher |
| **premortem** | Surfaces how a plan could fail before you commit | project-planner |
| **daily-brief** | A morning brief from your notes and the web | vault-librarian + web-searcher |
| **visual-explainer** | Turns content into a shareable HTML one-pager | — |
| **slides** | Builds an HTML slide deck | — |
| **canvas-design** | Designs canvas/poster-style visual layouts | — |
| **pdf-create** | Produces a polished PDF | — |
| **here-now** | Publishes a file/folder to a live `{slug}.here.now` URL | — |
| **verify-work** | Checks finished work against what was actually asked, using fresh adversarial sub-agents | critical-friend + fact-checker |
| **convert-docs** | Converts Word / PowerPoint / Excel / PDF / EPUB and more into clean Markdown, using [anydoc](https://github.com/firecrawl/anydoc) — free, open source, and it runs on your own machine, so nothing is uploaded | — |
| **skill-creator** | Interviews you and packages a repeatable workflow as a new skill (Claude Code only — Codex ships its own first-party skill-creator) | — |
| **browser-agent** | Drives a real browser — fills web forms, clicks through flows, extracts page content (agent-browser CLI) | — |

## External connections (`mcp/`)

Agent-followable setup guides — point your agent at one and say *"follow this and set it up for me"*:

| Guide | What it unlocks | Key? |
|-------|-----------------|------|
| [`mcp/paper-search.md`](mcp/paper-search.md) | Academic literature — arXiv, PubMed, Semantic Scholar and ~20 more | None to start |
| [`mcp/data-commons.md`](mcp/data-commons.md) | Public statistics — World Bank, UN, US Census, ABS · 180+ datasets from 85+ sources | Free key |
| [`mcp/openrouter.md`](mcp/openrouter.md) | Live cited search, X/social search, image generation, PDF→Markdown conversion | One paid key (~$10 credit) |

Together these fill out the `web-searcher` agent's lanes — it routes queries to whichever source fits, and falls back to built-in web search when a lane isn't set up.

> **Before you install Paper Search**, read the warning at the top of its guide. The server
> it connects includes tools that download from Sci-Hub, reached **automatically** as a
> fallback rather than only when you ask. Whether that's fine or a problem depends entirely
> on whose machine you're on — the guide explains it and shows how to block those two tools
> if you'd rather they couldn't run. Your call, made with the facts.

## Plain-English guides (`guides/`)

Short how-tos for the questions that came up most in the course — written so you can read them *or* point your agent at them and say *"set this up for me"*:

| Guide | What it covers |
|-------|----------------|
| [`guides/file-conversion.md`](guides/file-conversion.md) | Converting PDFs, Word, PowerPoint, Excel and more to Markdown (and back) — free and local via anydoc, OCR for scans. The **`convert-docs`** skill does it all for you |
| [`guides/github-basics.md`](guides/github-basics.md) | What GitHub is, backup/sharing/version-history, agent-followable setup, second computers |
| [`guides/interface-and-settings.md`](guides/interface-and-settings.md) | Where the context meter is (Claude *and* Codex), permission modes, a sane always-allow list |
| [`guides/folder-guardrails.md`](guides/folder-guardrails.md) | Actually blocking your agent from sensitive folders — includes **`guard-folders/`**, a ready-made, tested guard your agent installs in a minute |
| [`guides/on-the-go.md`](guides/on-the-go.md) | Talking to your agent from your phone (Claude Remote Control and Dispatch; Codex inside the ChatGPT app) |
| [`guides/vscode-setup.md`](guides/vscode-setup.md) | Setting up VS Code as your shared workspace, with the recommended extensions |
| [`guides/browser-agent.md`](guides/browser-agent.md) | Your agent driving a real browser — install, the separate-profile safety rule, form-filling |

## What's inside

```
.
├── .claude/                   # Claude Code kit
│   ├── agents/                #   6 subagents (.md)
│   └── skills/                #   16 skills (SKILL.md per folder)
├── .codex/                    # Codex kit (same capabilities, Codex-native)
│   ├── AGENTS.md
│   ├── config.toml            #   registers the agent roles (multi_agent = true)
│   ├── agents/                #   6 agent-role personas (.toml, via config_file)
│   └── skills/                #   15 skills (Codex ships its own skill-creator)
├── fluency-checklist.md       # What's worth setting up, and what you've done
│                              #   (template; the live copy goes to ~/.claude/)
├── course-notes/              # Reference library — 14 topic modules + snippets
│   └── agents-md-snippets.md  #   standing instructions for your orientation file
├── guides/                    # Plain-English how-tos (GitHub, file conversion, settings, …)
└── mcp/                       # Setup guides for external connections (data-commons, openrouter)
```

## Claude Code vs. Codex

Both runtimes have skills and subagents, configured differently:

| | Claude Code | Codex |
|---|---|---|
| Skills | `.claude/skills/<name>/SKILL.md` | `.codex/skills/<name>/SKILL.md` (same format) |
| Subagents | `.claude/agents/<name>.md` (markdown) | `.codex/agents/<name>.toml`, registered in `.codex/config.toml` |
| Subagent routing | automatic | explicit — *"use the web_searcher agent to…"* |

See [`.codex/AGENTS.md`](.codex/AGENTS.md) for the full Codex mapping and setup notes.

## How to kick things off

Once the kit is installed (see [Install](#install-let-your-agent-do-it) above), here's how to use it:

- **First time?** Run **`setup-workspace`**. It'll interview you for ~5 minutes and create your personalised `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/` *for you* — nothing to copy or save by hand. **Coming back after the course?** Run it again — it'll check what you've already got, fill in anything missing, and leave the rest alone. (If your workspace is already complete, it offers to add a project, refresh context, or add a guardrail instead.)
- **Starting something new — or not sure what to start?** Run **`new-project`**. It opens by asking what you'd like to work on, helps you find the project if you want ideas, then scaffolds it as a tracked project (`overview.md` / `plan.md` / `progress.md`) so a future session can pick up exactly where you left off.
- **Working on something concrete?** Invoke any skill on the real work — *"proofread this draft"*, *"build me slides on X"*, *"research-brief on Y"*, *"run a premortem on this plan"*, *"publish this with here-now"*.
- **Anything on your computer agents should never touch?** Client files, HR records, personal folders — say *"read `guides/guard-folders/README.md` and set up the folder guard for me"* and those folders become hard-off-limits, not just politely avoided.
- **Not sure what to do with any of this?** Paste this into your agent:

> *Read the course notes in `course-notes/`, then look at what's actually set up on my computer. What am I not using yet? Suggest three things worth putting into action this week — and walk me through the first one.*

## Make it yours

This is a starter, not a product. The whole point of the course was that you can shape these tools — so shape them:

- **Improve a skill** after it stumbles: *"that wasn't quite right — update the proofread skill so it keeps my heading style next time."*
- **Add a skill** when you notice a repeated task: *"I keep doing X by hand — turn it into a skill."* (Better still, add a line to your `CLAUDE.md` / `AGENTS.md` asking your agent to *suggest* these moments — see [`course-notes/self-improvement-and-memory.md`](course-notes/self-improvement-and-memory.md).)
- **Trim and tailor**: delete skills you never use, adjust defaults, add examples of your own documents to a skill's folder so outputs come out in your style.

Your agent can do all of this for you — just ask.

---

Part of the **AI Fluency** course by [Dragonfly Thinking](https://github.com/dragonfly-thinking). A starter scaffold, meant to be taken apart and made yours.
