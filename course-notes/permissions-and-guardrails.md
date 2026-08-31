# Permissions & Guardrails

*Deciding once what your agent may do on its own — and, for the things that genuinely matter, making it impossible rather than merely discouraged.*

The moment you do real work, the agent asks permission constantly: every web fetch, every file edit, every download. One task can throw thirty prompts. Left unmanaged, this trains you to click "yes" without reading, which is strictly worse than deciding once, deliberately.

There are two separate jobs here and they are easy to confuse. **Permission modes** set how much rope the agent has in general. **Guardrails** put specific things permanently out of reach. You want both.

---

## 1 · The modes — how much rope, in general

| Mode | What runs **without** asking | When |
|---|---|---|
| **Manual** *(config name: `default`)* | Reads only | Your first week, or unfamiliar territory |
| **Plan mode** | Reads, searches, explores — but will not edit your files until you approve the plan | Starting anything non-trivial; staying the director |
| **Accept edits** | Reads, file edits, everyday file commands | Iterating on something you're actively watching |
| **Auto** | **Everything**, with an automated safety check reviewing actions as they go | Long tasks, once you trust the direction |
| **Bypass / full access** | Everything, with nothing reviewing it | Rarely, and never with sensitive material around |

Two things the names invite you to get wrong:

- **Plan mode is not a cage.** It won't edit your files, but it *does* read them and run commands to look around. It's "propose before changing", not "sit still". It is the mode for staying the director: iterate on the plan, then **ask it to save the plan as a file** in your workspace before you switch out.
- **Auto is not a slightly-relaxed Accept-edits.** Accept edits frees up *file editing*. Auto lets **everything** run and leans on an automated reviewer instead of you. Genuinely a bigger step; take it deliberately.

**Where to find them:** Claude Code — the mode selector below the chat box, or **Shift+Tab** to cycle. Codex — the approval setting at the bottom, *ask for approval* versus *approve for me*, and typing `plan` triggers plan mode.

**A reasonable default:** **Accept edits** for everyday work, drop into **plan mode** for anything substantial, move up to **auto** once you know what the agent tends to do unsupervised — and note that [routines](routines-and-scheduling.md) need auto, or they stall silently. Auto isn't available on every account or every model; if you don't see it, you're not missing a setting.

## 2 · The allow / ask / never list — the traffic-light exercise

This is the piece that ends the thirty-clicks problem, and it is worth twenty minutes.

**Draw the line yourself, in three colours:**

- 🟢 **Green — allow.** Low risk and **cheap to undo**. If it goes wrong you just ask for it again. Reading files in your workspace, web search, fetching a page, creating and editing files where you're already working.
- 🟡 **Yellow — allow with a condition.** Fine *inside* a boundary, not outside it. The usual shape is *"you may write in this folder; if a task looks like it needs you to touch anything outside it, stop and ask me first — tell me what and why."*
- 🔴 **Red — never.** Deleting things, spending money, installing software, sending anything under your name, anything involving credentials.

**A sane starting split:**

| Fine to always allow | Keep asking |
|---|---|
| Web **search** and **fetching** pages | **Deleting** files or folders |
| **Reading** files in your workspace | Anything touching folders **outside** your workspace |
| **Creating/editing** files in your workspace | **Installing** software |
| Running your installed skills | **Sending** anything — email, posts, publishing |
|  | Anything involving **credentials or keys** |

The pattern: **reversible-and-contained can be automatic; destructive, outward-facing, or out-of-bounds stays a human decision.**

**How to actually set it, without writing config by hand.** Two routes, and the second is better:

1. **In the moment** — when a prompt appears for something you're comfortable with, choose the **"always allow"** option rather than plain "yes". A handful of these and the noise drops sharply.
2. **In one conversation** — hand your agent the whole job:

   > *"I keep getting permission prompts and I'm not a technical user. Here's my comfort level: [describe it]. Propose an allow / ask / never split for me, explain each line in one sentence, and once I'm happy, save it as the settings for this workspace."*

   Have it **explain each line**, and don't accept a config you can't read. `curl` is the one that will surprise you — it shows up constantly, because agents use it to pull text out of documents and pages.

**Reviewing it later:** *"look at what I've been approving repeatedly and add the safe ones to my allowlist — show me the list before you save it."* Note this only works once you have *been* approving things; on a brand-new setup, start from the table above instead.

Give it a **review date**, the same way you would your orientation file. Circumstances change and an allowlist written for one project can be wrong for the next.

## 3 · Guardrails — when asking isn't enough

An instruction in your orientation file does better than people expect. But understand what it is:

- **Layer 1 — an instruction.** *"Never read, list, edit, or run commands that touch `~/Private/`."* This is **asking**. It's like giving someone a key and requesting they stay out of one room. It works most of the time, and most of the time is not the same as always.
- **Layer 2 — a guardrail that blocks.** A small piece of configuration (in Claude these are called **hooks**) that **vetoes the action before it runs**. That's locking the door.

**Do both.** The instruction handles the ordinary case gracefully — the agent understands *why* and works around the boundary sensibly. The guardrail handles the case where something goes wrong.

The kit ships a **ready-made, tested folder guard** you can install in a minute: [`../guides/guard-folders/README.md`](../guides/guard-folders/README.md), with the layered strategy and the reasoning in [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md). It vetoes any tool call touching folders you list — reading, editing, or shell commands.

**Then verify it.** Install it, start a **fresh session**, and ask the agent to read something inside the protected folder. The right answer is a refusal. An unverified guardrail is a belief, not a control.

⚠️ **For genuinely high-stakes material** — health records, anything where no third party can ever see it — the honest current answer is still *don't put it on the machine the agent runs on*. A guardrail protects a folder; the safest folder is one the agent never sees. If you must have both on one machine, **separate operating-system user profiles** for work and personal is the pragmatic move, though it is not an absolute barrier if the account has administrator rights.

## 4 · The practical limit: it drafts, you send

The most useful single boundary anyone sets, and it comes out of how [prompt injection](judgement-and-what-goes-wrong.md) actually works rather than from general caution.

**Give the agent read access to your email and let it draft. Never let it send.** Same for posting, publishing, and anything else that leaves the building under your name. It costs you almost nothing — you press one button — and it breaks the attack chain that everything else in this space is worried about.

Generalise it into a standing line:

```markdown
## Always
- Never send, post or publish anything under my name. Draft it and show me — I press send.
- Before anything irreversible — deleting files, overwriting a document, spending money —
  stop and ask, even if I've already approved something similar.
- Never write passwords, API keys or access tokens into a file. If I paste one, tell me
  where it should live instead.
```

Those three lines are the safety floor from [Snippets for your orientation file](agents-md-snippets.md). If you paste nothing else, paste those.

## Quick fixes

- **Agent seems frozen mid-task?** Look for a **permission prompt waiting quietly** — this is the commonest cause, and it is the failure mode that kills unattended routines.
- **Everything suddenly feels dumber?** Check `/context`. You're probably deep into a compacted session; write a handover and restart.
- **Not sure what your setup even is?** Ask: *"show me my current mode, model, and what's in my allowlist."* It can read its own settings.

Full interface reference, including where the context meter lives in each tool: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## Try this

> I want to sort out permissions properly. Ask me what I'm comfortable with, then propose an
> allow / ask / never split — one sentence of plain English per line, no config I can't read.
> Once I've agreed it, save it. Then ask me whether there's anything on this machine you
> should never open, and if there is, install the folder guard and prove it works in a fresh
> session.
