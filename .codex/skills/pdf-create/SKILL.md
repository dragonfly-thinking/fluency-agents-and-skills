---
name: pdf-create
description: >-
  Convert markdown, notes, or structured content into a polished PDF. Good for
  reports, proposals, one-pagers, anything that needs to be sendable and
  print-ready. Use when "open in browser" isn't enough.
version: 1.1.0
---

# PDF Create

Turn markdown into a PDF that doesn't look like a markdown export. Typography, spacing, a cover page if you want one, page numbers, the basics done right.

**When to use this skill:**
- "Make this into a PDF"
- "Export this proposal as PDF"
- "I need a print-ready version"
- "Convert this report to PDF for the board"

**Not this skill?** For a single scrollable web page, use **Visual Explainer**; for a multi-slide deck, use **Slides**; for a designed art object (poster, cover), use **Canvas Design**. This skill is specifically a **print-ready PDF from markdown**.

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

1. Convert the markdown to a single styled HTML file (typography, margins, page CSS — all inline). Start from [`assets/pdf-shell.html`](assets/pdf-shell.html) — it carries the print CSS (page size, margins, serif body / sans headings, `@page` counter) with a `<!-- CONTENT -->` slot; drop the rendered markdown into the slot rather than rebuilding the CSS each time.
2. Render that HTML to PDF using a browser that's almost certainly already installed:
   - **macOS:** `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` (or Microsoft Edge / Chromium at the equivalent path) — quote the path, it contains a space
   - **Windows / Linux:** the `chrome` / `msedge` / `chromium` binary on PATH
   - Command (Chrome prints its own footer, which includes page numbers):
     `"<browser>" --headless --disable-gpu --print-to-pdf="out.pdf" "in.html"`
3. If no Chromium-family browser is found, **do not install anything.** Save the styled HTML and tell the user: *"Open this file in your browser and press Cmd/Ctrl+P → Save as PDF."* That's the zero-dependency fallback.

Embedded images and working links render natively. **Page numbers** come from the footer: the command above keeps Chrome's default footer (page numbers plus a date and the file path). For a cleaner, branded footer, add `--no-pdf-header-footer` and put a CSS `@page` page-counter in the HTML — but headless Chrome renders `@page` margin-box counters inconsistently, so open the result and confirm the numbers actually appear before sending.

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

Reads your `tools.md` for a brand spec if you have one (colours, fonts). Otherwise, uses sensible defaults — black text, serif body, simple headings. If you've never run the **Slides** skill, no `tools.md` exists yet — that's fine, defaults apply.

### Branded — your visual style

If you have a saved brand (set up via the **Slides** skill or in `tools.md`), this mode applies it: brand colours, brand fonts, optional logo on the cover. Useful for client-facing material.

---

## What it does *not* do

- Doesn't restructure your content — the markdown is the source of truth
- Doesn't add filler or pad to fill pages
- Doesn't try to rewrite for "PDF style" — that's not a thing
- Doesn't replace **Slides** — if you want a deck, use that

---

## Gotchas

- **Quote the browser path.** The macOS binary lives at a path with a space (`/Applications/Google Chrome.app/...`); unquoted, the command silently fails to launch.
- **Make image paths absolute, or embed them.** Relative `src` paths (`![](images/logo.png)`) often don't resolve when Chrome loads the HTML, so images come out blank. Convert them to absolute file paths, or inline them as `data:` URIs, before rendering.
- **Exit code 0 doesn't mean it worked.** Headless Chrome can exit cleanly while writing a blank or single-page PDF if the HTML failed to load. After rendering, check the output file exists and its size is plausible (more than a few KB); if it's suspiciously small, open the HTML in a real browser to see what broke.
- **Page numbers depend on the footer choice** (see "How it renders"). With `--no-pdf-header-footer` they appear only if the CSS `@page` counter rendered — unreliable in headless Chrome. Verify before sending.
- **No Chromium-family browser? Don't install one.** Fall back to "open in browser → Cmd/Ctrl+P → Save as PDF." Heavy installs (LaTeX, weasyprint, wkhtmltopdf) fail for non-technical users.

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
"PDF the whole project-notes/ folder"
```

Combines all the markdown files in `project-notes/` (in filename order) into one PDF with a TOC. Useful for handing someone a quarter's worth of reviews.

---

## Pairs well with

- **Slides** — when "PDF" is actually the wrong format and you want a deck
- **Visual Explainer** — for single-page explanations with more visual richness
- **Proofread** — clean up the markdown before converting, not after
- **Here.now** — alternative if you want a shareable URL instead of a file attachment
