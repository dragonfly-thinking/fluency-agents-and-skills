---
name: visual-explainer
description: >-
  Generate a beautiful, self-contained HTML page that visually explains an idea,
  process, comparison, timeline, or dataset. Use when the user wants to explain
  something visually, create a comparison, build a timeline, or turn dense
  information into something scannable and shareable. Produces a single scrollable
  HTML page — for a multi-slide deck use the Slides skill; for a print-ready PDF
  document use PDF Create; for a static PNG/PDF art object use Canvas Design.
version: 1.1.0
---

# Visual Explainer

Generate a self-contained HTML file that turns an idea, process, or dataset into a visual page. The output is a single `.html` file the user can open in any browser, email, or publish.

**When to use this skill:**
- "Explain this process visually"
- "Create a comparison of these options"
- "Turn this into a visual one-pager"
- "Make a timeline of this project"
- "Visualize this data as a table"
- "Help me explain this concept to my team"

## What you can create

- **Process flows** — approval workflows, sales funnels, onboarding journeys, decision trees
- **Comparisons** — vendor evaluations, pros/cons, approach options, side-by-side analysis
- **Data tables** — feature matrices, checklists, audit results, requirement tracking
- **Timelines & roadmaps** — project phases, historical events, planning horizons, milestones
- **Concept explanations** — org structures, frameworks, mental models, how-things-work
- **One-pagers** — executive summaries, project overviews, proposals

---

## How to build one

### 1. Get the inputs

Before writing anything, pin down three things (ask if the user hasn't said):

- **Content** — what information needs to be visualized? Get the raw notes/data.
- **Audience** — team, executives, clients, general public? A page for a CEO looks different from one for new hires.
- **Purpose** — inform, persuade, compare, or explain?

### 2. Pick a style and commit to it

Choose the style that fits the content, or use the one the user requests. **Read `references/styles.md`** for the concrete palette, type, spacing, and detailing of each — and for the anti-AI-tells checklist that keeps the output from looking generated. Don't half-apply a style; commit to its whole system.

| Style | Best for | Feel |
|-------|----------|------|
| **Editorial** | Reports, proposals, thought pieces | Refined, generous whitespace, serif headings |
| **Blueprint** | Processes, technical flows, systems | Precise, technical-drawing feel, monospace labels |
| **Paper/Ink** | Friendly explanations, informal content | Warm, approachable, cream backgrounds |
| **Clean** | Data tables, comparisons, matrices | Minimal, content-forward |
| **Dashboard** | Metrics, KPIs, status overviews | Data-dense, cards and numbers |

### 3. Generate the page

Produce a single HTML file:
- Styled per the chosen style's system (palette, type scale, spacing scale from `references/styles.md`)
- Interactive diagrams where they genuinely help
- Responsive — works on desktop and mobile
- Dark/light mode via `prefers-color-scheme`
- **Fully self-contained** — inline all CSS, embed images as data URIs, no external dependencies. It must work offline.

### 4. Save and hand off

Save to the user's workspace and tell them the exact path. They can open it (double-click / drag into a browser), share it (email the file, or use the Here.now skill to publish), or edit the HTML directly.

---

## Examples

- **"Explain our hiring process"** → a flowchart: Application → Screening → Phone → On-site → Offer → Onboarding, with decision points, typical timelines, and owners at each stage.
- **"Compare these three vendors"** → a feature matrix, pricing row, pros/cons per option, and a recommendation summary.
- **"Visualize our Q2 roadmap"** → a timeline with monthly milestones, key deliverables, cross-workstream dependencies, and status indicators.
- **"Turn these meeting notes into a visual summary"** → a one-pager: decisions highlighted, action items with owners, discussion points summarised, next steps.

---

## Tips to pass on to the user

- **Be specific about what to include.** "Show the three pricing tiers with features and target customer for each" beats "visualize our product".
- **Say who's looking.** The audience changes the design.
- **Flag format constraints.** "Make it print as a single page" or "this is for a big screen in a meeting."
- **Provide the raw information.** Notes, bullets, or rough data — structure and visualize from there.

---

## Gotchas

- **Self-contained or it breaks.** Inline every stylesheet, embed images as data URIs, and use system font stacks (or `@font-face` with embedded data). A `<link>` to a CDN or Google Font makes the file fail the moment it's opened offline or emailed.
- **Always include `<meta charset="utf-8">`.** Without it, em-dashes, curly quotes, and arrows render as mojibake — a common and ugly failure.
- **The default look is the enemy.** All-blue palettes, oatmeal beige, and title-then-italic-subtitle are the tells that scream "AI made this". `references/styles.md` has the full avoid-list — apply it.
- **One accent, from a real scale.** Pulling arbitrary hex values and three competing accents is what makes a page look loose. Commit to one style's palette and its type/spacing scales.
- **Match density to audience.** An exec one-pager and a team explainer are not the same page — don't ship a wall of text as a "visual" explainer.

---

## Pairs well with

- **Here.now** — publish the visual to a shareable URL instantly
- **Slides** — when the user needs a multi-slide presentation instead of a single page
- **PDF Create** — convert the HTML to a print-ready PDF for formal sharing
- **Research Brief** — get the information first, then visualize it
