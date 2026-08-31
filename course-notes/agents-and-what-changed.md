# Agents, and What Changed

*The shift everything else here builds on: from an AI you converse with to one that works on your own files, on your own computer.*

If you have used ChatGPT or Claude in a browser, you have used a very capable assistant that can only see what you paste into it. An **agent** is the same intelligence with hands: it reads your files where they already sit, writes new ones, runs things, searches the web, and keeps going until the job is done or it needs you. Nothing else in these notes makes sense until that distinction is concrete, so start here.

---

## Assistant → agent

- **Assistant** = a chat tool you converse with, one message at a time. Linear, and *you* orchestrate it — do this, now change that — babysitting each step.
- **Agent** = a model plus tools plus an environment. You give it a **goal**, not a click-path, and it works out how to get there. It writes itself a to-do list, works unattended, and routes around blockers rather than stopping to report them.
- **The model is the engine; the agent is the car.** Same intelligent model — now with chassis, steering, brakes, and the ability to actually take you somewhere. This is the single most useful analogy in the whole course, because it explains why the same model can feel transformative in one product and unremarkable in another.
- Four properties distinguish an agent:
  - **Goal-directed** — you hand it an outcome ("clean up my bibliography"), not a sequence of steps.
  - **Self-organising** — it finds the context it needs, makes a plan, tracks and ticks off tasks, and picks its own tools.
  - **Context-aware** — rather than a blank slate each time, its environment can be set up so it starts already briefed. That is what [Context Engineering](context-engineering.md) is about.
  - **Adaptive** — it works *around* roadblocks instead of stopping at "computer says no."
- **What matters now is often less the model than the "harness"** — the scaffolding of tools and structure built around it. A well-harnessed weaker model beats a bare stronger one, which is why the work in these notes pays off more than switching models does.

## Why a coding agent can do almost any knowledge work

- **There is a little agent living on your machine.** Picture dropping a small agent into a folder when you start a session — like placing a character on a spot on a map; it has to be *somewhere* to work. **A folder is a room; the root of your computer is the building.** It works directly on *your* files where they already sit, rather than on copies you upload to a website. (The heavy thinking still runs on the provider's servers — but your files stay on your machine unless you publish or sync them.) This is the mental model people are slowest to grasp, and the one everything else rests on.
- A **coding agent** — Claude Code, or Codex inside the ChatGPT app — is an agent that can **write and run code on your computer**. *"If it can use a computer, it can do almost anything"*, because nearly all knowledge work happens on a computer. You do not write the code and you never see it unless you ask.
- **Code is the universal connector.** An agent can write code to read and move files, produce a PDF, publish a web page, or reach any service with an API — payments, email, calendars, or open data sources. That is why the ceiling is so much higher than a chat window.
- **Navigating your files is the superpower.** Unlike a chatbot that only sees what you paste in, a coding agent can search across thousands of files on your machine almost instantly, find a phrase everywhere it appears, read only what it needs, and reorganise folders itself.
- **Retrieval vs agentic search — why this beats "throw it in a project."** Chat tools (ChatGPT projects, Claude projects, NotebookLM) use **vector retrieval**: they chop your documents into chunks and pull only the chunks that seem *semantically* nearest — so they may **never read everything you uploaded**, and "semantically similar" is not always what is actually relevant. **Agents do agentic search instead**: given a task, they search your real files and can read *whole* documents. Convert your PDFs to text first (see [Markdown & File Conversion](markdown-and-file-conversion.md)) and the whole document goes into context, not a lossy sample.

## Tokens, context, and context rot

- **Tokens** are the unit of processing — roughly ¾ of a word (1,000 tokens ≈ 750 words). Everything becomes tokens: your instructions, the conversation history, PDFs, images. Tokens are also how usage is priced and how context is measured.
- **The context window** is how much the model can hold in working memory at once. It has grown from a few thousand words at ChatGPT's launch to **a million tokens or more** — around 750,000 words, roughly ten books. If your work is mostly text, your life's work might fit inside a single window.
- **A big window does not remove the problem.** Information being *in* the window doesn't guarantee the agent still attends to it: an instruction given hundreds of thousands of tokens ago may simply be missed, and instructions placed in the *middle* get dropped more often than ones at either end. This is **context rot**, and the tell is that nothing announces it — the agent just goes from sharp to vague.
- **Compaction helps, and it is lossy.** When the window nears full, the tools auto-summarise the conversation to make room, and that summary drops detail without knowing which small detail was load-bearing. **A fresh session beats a compacted one, every time.**
- **The remedy is a handover note.** *Before* the window fills, ask for one: a short file capturing what this session did, decided, and is up to. Then start fresh and hand it that file. Think of it as going on leave — you write the handover so whoever picks up isn't lost.

  > *"We're getting long. Write a handover note to `handover.md` — what we've done, key decisions, and exactly where we're up to — so a fresh session can continue."*

- **Searches and tool use eat tokens too.** A big search task can quietly burn 100k–200k tokens. That is the argument for [Subagents](subagents.md) and for a workspace an agent can navigate: *your context window is finite, but your workspace doesn't have to be.*
- Where to find the meter in each tool: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## From doer to director

- The celebrated roles used to be the actor, the athlete, the writer — the individual contributor. Working with agents, often several at once, you become the **director**: setting the vision, intervening with feedback, coaching the output toward what you actually want.
- That makes your **taste and expertise** the valuable thing — the ability to spot the wrong 1% and correct it.
- **It is more cognitively demanding, not less.** You are context-switching across agents and constantly evaluating outputs. Anyone who tells you this is about doing less thinking has not done it.
- **Models come in tiers**, and the tier decides both capability and cost. Cheaper, faster tiers trade reasoning for speed; the top tiers reason better and burn usage far faster. Match the model to the job, and treat the ladder as directional rather than fixed — it reshuffles with every release. For most of what these notes describe, a **mid-tier model is the right default**.

> **On specifics versus principles.** Model names, prices and capability figures in any course material date fast. Don't lean on the specifics; lean on what doesn't move: **tiers exist and cost real money, so match the model to the job**; **effort / reasoning level is your main cost dial**; **verify what matters**; and keep your working files in **markdown**. Those hold whichever model you are on.

## Learned agency

- The old reflex was "computer says no → I'm stuck." Because agents are intelligent, have web access, and run *on your machine*, a blocker is rarely the end of the road — **ask the agent.** It can explain a concept at any level until it clicks, or simply do the setup you're stuck on.
- A story worth repeating: one of Dragonfly's co-founders was stuck with her agent and messaged the other for help. The reply was, *"have you asked your agent?"* She hadn't. It sorted it out. Neither founder came from a technical background.
- One participant's version of the same move, and the most transferable line anyone has offered in these sessions: *"explain everything to me as if I'm a nine-year-old."* It came back with diagrams and plain words, and the penny dropped.
- This applies to these notes too. When something here doesn't match your setup, don't stop — ask your agent to bridge the gap. **Learned agency, not learned helplessness.**

## Practical notes

- **Voice, not typing.** Most people type 40–50 words a minute and speak at 100–150. Modern speech-to-text is accurate enough to dictate straight into any app, and it handles punctuation for you. The real power is *briefing* an agent: instead of carefully typing a prompt, hit record and give a five-minute brain-dump of context and intent. Typing friction is the main reason people under-brief their agents, and this is the fastest habit to fix it. It was the single most-recommended habit of the whole course.
- **Use the desktop app, not the browser.** These tools need to reach your file system. The web versions cannot, and someone in every cohort loses twenty minutes to this.
- **Which tool?** Claude Code (the **Code** view of the Claude desktop app) and **Codex** (inside the ChatGPT desktop app) are functionally equivalent — point either at a folder and it works with your files. Either is fine; some people keep both, one for work and one for personal. If you have no preference, Codex is currently the slightly simpler starting point.
- **Hallucinations** are much less common than they were, especially with web access — but see [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md) before you rely on that.
- **Safety.** These agents can create, move, rename and delete files. Decide what they should never touch, and make it a rule that blocks rather than a hope — see [Permissions & Guardrails](permissions-and-guardrails.md).

## Background — the energy and water question

*Not part of the taught course, but it comes up in every room, so here is the honest read.*

- **The concern is legitimate and the headline numbers are badly overblown.** A single prompt uses roughly **10–25 mL** of water. Charging your phone ≈ 50 prompts; a shower ≈ 17,000 prompts; a long-haul flight ≈ millions. One bestselling book overstated AI water use by around **1,000×**.
- **The nuance cuts both ways.** Aggregate demand *is* climbing fast — this is **Jevons paradox**: make a resource cheaper and total demand can rise *more*, not less. *Where* a data centre sits matters for local water and power, and working with agents uses far more prompts than chatting does.
- AI also *reduces* consumption elsewhere — DeepMind cut Google's data-centre cooling energy substantially. Real costs, real nuance, not the doomsday story.
- Source for the comparisons: [Andy Masley's blog on AI energy and water](https://blog.andymasley.com/).

## The autonomy trend

- The [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) research tracks **how long an agent can work unsupervised** on a task it completes about half the time, measured as how long the same task takes a human. It was flat for years, then went near-vertical.
- At the time of writing, the top models work autonomously for the better part of a working day, and with a well-built harness people already run them for days on a single goal. **The specific hours will be wrong by the time you read this; the trend is the point.** Expect agents working in the background for you to become normal.

## Further reading

- **[Claude](https://claude.com/download)** — the desktop app. Use the **Code** view.
- **[OpenAI Codex](https://developers.openai.com/codex/cli)** — OpenAI's coding agent, which lives inside the ChatGPT desktop app. There is no separate Codex download.
- **[Directors, Coaches, and Editors: The Human Role in the Age of AI](https://www.dragonflythinking.com/insights/directors-coaches-and-editors-the-human-role-in-the-age-of-ai)** — Anthea Roberts on the shift from performing to directing.
- **[Learned Agency vs Learned Helplessness](https://www.dragonflythinking.com/insights/learned-agency-vs-learned-helplessness)** — why "computer says no" is no longer a stopping point.
- **[Learning Agency: Two Processes, Not Just One](https://www.dragonflythinking.com/insights/learning-agency)** — same AI, two divergent outcomes: amplified agency or atrophied agency. Choose deliberately.
- **[NotebookLM](https://notebooklm.google/)** — a strong free **vector-retrieval** tool for very long documents. Complementary to an agent rather than a replacement; see *retrieval vs agentic search* above.

## Try this

> Point me at a folder of real documents I already have. Ask me what's in it, then compare
> the documents — where do they converge, where do they disagree? Produce a short brief as
> an HTML page I can open. Don't ask me to upload anything.

Then read [Context Engineering](context-engineering.md), which is where the leverage actually is.
