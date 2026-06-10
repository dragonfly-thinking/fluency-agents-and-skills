# Fluency Agents and Skills

Everything you take home from the Dragonfly Thinking **AI Fluency** course: the agents and skills we built and used, setup guides for the external connections we covered, and the key points from each session. Open it in [Claude Code](https://claude.ai/download) or [OpenAI Codex](https://developers.openai.com/codex/cli) and you have a real multi-agent setup — to use as-is, and to make your own.

A skill is a *verb* you invoke ("proofread this", "build me a deck"). A subagent is a *specialist* a skill can hand work to. Several skills delegate to the base agents below.

**Fresh from the course?** After installing, start with [`course-notes/`](course-notes/) — the key points from all four sessions, with ready-to-paste prompts for putting them into action.

## Install (let your agent do it)

No GitHub account needed — this page is public. Copy this page's link, paste it into Claude Code or Codex, and say:

> **"Read the AGENTS.md at this link and install the kit for me."**

Your agent does the rest: it downloads the kit, follows [`AGENTS.md`](AGENTS.md), and copies the 6 agents and 15 skills into your setup (`~/.claude/` or `~/.codex/`) so they're available in every session. When it's done, it'll tell you what to try first.

Already downloaded the kit (the green **Code → Download ZIP** button)? Same idea — tell your agent: *"I've downloaded the fluency kit to my Downloads folder — install it for me."* (Took the course earlier and still have last time's copy? Just paste the link above instead — your agent grabs the current version, since the kit keeps improving.)

<details>
<summary>Prefer to do it by hand? (terminal commands)</summary>

From inside the downloaded/cloned folder:

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
| **setup-workspace** | Sets up your `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/`, writing the files for you. Smart-detects what you've got: builds from scratch if there's nothing, fills the gaps if your setup is half-done, or adds a project / refreshes context / adds a guardrail if it's complete. | new-project / discovery-interview |
| **new-project** | Interviews you to find and shape your next project — offers ideas if you're not sure what to work on — then scaffolds it as a tracked project: `overview.md` + `plan.md` + `progress.md` + a router entry. | discovery-interview / project-planner |
| **proofread** | Clarity / grammar / structure / tone pass | writing-editor |
| **critical-review** | Stress-test an argument and fact-check its claims, in parallel | critical-friend + fact-checker |
| **research-brief** | Sourced briefing on a topic | web-searcher |
| **discovery-interview** | Interviews you to turn a vague idea into a spec | project-planner |
| **premortem** | Surfaces how a plan could fail before you commit | project-planner |
| **weekly-review** | Pulls the week together into a review | vault-librarian + project-planner |
| **daily-brief** | A morning brief from your notes and the web | vault-librarian + web-searcher |
| **visual-explainer** | Turns content into a shareable HTML one-pager | — |
| **slides** | Builds an HTML slide deck | — |
| **canvas-design** | Designs canvas/poster-style visual layouts | — |
| **pdf-create** | Produces a polished PDF | — |
| **here-now** | Publishes a file/folder to a live `{slug}.here.now` URL | — |
| **generate-image** | Generates an image from a prompt (Nano Banana via one OpenRouter key) | — |

## External connections (`mcp/`)

Agent-followable setup guides — point your agent at one and say *"follow this and set it up for me"*:

| Guide | What it unlocks | Key? |
|-------|-----------------|------|
| [`mcp/paper-search.md`](mcp/paper-search.md) | Academic literature — arXiv, PubMed, Semantic Scholar and ~20 more | None |
| [`mcp/data-commons.md`](mcp/data-commons.md) | Public statistics — World Bank, WHO, UN, ABS and ~240 datasets | Free key |
| [`mcp/openrouter.md`](mcp/openrouter.md) | Image generation (`generate-image`), live cited search, X/social search | One paid key (~$10 credit) |

Together these fill out all of the `web-searcher` agent's lanes — it routes queries to whichever source fits.

## What's inside

```
.
├── .claude/                   # Claude Code kit
│   ├── agents/                #   6 subagents (.md)
│   └── skills/                #   15 skills (SKILL.md per folder)
├── .codex/                    # Codex kit (same capabilities, Codex-native)
│   ├── AGENTS.md
│   ├── config.toml            #   registers the agent roles (multi_agent = true)
│   ├── agents/                #   6 agent-role personas (.toml, via config_file)
│   └── skills/                #   the same 15 skills, SKILL.md format
├── course-notes/              # Key points from the 4 sessions + put-into-action prompts
└── mcp/                       # Setup guides for external connections (paper-search, …)
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
- **Have an idea you can't quite write down?** Run **`discovery-interview`**. It asks the non-obvious questions until the shape of what you want is clear, then writes the spec.
- **Working on something concrete?** Invoke any skill on the real work — *"proofread this draft"*, *"build me slides on X"*, *"research-brief on Y"*, *"run a premortem on this plan"*, *"publish this with here-now"*.
- **Not sure what to do with any of this?** Paste this into your agent:

> *Read the course notes in `course-notes/`, then look at what's actually set up on my computer. What from the course am I not using yet? Suggest three things worth putting into action this week — and walk me through the first one.*

## Make it yours

This is a starter, not a product. The whole point of the course was that you can shape these tools — so shape them:

- **Improve a skill** after it stumbles: *"that wasn't quite right — update the proofread skill so it keeps my heading style next time."*
- **Add a skill** when you notice a repeated task: *"I keep doing X by hand — turn it into a skill."* (Tip from Session 3: add a line to your `CLAUDE.md` / `AGENTS.md` asking your agent to *suggest* these moments.)
- **Trim and tailor**: delete skills you never use, adjust defaults, add examples of your own documents to a skill's folder so outputs come out in your style.

Your agent can do all of this for you — just ask.

---

Part of the **AI Fluency** course by [Dragonfly Thinking](https://github.com/dragonfly-thinking). This is the AI Fluency tier — a starter scaffold, not a methodology-license deployment.
