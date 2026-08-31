# Routines & Scheduling

*Work that happens without you pressing go — and the two settings that decide whether it actually runs.*

A **routine** (Claude) or **scheduled task** (Codex) is a saved prompt that fires on a schedule — daily, weekly, or when you trigger it — as a **full agent session**, with access to everything you've built: your skills, your subagents, your folders, your orientation file.

This is the point where you leave the middle of the loop. Up to now, nothing happens unless you type something. After this, something other than you presses go.

---

## Start with a skill you already built

The best first routine is not a new idea. It's **something you already made and already trust**, put on a schedule.

If you've built a [skill](skills.md) for a job you do regularly, schedule that. It proves the skill was real, the routine has a job worth doing, and you're debugging one new thing instead of two. `/proofread` and `/daily-brief` are both in the kit and both work fine as a first routine if you haven't built your own yet.

Other things people actually run: a **morning brief**, a **news or regulator digest** rendered as a clean HTML page, an **important-email flag**, an overnight **batch conversion** of whatever landed in an inbox folder, and a weekly **"tidy and document my workspace"** pass that reviews the week's sessions and makes sure the work is written down.

## ⚠️ Don't hand-write the instruction

This is the method that makes the difference, and it takes thirty seconds.

**Start a normal chat first.** Say: *"I want to build a routine that does X. What would a good instruction for it look like?"* Iterate with it there, in the interface you already know. **Then copy the result and paste it into the routine.**

Why it works: setting up a routine means an unfamiliar screen with fields you've never seen. This converts an unfamiliar-interface problem into a familiar chat problem — and you end up with a far better instruction than you'd have written cold into a small text box.

## ⚠️ Set permissions to auto, or it silently stalls

**This is the single most common way a routine fails, and it fails invisibly.**

Above the folder selector there is a permissions setting. If it's left asking for approval, the routine starts on schedule, hits its first action, and **sits there waiting for a click that will never come** — because you're asleep, or in a meeting, or the app isn't open. It doesn't error. It doesn't tell you. It just never finishes.

Set it to **auto**. And if a routine ever seems stuck on "running", click into it and look for a permission prompt waiting quietly.

The second setting worth getting right: **match the model to the job.** A heavyweight model for anything that needs real thinking, a fast one for mechanical work. This is where cost actually lives.

## The three ways to schedule — and the difference matters

|  | **Desktop scheduled task** | **Cloud routine** | **`/loop`** |
|---|---|---|---|
| Needs GitHub | **No** | **Yes** | No |
| Sees your local files | **Yes** | No — a fresh copy from your repo | Yes |
| Survives closing the session | Yes | Yes | No |
| Needs your machine on | Yes (awake, app open) | No | Yes |

**Start with a desktop scheduled task.** No GitHub, no repository, and it works on your **real files** — which is the whole premise of working this way. Set one up from the desktop app's **Routines → New routine → Local**, or just ask in any session: *"set up a daily review that runs every morning at 9am."* Codex's equivalent lives under **Scheduled** and works the same way against a local project folder.

**Cloud routines are the "when my laptop is shut" option**, and the trade is real: they need a **GitHub repo** ([`../guides/github-basics.md`](../guides/github-basics.md)), they work on a fresh copy pulled from it rather than your machine, and your files therefore travel to a third party. Fine and standard for most work; keep genuinely sensitive routines local.

> ⚠️ **The failure signature to recognise:** you pick the cloud option, and it asks you to select a repository. If you don't have one, that screen is alarming and it looks like you've done something wrong. You haven't — **you're in the wrong option.** GitHub is required for cloud and not required for the one on your computer. Back out and choose local.

**`/loop` is session-scoped** — it dies when you close the terminal. Useful for babysitting something for an hour; not for anything durable.

## Connections carry over — sometimes

A routine can use the email, calendar and other [connections](connections-apis-and-mcp.md) you've set up in the desktop app, so a scheduled agent really can read your inbox and flag what matters. But a **cloud** routine may not see connections you only wired up locally. If a routine can't reach a tool, check *where it's running* before you assume the connection is broken.

## Cost

- Entry-level plans are a great taste, and heavy use will hit their limits — because doing something *well* takes more loops than you expect.
- **Routines themselves are not especially token-hungry.** Several running daily and weekly on a standard plan is normal.
- The reframe worth making: don't compare this to an app subscription. Compare it to **what you'd pay a person to do the work**. You're paying for compute, not for access to software.

## Other gotchas

- **Check the output folder.** A routine sometimes finishes without announcing it.
- **Give it somewhere to write.** A routine that produces something you never find is the same as one that didn't run. Tell it the folder, and tell it the filename convention.
- **Build the verification in.** For anything you'll act on without reading closely, put a checking step inside the routine itself — see [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md).
- **Which tool?** If you have no existing preference, Codex is currently the simpler of the two to set a routine up in. A preference, not a verdict.

## From your phone

The pattern: your computer stays home doing the work; your phone becomes a remote control for it. Triggering a routine you've already built is one of the things that genuinely works well from a phone. Setup for both tools: [`../guides/on-the-go.md`](../guides/on-the-go.md).

## Try this

> I want to build my first routine. Ask me what I'd actually find useful, then draft the
> instruction here in the chat so we can refine it together. Once it's good, walk me
> through creating a **local** scheduled task with it — and make sure I set permissions to
> auto before we finish, so it doesn't sit waiting for approval overnight.
