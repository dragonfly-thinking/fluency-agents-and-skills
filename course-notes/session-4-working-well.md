# AI Fluency Session 4 — Key Points

**Session 4: Working Well (Consolidation)**

The final session. Instead of racing on to new capabilities, we consolidated what we already have and learned to *use it well*: where everything actually lives on your computer, how to set up a project properly (by letting the agent interview you), how to stay the director with planning mode and permission modes, and how to structure ongoing work so your agent can always pick up where it left off. The one genuinely new capability: **routines** — scheduled tasks that run in the background, which everyone set up and ran live. We closed the course with the path forward: a final resource pack with everything covered, external data connections to set up in your own time, and the core skill underneath it all — knowing you can figure it out with your agent as the teacher.

---

## The Story So Far

- **Session 1** — got an agent installed and pointed at a folder.
- **Session 2** — built its workspace and gave it a map (AGENTS.md / CLAUDE.md, context files, sub-agents).
- **Session 3** — gave the agent skills and connected it out to other tools; published to the live web.
- **Today** — consolidation: use what you have *well*, plus background routines.

## A quick teaser: anyone can build apps now

- Sam opened with a look at **Replit** (replit.com) — an app builder where you describe what you want in chat and it builds the app for you.
- Starter plan ~US$20/month. You won't build Microsoft Outlook, but a recipe planner or a small internal tool for your team is genuinely within reach — including logins so you can share it with specific people.
- The point: if you ever think "I wish there was a little app for this," there can be. It's never been easier.

## Where everything lives (the recap that matters)

- **These tools work on your file system.** You create a folder, open it with Claude/Codex, and that folder becomes the agent's workspace — it can read, create, move, and edit everything inside it.
- **The apps are just different windows into the same folder.** Claude Code, Cowork, Codex, a code editor — same files and folders underneath. (For Microsoft Cowork folks, the equivalent "window" is your OneDrive.)
- **Orientation files** (`CLAUDE.md` for Claude, `AGENTS.md` for Codex/Cursor) are preloaded instructions read at the start of *every* session. Every new session is a blank slate — this file is how you stop re-explaining yourself.
- **They stack.** One at the workspace root for general orientation; another inside a project folder for project-specific instructions. The deeper you go, the more specific they get — and the agent loads both.
- **The `.claude` folder** holds your sub-agents and skills. The dot means "configuration" and makes it invisible in Finder by default — it's still there, and a code editor (or asking your agent) will show it.
- **Viewing markdown nicely:** markdown is plain text with hashes. Apps like **Obsidian** render it as formatted documents — worth installing if you're not working in a code editor.

## Set up a project by letting the agent interview you

- We pasted in a **project-setup prompt** that interviews you — asking what you're trying to achieve, what you're working with — and then configures the project folder for ongoing collaboration.
- Why the interview pattern works: when you're doing something new, you often don't know what the agent needs to know — or the extent of your own ignorance. Letting it ask the questions surfaces the useful context you wouldn't have thought to provide.
- The questions adapt to what's already in your folder — it searches first, then asks what it actually needs.

## Planning mode — staying the director

- The mode selector gives the agent different levels of permission: **ask-each-time**, **accept edits**, **auto**, up to bypass-everything. Auto saves you clicking "yes, yes, yes."
- **Plan mode** is special: the agent *cannot take action* while in it. It goes back and forth with you, builds a plan, and asks before switching back to a mode where it can act. No more jumping the gun.
- In Codex, type `plan` or press shift-tab. No direct equivalent in Copilot? Just say *"plan this out — don't take any action yet"* and you get most of the benefit.
- Best practice: go back and forth in plan mode, then **ask it to save the plan as a file** in the project so it can be referenced in future sessions.

## Plans, task files, and progress logs — work that tracks itself

- Context windows are finite (200K–1M tokens, roughly 150–750K words) and the automatic summaries agents make when context fills up are lossy — they don't know which fine details are crucial.
- The answer: **break work into self-contained units with their own files.** A task index with checkboxes the agent ticks off, one file (or folder) per task for bigger work, and a **progress log** updated as it works.
- The payoff: when you start a new session — or your computer crashes mid-task — the agent reads the project files and picks up exactly where it left off. Other agents (and sub-agents) can get up to speed the same way.
- Update the project's orientation file to point at these: *"if you need to be brought up to speed, read these context documents."*

## Routines — your agent working in the background

- Both Claude and Codex support **routines**: scheduled tasks that run on a recurrence you choose (daily, hourly, weekly, or manually triggered) — on your computer (local) or in the cloud (runs even with your laptop closed).
- Sam's example: a **daily explainer** routine that uses the visual-explainer skill to teach him one new AI concept each morning, saved to a folder. We each built and ran one live (Thai recipes featured).
- Routines can use everything you've already built — your skills, sub-agents, and folders. They're not lightweight extras; they're full agent sessions on a schedule.
- Practical gotchas we hit live: choose **local** unless you want the GitHub-connected cloud setup; if a routine seems stuck on "running," click into it — there may be a **permission prompt waiting quietly**; and check the output folder, because it sometimes finishes without saying so.
- Use-cases generated in the room: a fortnightly **blog editorial pipeline** (generate candidate questions every two months), an **alert system tracking regulator publications**, weekly news digests on a topic, and batch-converting PDFs to markdown overnight to save tokens.

## Tokens, plans, and the cost mindset

- The $20/month plans are a great *taste* of the capabilities — and when you start running routines and real work, you'll hit their limits.
- Reframe: don't compare it to app subscriptions; compare it to *what you'd pay a person to do the work*. AI isn't traditional software — every request consumes real resources, like fuel. The higher tiers currently give you far more token value than they cost.

## Deferred to the final resource pack

In the interest of time (and sanity), some things moved to the take-home pack rather than live setup:

- **Research connections**: a tool giving your agent access to open-access academic journals, and Google's **Data Commons** (hundreds of statistical sources — World Bank, ABS, and more; free, needs an API key).
- **One key to rule them all**: a single service (one API key) that unlocks search, image generation, better PDF→markdown conversion, and more — instead of signing up for everything separately.
- **You're holding the pack** — this repo is it: all the skills, the agents, and setup instructions. **Recommended move:** point your agent at it and *chat about it* — "what fun stuff could we set up from this?" — and let it walk you through installation.

## Wrapping up the course

- The real outcome isn't any single capability — it's that **you can go out and figure it out**. When you don't know how to do something, you know the agent can teach you. When the computer says no, talk back.
- Iterate on everything: skills won't be right the first time; review outputs and improve them as you go. It's never one-and-done.
- **Office hours** continue — bring your stuck routines and broken setups.
- **Referrals:** share the course with someone and they get the group price.
- **Going further:** Dragonfly's AI-native services — a four-week hands-on sprint building custom skills and workflows inside your organisation, tailored to your actual tools — with a discount for course participants. Reach out if that sounds useful.
