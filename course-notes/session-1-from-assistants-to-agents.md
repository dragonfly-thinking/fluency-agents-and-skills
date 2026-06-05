# AI Fluency Session 1 — Key Points

**Session 1: From Assistants to Agents**

This session introduced the shift from chat-based AI assistants to AI agents — tools that can take action on your computer, not just respond to questions. We covered how large language models work (tokens, context windows, why "context is king"), what makes coding agents different (they can use your computer to do almost anything), and got hands-on with Claude Desktop or OpenAI Codex. The key takeaway: you don't need to know how to code — the agent handles that — but you do need to develop taste and judgment as a "director" of AI work.

---

## The AI Revolution

- We're witnessing the biggest shift since the personal computer — possibly bigger
- AI lets us externalize *cognitive* work the way machines/fossil fuels let us externalize *physical* work
- We don't fully understand what these systems can do yet — researchers are still probing their capabilities
- This is the age of the **10X knowledge worker**: with AI, one person can be an order of magnitude more effective than their peers
- You can't understand AI just by reading about it — you have to be hands-on

## How Large Language Models Work

- LLMs are built by compressing massive amounts of data (internet, books, documents) and identifying patterns
- Think of it like DNA — compressed information that can be "expanded" back into something very close to the original
- **Tokens** are the unit of measurement — roughly ¾ of a word
- **Context window** = how much the model can hold in its "head" at once
  - ChatGPT launched with ~3,000 words
  - Current models handle ~1 million tokens (~10 books worth)
- **"Context is king"** — what you provide the model matters more than which model you use
- The "You are an expert in X" framing shifts the probability distribution of outputs — less important than it used to be, but setting context (your organization, preferences, spelling conventions) still matters

## Assistants vs. Agents

- **Assistant** = chat-based tool you converse with
- **Agent** = model + tools — it can take actions, not just respond
- **Coding agent** = agent with access to a computer/terminal
  - Can read/write files, navigate folders, execute commands
  - "If it can code, it can use a computer. If it can use a computer, it can do anything."
  - You don't need to know how to code — the agent handles that
- Code is the **universal connector** — agents can write code to query Stripe, Outlook, calendars, APIs, etc.

## Tools We're Using

- **Claude Desktop (Cowork mode)** or **OpenAI Codex** — functionally equivalent
- Both let you point an agent at a folder and have it work with your files
- Claude Cowork = slightly more guardrails / safer defaults
- Claude Code = more powerful, fewer guardrails
- Worth having subscriptions to both (one for work, one for personal)

## The Demo

- Pointed Codex at a folder containing 4 PDF submissions on AI guidelines
- Asked it to summarize what's in each document
- Asked it to compare: "Where do they converge and what do they disagree on?"
- Agent read all PDFs, produced a comparison table in Markdown
- Converted the output to HTML for web viewing
- Key insight: the agent reads, reasons, and produces — you just describe what you want

## Practical Notes

- **Safety**: These agents can modify/delete files — be mindful of what folders you give them access to
- **Hallucinations**: Much less common now, especially with internet access and self-checking (which is something you can configure your agents for) — but still verify important outputs
- **Markdown**: Recommended format for working with AI (more token-efficient than PDFs, easier to edit)

## Resources Mentioned

### Tools used in the demo
- **[Claude Desktop / Cowork / Claude Code](https://claude.com/download)** — Anthropic's desktop app. Cowork is the friendlier mode; Code is the more powerful tab.
- **[OpenAI Codex CLI](https://developers.openai.com/codex/cli)** — OpenAI's coding agent; the Codex equivalent of Claude Code. The tool Sam demoed live.
- **[here.now](https://here.now)** — Free hosting that lets an agent publish files/HTML to a live `{slug}.here.now` URL. Mentioned in passing as a way to share what your agent makes; see the Session 3 notes for the full walkthrough.

### Speech-to-text tools
- **[Wispr Flow](https://wisprflow.ai/)** — Cloud-based voice-to-text that pastes polished text wherever your cursor is. Sam's daily driver.
- **[Aqua Voice](https://withaqua.com/)** — Similar cloud dictation tool with app-aware formatting.
- **[Superwhisper](https://superwhisper.com/)** — Mac/Windows/iOS dictation; offers both cloud and **local** models, making it the better pick for sensitive/government-adjacent work.
- **[Happy](https://happy.engineer/)** — Free, fully-local dictation. The most privacy-friendly option; what Sam was using on screen during the session.

### Anthea Roberts' blog posts referenced
- **[Directors, Coaches, and Editors: The Human Role in the Age of AI](https://www.dragonflythinking.com/insights/directors-coaches-and-editors-the-human-role-in-the-age-of-ai)** — The shift from being the actor/athlete/writer to directing, coaching and editing the AI that performs.
- **[Learned Agency vs Learned Helplessness](https://www.dragonflythinking.com/insights/learned-agency-vs-learned-helplessness)** — Why "computer says no" is no longer an acceptable stopping point now that you have an agent.
- **[Learning Agency: Two Processes, Not Just One](https://www.dragonflythinking.com/insights/learning-agency)** — Same AI, two divergent outcomes: amplified agency vs atrophied agency. Choose deliberately.

### Also worth knowing
- **[METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)** — The "agent autonomy is climbing" graph shown on the slide. ~7-month doubling time in how long an AI can work alone.
- **[NotebookLM](https://notebooklm.google/)** — Google's tool for working with very long documents and generating podcast/video overviews. Mentioned by a participant as a tool they already use.
- **[Landing.AI](https://landing.ai/)** — Agentic document extraction. The tool Sam uses for pulling structured data out of messy PDFs (e.g. door schedules).
- **[Mike — open-source legal AI](https://mikeoss.com/)** — A free, self-hostable open-source alternative to Harvey/Legora. Bring your own model API key. Useful for the lawyers in the room.
- **[Cursor](https://cursor.com/)** — An AI-native code editor some participants use to see their workspace files with a visible file tree. Mentioned in passing.
- **[Mistral OCR](https://mistral.ai/)** — Sam's recommended PDF→Markdown converter: you pay cents per document, high fidelity, keeps the images.
- **[Andy Masley — AI energy & water blog](https://blog.andymasley.com/)** — Source for the "AI prompts vs charging your phone / driving / flying" comparison on the Energy & Water slide. Argues the AI environmental panic is overstated by ~10× to 1000×.
- **[*Empire of AI* by Karen Hao](https://www.penguinrandomhouse.com/books/743569/empire-of-ai-by-karen-hao/)** — Cited as the book that overstated AI water consumption by a factor of ~1,000. Sam's view: read it, but read the corrections too.

## How the Course Unfolded

| Session | Focus |
|---------|-------|
| **2** | Setting up your agent's environment — default instructions, context files, so it knows who you are and how you work |
| **3** | Extending capabilities — skills, sub-agents, and connecting to external tools (MCP, APIs); publishing to the web |
| **4** | Working Well — consolidation: projects set up properly, planning mode, progress logs, and background routines |

## Next Steps

Experiment with Claude Cowork or Codex as your first hands-on exercise:
- Point it at a folder with some documents
- Ask it to summarize, compare, organize, or convert files
- Get a feel for what it can do
