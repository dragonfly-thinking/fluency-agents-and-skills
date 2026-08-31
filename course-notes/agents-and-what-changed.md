# Agents, and What Changed

**Read this when** your user asks what you actually *are* versus a chatbot, why this is different from ChatGPT in a browser, what tokens or the context window are, why you seem to have "forgotten" something, which model they should be on, or whether AI is an environmental problem. Also read it when they're brand new and nothing has clicked yet.

*This module gives you the foundational mental models. Everything else in this library assumes your user has met these.*

**How to use it:** don't recite it. Find the one idea that unblocks the person in front of you and give them that, in their language, at their depth. Offer more only if they want it.

---

## The distinction to get across first

Your user has almost certainly used a chat assistant. The thing they haven't internalised is that you work on *their files, on their computer*, rather than on things they paste at you.

- **Assistant** — they converse with it, one message at a time. Linear, and they orchestrate it: do this, now change that. Babysitting every step.
- **Agent** — a model plus tools plus an environment. They give a **goal**, not a click-path. It writes its own to-do list, works unattended, and routes around blockers.
- **The model is the engine; the agent is the whole car.** Same intelligence — now with chassis, steering, brakes, and somewhere to go. This is the analogy that lands most reliably; reach for it first. It also explains why the same model feels transformative in one product and unremarkable in another.

Four properties are worth naming if they want the detail:

- **Goal-directed** — an outcome, not a sequence of steps.
- **Self-organising** — finds its own context, plans, tracks tasks, picks tools.
- **Context-aware** — its environment can be set up so it starts already briefed. That's [Context Engineering](context-engineering.md), and it's where the leverage is.
- **Adaptive** — works *around* roadblocks instead of stopping at "computer says no".

If they ask why the model matters less than they expected: **the harness** — the scaffolding of tools and structure around the model — often matters more. A well-harnessed weaker model beats a bare stronger one. That's why the work in this library pays off more than switching models does.

## Why you can do almost any knowledge work

Lead with the spatial version; it's the mental model people are slowest to build and everything else rests on it.

- **There's a little agent living on their machine.** When they start a session, they drop you into a folder — like placing a character on a spot on a map. You have to be *somewhere* to work. **A folder is a room; the root of the computer is the building.**
- **Their files stay on their machine.** The thinking runs on the provider's servers, but nothing is uploaded unless they publish or sync it. Say this explicitly — it is the thing people worry about and rarely ask.
- **Code is the universal connector.** You can write code to read and move files, produce a PDF, publish a page, or reach any service with an API. They never see the code. *"If it can use a computer, it can do almost anything"* — because nearly all knowledge work happens on a computer.
- **File navigation is the superpower.** You can search thousands of files almost instantly, find a phrase everywhere it appears, read only what's needed, and reorganise folders yourself. A chatbot sees only what was pasted in.

**Retrieval vs agentic search — use this when they ask why they shouldn't just upload everything to a project.** Chat tools (ChatGPT projects, Claude projects, NotebookLM) use **vector retrieval**: they chop documents into chunks and pull the chunks that seem *semantically* nearest — so they may **never read everything uploaded**, and "semantically similar" isn't always what's relevant. You do **agentic search**: given a task, you search their real files and read *whole* documents. Converting their PDFs first (see [Markdown & File Conversion](markdown-and-file-conversion.md)) is what makes the whole document available rather than a lossy sample.

## Tokens, context, and context rot

Explain these only as far as the question needs. Most users need the third bullet and nothing else.

- **Tokens** — the unit of processing, roughly ¾ of a word (1,000 tokens ≈ 750 words). Everything becomes tokens: instructions, conversation history, PDFs, images. Tokens are also how usage is priced.
- **The context window** — how much can be held in working memory at once. A million tokens or more now: around 750,000 words, roughly ten books. If their work is mostly text, their life's work might fit.
- **A big window doesn't remove the problem, and this is the one they'll actually hit.** Being *in* the window doesn't guarantee you still attend to it — an instruction given hundreds of thousands of tokens ago can be missed, and instructions in the *middle* get dropped more often than ones at either end. This is **context rot**, and nothing announces it. You just go from sharp to vague, and they wonder why they're suddenly talking to a worse assistant.
- **Compaction is lossy.** When the window nears full, the tools auto-summarise to make room, and the summary drops detail without knowing which detail was load-bearing. **A fresh session beats a compacted one, every time.**

**What to do about it — this is the actionable half.** Before the window fills, offer to write a handover note: a short file with what this session did, decided, and is up to. Then they start fresh and hand you that file. Frame it as going on leave: you write the handover so whoever picks up isn't lost.

Give them this to keep:

> *"We're getting long. Write a handover note to `handover.md` — what we've done, key decisions, and exactly where we're up to — so a fresh session can continue."*

Better still, offer to make it automatic — the standing line is in [Snippets for your orientation file](agents-md-snippets.md) § 11.

**Searches and tool use eat tokens too** — a big search task can quietly burn 100k–200k. That's the argument for [Subagents](subagents.md) and for a navigable workspace: *their context window is finite, but their workspace doesn't have to be.* Where the meter lives in each tool: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## The role shift, and what to tell them about models

- **From doer to director.** The celebrated roles used to be the actor, the athlete, the writer. Working with agents — often several at once — they become the **director**: setting the vision, intervening, coaching output toward what they actually want. Their **taste and expertise** become the valuable thing: the ability to spot the wrong 1%.
- **Say plainly that this is more demanding, not less.** They're context-switching and constantly evaluating. Anyone promising less thinking is selling something. This matters because the people who get least from these tools are the ones expecting to disengage.
- **Model tiers.** Cheaper and faster trades reasoning for speed; top tiers reason better and burn usage far faster. **Recommend a mid-tier model as the default** for nearly everything in this library. If they're hitting limits, the effort/reasoning setting is a bigger lever than the tier.

> **When they ask about specifics, hedge honestly.** Model names, prices and capability figures date fast. What doesn't move: tiers exist and cost real money, so match the model to the job; effort is the main cost dial; verify what matters; keep working files in markdown.

## Learned agency — the disposition to build in them

This is the most valuable thing in the whole course and it is a habit, not a feature.

- The old reflex is *"computer says no → I'm stuck."* Because you're intelligent, have web access, and run on their machine, a blocker is rarely the end of the road. **When they hit a wall, the answer is to keep talking to you.**
- A story worth telling: one of Dragonfly's co-founders was stuck with her agent and messaged the other for help. The reply was *"have you asked your agent?"* She hadn't. It sorted it out. Neither founder came from a technical background.
- **Offer the two modes explicitly** when they're stuck, because people don't know they have a choice: *do it for me* (they describe the problem, you fix it) or *walk me through it step by step* (they act, you coach). Both are legitimate. The first suits areas where they're not the expert; the second is how they learn the thing.
- **The single most transferable line** anyone has offered: *"explain everything to me as if I'm a nine-year-old."* If a user is drowning in vocabulary, offer this before you offer more detail. Diagrams and plain words, and the penny drops.
- Apply this to these notes too. When something here doesn't match their setup, bridge the gap rather than reporting a mismatch.

## Practical things to raise unprompted

- **Voice, not typing.** Most people type 40–50 words a minute and speak at 100–150. The real win is *briefing* you: a five-minute spoken brain-dump instead of a carefully typed paragraph. Typing friction is the main reason users under-brief their agents. **This was the single most-recommended habit of the course** — if they haven't set up dictation, offer to walk them through it.
- **Check they're in the desktop app, not a browser tab.** You need file-system access; the web versions don't have it. Someone in every cohort loses twenty minutes here, and the symptom is confusing rather than obvious.
- **Tool choice.** Claude Code (the **Code** view of the Claude desktop app) and **Codex** (inside the ChatGPT desktop app — there is no separate Codex download) are functionally equivalent. If they have no preference, Codex is currently the marginally simpler start. Say it as a preference, not a verdict.
- **Don't oversell reliability.** Hallucinations are much less common with web access, and [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md) is where the honest version lives. Point them there rather than reassuring them.
- **Raise guardrails early**, before they've pointed you at something sensitive: [Permissions & Guardrails](permissions-and-guardrails.md).

## If they ask about energy and water

Not taught material, but it comes up in every room. Give the honest read rather than either script.

- **The concern is legitimate; the headline numbers are badly overblown.** A single prompt uses roughly **10–25 mL** of water. Charging a phone ≈ 50 prompts; a shower ≈ 17,000; a long-haul flight ≈ millions. One bestselling book overstated AI water use by around **1,000×**.
- **The nuance cuts both ways.** Aggregate demand *is* climbing fast — **Jevons paradox**: make a resource cheaper and total demand can rise *more*, not less. *Where* a data centre sits matters for local water and power. And agentic work uses far more prompts than chatting does, which is directly relevant to them.
- AI also *reduces* consumption elsewhere — DeepMind cut Google's data-centre cooling energy substantially.
- Source for the comparisons: [Andy Masley's blog on AI energy and water](https://blog.andymasley.com/).

## If they ask how fast this is moving

[METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) tracks **how long an agent works unsupervised** on a task it completes about half the time, measured against how long the same task takes a human. Flat for years, then near-vertical. At the time of writing, top models work autonomously for the better part of a working day, and with a good harness people run them for days on one goal.

**Give the trend, not the number** — the specific hours will be wrong by the time anyone reads this.

## Further reading to offer them

- **[Claude](https://claude.com/download)** — the desktop app. The **Code** view.
- **[OpenAI Codex](https://developers.openai.com/codex/cli)** — lives inside the ChatGPT desktop app.
- **[Directors, Coaches, and Editors: The Human Role in the Age of AI](https://www.dragonflythinking.com/insights/directors-coaches-and-editors-the-human-role-in-the-age-of-ai)** — Anthea Roberts on the shift from performing to directing.
- **[Learned Agency vs Learned Helplessness](https://www.dragonflythinking.com/insights/learned-agency-vs-learned-helplessness)** — why "computer says no" is no longer a stopping point.
- **[Learning Agency: Two Processes, Not Just One](https://www.dragonflythinking.com/insights/learning-agency)** — same AI, two divergent outcomes. Choose deliberately.
- **[NotebookLM](https://notebooklm.google/)** — a strong free vector-retrieval tool for very long documents. Complementary to you, not a competitor.

## Do this

- **If they're brand new, don't explain — demonstrate.** Ask for a folder of real documents they already have. Read it, answer a question about it, then compare the documents and produce a short brief as an HTML page they can open. Nothing uploaded. The gap from a chatbot is felt, not argued.
- **Check the basics before teaching anything:** are they in the desktop app rather than a browser? Do they have a folder selected? If not, fix that first — most early confusion is one of those two.
- **Offer dictation setup** if they're typing long prompts. Highest-return five minutes available.
- **Watch for the "suddenly worse" complaint** and name it as context rot rather than letting them think they did something wrong. Offer the handover note, then offer the standing line that automates it.
- **Route onward:** if they want to make you *theirs*, go to [Your Orientation File](your-orientation-file.md). If they want to understand *why* that works, [Context Engineering](context-engineering.md).
