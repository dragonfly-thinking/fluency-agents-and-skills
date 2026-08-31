# Your Orientation File

**Read this when** your user asks about `CLAUDE.md` or `AGENTS.md`, says "how do I stop re-explaining myself", wants you to know who they are, asks why you seem to be ignoring their instructions, mentions wearing several hats, or wants their writing to sound less like AI. Also read it when they're new and you're deciding what to set up first — this is it.

*This is the highest-leverage file your user will ever build. If you only ever help them with one thing, help them with this.*

---

## What it is, and what to say about the naming

A plain markdown file — no code, no configuration syntax — that gets **loaded at the start of every session**. It's the difference between arriving briefed and arriving a blank slate.

- `AGENTS.md` is the emerging cross-tool standard ([agents.md](https://agents.md)); `CLAUDE.md` is what Anthropic's tools look for. **Functionally identical.** Don't let a user get stuck on the distinction.
- **Recommend one file, satisfied twice**: a real `AGENTS.md` holding everything, plus a one-line `CLAUDE.md` that imports it:

  ```markdown
  @AGENTS.md
  ```

  ⚠️ **This line is load-bearing, and its absence fails silently.** A tool looking only for `CLAUDE.md` finds nothing, produces **no error**, and simply behaves as though the file was never written. **If a user reports that you're ignoring everything they told you, check this before anything else** — it is the most common cause and the least visible.
- Frame it as onboarding a new colleague: who they are, how they work, their conventions, and — crucially — **where to find more information**.

## Build it by interview — never let them start from a blank page

This is the part to be firm about. Writing it cold is hard because most of how someone works is **tacit** — never written down, just in their head. They can't tell you what they never think to say.

- **Run the interview.** Ten minutes of questions, then you write the file. The kit's **`setup-workspace`** skill packages this properly.
- **Ask them to have material to hand** — their LinkedIn, their organisation's website, a few things they actually wrote.
- **You create the files.** Never hand them something to save or paste by hand. Confirm afterwards that the file actually landed in the workspace.

### Push them through the second draft

The interview gets 80% there. Users stop at that point and shouldn't. Three moves, and offer them proactively:

1. **Make it specific.** If a line could describe any competent professional in their field, it isn't doing any work — cut it. These models over-write; say so and prune yours.
2. **Interview them a second time.** You ask better questions the second round, because you can see the gaps in your own draft. Offer this a day or two later.
3. **Get a real writing sample** — something they actually wrote, as a gold standard. **Several, not one**, or you over-imitate the sample.

## Keep it lean — and hold this line even when they push

Users want to add. Adding feels like diligence. It isn't, and the reason is worth explaining once:

**A long orientation file actively backfires.** As it grows, you start missing the instructions that matter, because they're buried among ones that don't. Every line added makes the others slightly weaker.

Three reasons to prune, in the order they'll bite:

- **They will actually open it.** A short file gets maintained. A long one rots.
- **You navigate faster**, fetching what matters rather than carrying everything.
- **Stale lines mislead.** Pruning removes instructions that were true six months ago and are now quietly wrong.

**Signpost, don't dump.** Rather than three thousand words pasted in, point at files and folders by **path**. You read them when the task calls for it, at no standing cost.

**Give them the test:** *would removing this line cause a mistake?* If not, cut it. If you'd already do the thing correctly without being told, say so and cut it.

**Line or skill?** If it applies to **nearly everything they do**, it belongs here. If it only matters **sometimes** — a report format, one client's conventions — it belongs in a [skill](skills.md), loaded only when relevant. Occasional instructions in the orientation file are the commonest cause of bloat; offer to move them.

## Separate profile, linked not embedded

The interview usually produces two files: the orientation file *and* a `USER.md` profile — who they are, how they work, what they care about.

**Link, don't embed.** The orientation file loads on *every* message and must stay lean; the profile is read only when a task needs it. The link in the always-loaded file guarantees you know the profile exists, at no standing context cost. `USER.md` is also portable — it describes *them*, not their setup, so it moves to any tool. Worth mentioning; people like knowing they aren't locked in.

## Wearing several hats

Most users don't have one job. Ask directly — *"how many hats do you wear? Let's tease out what's common and what changes with each"* — then offer a shape:

- **One global file as the map**, with a file per hat that it points at. Best when they switch hats *within* a single conversation.
- **A folder per hat**, each with its own orientation file. Best when the work is already separated by project.

Either way, **the global file's job is to be the map**: who they are, and where to look for the rest. How the files combine: [Where Things Live](where-things-live.md).

## When they say the writing sounds like AI

Be honest: this is **improvement, not resolution**. Long-form writing in someone's own voice is still imperfect. Then do these, in order of return:

- **Get several samples**, never one — a single sample gets over-indexed on.
- **Analyse their actual writing** and describe how they build sentences. Keep that description as a file and point the orientation file at it.
- **Build a do-not list** — the constructions they hate — per context.
- **Keep a running list of the jargon you over-reach for**, fed back as a reference so you can self-correct. This one is unusually effective and users rarely think of it.

## Common failures to watch for

- **Too much information** — the biggest one, and it feels like effort while it's happening.
- **Empty filler** — "do a good job", "be accurate". You're already trying to.
- **Stale information.** You have no memory of "before", so an outdated detail is simply wrong information: old company name, superseded style, a finished project.
- **Secrets.** Never let a password, API key or token go into a file. If they paste one, tell them where it should live instead.
- **Bare prohibitions.** A "never" on its own leaves you stuck the moment you hit that situation. Pair it with what to do instead — *"don't X; do Y"* or *"don't X; stop and ask me."* Rewrite theirs when you see it.

## Checking it actually works

Most people paste something in and never check. Offer the check:

- **Did it load?** In Claude Code, `/context` shows what's taking up the session's memory, including the orientation file. Not listed means not loaded, and nothing else matters. In Codex, `/status`.
- **Loaded but ignored?** Their instinct will be to add emphasis. Usually the file is **too long** and the rule is lost. Prune first, then look again.
- **Still ignored after pruning?** Mark that *one* line `IMPORTANT`. It works because it's rare — don't let them mark five.

## Give it a review date

Take the job of noticing staleness off them:

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

Better still, offer to put it on a [routine](routines-and-scheduling.md) so it happens monthly regardless. And the line that catches things *in the moment* rather than at review time is in [Self-Improvement & Memory](self-improvement-and-memory.md) — that's the one to offer first.

## Ready-made lines

Don't write these from scratch. **[Snippets for your orientation file](agents-md-snippets.md)** is a grouped, paste-able collection with the reasoning for each, plus a three-line safety floor worth having whatever else they take.

⚠️ **Offer them one at a time and append only on an explicit yes.** Never paste the set in, never rewrite their file to tidy it. They wrote it, often in a live session with an instructor. **Take fewer than they want to.**

## Do this

- **If they have no orientation file, this is the first thing you set up.** Don't write it from what you already know about them — run the interview. The interview is what surfaces the tacit things.
- **If they have one, read it back to them as a new colleague would** and ask: what would you still not know? What's vague enough that you'd guess? What's in here that you'd get right anyway — so it could go?
- **Check the `@AGENTS.md` import exists** whenever a user reports being ignored. First check, every time.
- **Offer the second interview** a few days after the first — they won't think to ask.
- **Offer two or three snippets**, one at a time, chosen against how they actually work. Never the whole set.
- **When they correct you twice on the same thing**, stop and propose the line that stops a third time. That habit is [Self-Improvement & Memory](self-improvement-and-memory.md); this file is where the line lands.
