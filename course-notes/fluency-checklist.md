# Your Fluency checklist

*A working list of the things in this kit that actually pay off — and which of them you've done.*

This is a **template**. Your agent copies it to `~/.claude/fluency-checklist.md` (or `~/.codex/`) on install, and that copy is yours: it lives outside the kit folder so updating the kit never wipes it.

---

> ## For the agent — read this before you touch the list
>
> **This is a conversation, not a form.** Do not paste the whole list at the user and ask them to
> pick. Thirteen unticked boxes is the blank-page problem that stalls people.
>
> 1. **Look before you ask.** Check what's actually on their machine — orientation file, settings,
>    installed skills, whether any documents are already converted — and tick what's already true.
>    Say what you found. People have usually done more than they think.
> 2. **Offer exactly one next thing.** Pick the item with the best payoff for how they actually
>    work, say in one sentence what it would change for them, and offer to do it *now, with them*.
>    If they'd rather not, drop it and move on — don't re-ask.
> 3. **Tick as you go**, and write one line under the item saying what was actually done. Future
>    sessions read this instead of asking again.
> 4. **Never replace an existing checklist.** If `~/.claude/fluency-checklist.md` already exists,
>    leave it in place. If this template has items theirs doesn't, add just those, unticked, at the
>    end. Their ticks and their notes stay exactly as they are.
> 5. **Nothing here is compulsory.** Someone who never publishes a webpage isn't behind. The point
>    is that they *chose*, not that every box gets ticked.

---

## Set up once

- [ ] **Orientation file, built by interview** — run `setup-workspace` and let it ask you questions rather than writing the file cold. It pulls out the things you'd never think to mention.
- [ ] **Permissions: your allow / ask / never list** — decide once what your agent may do without asking, so you stop clicking approve thirty times a task. See [`../guides/interface-and-settings.md`](../guides/interface-and-settings.md).
- [ ] **Snippets discussed and added** — the standing instructions in [`agents-md-snippets.md`](agents-md-snippets.md). Three is plenty; you don't want all nine.
- [ ] **A guardrail on anything agents shouldn't touch** — client files, HR records, personal finances. An instruction asks; a guardrail blocks. [`../guides/folder-guardrails.md`](../guides/folder-guardrails.md).

## Make the workspace readable

- [ ] **Documents converted to Markdown** — one real folder of PDFs or Word files, so your agent can actually search inside them instead of paying to read each one. `convert-docs`.
- [ ] **Front matter on the files that matter** — a few labels at the top (`status`, `owner`, `updated`) so a folder can be scanned without opening everything.
- [ ] **An index for one real folder** — a single file listing what's in there and where, so your agent reads one file instead of fifty.

## Use what's installed

- [ ] **Run a skill on something real** — `/proofread` on a piece of your own writing. Do it once with the skill and once without, and look at the difference.
- [ ] **Turn a repeated task into a skill** — the next time you catch yourself explaining the same thing twice, say *"turn that into a skill."*
- [ ] **Make a subagent** — a specialist with its own instructions. Describe the role; your agent writes the file.

## Make it durable

- [ ] **A routine that runs itself** — a morning brief, a news digest, an overnight batch conversion. Something small that saves you a real task.
- [ ] **Workspace backed up** — so a dead laptop isn't a lost workspace. [`../guides/github-basics.md`](../guides/github-basics.md). **Back up your `.claude` / `.codex` folder too** — it holds your global orientation file, your skills and your settings, and it is *not* included when you back up a project folder.
- [ ] **Published something** — take a document, turn it into a page, get a link you can send someone. `here-now`.

---

## What I actually did

*The agent fills this in as things get ticked — one line each, so a future session knows what's here without asking again.*
