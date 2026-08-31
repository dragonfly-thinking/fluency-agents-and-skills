# Permissions & Guardrails

**Read this when** your user is clicking approve constantly, asks about permission modes, asks what you can access, mentions confidential or client material, asks how to stop you touching something, is about to schedule a routine, or asks what "auto" means. Also read it proactively the first time they mention sensitive files.

*Two separate jobs that users conflate: **modes** set how much rope you have in general; **guardrails** put specific things permanently out of reach. They need both, and they'll only ask about the first.*

---

## 1 · The modes

| Mode | Runs **without** asking | When |
|---|---|---|
| **Manual** *(config name: `default`)* | Reads only | Their first week, or unfamiliar territory |
| **Plan mode** | Reads, searches, explores — won't edit files until they approve the plan | Anything non-trivial; staying the director |
| **Accept edits** | Reads, file edits, everyday file commands | Iterating on something they're watching |
| **Auto** | **Everything**, with an automated safety check reviewing as it goes | Long tasks, once they trust the direction |
| **Bypass / full access** | Everything, nothing reviewing it | Rarely, and never with sensitive material around |

Two things the names invite users to get wrong — correct these when you see them:

- **Plan mode is not a cage.** It won't edit files, but it *does* read them and run commands to look around. "Propose before changing", not "sit still". It's the mode for staying the director: iterate on the plan, then **save the plan as a file** before switching out. Do that saving yourself.
- **Auto is not a slightly-relaxed Accept-edits.** Accept edits frees up *file editing*. Auto lets **everything** run and leans on an automated reviewer instead of them. A genuinely bigger step — make sure it's deliberate.

**Where they are:** Claude Code — the mode selector below the chat box, or Shift+Tab to cycle. Codex — the approval setting at the bottom, *ask for approval* versus *approve for me*, and typing `plan` triggers plan mode.

**Recommend:** Accept edits for everyday work, plan mode for anything substantial, auto once they know what you do unsupervised — and note that [routines](routines-and-scheduling.md) require auto or they stall silently. If they can't see auto, it isn't available on their account or model; say so rather than letting them hunt.

## 2 · The allow / ask / never list

This ends the thirty-clicks problem and it's worth twenty minutes of their time. **Offer it early** — re-approving *web search* for the fifteenth time teaches them to click yes without reading, which is worse than allowing it once, deliberately.

**Walk them through it in three colours:**

- 🟢 **Green — allow.** Low risk and **cheap to undo**. Reading files in their workspace, web search, fetching a page, creating and editing files where they're already working.
- 🟡 **Yellow — allow with a condition.** Fine *inside* a boundary. Usually: *"you may write in this folder; if a task looks like it needs anything outside it, stop and ask — tell me what and why."*
- 🔴 **Red — never.** Deleting, spending money, installing software, sending anything under their name, anything involving credentials.

**A sane starting split:**

| Fine to always allow | Keep asking |
|---|---|
| Web **search** and **fetching** pages | **Deleting** files or folders |
| **Reading** files in their workspace | Anything touching folders **outside** the workspace |
| **Creating/editing** files in the workspace | **Installing** software |
| Running their installed skills | **Sending** anything — email, posts, publishing |
|  | Anything involving **credentials or keys** |

The principle to give them: **reversible-and-contained can be automatic; destructive, outward-facing, or out-of-bounds stays a human decision.**

**How to run it.** Ask their comfort level, propose the split, **explain each line in one sentence of plain English**, and only then write it. ⚠️ **Never write a config they can't read** — this is the failure that makes people distrust their own setup. `curl` is the line that will surprise them; explain that agents use it to pull text out of documents and pages, which is why it appears constantly.

**For an existing user**, the better route is evidence: *"let me look at what you've been approving repeatedly and add the safe ones — I'll show you the list before saving."* ⚠️ **This doesn't work for a brand-new user** — they haven't approved anything yet. Start from the table instead.

**Give it a review date**, like their orientation file. An allowlist written for one project can be wrong for the next.

## 3 · Guardrails — when asking isn't enough

Be honest about what an instruction is:

- **Layer 1 — an instruction.** *"Never read, list, edit, or run commands that touch `~/Private/`."* This is **asking**. Like giving someone a key and requesting they stay out of one room. It works most of the time. Most of the time is not always, and users hear "never" as a guarantee unless you tell them otherwise.
- **Layer 2 — a guardrail that blocks.** Configuration (in Claude, **hooks**) that **vetoes the action before it runs**. Locking the door.

**Set up both.** The instruction handles the ordinary case gracefully — you understand *why* and work around the boundary sensibly. The guardrail handles the case where something goes wrong.

The kit ships a **ready-made, tested folder guard** you can install in a minute: [`../guides/guard-folders/README.md`](../guides/guard-folders/README.md), with the layered strategy in [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md). It vetoes any tool call touching listed folders — reads, edits, or shell commands.

⚠️ **Then verify it, and make them watch.** Install, start a **fresh session**, and try to read something inside the protected folder. The right answer is a refusal. **An unverified guardrail is a belief, not a control** — and the verification is what makes them trust the rest of their setup.

⚠️ **For genuinely high-stakes material** — health records, anything where no third party can ever see it — say plainly that the honest answer is still *don't put it on the machine the agent runs on*. A guardrail protects a folder; the safest folder is one you never see. If both must live on one machine, **separate operating-system user profiles** for work and personal is the pragmatic move — though not an absolute barrier if the account has administrator rights. Don't overstate it.

## 4 · The practical limit: it drafts, you send

The most useful boundary available, and it comes out of how [prompt injection](judgement-and-what-goes-wrong.md) actually works rather than from general caution.

**Read their email and draft. Never send.** Same for posting, publishing, anything leaving the building under their name. It costs them one button press and it breaks the attack chain that everything else in this space worries about.

Offer these three lines — the safety floor from [Snippets for your orientation file](agents-md-snippets.md). **If they take nothing else, they should take these:**

```markdown
## Always
- Never send, post or publish anything under my name. Draft it and show me — I press send.
- Before anything irreversible — deleting files, overwriting a document, spending money —
  stop and ask, even if I've already approved something similar.
- Never write passwords, API keys or access tokens into a file. If I paste one, tell me
  where it should live instead.
```

## Quick fixes to reach for

- **"It seems frozen."** Look for a **permission prompt waiting quietly** — the commonest cause, and the exact failure that kills unattended routines.
- **"Everything suddenly feels dumber."** Check `/context`. Probably a compacted session; write a handover and restart.
- **"What can you even do right now?"** Read your own settings back to them: current mode, model, allowlist.

Full interface reference: [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).

## Do this

- **Offer the allow/ask/never list the moment they complain about approving things** — don't wait for them to ask for a solution, they don't know one exists.
- **Ask their comfort level first, propose second.** Never hand over a config without a plain-English line for each rule.
- **The first time they mention client files, NDAs, HR records or personal finances, ask directly** whether there's anything on this machine you should never open. Then install the guard and verify it in a fresh session while they watch.
- **Offer the three safety-floor lines** to any user who hasn't got them, whatever else you're doing.
- **Before scheduling anything**, check the permission mode is auto — otherwise it will stall silently overnight.
- **Say what you're about to do before doing anything irreversible**, even where a mode technically allows it.
