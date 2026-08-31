# Working From Your Phone — your agent, out and about

The pattern: your computer stays home doing the work; your phone becomes a remote
control for it. Fire off an instruction from the bus, and the results are waiting
in your workspace when you sit back down.

**One honest caveat before the steps:** these features are new and their names and
menus are moving fast — several have been re-badged inside a few months. If a name
below doesn't match what you see, ask your agent — *"what's the current way to
connect my phone to you?"* — it can check the live docs.

**The common requirement:** your computer must be **awake, online, and running
the agent**. Phone-to-computer is a leash, not a replacement.

---

## Claude — two related features

- **Remote Control** — pairs the **Claude mobile app** (or claude.ai/code in a
  browser) with a **Claude Code session running on your computer**. This is the
  "talk to the agent on my machine from anywhere" feature: voice or text
  instructions from your phone; Claude works away on your files at
  home. Set it up from the Claude mobile app — look for the option to connect to
  your computer's session — with Claude Code running on the desktop.
- **Dispatch** (research preview, inside **Claude Cowork**) — assign and monitor
  *tasks* from your phone; they run through the Claude **Desktop** app with your
  files and connectors. Same idea, Cowork flavour: needs current Desktop + mobile
  apps, and the desktop awake with Claude open.

If in doubt, start with Remote Control — it's the closest to "my agent, from my
phone."

## Codex — inside the ChatGPT app

**There is no standalone Codex desktop app.** Codex is one of the surfaces inside
the **ChatGPT desktop app** — the same app carries chat and Codex — and it also
exists as a CLI and an IDE extension. If you go hunting for a "Codex" download,
you'll waste twenty minutes; install ChatGPT and switch surface.

Codex's phone experience lives in the **ChatGPT mobile app** (iOS and Android):

1. On your computer, have Codex running; the pairing flow shows a **QR code**.
2. Scan it from the ChatGPT app on your phone — the two are now linked.
3. From the phone you can kick off new tasks, watch output stream in, review
   changes, and approve actions. Your files and credentials stay on the computer.

**Both macOS and Windows are supported** for the desktop side. (An older version of
this page said macOS-only; that was true when it was written and is not now.)

## The "very dedicated" option — a cloud computer

The phone setups above die when your laptop sleeps. The fix, if you want an agent
that's *always* reachable: rent a small **cloud computer** (a "VPS" — a machine
that never sleeps, ~$5–20/month from providers like DigitalOcean or Hetzner),
install your agent on it, and connect from anywhere.

The honest framing: **powerful, not frictionless** — you'll meet the
terminal and a tool called SSH. But your agent can walk you through every step:
*"I want a small cloud server with Claude Code on it that I can reach from my
phone — plan it out, then set it up with me step by step."* Pair it with GitHub
([`github-basics.md`](github-basics.md)) so the cloud machine and your laptop
share the same workspace.

## What actually works well from a phone

- *"Summarise what arrived in the shared folder today."*
- *"Kick off the report conversion — I'll review when I'm back."*
- Triggering a routine you've already built (see [`../course-notes/routines-and-scheduling.md`](../course-notes/routines-and-scheduling.md)).
- Checking on / approving a long-running task.

Drafting fiddly multi-file work? Wait for the desk. Phone is for **starting,
steering, and checking** — not surgery.

---

*Re-verified **2026-09-01** against OpenAI's current Codex documentation: Codex runs
inside the ChatGPT desktop app (no standalone desktop download), with CLI and IDE
extension as additional surfaces, and **Windows is supported alongside macOS**. The
Claude side below was not re-verified against Anthropic's docs on that date — treat
the Claude feature names as indicative. This page is deliberately lighter on exact menu paths than
the other guides, because this is the corner of both products that changes
fastest — the caveat at the top is doing real work, not hedging. If the names
don't match, ask your agent to check the current docs before assuming you've done
something wrong.*
