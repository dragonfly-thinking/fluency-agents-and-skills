# The Interface & Settings — modes, the context meter, and what to always-allow

**Who this is for:** you're using Claude Code or Codex and keep wondering three
things — *what mode should I be in?*, *how full is the context window?*, and *do I
really have to click "approve" thirty times?* This page answers all three. Where
something is a command, just type it into the chat.

---

## 1. Permission modes — how much rope to give the agent

Both tools have a mode selector (bottom of the chat in Claude Code; shift-tab /
settings in Codex). The ladder, from cautious to trusting:

| Mode | What it means | When |
|---|---|---|
| **Plan mode** | The agent *cannot act at all* — it discusses, plans, and asks before switching to a mode where it can | Starting anything non-trivial; staying the director |
| **Ask each time** | Approves every action with you | Your first week, or unfamiliar territory |
| **Accept edits / Auto** | File edits (and pre-approved actions) run without asking; unusual actions still prompt | The sensible everyday setting once trust is built |
| **Bypass / full access** | Nothing prompts | Rarely. Only in a workspace where nothing can be damaged — and never on folders with sensitive material (see [`folder-guardrails.md`](folder-guardrails.md)) |

Course recommendation: live in **auto** for day-to-day work, drop into **plan
mode** at the start of anything substantial, and save the plan as a file.

## 2. The context meter — knowing how full the window is

The context window (the agent's working memory for this session) is finite; when
it fills, the tool auto-summarises and fine detail gets lossy. How to check it:

**Claude Code** — type **`/context`**. You get a breakdown of what's eating the
window (system prompt, your CLAUDE.md, skills, conversation). Claude also has a
configurable **status line** — run **`/statusline`** and ask it to show remaining
context permanently — and it warns you as it approaches auto-compact. In the VS
Code extension, use the same `/context` command in the session panel.

**Codex** — type **`/status`** for the session's context and token usage, and
**`/statusline`** to add a persistent footer showing context as you work.

**When the meter runs low**, don't push through — capture and restart: ask the agent
to *write a handover note* (a short file: what this session did, decided, and is up
to — there's a copy-able prompt in the session-2 course notes), then start a fresh
session and point it at that file. Fresh context beats compressed context.

## 3. Always-allow — ending the thirty-clicks problem

Approval prompts exist for good reasons, but re-approving *web search* for the
fifteenth time teaches you to click yes without reading — which is worse than
allowing it once, deliberately.

**The easy way:** when a prompt appears for something you're comfortable with,
choose the **"always allow"**-style option instead of plain "yes" — the tool
remembers. Do that a handful of times and the noise drops sharply.

**The systematic way:** tell your agent —

> *"I'm getting too many permission prompts. Look at what I've been approving
> repeatedly and add the safe ones to my allowlist — show me the list before you
> save it."*

**A sane default for what belongs on each side:**

| Fine to always allow | Keep asking |
|---|---|
| Web **search** and **fetching** pages | **Deleting** files or folders |
| **Reading** files in your workspace | Anything touching folders **outside** your workspace |
| **Creating/editing** files in your workspace | **Installing** software |
| Running the kit's skills | **Sending** anything (email, posts, publishing) |
|  | Anything involving **credentials or keys** |

The pattern: reversible-and-contained can be automatic; destructive, outward-facing,
or out-of-bounds should stay a human decision.

## 4. Quick fixes for the classic snags

- **Skill not showing when you type `/`?** Usually installed into a project's
  `.claude/skills/` instead of the global `~/.claude/skills/` — ask your agent to
  check and move them — then **start a new session** (new skills/agents load at
  session start).
- **Agent seems frozen mid-task?** Look for a **permission prompt waiting
  quietly** — routines and long tasks especially.
- **Everything suddenly feels dumber?** Check `/context` — you're probably deep
  into a compacted session. Handoff and restart.
- **Not sure what your current setup even is?** Ask: *"show me my current mode,
  model, and what's in my allowlist."* The agent can read its own settings.
