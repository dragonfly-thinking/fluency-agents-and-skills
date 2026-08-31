# Context Engineering

**Read this when** your user asks how to get better results, why your output is generic or off-base, whether they should be writing better prompts, "how do I make it understand my work", or why you guessed at something instead of asking. Also read it when they're about to invest effort in prompt wording and it would be better spent elsewhere.

*This module gives you the argument for everything else in this library. It is the module to reach for when someone is optimising the wrong thing.*

---

## The correction to make

Your user probably believes prompt wording is the lever. It was, early on, when output swung wildly on phrasing. It isn't any more — you understand what they *mean*. The bottleneck moved from comprehension to **access**.

> **Prompt engineering was learning to talk to a genius cleverly. Context engineering is handing that genius the keys to the filing cabinet.**

Say this once, plainly, and then stop arguing the point — it lands better as a demonstration than as a claim. The demonstration is in *Do this*.

## The failure it fixes: ungrounded guessing

Be honest with them about what you do when under-briefed, because it is the single most useful thing they can understand about working with you.

Frame yourself as a world-class consultant with total amnesia about them: brilliant, has read everything, has never met them, doesn't know their standards. What comes back is capped by the briefing.

With nothing to anchor on, you do the one thing these models always do — predict a **plausible continuation**. A plausible continuation with no grounding is a guess. **That is all "hallucination" really is:** plausible-sounding filler where a fact should be, not lying. Users find this framing far more useful than the word "hallucination", because it tells them what to do about it.

The concrete example worth giving: they ask *"what do you think of my analysis?"* with nothing attached. A well-set-up agent goes hunting through the workspace, finds *an* analysis, and comments on it confidently. Impressive reach; possibly the wrong file. Point at the right one and the guessing stops.

**So when you don't have what you need, say so and ask.** Don't fill the gap. If they haven't got a standing instruction to that effect, offer them one — [Snippets for your orientation file](agents-md-snippets.md) § 2.

## Affordances, not instructions

The lever is **what's in the environment**: the right files, folders and references being available and findable.

- **A short request in a furnished workspace beats a long one in an empty one.** A sub-150-word request can produce branded, sourced, house-voice output — because none of the branding, voice or company detail is in the request. You find it. That's the whole argument, and it's why effort belongs in the workspace rather than the wording.
- **The 1% is still theirs.** The one file or paragraph that matters most for *this* task is what they still need to point at. Everything else you can find. Say this so they don't over-correct into thinking setup removes their job.

## The four pieces, and where each lives

Route rather than explain — each has its own module:

| Piece | What it does | Module |
|---|---|---|
| **The orientation file** | Loaded automatically every session — who they are, how they work, where to look | [Your Orientation File](your-orientation-file.md) |
| **Where things live** | Global versus project, and how the files stack | [Where Things Live](where-things-live.md) |
| **Structure you can navigate** | Folder shape, front matter, index files, projects that track themselves | [Structuring a Workspace](structuring-a-workspace.md) |
| **A format you can read** | Markdown over PDF and Word, and why | [Markdown & File Conversion](markdown-and-file-conversion.md) |

If they only have appetite for one, **start with the orientation file** — it has the highest ratio of payoff to effort, and it makes the others easier to motivate later.

## Teach them to point at things

Three ways, and most users know none of them:

- **`@`-tag a file** in the message to pull it in by name. Fastest, works for folders too. Show them this early; it removes a lot of friction.
- **Give the path** when the file is elsewhere. On a Mac: **View → Show Path Bar** in Finder so they can always see where they are, then right-click → *Copy as Pathname*. On Windows, the address bar.
- **Point, don't copy — a copy goes stale, a pointer can't.** When they want to reuse context that lives elsewhere, reference it by **path** or an **`@import`** rather than pasting a duplicate. A path is read fresh; a pasted copy silently rots the moment the original changes. Correct them when they paste; it's a well-meant instinct that creates a maintenance problem.

## Voice is context too

Users under-supply context mostly because typing is slow, so raise the alternatives:

- **Meeting transcripts.** Transcription is very accurate now and there's a lot of value in meetings nobody mines. Offer to pull action items, notes, or a briefing out of one. Tools: their meeting platform's built-in transcript (Zoom, Teams, Meet), or [Otter](https://otter.ai), [Granola](https://www.granola.ai), [Fireflies](https://fireflies.ai).
- **Voice notes and voice calls** get transcribed into text you can use — and a call has the advantage that they can be interrupted and pushed back on while they think out loud.
- **Dictating a brief to you directly.** See [Agents, and What Changed](agents-and-what-changed.md) § *Practical things to raise unprompted*.

## When context runs out — or gets too big

Two different problems with two different answers, and users conflate them:

- **Too full** — the window degrades before it fills. Write a handover, start fresh. Mechanism in [Agents, and What Changed](agents-and-what-changed.md).
- **Too much reading for one session** — move the reading somewhere else entirely. That's [Subagents](subagents.md): a dispatched specialist reads in its own window and hands back only the answer.

And underneath both: **leave the trail in files, not in the chat**. See [Structuring a Workspace](structuring-a-workspace.md).

## Do this

- **Run the diagnostic rather than making the argument.** Look at their current setup and tell them, specifically: for a typical question about their work, what would you have to go and find, and what would you have to *guess* at? List the guesses out loud. That list is the argument, in their own material.
- **Then name the two or three files that would remove most of the guessing**, and offer to write the first one with them now. One file, not a plan.
- **Teach `@`-tagging in passing** the first time they describe a file instead of pointing at one.
- **Correct pasting into pointing** when you see it, and say why in one sentence.
- **If they're mid-way through writing a long prompt**, interrupt gently: ask whether the thing they're about to type belongs in a file that would be there every time instead.
