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
version: 1.0.0
---

# Convert Documents to Markdown

Agents work best on plain text. A content-heavy PDF or Word file becomes far more useful — searchable, quotable, editable, cheap in tokens — once it's Markdown. Renaming a file to `.md` does **not** convert it.

Your job here is to pick the right route and just do it. **Never make the user install anything to get their first conversion** — the default route needs no setup at all.

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

## Pick the route from the file type

**Everything here is free.** Nothing in the normal path costs money or needs an account.

| What they've got | Route | Needs | Speed |
|---|---|---|---|
| **Word, PowerPoint, Excel** — any number | **Bundled script** | nothing | 50 files in under a second |
| **PDF** with real text, more than a handful | **anydoc** | Node | ~1 s per file |
| **PDF** — any kind, including **scans**, a few files | **Read it yourself** | nothing | slow, uses your context |
| Huge scanned batch, *and* they already have OpenRouter | OCR — see the footnote | a paid key | — |

Two things drive that order, both measured rather than assumed:

- **For Office files the bundled script beats anydoc outright** — 10 files in 0.1 s versus 5.5 s,
  because anydoc starts up afresh for every file while the script does the lot in one pass. So
  don't reach for anydoc on a `.docx`; it's slower *and* it needs Node.
- **anydoc's real job is PDFs.** That's the one format the script can't touch, and the one where
  reading it yourself doesn't scale — 50 PDFs read page by page is slow and fills your context.

> **Prefer the original file over an exported PDF.** If both `deck.pptx` and `deck.pdf` are present, convert the `.pptx`. A PDF has thrown away the document's structure, so anything laid out in columns — slides especially — can come back with the columns read *across* instead of down, producing scrambled sentences. The native file keeps the structure and converts cleanly. Same for `.docx` over a PDF print of it. If the user hands you only the PDF, check the output for interleaved text before trusting it.

---

## Route: the bundled script — Word, PowerPoint, Excel

`scripts/office2md.py`, in this skill's own folder. Pure Python standard library: **nothing to
install, no network, no key**, and it works on the old Python that ships with macOS.

```bash
python3 scripts/office2md.py report.docx                    # -> report.md beside it
python3 scripts/office2md.py deck.pptx -o converted/deck.md # explicit output
python3 scripts/office2md.py *.docx *.pptx --outdir converted/   # the whole batch, one pass
```

Pass every file in one command for a batch — that's where the speed comes from. It keeps going
when a file fails, prints each result, and exits `0` all good / `1` nothing converted / `2` mixed.

Handles `.docx`, `.pptx`, `.xlsx` (and the macro variants). Headings, bullets, slide titles and
spreadsheet tables all survive. It does **not** do PDF — that's what the other routes are for.

- **Old `.doc`/`.ppt`/`.xls`** (pre-2007, a completely different binary format) fail with a clear
  message. Tell the user to re-save as `.docx` and carry on; don't try to parse them.
- **Spreadsheets come out as values only** — formulas, formatting and charts are gone, and the
  script notes that at the bottom of its own output. If the formulas are the point, say so rather
  than handing over a table that looks complete.
- **`python3` missing** (rare on macOS, possible on Windows) → fall through to reading the file
  yourself, or to anydoc if Node is there.

---

## Route: anydoc — PDFs, especially several of them

[anydoc](https://github.com/firecrawl/anydoc) converts text-based PDFs to GitHub-Flavoured Markdown in milliseconds, entirely on the user's machine — no API key, nothing leaves their computer. **Use it for PDFs**; for Office files the bundled script above is faster and needs no Node.

**Check what's available, in this order:**

```bash
command -v anydoc          # already installed? use it directly
node --version             # Node 20+? use npx — nothing to install
```

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
> defeats the point of converting it. One document per command — anydoc doesn't take a folder, so
> loop over the files yourself.

The first `npx` run downloads a few megabytes and takes a moment; later runs are about a second.

**If `npx` fails for any reason other than a missing Node** — proxy, blocked registry, offline, a
long silence then a wall of `npm error` — don't retry and don't debug it in front of the user.
Go straight to reading the file yourself, finish the job, and mention it once at the end. A locked-down work
laptop hits this, and a stalled download reads as a freeze.

If the user is converting more than a handful of documents, offer once to make it permanent —
`npm install -g @firecrawl/anydoc` — so every run is instant. Don't insist, and don't do it
mid-task without asking.

**If Node is missing, or older than 20** — most participants won't have it, so this is the normal
case, not an edge case. What to do depends on the size of the job, because that's what decides
whether setup is worth their time:

- **One or a few documents** → don't mention Node at all. Read them yourself, convert them, done. Setup
  would take longer than the task. Raising it here is exactly the derailment we're trying to avoid.
- **A folder, a batch, or anything they'll clearly repeat** → offer *before* you start, because
  here the difference is real (about a second a file, versus reading every one of them in full):
  *"There's a free tool that would convert all 40 of these in under a minute. It takes about two
  minutes to set up, one time. Want me to, or shall I just start now the slower way?"*
- **Either way, if they decline or it fails** → read them yourself, finish the job, don't ask again.

When they say yes, follow **[`setup-node.md`](setup-node.md)** in this skill's own folder (the participant-facing version of the same steps is at https://courses-visuals.dragonflythinking.com/fluency-doc-conversion/) — it has
the per-platform steps, what to do when a work laptop blocks it, and the parts that need the user
rather than you. Then come back and do the conversion they actually asked for.

**Verify before claiming success.** anydoc is young software (0.1.x). Open the output and check it's real Markdown with actual content — not empty, not a wall of mojibake, tables not collapsed to nothing. If it looks wrong, say so and escalate to reading it yourself rather than handing over a broken file.

## Route: read it yourself — any PDF, including scans

For a digitally-created PDF or Word file, you can read the file yourself and write out the Markdown. Slower and costs tokens on a long document, but needs nothing installed and no key. This is the universal backstop: it always works, needs nothing installed, and — because you see the page as an image — it reads **scanned and photographed documents too**, for free. The catch is speed and context: fine for a few files, not for fifty.

Preserve the heading structure, keep tables as Markdown tables, and don't summarise — this is a conversion, not a précis. Say explicitly if you've had to drop anything (complex figures, multi-column layouts that don't linearise).

## Footnote: paid OCR — only if they already have OpenRouter

A scanned document is a *picture* of text: the bundled script and anydoc both return nothing useful. If the user has the kit's OpenRouter key set up (`~/.fluency/openrouter.key` — see `mcp/openrouter.md` in the kit repo (normally `~/fluency-agents-and-skills/`)), use its `file-parser` plugin. Full request shape is in `guides/file-conversion.md` in the kit repo (normally `~/fluency-agents-and-skills/`).

> ⚠️ **Always name the engine explicitly.** Omit it and OpenRouter falls back to `mistral-ocr`, which **bills**. Set `"engine": "cloudflare-ai"` (free) unless you've decided OCR is genuinely needed.
>
> **`mistral-ocr` costs $2 per 1,000 pages. Tell the user the estimated cost and get a yes before you run it** — every time, including inside a batch. A 400-page batch is a real invoice, and it is not your money.

No OpenRouter key set up? Say what's blocking you and offer to set it up (`mcp/openrouter.md` is agent-followable) rather than silently returning nothing.

### Mistral OCR direct

Only when a document's images and figures must *all* survive — the direct API returns every image, where the OpenRouter route above caps at 8 per PDF. Needs its own key and costs per page. Full recipe in `guides/file-conversion.md` in the kit repo (normally `~/fluency-agents-and-skills/`). Same consent rule: state the cost, get a yes.

---

## Batches

For a folder of documents:

1. **List what you're about to do first** — how many files, which route, and the cost (say "free" when it's free; say the number when it isn't). Get a yes before starting anything paid.
2. **Keep a progress log** as you go (`conversion-log.md`, in the same `converted/` folder — not loose among their files): filename, route used, outcome. If the run is interrupted, you can resume without redoing work or re-billing.
3. **Skip files already converted** — check for an existing `.md` before converting.
4. **Don't stop the whole batch on one failure.** Note it, carry on, and report the failures together at the end.
5. **Sample-check the output.** On a large batch, open two or three results and confirm they're sound before telling the user all 70 worked.

This is a good candidate for a **routine** — *"each night, convert any new documents in `~/Inbox` to Markdown"*. Offer that if they're clearly doing it repeatedly.

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
