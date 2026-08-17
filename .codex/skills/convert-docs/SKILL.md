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

## The routes, in order of preference

| Document | Route | Cost |
|---|---|---|
| Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV | **1 — anydoc** (local) | free |
| PDF with real text (exported, not scanned) | **1 — anydoc**, else **1b** | free |
| Scanned or photographed pages | **2 — OCR** | free engine first, then paid |
| Image/figure-heavy where every figure must survive | **3 — Mistral direct** | paid |

Work down the list. Only escalate when the cheaper route actually fails — don't pre-emptively reach for a paid one. These numbers match `guides/file-conversion.md` in the kit repo (normally `~/fluency-agents-and-skills/`), which has the full detail.

> **Prefer the original file over an exported PDF.** If both `deck.pptx` and `deck.pdf` are present, convert the `.pptx`. A PDF has thrown away the document's structure, so anything laid out in columns — slides especially — can come back with the columns read *across* instead of down, producing scrambled sentences. The native file keeps the structure and converts cleanly. Same for `.docx` over a PDF print of it. If the user hands you only the PDF, check the output for interleaved text before trusting it.

---

## Route 1 — anydoc (default, local, free)

[anydoc](https://github.com/firecrawl/anydoc) converts office documents and text-based PDFs to GitHub-Flavoured Markdown in milliseconds. It runs entirely on the user's machine, needs no API key, and nothing leaves their computer. Preserves headings, tables, lists, links and footnotes.

**Check what's available, in this order:**

```bash
command -v anydoc          # already installed? use it directly
node --version             # Node 20+? use npx — nothing to install
```

**If `anydoc` is installed:**

```bash
anydoc report.docx -o report.md
```

**If it isn't, but Node 20 or newer is present — use `npx`, which fetches and runs it without installing:**

```bash
npx -y @firecrawl/anydoc report.docx -o report.md
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
Go straight to Route 1b, finish the job, and mention it once at the end. A locked-down work
laptop hits this, and a stalled download reads as a freeze.

If the user is converting more than a handful of documents, offer once to make it permanent —
`npm install -g @firecrawl/anydoc` — so every run is instant. Don't insist, and don't do it
mid-task without asking.

**If Node is missing, or older than 20:** do **not** send the user off to install Node in the middle of their actual task. Drop to Route 1b for this job, finish what they asked for, and *then* mention it once: *"I can set up a faster local converter for next time — it needs Node, which takes a minute to install. Want me to?"* (`guides/browser-agent.md` has the Node install commands per platform.)

**Verify before claiming success.** anydoc is young software (0.1.x). Open the output and check it's real Markdown with actual content — not empty, not a wall of mojibake, tables not collapsed to nothing. If it looks wrong, say so and escalate to Route 1b rather than handing over a broken file.

## Route 1b — let the model read it directly

For a digitally-created PDF or Word file, you can read the file yourself and write out the Markdown. Slower and costs tokens on a long document, but needs nothing installed and no key. This is the fallback whenever Route 1 isn't available, and the escalation when Route 1's output looks wrong.

Preserve the heading structure, keep tables as Markdown tables, and don't summarise — this is a conversion, not a précis. Say explicitly if you've had to drop anything (complex figures, multi-column layouts that don't linearise).

## Route 2 — OCR, for scans

A scanned document is a *picture* of text: Routes 1 and 1b return nothing useful. If the user has the kit's OpenRouter key set up (`~/.fluency/openrouter.key` — see `mcp/openrouter.md` in the kit repo (normally `~/fluency-agents-and-skills/`)), use its `file-parser` plugin. Full request shape is in `guides/file-conversion.md` in the kit repo (normally `~/fluency-agents-and-skills/`).

> ⚠️ **Always name the engine explicitly.** Omit it and OpenRouter falls back to `mistral-ocr`, which **bills**. Set `"engine": "cloudflare-ai"` (free) unless you've decided OCR is genuinely needed.
>
> **`mistral-ocr` costs $2 per 1,000 pages. Tell the user the estimated cost and get a yes before you run it** — every time, including inside a batch. A 400-page batch is a real invoice, and it is not your money.

No OpenRouter key set up? Say what's blocking you and offer to set it up (`mcp/openrouter.md` is agent-followable) rather than silently returning nothing.

## Route 3 — Mistral OCR direct

Only when a document's images and figures must *all* survive — the direct API returns every image, where Route 2 caps at 8 per PDF. Needs its own key and costs per page. Full recipe in `guides/file-conversion.md` in the kit repo (normally `~/fluency-agents-and-skills/`). Same consent rule as Route 2.

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
- **Don't reach for a paid route first.** Work down the table.
- **Don't run a paid conversion without explicit consent**, and never on a batch without stating the total.
- **Don't block on an install.** Every route has a fallback that needs nothing; use it and offer the setup afterwards.
- **Don't claim success without looking at the output.**
