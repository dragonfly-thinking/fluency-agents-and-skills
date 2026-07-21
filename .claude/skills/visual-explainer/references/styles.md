# Visual Explainer — Style Reference

Concrete direction for each named style: palette, type, spacing, and the details that separate a considered page from a generic one. Read the row for the style you're building, then commit to it fully — half-applying a style is what makes output look templated.

A style is a set of *decisions made in advance*. The failure mode isn't ugliness, it's blandness: safe defaults that no human would have chosen. Pick a style, honour its whole system, and let it show a point of view.

---

## Editorial — reports, proposals, thought pieces

Refined, generous whitespace, a magazine feel.

- **Palette:** warm off-white background (`#FBFAF7`), near-black ink (`#1A1A18`), one restrained accent (deep claret `#7A2E2E` or forest `#2E4739`). No second accent.
- **Type:** serif headings (Lora, Crimson Pro, Young Serif), sans body (Instrument Sans, Work Sans). Large heading scale — the H1 should feel like a cover line, 3–4rem.
- **Spacing:** wide margins (max-width ~68ch for text), generous line-height (1.6), lots of air between sections. Let whitespace do the work.
- **Details:** a thin rule under section headings; small-caps or letter-spaced eyebrow labels above headings; drop the shadow, use space instead.

## Blueprint — processes, technical flows, systems

Precise, technical-drawing feel.

- **Palette:** cool paper (`#F0F4F8`) or deep navy ground (`#0E2233`) with cyan/white ink. One structural accent line colour.
- **Type:** monospace labels (JetBrains Mono, IBM Plex Mono) for annotations and node labels; clean sans (Outfit) for anything longer. Small type, tight tracking.
- **Spacing:** grid-aligned, everything on a visible or implied module. Consistent connector lengths. Right angles, not curves.
- **Details:** thin 1px rules, corner ticks/crop marks, coordinate-style reference markers (A1, §2.3), dashed dependency lines. Think engineering diagram, not infographic.

## Paper / Ink — friendly explanations, informal content

Warm, approachable, hand-made calm.

- **Palette:** cream (`#F5EFE0`), soft brown-black ink (`#2B2620`), muted earth accent (terracotta `#C06B4A`, sage `#7C8A6B`).
- **Type:** a warm serif (Lora) or humanist sans (Work Sans). Medium scale, nothing shouts.
- **Spacing:** comfortable, unhurried. Rounded containers (border-radius 10–14px). Content in soft cards.
- **Details:** subtle paper-grain via a faint CSS texture or a 2–3% noise overlay; soft, low-contrast shadows; underlines that look drawn, not default blue links.

## Clean — data tables, comparisons, matrices

Minimal, content is the design.

- **Palette:** true white or `#FCFCFD`, ink `#18181B`, a single functional accent for emphasis/highlight rows. Neutral grays for structure.
- **Type:** one neutral sans throughout (Instrument Sans, Outfit), two weights only. Numerals tabular if you can.
- **Spacing:** tight but breathable table padding (12–16px cells), zebra striping only if it aids scanning, generous whitespace around the table.
- **Details:** hairline borders (`#E4E4E7`), one highlighted column or row max, aligned decimals, no chartjunk.

## Dashboard — metrics, KPIs, status overviews

Data-dense, cards and numbers.

- **Palette:** light `#F7F8FA` or dark `#0F172A` ground, cards one step off the ground. A semantic set — green up, amber caution, red down — used *only* semantically, never decoratively.
- **Type:** display sans (Big Shoulders, Outfit) for the big numbers (huge — 2.5–4rem), small sans labels above them.
- **Spacing:** card grid, consistent gaps (16–24px), the number is the hero of each card.
- **Details:** the metric first and largest, label small and above, delta/trend small and below with its semantic colour. Sparklines welcome; gradients on the number, not the card.

---

## Anti-AI-tells — avoid these on every style

Generated pages have a house style. Break it on purpose:

- **No all-blue palette.** The `#3B82F6`-and-white "SaaS default" is the single biggest tell. Every style above names a non-blue accent — use it. If the content genuinely needs blue, make it a *specific* blue (deep `#0E2233`, not the default).
- **No oatmeal.** Beige-on-cream-on-taupe with no contrast anchor reads as "AI played it safe". Every palette needs a true dark and a committed accent.
- **No title-then-italic-subtitle.** The `<h1>` immediately followed by a centred italic one-liner is a dead giveaway. Use an eyebrow label above the heading, or let the heading stand alone.
- **No three-emoji-cards-in-a-row.** Feature triplets with a big emoji, a bold noun, and a grey sentence are the canonical AI layout. If you use cards, vary their size and content; drop the decorative emoji.
- **No centre-everything.** Centred headings, centred body, centred buttons all the way down signals a template. Use a real grid; left-align body text.
- **Commit to one accent.** Two or three accent colours fighting for attention is what "AI-generated" looks like. One accent, used consistently, reads as designed.
- **Vary the rhythm.** Identical evenly-spaced sections feel machine-made. Change section heights, alternate full-bleed and contained, let one thing be large.

## Craft baseline — regardless of style

- Establish a **type scale** (e.g. 1rem / 1.25 / 1.6 / 2.5 / 4rem) and a **spacing scale** (4/8/16/24/48/96px). Use only values from your scales — arbitrary numbers are what makes a layout feel loose.
- Set a **max-width** on text (~68ch) so lines stay readable.
- Support **dark and light** via `prefers-color-scheme` — pick both palettes deliberately, don't just invert.
- Everything **self-contained**: inline all CSS, embed any image as a data URI, no CDN/external fonts (system font stacks or `@font-face` with embedded data). The file must work offline.
