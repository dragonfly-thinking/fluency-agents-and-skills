# Fluency checklist — for the agent

**You are the user's agent. This is your working list of what's worth setting up for them from the AI Fluency kit, and what they've already got.** It is not a form for them to fill in; most of these items are things *you* do, with them, in a couple of minutes.

This file in the repo is a **template**. The live copy is at `~/.claude/fluency-checklist.md` (or `~/.codex/`) — outside the kit folder, so updating the kit never wipes it.

---

## How to use this

**Never show the user the whole list.** Fourteen unticked boxes reads as homework and stalls people — which is the exact failure this file exists to prevent.

1. **Check before you ask.** Look at what's actually on their machine — orientation file, settings, installed skills, whether documents are already converted — and tick what's already true. Tell them what you found. People have usually done more than they think, and starting with three ticks changes how the rest lands.
2. **Offer one thing.** Pick the item with the best payoff given how they actually work, say in a sentence what it would change *for them*, and offer to do it now, together. Not a menu.
3. **Do it with them, don't assign it.** Almost everything here is you doing the work while they watch and steer. "Shall I set that up now?" beats "you should set that up."
4. **Tick as you go**, and write a line under *Notes* saying what was actually done. Future sessions read that instead of asking again.
5. **If they decline, drop it.** Don't re-offer the same item next session. Not every box needs ticking — someone who never publishes a webpage isn't behind.
6. **Never replace an existing checklist.** If `~/.claude/fluency-checklist.md` already exists, leave it. If this template has items theirs doesn't, append just those, unticked. Their ticks and notes stay exactly as they are.

---

## Set up once

- [ ] **Orientation file, built by interview** — if they haven't got a `CLAUDE.md` / `AGENTS.md`, run `setup-workspace` and let it interview them. Don't write it cold from what you already know; the interview is what surfaces the tacit things they'd never think to tell you.
- [ ] **Permissions: an allow / ask / never list** — they will be clicking approve constantly. Propose a starting split from [`guides/interface-and-settings.md`](guides/interface-and-settings.md) § *Always-allow* and explain each line in a sentence. Don't write a config they can't read.
- [ ] **Snippets offered** — walk [`course-notes/agents-md-snippets.md`](course-notes/agents-md-snippets.md) against how they actually work and suggest two or three. **One at a time, appended only on an explicit yes.** Never paste the set in, never rewrite their file.
- [ ] **A guardrail on anything you shouldn't touch** — ask whether there's anything on this machine you should never open (client files under NDA, HR records, personal finances). If yes, install it from [`guides/folder-guardrails.md`](guides/folder-guardrails.md) and verify in a fresh session.

## Make the workspace readable

- [ ] **One real folder of documents converted** — find a folder of their PDFs or Word files and convert it with `convert-docs`, so you can actually search inside them. Do it on their real work, not a sample.
- [ ] **Front matter on the files that matter** — add `status` / `owner` / `updated` / `related` so a folder can be scanned without opening everything, and keep them current yourself from then on.
- [ ] **An index for one busy folder** — a single file listing what's in there and where, so you read one file instead of fifty. Best done on whichever folder they complain about.

## Use what's installed

- [ ] **A skill run on something real** — `/proofread` on a piece of their own writing. Show them the same thing without the skill afterwards; the contrast is the point.
- [ ] **A skill made from something they repeat** — listen for it. The second time they explain the same preference, offer to package it.
- [ ] **A subagent for a role they keep needing** — they describe the specialist; you write the file. Never make them hand-write it.

## Make it durable

- [ ] **A routine scheduled from a skill they built** — not a fresh toy. Take the skill they made under *Use what's installed* and put it on a schedule: it proves that work was real, the routine has a job worth doing, and you're only debugging one new thing. (No skill of their own yet? `/proofread` or `/daily-brief` work fine.) Start with a **desktop scheduled task**: no GitHub, and it can see their real files. ⚠️ **Set permissions to auto**, or it starts and sits waiting for an approval that never comes.
- [ ] **A `DESIGN.md` for how output should look** — their colours, fonts, layout preferences, and the things they never want. Same idea as the orientation file, pointed at visuals instead of behaviour. Offer it the first time they say an output looks generic; that's the moment it lands. [`course-notes/publishing-and-sharing.md`](course-notes/publishing-and-sharing.md).
- [ ] **Workspace backed up** — [`guides/github-basics.md`](guides/github-basics.md). **Back up their `.claude` / `.codex` folder as well**: it holds their global orientation file, skills and settings, and backing up a project folder does *not* include it. This is what people lose when they change laptop.
- [ ] **Something published** — take a document they care about, turn it into a page, hand them a link they can send someone. `here-now`. Usually the moment it clicks.

---

## Notes

*Fill this in as you tick things — one line each, so a future session knows what's here without asking again.*
