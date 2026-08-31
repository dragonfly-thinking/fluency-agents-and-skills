# Context Engineering

*The one idea that decides whether your agent is impressive or generic: not what you tell it to do, but what it can reach.*

Prompt engineering mattered enormously in the early days, because output quality swung wildly on phrasing. It still matters, but far less — the models now understand what you *mean*. The bottleneck moved. It is no longer comprehension; it is **access**.

> **Prompt engineering was learning to talk to a genius cleverly. Context engineering is handing that genius the keys to your filing cabinet.**

---

## The failure it fixes: ungrounded guessing

Think of an agent as a world-class consultant with total amnesia about you — brilliant, has read everything, has never met you, doesn't know your standards. What you get back is capped by how well it is briefed.

With nothing to anchor on, it does the one thing these models always do: predict a **plausible continuation**. A plausible continuation with no grounding is a guess. That is all "hallucination" really is — plausible-sounding filler where a fact should be, not lying.

Ask *"what do you think of my analysis?"* with nothing attached, and a well-set-up agent will go hunting through your workspace, find *a* previous analysis, and confidently comment on it. Impressive reach; possibly the wrong file. Point it at the right one and the guessing stops.

## Affordances, not instructions

- The lever is **what's in the environment**, not the wording of the request: the right files, folders, and references being available and findable.
- The proof is easy to see for yourself. Give two agents the same short request — one in a workspace with an orientation file, a background folder and an index; the other in a bare folder. The first reads three files and answers. The second searches blindly, burns several times the tokens, takes noticeably longer, and produces a worse answer. Same model, same prompt.
- A **sub-150-word request** in a well-furnished workspace can produce branded, sourced, house-voice output — because none of the branding, voice or company detail is in the prompt. The agent finds it. That is the whole argument for investing in context rather than in prompt wording.
- **The 1% is still yours.** The one file or paragraph that matters most for *this* task is what you still have to point at. Everything else the agent can find.

## What actually goes in the environment

Four things, each covered in its own module:

| Piece | What it does | Where |
|---|---|---|
| **The orientation file** | Loaded automatically at the start of every session — who you are, how you work, where to look | [Your Orientation File](your-orientation-file.md) |
| **Where things live** | Global versus project, and how the files stack | [Where Things Live](where-things-live.md) |
| **Structure it can navigate** | Folder shape, front matter, index files, projects that track themselves | [Structuring a Workspace](structuring-a-workspace.md) |
| **A format it can read** | Markdown over PDF and Word, and why | [Markdown & File Conversion](markdown-and-file-conversion.md) |

## Pointing at things

- **`@`-tag a file** in your message to pull it in by name — the fastest way to hand the agent the specific document you mean.
- **Give it the path** when the file is somewhere else. On a Mac, right-click → *Copy as Pathname*, or turn on **View → Show Path Bar** in Finder so you can always see where you are. On Windows, copy from the address bar.
- **Point, don't copy — a copy goes stale, a pointer can't.** To reuse context that lives elsewhere, reference it by **file path** or an **`@import`** rather than pasting a duplicate in. A path is read fresh on demand. Paste a copy and it silently rots the moment the original changes.

## Voice is context too

You don't need a meeting to get what's in your head into the workspace.

- **Record your meetings and put the transcripts in.** Transcription is now very accurate and there is a lot of value sitting in meetings nobody ever mines. Then ask for action items, notes, or a briefing built from them.
- **Voice notes and voice calls** get transcribed into text an agent can use — and a call has the bonus that the agent can ask clarifying questions and push back while you talk it through.
- Common tools: your meeting platform's built-in transcript (Zoom, Teams, Meet), or a dedicated note-taker such as [Otter](https://otter.ai), [Granola](https://www.granola.ai) or [Fireflies](https://fireflies.ai).

## Where the context goes when it runs out

Context engineering has a maintenance half, because the window is finite and it degrades before it fills. Two habits carry it:

- **Write a handover before the window fills**, and start fresh. Detail on why in [Agents, and What Changed](agents-and-what-changed.md) § *Tokens, context, and context rot*.
- **Leave the trail in files, not in the chat.** A chat is ephemeral; a file is not. See [Structuring a Workspace](structuring-a-workspace.md).

And when the context is *too large* rather than too small, the answer is to move the reading somewhere else entirely — which is what [Subagents](subagents.md) are for.

## Try this

> Look at how I'm set up right now. If I asked you a typical question about my work,
> what would you have to go and find, and what would you have to guess at? List the
> guesses. Then tell me the two or three files that, if they existed, would remove
> most of the guessing — and offer to write the first one with me.
