---
name: pdf-create
description: Convert markdown, notes, or structured content into a polished PDF. Good
  for reports, proposals, one-pagers, anything that needs to be sendable and print-ready.
  Use when "open in browser" isn't enough.
---

# PDF Create

Turn markdown into a PDF that doesn't look like a markdown export. Typography, spacing, a cover page if you want one, page numbers, the basics done right.

**When to use this skill:**
- "Make this into a PDF"
- "Export this proposal as PDF"
- "I need a print-ready version"
- "Convert this report to PDF for the board"

---

## What you get

A single `.pdf` file with:

- Proper typography (serif body, sans headings — or whatever your brand says)
- Sensible margins and line height
- Page numbers in the footer
- A cover page (optional, opt-in)
- A table of contents (optional, for longer docs)
- Working hyperlinks (URLs and internal anchors)
- Embedded images (no broken links when sent)

Designed to look like a document someone produced deliberately, not a raw markdown dump.

---

## How it renders (no install required)

**Always render via a headless web browser. Never install LaTeX, pandoc, weasyprint, or wkhtmltopdf** — those are heavy installs that fail for non-technical users.

The pipeline is:

1. Convert the markdown to a single styled HTML file (typography, margins, page CSS — all inline).
2. Render that HTML to PDF using a browser that's almost certainly already installed:
   - **macOS:** `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` (or Microsoft Edge / Chromium at the equivalent path)
   - **Windows / Linux:** the `chrome` / `msedge` / `chromium` binary on PATH
   - Command: `<browser> --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="out.pdf" "in.html"`
3. If no Chromium-family browser is found, **do not install anything.** Save the styled HTML and tell the user: *"Open this file in your browser and press Cmd/Ctrl+P → Save as PDF."* That's the zero-dependency fallback.

This produces page numbers, embedded images, and working links natively — no extra tooling.

---

## Inputs it accepts

| Input | What happens |
|-------|--------------|
| A markdown file | Convert directly |
| A markdown string (pasted in) | Save + convert |
| A vault note | Pull from your vault, convert |
| A folder of markdown | Combine into one PDF in file-name order |
| HTML | Convert (treats it like rich source) |

---

## Two modes

### Default — clean document

Reads your `tools.md` for a brand spec if you have one (colours, fonts). Otherwise, uses sensible defaults — black text, serif body, simple headings.

### Branded — your visual style

If you have a saved brand (set up via the **Slides** skill or in `tools.md`), this mode applies it: brand colours, brand fonts, optional logo on the cover. Useful for client-facing material.

---

## What it does *not* do

- Doesn't restructure your content — the markdown is the source of truth
- Doesn't add filler or pad to fill pages
- Doesn't try to rewrite for "PDF style" — that's not a thing
- Doesn't replace **Slides** — if you want a deck, use that

---

## Examples

### Markdown to clean PDF

```
"Convert vault/proposals/acme-q3-scope.md to PDF"
```

Result: `acme-q3-scope.pdf` in the same folder. Two-column-ready, page numbers, cover page if the doc is over 4 pages.

### Branded proposal

```
"PDF this with the Dragonfly brand"
```

The skill applies the saved brand (blue accent, the right font pairing, logo on cover) and outputs a sendable document.

### Combined folder

```
"PDF the whole weekly-review/ folder"
```

Combines all the markdown files in `weekly-review/` (in filename order) into one PDF with a TOC. Useful for handing someone a quarter's worth of reviews.

---

## Pairs well with

- **Slides** — when "PDF" is actually the wrong format and you want a deck
- **Visual Explainer** — for single-page explanations with more visual richness
- **Proofread** — clean up the markdown before converting, not after
- **Here.now** — alternative if you want a shareable URL instead of a file attachment
