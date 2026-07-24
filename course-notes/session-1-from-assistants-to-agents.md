# From Assistants to Agents

*Part 1 of the AI Fluency course notes.*

The shift from chat-based AI assistants to AI **agents** — tools that take action on your computer, not just answer questions — is the foundation everything else builds on. This note covers why the moment matters, how large language models actually work (tokens, context windows, why "context is king"), the nuance in the energy/water debate, and what makes a *coding agent* different from a chatbot. The through-line: you don't need to know how to code — the agent handles that — but you do need taste and judgment as the **director** of the work.

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
- **"Context is king" — what you put in front of the model shifts what comes out.** A live example: the word *"Java"* predicts *language / script / developer* — but add a system instruction *"you are a barista taking an order"* and *coffee* becomes the likely next word. Same word, different context, different output. Persona-priming ("you are an expert in X") still helps, but giving the *right information* — your organisation, your preferences, British vs. American spelling — matters more. (See [Setting Up Your Agent's Workspace](session-2-setting-up-your-agentic-environment.md).)
- **Models come in tiers.** Cheaper/faster ones (e.g. Claude Haiku) trade capability for speed and cost; more capable ones (Sonnet, then Opus) reason better but cost more, with a powerful new tier — **Fable / Mythos** — above them. The gap between tiers narrows with each release, so treat the ladder as directional, not fixed. Which tier you pick has real cost consequences (see Practical Notes).

> **A note on specifics vs. principles.** The model names, prices, and the exact autonomy figures in these notes will date fast — there were several new frontier models in the months around this course, and each one reshuffles the picture. Don't lean on the specifics; lean on what doesn't move: tiers exist and cost real money, so **match the model to the job**; **effort / reasoning level is your main cost dial** — turn it down for easy work; **verify what matters** and **red-team important plans with fresh context**; and keep your working files in **markdown**. Those hold whichever model you're on.

## Energy & Water — the nuance

The concern is legitimate — data centres do use real energy and water — but the headline numbers are badly overblown, and some of the panic is being pushed deliberately.

- **Water:** a single prompt uses roughly **10–25 mL** of water. Charging your phone ≈ 50 prompts; a shower ≈ **17,000 prompts**; a long-haul flight ≈ **millions of prompts**. One bestselling book (*Empire of AI*) overstated AI water use by around **1,000×**. Microsoft's CEO has noted that training a large model uses about as much water as a fast-food restaurant does — once you count the water in the beef.
- **The nuance cuts both ways.** Aggregate demand *is* climbing fast — this is **Jevons paradox**: make a resource cheaper and more available and total demand can rise *more*, not less (like adding traffic lanes and getting more traffic). *Where* a data centre sits matters for local water and power, as does whether the water is consumed or run in a closed loop. And working with **agents** uses far more prompts than chatting does.
- But AI also *reduces* consumption elsewhere — Google's DeepMind cut its data-centre energy use by ~40%. The honest read: real costs, real nuance, not the doomsday story.

## Speech-to-Text — the five-minute win

One of the fastest productivity unlocks in the whole toolkit — and you can set it up in five minutes.

- People type ~40–50 words per minute but speak far faster. Modern speech-to-text is accurate enough to dictate straight into any app, and it handles punctuation and capitalisation for you. Most AI chat tools already have a mic button built in.
- **The real power is briefing an agent.** Instead of carefully typing a prompt, hit record and give a 5–10 minute **"brain dump"** of context and what you're trying to achieve. Typing friction is what stops people briefing agents properly — and these tools pick up intent well, so you don't need to be precise.
- Good starting point: **Whisper Flow** (cloud). For privacy-sensitive work, **Handy** runs fully locally on your computer. (Links in Resources.)

## Assistants vs. Agents

- **Assistant** = a chat tool you converse with, one message at a time. It's linear and you orchestrate it — do this, now change that — babysitting each step.
- **Agent** = a model + tools + an environment. You give it a **goal**, not step-by-step instructions, and it works out how to get there. A helpful analogy: **a model is the engine; an agent is the whole car** — engine plus steering, brakes, and the ability to actually take you somewhere. Same intelligent model, now able to *act* in the world instead of only answering.
- Four properties distinguish an agent:
  - **Goal-directed** — you hand it an outcome ("clean up my bibliography"), not a click-path.
  - **Self-organising** — it finds the context it needs, makes a plan, tracks and ticks off tasks, and picks its own tools (search, creating or deleting files, and more).
  - **Context-aware** — rather than a blank slate each time, its environment can be set up so it starts from a lot of pre-loaded knowledge (see [Setting Up Your Agent's Workspace](session-2-setting-up-your-agentic-environment.md)).
  - **Adaptive** — it works *around* roadblocks rather than stopping at "computer says no." (That same trait is part of why AI safety is hard.)
- **What matters now is often less the model than the "harness"** — the scaffolding of tools and structure built around the model that lets it run on its own. A well-harnessed weaker model can beat a bare stronger one.
- **The role shift: from doer to director.** The celebrated roles used to be the actor, the athlete, the writer — the individual contributor. Working with agents (often several at once, running concurrently) you become the **director / manager**: setting the vision, intervening with feedback, coaching the output toward what you actually want. This makes your **taste and expertise** the valuable thing — the ability to spot the wrong 1% and correct it. And it's **more cognitively demanding, not less**: you're context-switching across agents and constantly evaluating outputs. This is not cognitive offloading.

## The Autonomy Trend (METR)

- The METR graph tracks **how long an agent can work unsupervised** on a task it completes ~50% of the time (measured as how long the same task takes a human). It was flat for years, then went **near-vertical from 2025**.
- Concretely (at the time of writing): Opus can work autonomously for around **12 hours**; the top tier (Mythos) for **17–18 hours** — nearly a full day. The exact hours climb with each release — the point is the trend, not the number.
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
- This applies to these notes too: when something here doesn't quite match your setup, don't stop — ask your agent to bridge the gap. Develop **learned agency** rather than learned helplessness.

## Tools

- These notes use **Claude Code** (the **Code** tab in the Claude desktop app) and **OpenAI Codex**. They're functionally equivalent — point either at a folder and it works with your files. Codex is often slightly smoother to get started; Claude Code is a touch more developer-flavoured. Either is fine.
- Claude's desktop app also has a **Cowork** mode — simpler and friendlier — but it's finickier and adds friction, so **it's not the mode used here.** Stay in the Code tab.
- Claude *chat* (on the web) is separate: it doesn't share a workspace with Code or Cowork. Code and Codex work on files on your computer; chat sends requests to the web.
- Worth having a subscription to at least one; some people keep both (one for work, one for personal). Interface and settings walkthrough: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## A First Task — Point It at a Folder

The clearest way to feel the difference from a chatbot: put some documents in a folder, point an agent at it, and ask.

- **Ask "what's in here?"** — it lists and reads the files and answers from context, with nothing to upload.
- **Ask it to compare** — "where do these converge, and where do they disagree?" — and it can produce a comparison table, then a synthesised **board-style brief** as an **HTML file** (a web page you open in your browser), in minutes.
- The pattern is **read → reason → produce**: you describe what you want, and the agent does the reading and the making. It can *create* files and folders too, not just read them — ask it to make a `reports/` folder and move the output there, or to reorganise a messy folder and build an index.
- Markdown supports **Mermaid**, a way to write diagrams as plain text — so agents generate flowcharts and mind-maps directly, no drawing tool needed.

## Practical Notes

- **Permissions.** Agents can create, move, rename, and delete files, so they run under a permission mode: **ask-for-approval → auto → full-access / bypass.** **Auto is the recommended default** — like autopilot, it asks only for the genuinely risky things and runs the rest. **Plan mode** is useful for bigger projects: the agent writes a plan *without* taking any action, so you can agree the approach first. Bypass / full-access gives free rein — powerful but riskier, including exposure to **prompt injection** (a poisoned web page hijacking your agent). Codex's "approved for me" is a sensible default. (Fuller map of modes: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).)
- **Model choice saves tokens.** On a $20 plan, start with **Sonnet or Haiku**, not Opus, and set effort to "faster" (Codex: "light" reasoning). Agents burn through usage far faster than chat, so this matters more here than in a chatbot.
- **Working with locked-down data.** If your organisation's sensitive data can't touch an agent, do the public-data research in an open or personal environment (or a GitHub-connected setup so nothing sensitive is involved), then bring the results into your locked-down environment for the confidential work.
- **Markdown is the working format** — more token-efficient than PDFs and easier to edit; agents both read and write it well. Convert PDFs where you can.
- **Hallucinations** are much less common now, especially with web access and self-checking (which you can configure) — but still verify important outputs.
- **Safety** — these agents can modify and delete files, so be mindful of which folders you point them at.

## Resources

### Agent tools
- **[Claude Code / Cowork / desktop app](https://claude.com/download)** — Anthropic's desktop app. **Code** is the tab to use; Cowork is the simpler mode to skip. Chat (web) is separate.
- **[OpenAI Codex CLI](https://developers.openai.com/codex/cli)** — OpenAI's coding agent; the Codex equivalent of Claude Code.
- **[here.now](https://here.now)** — Free hosting that lets an agent publish files/HTML to a live `{slug}.here.now` URL. Mentioned in passing as a way to share what your agent makes; see [Extending Your Agent](session-3-extending-your-agent.md) for the full walkthrough.

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
- **[METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)** — The source behind the autonomy trend above: ~7-month doubling time in how long an AI can work alone.
- **[NotebookLM](https://notebooklm.google/)** — Google's tool for working with very long documents and generating podcast/video overviews. A strong, free **vector-retrieval** tool for research-heavy tasks — complementary to agents (see "retrieval vs. agentic search" above).
- **[Landing.AI](https://landing.ai/)** — Agentic document extraction. The tool Sam uses for pulling structured data out of messy PDFs (e.g. door schedules).
- **[Mike — open-source legal AI](https://mikeoss.com/)** — A free, self-hostable open-source alternative to Harvey/Legora. Bring your own model API key. Useful if you work in law.
- **[Cursor](https://cursor.com/)** — An AI-native code editor that shows your workspace files with a visible file tree.
- **[Mistral OCR](https://mistral.ai/)** — Sam's recommended PDF→Markdown converter: you pay cents per document, high fidelity, keeps the images.
- **[Andy Masley — AI energy & water blog](https://blog.andymasley.com/)** — Source for the "AI prompts vs charging your phone / driving / flying" comparison in the Energy & Water section above. Argues the AI environmental panic is overstated by ~10× to 1000×.
- **[*Empire of AI* by Karen Hao](https://www.penguinrandomhouse.com/books/743569/empire-of-ai-by-karen-hao/)** — Cited as the book that overstated AI water consumption by a factor of ~1,000. Sam's view: read it, but read the corrections too.

## Put This Into Action

- Point an agent at a folder of real documents and ask it to summarise, compare, organise, or convert them — the fastest way to feel what it can do that a chatbot can't.
- Set up speech-to-text and brief your next task by voice instead of typing it.
- Once an agent lives on your computer, decide what it must never touch (client files, HR records, personal folders) and make that a hard rule, not a hope — set a guardrail that actually blocks access, then verify by asking a fresh agent to read something inside a protected folder (the right answer is a refusal). Setup: [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md).
- When you're ready to make the agent truly *yours*, move on to [Setting Up Your Agent's Workspace](session-2-setting-up-your-agentic-environment.md).
