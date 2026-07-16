# Working From Your Phone — your agent, out and about

The pattern from Session 4: your computer stays home doing the work; your phone
becomes a remote control for it. Fire off an instruction from the bus, and the
results are waiting in your workspace when you sit back down.

**One honest caveat before the steps:** these features are new and their names
and menus are moving fast (some were re-badged between our May and July cohorts).
If a name below doesn't match what you see, ask your agent — *"what's the current
way to connect my phone to you?"* — it can check the live docs.

**The common requirement:** your computer must be **awake, online, and running
the agent**. Phone-to-computer is a leash, not a replacement.

---

## Claude — two related features

- **Remote Control** — pairs the **Claude mobile app** (or claude.ai/code in a
  browser) with a **Claude Code session running on your computer**. This is the
  "talk to the agent on my machine from anywhere" feature demoed in the course:
  voice or text instructions from your phone; Claude works away on your files at
  home. Set it up from the Claude mobile app — look for the option to connect to
  your computer's session — with Claude Code running on the desktop.
- **Dispatch** (research preview, inside **Claude Cowork**) — assign and monitor
  *tasks* from your phone; they run through the Claude **Desktop** app with your
  files and connectors. Same idea, Cowork flavour: needs current Desktop + mobile
  apps, and the desktop awake with Claude open.

If in doubt, start with Remote Control — it's the closest to "my agent, from my
phone."

## Codex — inside the ChatGPT app

Codex's phone experience lives in the **ChatGPT mobile app** (iOS and Android —
available on all plans as a preview):

1. On your **Mac**, have Codex running; the pairing flow shows a **QR code**.
2. Scan it from the ChatGPT app on your phone — the two are now linked.
3. From the phone you can kick off new tasks, watch output stream in, review
   changes, and approve actions. Your files and credentials stay on the Mac.

(As of mid-2026 the computer side of this pairing is **macOS-only**; Windows
support is promised but undated.)

## The "very dedicated" option — a cloud computer

The phone setups above die when your laptop sleeps. The fix, if you want an agent
that's *always* reachable: rent a small **cloud computer** (a "VPS" — a machine
that never sleeps, ~$5–20/month from providers like DigitalOcean or Hetzner),
install your agent on it, and connect from anywhere.

The course's honest framing: **powerful, not frictionless** — you'll meet the
terminal and a tool called SSH. But your agent can walk you through every step:
*"I want a small cloud server with Claude Code on it that I can reach from my
phone — plan it out, then set it up with me step by step."* Pair it with GitHub
([`github-basics.md`](github-basics.md)) so the cloud machine and your laptop
share the same workspace.

## What actually works well from a phone

- *"Summarise what arrived in the shared folder today."*
- *"Kick off the report conversion — I'll review when I'm back."*
- Triggering a routine you've already built (the media-scan moment from Session 4).
- Checking on / approving a long-running task.

Drafting fiddly work multi-file work? Wait for the desk. Phone is for **starting,
steering, and checking** — not surgery.
