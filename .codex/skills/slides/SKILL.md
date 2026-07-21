---
name: slides
description: >-
  Create a stunning HTML slide presentation. Two modes — `/slides new` discovers
  the user's brand through visual previews and saves it, `/slides` reuses a saved
  brand for fast generation. Use when the user needs a presentation, pitch deck, or
  slide deck they page through. For a single scrollable explanatory page use Visual
  Explainer; for a print-ready PDF document use PDF Create.
version: 1.1.0
---

# Slides

Create a beautiful, animation-rich slide presentation as a single HTML file. No PowerPoint needed — it opens in any browser.

**When to use this skill:**
- "Create a presentation about..."
- "Make a pitch deck for..."
- "Turn this into slides"
- "I need a slide deck for my meeting"

---

## Two modes

### `/slides new` — brand discovery

Use for the user's **first presentation**, or when they want a **new visual style**. Walk them through:

1. **What's it for?** — purpose, audience, roughly how many slides
2. **What mood?** — professional, bold, minimal, warm?
3. **Pick a style** — show three visual previews and let the user choose
4. **Save the brand** — persist the chosen style so next time is instant (see *Saving a brand* below)
5. **Generate** — the full deck, ready to present

### `/slides` — from a saved brand

Use for **repeat presentations** in an already-established style:

1. Read the saved brands from `config.json` and list them (e.g. "Company Pitch", "Team Updates")
2. Let the user pick one, or suggest one based on context
3. Take the content
4. Generate the deck in that established style

If no saved brands exist yet, start brand discovery automatically.

---

## What you produce

A single `.html` file that:
- **Works anywhere** — Chrome, Safari, Firefox, Edge
- **Looks professional** — custom typography, smooth animations, polished design
- **Needs no internet** — self-contained except fonts (see Gotchas)
- **Is easy to share** — email the file, upload to Drive, or publish with Here.now

### Navigation to build in

| Key | Action |
|-----|--------|
| → or Space | Next slide |
| ← | Previous slide |
| Home | First slide |
| End | Last slide |
| F | Fullscreen |
| O | Overview (all slides) |

---

## Slide types

Use the right type for each piece of content:

| Type | Best for |
|------|----------|
| **Title** | Opening slide, the headline |
| **Section Divider** | Breaking into new topics |
| **Content** | Bullet points, key messages |
| **Split** | Before/after, comparisons, two perspectives |
| **Diagram** | Processes, flows, org charts |
| **Dashboard** | KPIs, metrics, numbers that matter |
| **Table** | Data comparisons, feature lists |
| **Quote** | Testimonials, key insights |
| **Full-Bleed** | Big images, dramatic statements |

---

## Saving a brand

After `/slides new`, persist the chosen style so the user can reuse it. Save to `config.json` in this skill directory, keyed by brand name:

```json
{
  "brands": {
    "Company Pitch": {
      "colors":     { "primary": "#0E2233", "accent": "#C06B4A", "background": "#FBFAF7" },
      "typography": { "headings": "Big Shoulders", "body": "Instrument Sans" },
      "animation":  "subtle-fade",
      "layout":     "generous-whitespace"
    }
  }
}
```

On `/slides`, read this file, list `brands` by key, and generate in the selected brand's system. When the user says "make slides using my Company Pitch style" or "in the Team Updates brand", match the key. Add a new top-level key each time discovery runs; never overwrite an existing brand unless the user asks.

---

## Tips to pull from the user

- **Audience?** Investors, team, clients, board?
- **Goal?** Inform, persuade, update, celebrate?
- **Length?** A quick 5-slider or a 25-slide deep-dive?
- **Content?** Bullet points, a document to convert, a `.pptx` to redesign (extract and rebuild), or just a topic (help structure it).
- **Constraints?** "Under 10 slides", "we always use blue and white", "this is for a big screen", "include our logo" (get the image).

---

## Examples

- **"Create a pitch deck for my startup"** → ask about company, audience, key points, then build a narrative arc: Hook → Problem → Solution → Market → Traction → Team → Ask.
- **"Turn these meeting notes into slides"** → extract and structure: Context → Decisions → Action Items → Next Steps.
- **"Make a quarterly review"** → Executive Summary → KPIs Dashboard → Highlights → Challenges → Next Quarter.
- **"I have a PowerPoint but it's ugly"** → extract the content from the `.pptx` and rebuild it with professional design and consistent styling.

---

## Gotchas

- **Fonts are the one external dependency.** Everything else must be inline and self-contained. If the deck may be shown offline, embed the fonts as `@font-face` data URIs or fall back to a system font stack — a deck that loads its fonts from a CDN will render in Times New Roman on a plane.
- **Persist the brand, don't just claim to.** The two-mode value depends on `config.json` actually being written on `/slides new` and read on `/slides`. If you skip the write, "reuse my brand" silently does nothing.
- **Commit to the brand's system.** Pulling in off-brand colours or a second heading font on a saved-brand deck defeats the point. Read the brand's `colors`/`typography` and stay inside them.
- **Right tool check.** A single scrollable page is Visual Explainer's job, and a print-ready document is PDF Create's — only build a paged deck here.
- **Don't over-animate.** Animation should support the content, not distract from it. One considered transition style beats a different effect on every slide.

---

## Pairs well with

- **Here.now** — publish the slides to a shareable URL
- **Visual Explainer** — for a single-page explanation instead of a presentation
- **PDF Create** — convert the deck to PDF for formal distribution
