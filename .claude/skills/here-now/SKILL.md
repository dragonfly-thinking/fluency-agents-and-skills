---
name: here-now
description: >-
  Publish files, folders, or HTML to the web instantly. Static hosting for
  sites, images, PDFs, slides, anything. Returns a live shareable URL at
  `{slug}.here.now`. Use when you want to send a link instead of an attachment.
version: 1.0.0
_nf_types:
  name: text
  description: text
  version: text
---

# Here.now

Turn any file or folder into a live URL in seconds. No build step, no hosting setup, no FTP. Just publish and share.

**When to use this skill:**
- "Publish this"
- "Put this online"
- "Share this as a link"
- "Make this a website"
- "Host this slide deck"

---

## What you get

A live URL like `https://bright-canvas-a7k2.here.now/` that anyone can open in a browser.

- **HTML sites** — full site with assets, routing, scripts
- **Single files** — image, PDF, video, audio get a rich auto-viewer
- **Folders without HTML** — auto-generated directory listing
- **Slides** — the deck you made with the **Slides** skill, instantly shareable
- **PDFs** — viewer with download button
- **Visual Explainers** — share without "open this attached HTML file"

---

## Anonymous vs. authenticated

| Mode | What you get | How long it lasts |
|------|--------------|-------------------|
| **Anonymous** (no setup) | Random slug | 24 hours |
| **Authenticated** (free API key) | Custom slugs, edits, permanent | Forever |

For most starter-kit uses you'll want the API key. Setup walks you through it the first time you publish.

---

## Examples

### Share a one-page explainer

```
"Publish this Visual Explainer"
```

The skill runs `here.now` on the HTML file, returns a URL like
`https://q3-pricing-explainer.here.now/` — you paste that into Slack or an
email instead of attaching the file.

### Share a slide deck

```
"Put this deck online"
```

Slide deck (produced by the **Slides** skill) becomes a URL. Recipients
present in the browser, fullscreen, no download needed.

### Share a folder of files

```
"Publish this folder of board pack docs"
```

The skill uploads the folder, generates a clean directory listing, returns one URL. The recipient sees a tidy index with one-click download per file.

### Quick draft site

```
"Make this markdown into a website"
```

The skill renders the markdown to HTML and publishes it. Useful for a quick
project page, course page, or doc site.

---

## What it does *not* do

- Doesn't replace a real website — this is for shares, demos, drafts, internal pages
- Doesn't index your content publicly unless you ask
- Doesn't auto-publish anything — you always confirm before the URL goes live

---

## Updating a site

If you publish version 2 of a doc, you can pass the same slug to update in place:

```
"Update the q3-pricing-explainer site with this new version"
```

The link doesn't change. Whoever you sent it to sees the new version when they refresh.

---

## Pairs well with

- **Slides** — most decks are more useful as a URL than as a file
- **Visual Explainer** — explainers are designed to be shared as links
- **PDF Create** — when a PDF needs to be linkable, not just attachable
