---
name: convert-docs
description: >-
  Converts documents — Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV,
  PDF — into clean Markdown so they're searchable, quotable and cheap to work
  with. Use when the user asks to "convert this to markdown", "turn these PDFs
  into text", "make this readable for you", "extract the text from", or drops a
  folder of documents and wants to work with the contents. **Also use it before
  reading a batch of Word, PowerPoint, Excel or PDF files for any other purpose**
  — summarising, searching, comparing, mining them — converting first is faster
  and cheaper than reading each one directly. Handles single files and large
  batches. Also covers going the other way (Markdown out to PDF, Word, slides)
  by pointing at the right skill.
version: 2.0.0
---

# Convert Documents to Markdown

Agents work best on plain text. A content-heavy PDF or Word file becomes far more useful — searchable, quotable, editable, cheap in tokens — once it's Markdown. Renaming a file to `.md` does **not** convert it.

**One tool does this: [anydoc](https://github.com/firecrawl/anydoc).** It's free, open source, and runs entirely on the user's own machine — no account, no API key, nothing uploaded. It handles Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV and text-based PDFs, in milliseconds.

There are two ways to run it and one backstop for what it can't do. Pick the route and get on with the conversion — **don't turn this into a setup project**.

## Where the output goes — decide this before you convert

A conversion creates a **plain-text copy** of the original. That matters more than it sounds: these
documents are often confidential — client files, HR records, draft advice — and a Markdown copy is
searchable, un-permissioned, and easy to sync somewhere it shouldn't be.

- **Default to a `converted/` subfolder** next to the source, not loose beside the originals. Say
  where you've put things when you're done.
- **When the request wasn't actually about converting** — *"summarise these six memos"*, *"compare
  these reports"* — converting is your internal step, not their deliverable. Use a temp folder,
  and **ask** before leaving permanent copies in their folders. Don't silently double the number
  of copies of a privileged document.
- **Never write into a folder the user hasn't pointed you at**, and if the source sits in an
  obviously synced or shared location (Dropbox, OneDrive, a team drive), say so before writing.
- **Don't go hunting for files to convert.** If it isn't obvious which documents they mean, ask.
  Searching someone's Desktop or Documents can surface client files, HR records or draft advice
  they never intended you to open — and they may be screen-sharing while you print the contents.

## Pick the route

```bash
command -v anydoc          # already installed? use it directly
node --version             # Node 20+? use npx — nothing to install
```

| Situation | Route |
|---|---|
| Node 20+ present (or `anydoc` already installed) | **Route 1 — anydoc on the command line** |
| No Node, and they'd rather not install it | **Route 2 — anydoc in a browser tab** |
| Scanned or photographed pages | **Route 3 — read it yourself** (anydoc can't OCR) |
| Huge scanned batch, *and* they already have OpenRouter | the paid OCR footnote |

> **Prefer the original file over an exported PDF.** If both `deck.pptx` and `deck.pdf` are present, convert the `.pptx`. A PDF has thrown away the document's structure, so anything laid out in columns — slides especially — can come back with the columns read *across* instead of down, producing scrambled sentences. The native file keeps the structure and converts cleanly. Same for `.docx` over a PDF print of it. If the user hands you only the PDF, check the output for interleaved text before trusting it.

---

## Route 1 — anydoc on the command line

**If `anydoc` is installed:**

```bash
anydoc report.pdf -o report.md
```

**If it isn't, but Node 20 or newer is present — use `npx`, which fetches and runs it without installing:**

```bash
npx -y @firecrawl/anydoc report.pdf -o report.md
```

> **Always include `-y` and `-o`.** `-y` pre-answers `npx`'s install prompt — you won't normally
> see that prompt when running non-interactively, but a user running the same command by hand
> will, so it belongs in anything you show them. `-o <file>` is the load-bearing one: without it
> the entire document prints to your terminal, which floods your context on a long file and
> defeats the point of converting it. **One document per command** — anydoc doesn't take a folder,
> so loop over the files yourself.

The first `npx` run downloads a few megabytes and takes a moment; later runs are about a second.

If the user is converting more than a handful of documents, offer once to make it permanent —
`npm install -g @firecrawl/anydoc` — so every run is instant. Don't insist, and don't do it
mid-task without asking.

**If `npx` fails for any reason other than a missing Node** — proxy, blocked registry, offline, a
long silence then a wall of `npm error` — don't retry and don't debug it in front of the user.
Go to Route 2 or Route 3, finish the job, and mention it once at the end. A locked-down work
laptop hits this, and a stalled download reads as a freeze.

### If Node is missing or older than 20

**Most course participants won't have Node, so this is the normal case, not an edge case.** What
to do depends on the size of the job, because that's what decides whether setup is worth their time:

- **One or a few documents** → don't mention Node at all. Use Route 3 and finish. Setup would take
  longer than the task, and raising it here is exactly the derailment we're trying to avoid.
- **A folder, a batch, or anything they'll clearly repeat** → offer *before* you start, and give
  them both options: *"There's a free converter that would do all 40 of these in under a minute.
  I can set it up properly — about two minutes, one time — or you can drag them into a browser
  page that does the same thing with nothing to install. Or I can just start now the slower way."*

When they want it installed, follow **[`setup-node.md`](setup-node.md)** in this skill's own
folder (the participant-facing version of the same steps is at
https://courses-visuals.dragonflythinking.com/fluency-doc-conversion/) — it has the per-platform
steps, what to do when a work laptop blocks it, and the parts that need the user rather than you.
Then come back and do the conversion they actually asked for.

## Route 2 — anydoc in a browser tab

The same converter runs at **https://firecrawl.github.io/anydoc/** with **nothing to install** —
it runs inside the browser page, so files never leave their computer. Drag a document in, get
Markdown out, save it into the workspace.

Use this when Node is missing and they'd rather not install it, or when a work laptop blocks
`npx`. **You can't drive this one** — it's the user's hands — so give them the link, tell them
where to save the result, and pick the work back up when they have.

For one or two files this is often the fastest path for a non-technical user. For a folder of
fifty it isn't; steer them to Route 1 or do Route 3 yourself.

## Route 3 — read it yourself

You can read a document and write the Markdown out yourself. Slower and it costs tokens on a long
file, but it needs nothing installed and it is the **only free route that handles scans and
photographs** — because you see the page as an image, where anydoc sees no text at all.

This is the universal backstop. Use it whenever the routes above aren't available, and always for
scanned documents.

Preserve the heading structure, keep tables as Markdown tables, and don't summarise — this is a
conversion, not a précis. Say explicitly if you've had to drop anything (complex figures,
multi-column layouts that don't linearise).

## Footnote: paid OCR — only if they already have OpenRouter

A scanned document is a *picture* of text, and anydoc returns nothing useful from it. Route 3
handles scans for free and should be your default. Only for a batch too large to read yourself,
*and* where the user already has the kit's OpenRouter key set up (`~/.fluency/openrouter.key` —
see `mcp/openrouter.md` in the kit repo, normally `~/fluency-agents-and-skills/`), use its
`file-parser` plugin. Full request shape is in `guides/file-conversion.md`.

> ⚠️ **Always name the engine explicitly.** Omit it and OpenRouter falls back to `mistral-ocr`, which **bills**. Set `"engine": "cloudflare-ai"` (free) unless you've decided OCR is genuinely needed.
>
> **`mistral-ocr` costs $2 per 1,000 pages. Tell the user the estimated cost and get a yes before you run it** — every time, including inside a batch. A 400-page batch is a real invoice, and it is not your money.

No OpenRouter key set up? Say what's blocking you and offer to set it up (`mcp/openrouter.md` is agent-followable) rather than silently returning nothing.

---

## Verify before claiming success

anydoc is young software (0.2.x). **Open the output and look at it** — real Markdown with actual
content, not empty, not a wall of mojibake, tables not collapsed to nothing. Tables and
multi-column layouts are where it slips. If it looks wrong, say so and fall back to Route 3
rather than handing over a broken file.

## Batches

For a folder of documents:

1. **List what you're about to do first** — how many files, which route, and the cost (say "free" when it's free; say the number when it isn't). Get a yes before starting anything paid.
2. **Keep a progress log** as you go (`conversion-log.md`, in the same `converted/` folder — not loose among their files): filename, route used, outcome. If the run is interrupted, you can resume without redoing work or re-billing.
3. **Skip files already converted** — check for an existing `.md` before converting.
4. **Don't stop the whole batch on one failure.** Note it, carry on, and report the failures together at the end.
5. **Sample-check the output.** On a large batch, open two or three results and confirm they're sound before telling the user all 70 worked.

This is a good candidate for a **routine** — *"each night, convert any new documents in `~/Inbox` to Markdown"*. Offer that if they're clearly doing it repeatedly.

**Make it automatic.** If they're converting documents regularly, the better fix is a standing
instruction in their orientation file so they never have to ask again. The line is in
`course-notes/agents-md-snippets.md` (§1) in the kit repo — offer it, don't paste it in without
asking.

## Going the other way — Markdown out

- **→ PDF:** the **`pdf-create`** skill.
- **→ slides:** the **`slides`** skill.
- **→ Word:** just do it — `pandoc` handles it; installing it once is fine.
- **→ a shareable link:** the **`here-now`** skill.

## Don't

- **Don't rename a file and call it converted.** `.docx` → `.md` changes nothing about the contents.
- **Don't reach for a paid route at all** unless the user already has OpenRouter *and* the batch is too big to read. Scans are free — you can read them yourself.
- **Don't run a paid conversion without explicit consent**, and never on a batch without stating the total.
- **Don't block on an install.** Every route has a fallback that needs nothing; use it and offer the setup afterwards.
- **Don't claim success without looking at the output.**
