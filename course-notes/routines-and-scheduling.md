# Routines & Scheduling

**Read this when** your user asks about scheduling, automation, background work, "can it run this every morning", a daily brief or digest, why a routine didn't run, or what the difference between local and cloud is. Also read it when they've just built a skill — that's the moment to offer scheduling it.

*This is where they stop pressing go. Two settings decide whether it works, and both fail silently if wrong.*

---

## What it is

A **routine** (Claude) or **scheduled task** (Codex) is a saved prompt that fires on a schedule — daily, weekly, or on demand — as a **full agent session**, with access to everything they've built: skills, subagents, folders, orientation file.

The framing worth giving: up to now, nothing happens unless they type something. After this, something other than them presses go.

## Start with a skill they already built

**The best first routine is not a new idea.** It's something they already made and already trust, put on a schedule.

If they've built a [skill](skills.md) for a job they do regularly, schedule that. It proves the skill was real, the routine has a job worth doing, and you're debugging one new thing instead of two. `/proofread` and `/daily-brief` are both installed and work fine as a fallback if they haven't built their own.

**Offer this the moment they finish building a skill** — the connection is obvious to you and invisible to them.

Other things that work: a **morning brief**, a **news or regulator digest** rendered as a clean HTML page, an **important-email flag**, an overnight **batch conversion** of an inbox folder, and a weekly **"tidy and document my workspace"** pass.

## ⚠️ Don't let them hand-write the instruction

The method that makes the difference, and it takes thirty seconds.

**Start in a normal chat first.** *"I want a routine that does X — what would a good instruction for it look like?"* Iterate there, in the interface they already know. **Then copy the result into the routine.**

Why: setting up a routine means an unfamiliar screen with fields they've never seen. This converts an unfamiliar-interface problem into a familiar chat problem — and produces a far better instruction than anyone writes cold into a small text box.

**Do the drafting for them.** Don't describe the method; run it.

## ⚠️ Auto permissions, or it stalls silently

**The single most common way a routine fails, and it fails invisibly.**

Above the folder selector is a permissions setting. Left asking for approval, the routine starts on schedule, hits its first action, and **sits waiting for a click that never comes** — they're asleep, in a meeting, or the app is closed. **No error. No notification. It just never finishes.**

**Check this before they finish setting anything up.** Set it to auto.

And when a user says a routine "seems stuck on running", look for the permission prompt waiting quietly before investigating anything else.

The second setting: **match the model to the job.** Heavyweight for real thinking, fast for mechanical work. This is where cost actually lives.

## The three ways to schedule

|  | **Desktop scheduled task** | **Cloud routine** | **`/loop`** |
|---|---|---|---|
| Needs GitHub | **No** | **Yes** | No |
| Sees their local files | **Yes** | No — a fresh copy from their repo | Yes |
| Survives closing the session | Yes | Yes | No |
| Needs their machine on | Yes (awake, app open) | No | Yes |

**Default to a desktop scheduled task.** No GitHub, no repository, and it works on their **real files** — which is the whole premise of working this way. Claude: **Routines → New routine → Local**. Codex: under **Scheduled**, against a local project folder. Or just set it up when asked: *"set up a daily review that runs every morning at 9am."*

**Cloud routines are the "when my laptop is shut" option**, and the trade is real: a **GitHub repo** ([`../guides/github-basics.md`](../guides/github-basics.md)), a fresh copy pulled from it rather than their machine, and their files therefore travelling to a third party. Fine for most work; keep genuinely sensitive routines local, and say so rather than letting them find out.

> ⚠️ **The failure signature to recognise, because it looks like their mistake and isn't:** they pick cloud, and it asks them to select a repository. If they don't have one, that screen is alarming. **They're in the wrong option, not doing it wrong.** GitHub is required for cloud and not required for the one on their computer. Back them out and choose local.

**`/loop` is session-scoped** — it dies when the terminal closes. Fine for babysitting something for an hour; not for anything durable.

## Connections carry over — sometimes

A routine can use the email, calendar and other [connections](connections-apis-and-mcp.md) set up in the desktop app, so a scheduled agent really can read an inbox and flag what matters. But a **cloud** routine may not see connections wired up only locally. **If a routine can't reach a tool, check where it's running before assuming the connection is broken.**

## Cost

- Entry-level plans are a taste; heavy use hits their limits, because doing something *well* takes more loops than expected.
- **Routines themselves are not especially token-hungry.** Several running daily and weekly on a standard plan is normal — worth saying, because people assume automation is expensive and don't start.
- The reframe if they baulk at a higher tier: not an app subscription, but **what they'd pay a person to do the work**. They're paying for compute, not access to software.

## Other things to get right

- **Check the output folder.** A routine sometimes finishes without announcing it.
- **Give it somewhere to write.** A routine producing something they never find is the same as one that didn't run. Set the folder and the filename convention when you build it.
- **Build verification in** for anything they'll act on without reading closely — see [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md).
- **If they ask which tool:** Codex is currently the simpler of the two for setting a routine up. A preference, not a verdict.
- **From a phone**, triggering a routine already built is one of the things that genuinely works well: [`../guides/on-the-go.md`](../guides/on-the-go.md).

## Do this

- **When they finish building a skill, offer to schedule it.** That's the moment, and they won't connect the two themselves.
- **Draft the instruction in the chat with them first**, then move it into the routine. Never send them to a blank routine field.
- **Set permissions to auto before you finish**, and say why in one sentence.
- **Steer them to local** unless they specifically need it running with the laptop shut.
- **When a routine "doesn't work", check in this order:** permission mode, then whether it ran at all, then the output folder, then whether a connection is missing because it's running in the cloud.
- **Tell them routines are cheap** if they're hesitating on cost — the assumption stops people starting.
