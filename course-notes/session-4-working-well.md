# AI Fluency Session 4 — Key Points

**Session 4: Going AI-Native — working well with your agent**

The final session. Instead of racing on to new capabilities, we consolidated what we already have and learned to *use it well*: moving into a proper editor (**VS Code**) as a shared workspace, knowing where your agents actually live on your computer, setting up projects that document themselves, staying the director with planning mode, and — the one genuinely new capability — **routines**: scheduled tasks that run in the background, which everyone set up and ran live. Along the way: keeping sensitive folders out of bounds, talking to your agent from your phone, GitHub, converting file formats, and verifying an agent's work. The closing theme tied the course together: **augmentation, not automation** — don't slot these tools into your old process; reinvent the process around them.

---

## The Story So Far

- **Session 1** — put a little agent *inside your computer*, pointed at a folder.
- **Session 2** — gave it a **map** (the `AGENTS.md` / `CLAUDE.md` orientation file), furnished its environment with context, and met **sub-agents**.
- **Session 3** — handed it **tools and a filing cabinet of skills**, and published to the live web.
- **Today** — bring it together: work *closely* with your agent in an editor, set it running in the **background**, and keep the workspace organised over time.

## Why VS Code (and the tour)

- **VS Code** is a free code editor built by Microsoft that developers use every day — and it turns out to be an excellent *shared workspace* for working with agents, even if you never write code.
- The chat apps are great, but they're constrained when you want to be **hands-on with the outputs**: making edits yourself, viewing PDFs and spreadsheets in place, collaborating on a document rather than just asking for changes.
- **"Isn't this just Claude Code in another window?"** Almost — and that's the point. The difference isn't new powers, it's *posture*. In the chat you send the agent off to execute; here you work *beside* it as a collaboration partner — typing in the document yourself, highlighting a line and reshaping it, editing the output directly. That matters most where **the last 1% of nuance is the whole game** — the wording only you can get right. You keep your hands on the work without giving up any of the agent's power.
- The key mental model: VS Code, Claude Code and Codex are all just **windows into the same folder**. Opening a folder in VS Code and in Claude isn't syncing two copies — it's *the same files*, seen through two windows.
- **The tour:** the file tree on the left mirrors your file explorer (click to open, right-click to create); **extensions** add abilities — start with the **Claude** and/or **Codex** extension (the full agent as a sidebar in your workspace), plus a Markdown editor (render *and edit* — see below), a PDF viewer, and CSV/Word viewers. The recommended set, with install steps, is in [`../guides/vscode-setup.md`](../guides/vscode-setup.md).
- **Draft in Markdown, right where the agent can see it.** With the Markdown extension a `.md` file isn't just *previewed* — it's a two-way writing surface: it renders like a document and you edit it in place, typing `/` for a formatting menu (headings, bullets, checkboxes) instead of remembering the raw symbols. Behind the scenes it stays plain text. So create a `.md` file, brain-dump or scaffold there, then: *"read my `writing.md` and turn it into a report in this style."* No copy-paste shuffle — and you make the last-15% edits yourself, which is exactly where these tools sometimes fall short.
- **Three quick wins worth the muscle memory:** **voice-to-text** — press the mic (⌘D in the Claude sidebar) and *talk* instead of typing. If you take one thing from this session other than "use agents at all," make it this: a spoken brain-dump is the fastest way to get context in, and it's how the project setup below is best run. **Shift-Tab** cycles the permission modes. And remember the **`.md`** ending when you name a new file, or it won't render as Markdown.

## Where everything lives (the recap that matters)

- **These tools work on your file system.** The folders and files are on your computer; the apps are just windows onto them. The AI *processing* happens on the provider's servers (whatever's in the context window gets sent off), but your files stay put unless you explicitly publish or sync them.
- **Global vs. project config.** Configuration lives in hidden **dot-folders** (`.claude` / `.codex`): a **global** one in your home folder (`~`) that applies everywhere, and **project-local** ones that apply only inside that folder. Easiest way to find your global config: *ask your agent to open it for you*.
- **Orientation files stack.** One at the workspace root for general orientation; another inside a project folder for project-specific instructions. The agent loads both.
- **File paths.** Every file has a unique address. Right-click a file for **two** ways to hand the agent that address: **Copy Path** (its full address on your whole computer) or **Copy Relative Path** (its address *from the folder you've opened* — the "root"). The difference is like posting a parcel versus inviting a friend over: to another country you write out country, city and street; to someone already in your city you just say *"come to mine, I'm at number 12."* Use the full path to point the agent at something *outside* the current folder; the relative path is enough *inside* it. Either way — or an **@-tag** by name in the chat — beats making it search.
- **Viewing markdown nicely:** VS Code previews it; outside an editor, **Obsidian** renders Markdown as formatted documents.

## Keeping sensitive folders out of bounds

- By default agents won't rummage through unrelated folders — but don't just *trust* that. Two layers:
  1. **Instructions** in your `AGENTS.md` / `CLAUDE.md` ("never open `~/Private`") — good, but it's *asking*, like giving someone a key and requesting they stay out of one room.
  2. **Guardrails** — a small piece of configuration that actually *blocks* the action before it runs (in Claude these are called **hooks**). That's locking the door rather than asking.
- Do both. A worked, copy-able guardrail example lives in [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md).

## Set up a project by letting the agent interview you

- The **`new-project`** skill (in this kit — just type `/new-project`) interviews you about what you're trying to achieve, then scaffolds the project folder: an **overview**, a **plan**, a **progress log**, plus a tasks folder for bigger pieces of work.
- Why the interview pattern works: when you're doing something new you don't know what the agent needs to know — or the extent of your own ignorance. Letting it ask the questions surfaces context you'd never have thought to volunteer. (It searches the folder first and only asks what it actually needs.)
- **Properties (frontmatter).** A few labels at the top of a Markdown file — `status`, `owner`, `updated`, `tags` — let your agent answer *"which tasks are still pending?"* by reading the labels instead of re-reading everything. The agent maintains these, not you.
- The skill is a sensible default, not a rule — edit it to match how you like to organise your work.

## Planning mode — staying the director

- The mode selector gives the agent different levels of permission: **ask-each-time**, **accept edits**, **auto**, up to bypass-everything. Auto saves you clicking "yes, yes, yes." (A fuller map of modes and safe defaults: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).)
- **Plan mode** is special: the agent *cannot take action* while in it. It goes back and forth with you, builds a plan, and asks before switching back to a mode where it can act. No more jumping the gun.
- In Codex, type `plan` or press shift-tab. In Copilot, say *"plan this out — don't take any action yet"* for most of the benefit.
- Best practice: iterate in plan mode, then **ask it to save the plan as a file** in the project so future sessions can pick it up.

## Plans, task files, and progress logs — work that tracks itself

- Context windows are finite, and the automatic summaries agents make when context fills are lossy — they don't know which fine detail was crucial.
- The answer: **break work into self-contained units with their own files.** A task index with checkboxes, one file (or folder) per task for bigger work, a **progress log** updated as it works.
- The payoff: a new session — or a recovery after a crash — reads the project files and picks up exactly where things left off. Sub-agents get up to speed the same way.
- Point your project's orientation file at them: *"if you need to be brought up to speed, read these context documents."*
- The habit underneath all of this — and how to bake it in so it happens without you remembering — is [Self-Documenting Workspaces](self-documenting-workspaces.md).

## A self-improving workspace

- Small additions to your `AGENTS.md` / `CLAUDE.md` make the setup get better on its own: **suggest improvements after running a skill**, **propose a skill when a task repeats**, keep a **`gotchas.md`** of things learned the hard way.
- You can even run a routine that periodically reviews how you've been working and proposes new skills, folders or resources.
- The ready-to-paste lines are in [Self-Documenting Workspaces](self-documenting-workspaces.md) — and the `setup-workspace` skill seeds them into your orientation file automatically.

## Routines — your agent working in the background

- A **routine** (Claude) or **scheduled task** (Codex) is a pre-saved prompt that fires on a schedule — daily, weekly, or manually triggered — as a full agent session, with access to everything you've built (skills, sub-agents, folders).
- Examples from the course: a **daily news digest** (one uses the visual-explainer skill to produce a clean HTML page each morning), a **morning brief**, an important-email flag, an alert system tracking regulator publications, batch-converting PDFs to Markdown overnight — and a **weekly "tidy and document my workspace" pass** that reviews the week's sessions and makes sure the work is written down, so a future session (or a recovery after a crash) can get up to speed fast. That last one is the routine that keeps [Self-Documenting Workspaces](self-documenting-workspaces.md) honest without you remembering to.
- **Local vs. cloud:** local runs on your laptop (awake and online); cloud runs without it — for Claude, cloud routines work through **GitHub** (files pulled from your repo, processed, results written back — see [`../guides/github-basics.md`](../guides/github-basics.md)). No GitHub? Run it locally. Note that cloud means your files travel to GitHub (a third party — secure and standard practice, but a real consideration for genuinely sensitive material; keep those routines local).
- **Two settings to get right:** permissions to **auto** (so it can finish without waiting on approvals), and **choose the model to match the job** (a heavyweight model for real thinking; a fast/cheap one for mechanical tasks).
- **Connections carry over — sometimes.** A routine can use the email/calendar/other connections you set up in the Claude desktop app (their credentials live in the cloud), so a scheduled agent really can, say, read your inbox and flag what matters. But a *cloud* routine may not see connections you only wired up locally — if a routine can't reach a tool, check where it's running.
- Practical gotchas we hit live: if a routine seems stuck on "running," click into it — there may be a **permission prompt waiting quietly**; and check the output folder, because it sometimes finishes without saying so.

## Working from your phone

- **Codex:** lives in the ChatGPT phone app — pair it with your computer (QR code) and kick off or steer tasks from anywhere.
- **Claude:** pair the Claude mobile app with the agent running on your computer (the feature demoed as *Dispatch* in the session — Claude currently splits this across **Remote Control** for Claude Code sessions and **Dispatch** in Cowork) and fire off voice or text instructions on the go while your machine (awake and online) does the work.
- Setup steps for both — and the cloud-computer option for the very dedicated — are in [`../guides/on-the-go.md`](../guides/on-the-go.md).

## What is GitHub?

- An online store for folders of files: **backup** (restore everything if your laptop dies), **collaboration** (share a workspace with your team), and **version history** (every change kept; roll back any mistake). It's how Dragonfly's own (mostly non-developer) team shares everything — and it's what unlocks Claude's cloud routines.
- Mild learning curve, but your agent knows it deeply. Plain-English explainer + agent-followable setup: [`../guides/github-basics.md`](../guides/github-basics.md).
- **The AI-native default: raw files + sync.** Agents work far better on plain files on your computer than inside walled-garden cloud apps — which is why AI-native teams (Dragonfly included) are drifting from complex cloud tools toward *files + GitHub sync*. A sensible middle ground: keep a fast file-based workspace for your own work, and connect to a shared tool only when others need in.
- **When you do need real-time collaboration**, the usual options are **GitHub** (push to save, pull to get changes), **Obsidian** (Markdown with built-in sync), and **Notion** — the most capable cloud tool here (databases, tags, statuses, its own agent), and one Claude Code can drive directly over **MCP** (the connection you met in Session 3). One gotcha with Git-style sync: it saves at the moment you *push*, not continuously — so if two people reorganise at once, you can collide and have to reconcile.

## Converting file formats

- Renaming a file to `.md` does **not** convert it. Instead **ask your agent to convert** — it moves reliably between PDF, Word, PowerPoint, HTML and Markdown. Agents work best on text, so converting content-heavy PDFs/Word docs to Markdown makes everything downstream better.
- A practical pattern from the room: wordy PowerPoint → save as **PDF** → agent turns it into a **visual HTML** page → iterate → distribute as PDF or a pin-gated `here.now` page.
- Full instructions — including the high-fidelity **Mistral OCR** route for scanned or complex PDFs — in [`../guides/file-conversion.md`](../guides/file-conversion.md).

## Verifying an agent's work

- *"How do you know it did what you asked?"* You're responsible for the output, so build verification in — and never let an agent mark its own homework.
- **Ad-hoc:** the **`verify-work`** skill (in this kit) spins up fresh adversarial sub-agents that check the finished work against what was actually asked, requirement by requirement.
- **Repeatable:** for processes you run often and know the "correct" answer for, build a dedicated verification step into the skill or routine itself.
- The deeper move (from a participant with a test-and-evaluation background): map how *you* actually check this kind of work — your own standards and tests — and mechanise *that*. Ask the agent *"what are my options here?"* as a thought-partner; keep your own judgement in the loop.

## Tokens, plans, and the cost mindset

- The $20/month plans are a great *taste* — real use (routines, verification passes, sub-agents) will hit their limits, because doing something *well* takes more loops than you first expect.
- Reframe: don't compare it to app subscriptions; compare it to *what you'd pay a person to do the work*. The higher tiers currently give you far more token value than they cost.

## The pack (you're holding it)

- **This repo is the take-home pack**: the agents, the skills (including `new-project`, `verify-work`, `handoff`), these course notes, plain-English guides (`guides/`), and setup instructions for external connections (`mcp/`) — academic papers, public statistics, and the **one-key** OpenRouter setup for search and image generation.
- **Recommended move:** point your agent at the repo and *chat about it* — "read the course notes, look at what's set up on my computer, and tell me what's worth doing next" — and let it walk you through installation and setup.

## Wrapping up the course

- The line that captures it: **augmentation, not automation.** When the electric motor arrived, productivity barely moved for decades — people slotted it into the existing process instead of redesigning around it. Don't just streamline your current workflow; **reinvent it** around what agents can now do.
- The real outcome isn't any single capability — it's that **you can go and figure it out**. When you don't know how to do something, the agent can teach you. When the computer says no, talk back.
- It's a fast-moving space and it can feel like a lot. Don't chase every new tool: **keep using Claude and Codex, reflect on how you're using them**, and you'll stay well ahead — you never know when you'll stumble on the workflow that makes you an order of magnitude more effective.
- **Office hours** continue — bring your stuck routines and broken setups. **Referrals:** share the course and they get a discount. **Going further:** Dragonfly's **AI-Native Sprints** operationalise all of this inside your organisation, tailored to your actual tools — with a graduate rate for course alumni.

## Homework (for the road)

- **Set up one routine** that saves you real time (a morning brief, a news digest, an important-email flag) and let it run.
- **Try VS Code** on a folder you already work in — install the Claude or Codex extension, draft something in a Markdown file, and edit alongside your agent.
- **Ask your agent to convert** a real document between formats, and — if you can — get **one external connection** (email, calendar, or one of the `mcp/` guides) going.
- Above all: **keep practising.**
