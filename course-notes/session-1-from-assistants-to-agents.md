# AI Fluency Session 1 — Key Points

**Session 1: From Assistants to Agents**

This session introduced the shift from chat-based AI assistants to AI agents — tools that can take action on your computer, not just respond to questions. We covered why this moment matters (an industrial revolution for cognition), how large language models actually work (tokens, context windows, why "context is king"), the nuance in the energy/water debate, and what makes a *coding agent* different from a chatbot — then got hands-on with Claude Code or OpenAI Codex, pointing it at a folder and having it read files and make something. The key takeaway: you don't need to know how to code — the agent handles that — but you do need to develop taste and judgment as a "director" of AI work.

---

## The AI Revolution

- We're living through a real revolution — plausibly bigger than the personal computer. The best analogy is the **industrial revolution**: just as we learned to harness energy *external* to ourselves and prosperity (GDP) exploded, we're now learning to tap into **intelligence** external to ourselves. The industrial revolution externalized *physical* work; this one externalizes *cognitive* work.
- This is the age of the **10X knowledge worker** — the idea, borrowed from software (the "10X engineer"), that one person who harnesses these tools can be an order of magnitude more effective than a peer. Learning to use them well is one of the highest-leverage things you can do right now.
- **The capabilities are real and climbing fast.** An OpenAI model recently solved an **Erdős problem** in mathematics that had been open for ~60–80 years — verified by a renowned mathematician. But these systems have **jagged intelligence**: brilliant at some things, surprisingly limited at others. Expect both.
- **You can't reason well about this technology without being hands-on** — and this matters most for leaders. You don't need to *do* the work forever, but you need direct experience to lead through the transition. The thought leaders who clearly aren't hands-on tend to miss the mark; you can hear it when they talk. Reading about AI isn't enough — you have to use it.

## How Large Language Models Work

- An LLM is built by processing an enormous amount of data (the internet, books, code, images) and learning which pieces tend to follow which. What comes out is a **predictive model** that, given a sequence, predicts what comes next — "next-token prediction."
- **A useful metaphor: a person who has read a book.** The model doesn't keep a verbatim copy of its training data — like you after reading, it keeps a compressed *interpretation* it can draw on and reproduce. (The architecture is loosely modelled on the brain.) Ask it something and it reconstructs a likely answer rather than looking one up.
- There's a **second training stage** on top of this: humans give feedback on the model's responses to shape its behaviour — making it more helpful, and refusing genuinely harmful requests.
- **Tokens** are the unit of processing — roughly ¾ of a word (1,000 tokens ≈ 750 words). Everything becomes tokens: your instructions, the conversation history, PDFs, images. Tokens are also how usage is priced and how context is measured.
- **Context window** = how much the model can hold in its "working memory" at once, measured in tokens. It has grown from ~3,000 words at ChatGPT's launch to **1,000,000+ tokens (~750,000 words, ~10 books)** today. If your work is mostly text, your life's work might fit inside a single context window.
- **"Context is king" — what you put in front of the model shifts what comes out.** A live example: the word *"Java"* predicts *language / script / developer* — but add a system instruction *"you are a barista taking an order"* and *coffee* becomes the likely next word. Same word, different context, different output. Persona-priming ("you are an expert in X") still helps, but giving the *right information* — your organisation, your preferences, British vs. American spelling — matters more. (Full session on this next time.)
- **Models come in tiers.** Cheaper/faster ones (e.g. Claude Haiku) trade capability for speed and cost; more capable ones (Sonnet, then Opus) reason better but cost more, with a powerful new tier — **Fable / Mythos** — above them. Which tier you pick has real cost consequences (see Practical Notes).

## Energy & Water — the nuance

The concern is legitimate — data centres do use real energy and water — but the headline numbers are badly overblown, and some of the panic is being pushed deliberately.

- **Water:** a single prompt uses roughly **10–25 mL** of water. Charging your phone ≈ 50 prompts; a shower ≈ **17,000 prompts**; a long-haul flight ≈ **millions of prompts**. One bestselling book (*Empire of AI*) overstated AI water use by around **1,000×**. Microsoft's CEO has noted that training a large model uses about as much water as a fast-food restaurant does — once you count the water in the beef.
- **The nuance cuts both ways.** Aggregate demand *is* climbing fast — this is **Jevons paradox**: make a resource cheaper and more available and total demand can rise *more*, not less (like adding traffic lanes and getting more traffic). *Where* a data centre sits matters for local water and power, as does whether the water is consumed or run in a closed loop. And working with **agents** uses far more prompts than chatting does.
- But AI also *reduces* consumption elsewhere — Google's DeepMind cut its data-centre energy use by ~40%. The honest read: real costs, real nuance, not the doomsday story.

## Speech-to-Text — the five-minute win

The fastest productivity unlock in the whole course, and you can set it up in five minutes.

- People type ~40–50 words per minute but speak far faster. Modern speech-to-text is accurate enough to dictate straight into any app, and it handles punctuation and capitalisation for you. Most AI chat tools already have a mic button built in.
- **The real power is briefing an agent.** Instead of carefully typing a prompt, hit record and give a 5–10 minute **"brain dump"** of context and what you're trying to achieve. Typing friction is what stops people briefing agents properly — and these tools pick up intent well, so you don't need to be precise.
- Good starting point: **Whisper Flow** (cloud). For privacy-sensitive work, **Handy** runs fully locally on your computer. (Links in Resources.)

## Assistants vs. Agents

- **Assistant** = a chat tool you converse with, one message at a time. It's linear and you orchestrate it — do this, now change that — babysitting each step.
- **Agent** = a model + tools + an environment. You give it a **goal**, not step-by-step instructions, and it works out how to get there. A helpful analogy: **a model is the engine; an agent is the whole car** — engine plus steering, brakes, and the ability to actually take you somewhere. Same intelligent model, now able to *act* in the world instead of only answering.
- Four properties distinguish an agent:
  - **Goal-directed** — you hand it an outcome ("clean up my bibliography"), not a click-path.
  - **Self-organising** — it finds the context it needs, makes a plan, tracks and ticks off tasks, and picks its own tools (search, creating or deleting files, and more).
  - **Context-aware** — rather than a blank slate each time, its environment can be set up so it starts from a lot of pre-loaded knowledge (next session's focus).
  - **Adaptive** — it works *around* roadblocks rather than stopping at "computer says no." (That same trait is part of why AI safety is hard.)
- **What matters now is often less the model than the "harness"** — the scaffolding of tools and structure built around the model that lets it run on its own. A well-harnessed weaker model can beat a bare stronger one.
- **The role shift: from doer to director.** The celebrated roles used to be the actor, the athlete, the writer — the individual contributor. Working with agents (often several at once, running concurrently) you become the **director / manager**: setting the vision, intervening with feedback, coaching the output toward what you actually want. This makes your **taste and expertise** the valuable thing — the ability to spot the wrong 1% and correct it. And it's **more cognitively demanding, not less**: you're context-switching across agents and constantly evaluating outputs. This is not cognitive offloading.

## The Autonomy Trend (METR)

- The METR graph tracks **how long an agent can work unsupervised** on a task it completes ~50% of the time (measured as how long the same task takes a human). It was flat for years, then went **near-vertical from 2025**.
- Concretely: Opus can work autonomously for around **12 hours**; the top tier (Mythos) for **17–18 hours** — nearly a full day.
- That's the model *alone*. With a well-built **harness**, people already run these systems for **days or weeks** on a single goal. The curve is still climbing, mostly through better harnesses — so expect agents working in the background for us, on both short and long tasks, to become normal.

## Coding Agents & Your Files

- **There's a little agent living on your machine.** Picture dropping a small agent into a folder when you start a session — like placing a character on a spot on a map; it has to be *somewhere* to work. A **folder is a room; the root of your computer is the building.** The shift from a chatbot: it works directly on *your* files where they already sit, rather than on copies you upload to a website. (The heavy AI thinking still runs on the provider's servers — but your files stay on your machine unless you publish or sync them.) This is the mental model most people are slowest to grasp, and the one everything else builds on.
- A **coding agent** (Claude Code, Codex) is an agent that can **write and run code on your computer**. "If it can use a computer, it can do almost anything" — because nearly all knowledge work happens on a computer. Code is the **universal connector**: an agent can write code to read and move files, query the web, or reach any service with an API — Stripe, your email, calendars, or open data sources (e.g. Google's Data Commons, which aggregates 200+ datasets like the World Bank's).
- **Navigating your files is the superpower.** Unlike a chatbot that only sees what you paste in, a coding agent can search across hundreds or thousands of files on your machine almost instantly, find a phrase everywhere it appears, spot patterns, read only what's needed, and reorganise folders itself.
- **File types matter.** Agents work best with **text** — code, config, and **Markdown** (plain text with light symbols: `#` = heading). PDFs, Word, and Excel work but cost more tokens and are **less searchable** — crucially, an agent can't search for text *inside* a PDF (it screenshots or extracts the pages), but it *can* search Markdown. CSV is cheaper than Excel (it's just text). So keeping a text/Markdown version of your PDFs makes agents far more reliable. (How to convert: [`../guides/file-conversion.md`](../guides/file-conversion.md).)
- **Retrieval vs. agentic search — why an agent beats "throw it in a project."** Chat tools (ChatGPT, Claude *projects*, NotebookLM) use **vector retrieval**: they chop your documents into chunks and, when you ask something, pull only the chunks that seem *semantically* nearest — so they may **never read everything you upload**, and "semantically similar" isn't always what's actually relevant. **Agents do agentic search instead** — given a task they search your real files (and the web) and can read *whole* documents. Convert PDFs to text first and the whole document goes into context, not a lossy sample.

## Learned Agency

- The old reflex was "computer says no → I'm stuck." Because agents are intelligent, have web access, and run *on your machine*, a blocker is rarely the end of the road — **ask the agent.** It can explain a concept at any level until it clicks, or do the setup you're stuck on for you.
- A Dragonfly story we tell: one co-founder was stuck with her agent and asked the other how to fix it — whose reply was simply, *"have you asked your agent?"* She hadn't; it sorted it out.
- This matters for the course itself: when something we cover doesn't quite match your setup, don't stop — ask your agent to bridge the gap. Develop **learned agency** rather than learned helplessness.

## Tools We're Using

- We teach **Claude Code** (the **Code** tab in the Claude desktop app) and **OpenAI Codex**. They're functionally equivalent — point either at a folder and it works with your files — and we move between them across the sessions. Codex is often slightly smoother to get started; Claude Code is a touch more developer-flavoured. Either is fine.
- Claude's desktop app also has a **Cowork** mode — simpler and friendlier — but it's finickier and adds friction for what we do, so **it's not what we use in this course.** Stay in the Code tab.
- Claude *chat* (on the web) is separate: it doesn't share a workspace with Code or Cowork. Code and Codex work on files on your computer; chat sends requests to the web.
- Worth having a subscription to at least one; some people keep both (one for work, one for personal). Interface and settings walkthrough: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## The Demo

- Pointed an agent at a folder of PDFs (submissions on AI guidelines) and asked "what's in here?" — it listed and read the files and answered from context, no uploading required.
- Asked it to compare them — "where do they converge, and what do they disagree on?" — and it produced a comparison table, then a synthesised **board-style brief** as an **HTML file** (a web page you can open in your browser), in a few minutes.
- The pattern: **the agent reads, reasons, and produces — you just describe what you want.** It can also *create* files and folders, not only read them: ask it to make a `reports/` folder and move the output there, or to reorganise a messy folder and build an index, and it will.
- One aside worth knowing: Markdown supports **Mermaid**, a way to write diagrams as plain text — so agents are good at generating flowcharts and mind-maps directly, no drawing tool needed.

## Practical Notes

- **Permissions.** Agents can create, move, rename, and delete files, so they run under a permission mode: **ask-for-approval → auto → full-access / bypass.** **Auto is the recommended default** — like autopilot, it asks only for the genuinely risky things and runs the rest. **Plan mode** is useful for bigger projects: the agent writes a plan *without* taking any action, so you can agree the approach first. Bypass / full-access gives free rein — powerful but riskier, including exposure to **prompt injection** (a poisoned web page hijacking your agent). Codex's "approved for me" is a sensible default. (Fuller map of modes: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).)
- **Model choice saves tokens.** On a $20 plan, start with **Sonnet or Haiku**, not Opus, and set effort to "faster" (Codex: "light" reasoning). Agents burn through usage far faster than chat, so this matters more here than in a chatbot.
- **Working with locked-down data.** If your organisation's sensitive data can't touch an agent, do the public-data research in an open or personal environment (or a GitHub-connected setup so nothing sensitive is involved), then bring the results into your locked-down environment for the confidential work.
- **Markdown is the working format** — more token-efficient than PDFs and easier to edit; agents both read and write it well. Convert PDFs where you can.
- **Hallucinations** are much less common now, especially with web access and self-checking (which you can configure) — but still verify important outputs.
- **Safety** — these agents can modify and delete files, so be mindful of which folders you point them at.

## Resources Mentioned

### Tools used in the demo
- **[Claude Code / Cowork / desktop app](https://claude.com/download)** — Anthropic's desktop app. **Code** is the tab we use; Cowork is the simpler mode we don't. Chat (web) is separate.
- **[OpenAI Codex CLI](https://developers.openai.com/codex/cli)** — OpenAI's coding agent; the Codex equivalent of Claude Code. The tool Sam demoed live.
- **[here.now](https://here.now)** — Free hosting that lets an agent publish files/HTML to a live `{slug}.here.now` URL. Mentioned in passing as a way to share what your agent makes; see the Session 3 notes for the full walkthrough.

### Speech-to-text tools
- **[Wispr Flow](https://wisprflow.ai/)** — Cloud-based voice-to-text that pastes polished text wherever your cursor is. Sam's daily driver.
- **[Aqua Voice](https://withaqua.com/)** — Similar cloud dictation tool with app-aware formatting.
- **[Superwhisper](https://superwhisper.com/)** — Mac/Windows/iOS dictation; offers both cloud and **local** models, useful for sensitive/government-adjacent work.
- **[Handy](https://handy.computer/)** — Free, fully-local dictation; runs entirely on your computer. The most privacy-friendly option, and Sam's pick for sensitive work.

### Anthea Roberts' blog posts referenced
- **[Directors, Coaches, and Editors: The Human Role in the Age of AI](https://www.dragonflythinking.com/insights/directors-coaches-and-editors-the-human-role-in-the-age-of-ai)** — The shift from being the actor/athlete/writer to directing, coaching and editing the AI that performs.
- **[Learned Agency vs Learned Helplessness](https://www.dragonflythinking.com/insights/learned-agency-vs-learned-helplessness)** — Why "computer says no" is no longer an acceptable stopping point now that you have an agent.
- **[Learning Agency: Two Processes, Not Just One](https://www.dragonflythinking.com/insights/learning-agency)** — Same AI, two divergent outcomes: amplified agency vs atrophied agency. Choose deliberately.

### Also worth knowing
- **[METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)** — The "agent autonomy is climbing" graph shown on the slide. ~7-month doubling time in how long an AI can work alone.
- **[NotebookLM](https://notebooklm.google/)** — Google's tool for working with very long documents and generating podcast/video overviews. A strong, free **vector-retrieval** tool for research-heavy tasks — complementary to agents (see "retrieval vs. agentic search" above).
- **[Landing.AI](https://landing.ai/)** — Agentic document extraction. The tool Sam uses for pulling structured data out of messy PDFs (e.g. door schedules).
- **[Mike — open-source legal AI](https://mikeoss.com/)** — A free, self-hostable open-source alternative to Harvey/Legora. Bring your own model API key. Useful for the lawyers in the room.
- **[Cursor](https://cursor.com/)** — An AI-native code editor some participants use to see their workspace files with a visible file tree. Mentioned in passing.
- **[Mistral OCR](https://mistral.ai/)** — Sam's recommended PDF→Markdown converter: you pay cents per document, high fidelity, keeps the images.
- **[Andy Masley — AI energy & water blog](https://blog.andymasley.com/)** — Source for the "AI prompts vs charging your phone / driving / flying" comparison on the Energy & Water slide. Argues the AI environmental panic is overstated by ~10× to 1000×.
- **[*Empire of AI* by Karen Hao](https://www.penguinrandomhouse.com/books/743569/empire-of-ai-by-karen-hao/)** — Cited as the book that overstated AI water consumption by a factor of ~1,000. Sam's view: read it, but read the corrections too.

## How the Course Unfolded

| Session | Focus |
|---------|-------|
| **2** | Setting up your agent's environment — default instructions, context files, so it knows who you are and how you work; plus sub-agents |
| **3** | Extending capabilities — skills, sub-agents, and connecting to external tools (MCP, APIs); publishing to the web |
| **4** | Working Well — consolidation: projects set up properly, planning mode, progress logs, and background routines |

## Next Steps

Experiment with Claude Code or Codex as your first hands-on exercise:
- Point it at a folder with some documents
- Ask it to summarize, compare, organize, or convert files
- Get a feel for what it can do — and ask it what it can do that ChatGPT can't

**Homework — put up the guardrails.** Now that an agent lives on your computer, decide
what it must never touch (client files, HR records, personal folders) and make that a
hard rule, not a hope: say *"read `guides/guard-folders/README.md` in the course kit
and set up the folder guard for me"*, then verify in a fresh session by asking the
agent to read something inside a protected folder — the right answer is a refusal.
Five minutes, and it settles the "is this thing safe on my machine?" question for good.
