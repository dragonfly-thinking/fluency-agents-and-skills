# Your Orientation File

*The single highest-leverage file you will build: the one your agent reads automatically, every session, before you type anything.*

If you take one thing from all of this, take this. An orientation file is a plain markdown file — no code, no configuration syntax — that gets **loaded at the start of every session**. It is the difference between an agent that arrives briefed and one that arrives a blank slate and starts guessing.

---

## What it is, and what it's called

- `AGENTS.md` is the emerging cross-tool standard ([agents.md](https://agents.md)); `CLAUDE.md` is what Anthropic's tools look for. **Functionally identical — treat them as the same thing.**
- **Keep one file, satisfied twice.** The tidy arrangement is a real `AGENTS.md` holding everything, plus a one-line `CLAUDE.md` that just imports it:

  ```markdown
  @AGENTS.md
  ```

  That way there is one file to maintain and both tools find it. **This line is load-bearing** — without it, a tool looking only for `CLAUDE.md` finds nothing, and *there is no error message*. It simply behaves as though you never wrote the file. If your agent seems to be ignoring everything you told it, check this first.
- Think of it like onboarding a new colleague: who you are, how you work, your conventions, and — crucially — **where to find more information**.
- It is a **living document**. Open it and edit it, or ask your agent to. No special app, no permission needed.

## Build it by interview — never from a blank page

Writing this cold is harder than it sounds, because most of how you work is **tacit**: never written down, just in your head. The agent cannot guess what you never say. So don't write it. Let it interview you.

- **Ask for the interview.** *"Interview me for about ten minutes, then write my orientation file and a `USER.md` profile. Ask about who I am, how I work, what I'm working on, and where my key files live."* The kit's **`setup-workspace`** skill packages this properly and writes the files for you.
- **Have material ready to feed it** — your LinkedIn, your organisation's website, and a few things you actually wrote.
- **The agent creates the files.** Nothing to save by hand. Confirm with *"make sure you've actually created the file in our workspace."*

### Treat the output as a first draft

The interview gets you 80% there in ten minutes. The last 20% is three moves:

1. **Make it specific.** If a line could describe any competent professional in your field, it isn't doing any work. Cut it. These models over-write; you prune.
2. **Let it interview you a second time.** It asks better questions the second round, because it can now see its own gaps.
3. **Give it a real writing sample** — something you actually wrote, as a gold standard — rather than leaving it to guess your voice. And give it **several**, not one, or it over-imitates the sample.

## Keep it lean — and this is not a style preference

A long orientation file doesn't just waste context. It **actively backfires**: as the file grows, the agent starts missing the instructions that matter, because they are buried among ones that don't. Every line you add makes the others slightly weaker.

Three reasons to prune, in the order they'll bite you:

- **You will actually open it.** A short file is one you'll maintain. A long one rots.
- **The agent navigates faster**, because it fetches what matters instead of carrying everything.
- **Stale lines mislead.** Pruning removes instructions that were true six months ago and are now quietly wrong.

**Signpost, don't dump.** Rather than pasting three thousand words in, point at files and folders by their **path**. The agent reads them when the task calls for it, at no standing cost.

**The test for each line:** *would removing this cause a mistake?* If not, cut it.

**Is it a line in the file, or a skill?** If it applies to **nearly everything you do**, it belongs here. If it only matters **sometimes** — a particular report format, one client's conventions — it belongs in a [skill](skills.md), which loads only when relevant. Putting occasional instructions in the orientation file is the commonest way these get bloated.

## Keep a separate profile, and link to it

The setup interview usually produces two files: the orientation file *and* a `USER.md` profile (who you are, how you work, what you care about).

The orientation file should **link** to the profile rather than embed it — because the orientation file loads on *every* message and must stay lean, while the profile is read only when a task actually needs it. The link in the always-loaded file is what guarantees the agent knows the profile exists, at no standing context cost. `USER.md` is also portable: it describes *you*, not your setup, so it moves to any tool.

## Wearing several hats

Most people don't have one job. Say so directly — *"here are the four hats I wear; tease out what's common and what changes with each"* — and then choose a shape:

- **One global file as the map**, with a file per hat that it points at. Best when you switch hats *within* a single conversation.
- **A folder per hat**, each with its own orientation file. Best when the work is already separated by project.

Either way, **the global file's real job is to be the map** — it says who you are and where to look for the rest. See [Where Things Live](where-things-live.md) for how global and project files combine.

## Beating "AI-sounding" writing

This comes up in every room, and the honest answer is *improvement, not resolution* — long-form writing in your own voice is still something these tools do imperfectly.

- Keep an explicit **style guide and a do-not list**, per context, and point the agent at them.
- Have it **analyse a body of your own writing** and describe how you actually build sentences. Then keep that description as a file.
- **Several samples, never one.** A single sample gets over-indexed on.
- Keep a running list of the **jargon it over-reaches for**, fed back as a reference so it can self-correct.

## Common failures

- **Too much information** — the biggest one, and the one that feels like diligence while it's happening.
- **Empty filler** — "do a good job", "be accurate". They're already trying to.
- **Stale information.** Agents have no memory of "before", so an outdated detail is simply wrong information: old company name, superseded style, a project that finished.
- **Never store secrets** — passwords, API keys, tokens. These tools read text files instantly and *will* surface them.
- **Bare prohibitions.** Never say "never" on its own; it leaves the agent stuck the moment it hits that situation. Pair it with what to do instead — *"don't X; do Y"*, or *"don't X; stop and ask me."*

## Is it actually working?

Most people paste something in and never check.

- **Did it even load?** In Claude Code, type **`/context`** — it shows what's taking up the session's memory, including your orientation file. If it isn't listed, it isn't loaded, and nothing else matters. In Codex, **`/status`**.
- **Loaded but ignored?** The instinct is to add emphasis. Usually the real problem is that the file is **too long** and the rule is lost among the others. Prune first, then look again.
- **Still ignored after pruning?** Mark that *one* line `IMPORTANT`. It works precisely because it's rare.

## Give it a review date

Hand the agent the job of noticing the file has gone stale, rather than relying on yourself to remember:

```markdown
## Keep this file honest
- Review date: [YYYY-MM-DD]. The first time we work together after that date, open with a
  short check: what in here is out of date, and what have we started doing that isn't
  written down? Update it, then set the next date.
```

You can go further and have a [scheduled routine](routines-and-scheduling.md) run this monthly, so it happens whether or not you remember. And the standing line that catches things *in the moment* — rather than at review time — is in [Self-Improvement & Memory](self-improvement-and-memory.md).

## Ready-made lines

Rather than writing these from scratch, take them from **[Snippets for your orientation file](agents-md-snippets.md)** — a grouped, paste-able collection with the reasoning behind each one, plus a three-line safety floor worth having whatever else you do. **Take fewer than you want to.**

## Try this

> Read my orientation file out loud back to me as if you were a new colleague on day one.
> What would you still not know? What in there is vague enough that you'd have to guess?
> And what's in there that you'd already do correctly without being told — so it could go?
