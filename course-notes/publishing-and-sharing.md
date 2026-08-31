# Publishing & Sharing

*Getting the work out of your folder and in front of someone — and the vocabulary that decides whether it looks like yours or like everyone else's.*

Your agent's natural output format is not Word. It's **HTML** — a web page. That sounds like a technical detail and it isn't: it's the reason an agent can hand you an interactive chart, a timeline, a diagram and a designed layout in the time it would take to format a document badly.

---

## What an HTML file actually is

Just **code** — the scaffolding everything on the web is built from. The agent writes the code; your browser reads it and renders the page you see. You never look at the code.

Two things follow, and the second is the one people don't expect:

- **It can be genuinely interactive.** Flowcharts, toggles, tabs, charts you can hover over. Not a picture of a diagram — a real one.
- **It's a file on your computer.** Opening it looks like a web page and even shows an address, but it is *not* on the internet. Email that address to a colleague and nothing happens for them. That's what publishing is for.

Markdown also supports **Mermaid**, a way to write diagrams as plain text, so agents produce flowcharts and mind-maps directly with no drawing tool involved.

## The workflow

1. **`/visual-explainer`** — turns a piece of content into a self-contained HTML one-pager with diagrams pulled out of the prose. It's surprisingly good at finding structure that was only implied: a text-only article with no charts of its own comes back with charts and a timeline built from data that was buried in the sentences.
2. **Iterate.** The first attempt is rarely the best one. Say what's wrong and ask again.
3. **`/here-now`** — publishes the page to a live, shareable URL.

You don't have to name either skill. Describe the job — *"turn this document into a visual explainer and publish it"* — and your agent picks them up. That's [progressive disclosure](skills.md) paying off in front of you.

## ⚠️ Ask for more — this is the part people skip

**The single biggest lever on whether the output is *yours* or generic is the vocabulary you use to ask.**

Ask for "a nice summary page" and you'll get the default: everything in shades of blue, an oatmeal-beige aesthetic, the giveaway title-then-*italicised-coloured-emphasis* pattern. That look is recognisable now, and it reads as unconsidered.

The fix is to **name what you want**, then iterate:

- **Name the form.** "A spider chart." "A timeline." "A comparison table with the tradeoffs called out." Knowing that a spider chart exists is what lets you ask for one — and building that vocabulary is a real skill, not a technicality.
- **Name the style.** "Brown ink, da Vinci-style line drawings." "Two colours only." "Editorial, lots of white space." Anything specific beats "make it look good."
- **Name your brand.** Point at your colours, your logo, your fonts. This is the highest-return sentence you will ever type at an agent producing something visual.
- **Ask for movement** if you want it. Animation, transitions, a reveal — just ask, then refine. It won't offer.
- **Ask what your options are.** *"What are the different ways you could present this?"* Use it as a thought partner rather than a vending machine.

## Give it a `DESIGN.md`

Then stop doing all that by hand.

Exactly like your [orientation file](your-orientation-file.md), but for how output should **look**: a plain markdown file with your colours, fonts, layout preferences, the things you never want (no gradients, no stock-photo aesthetic, no emoji in headings), and links to a couple of examples you're happy with.

```markdown
# DESIGN.md — how output should look

## Colours
Primary #0563FA · text #414041 · background white. No other colours without asking.

## Type
Headings and body in [font]. No decorative fonts, ever.

## Layout
Generous white space. One idea per section. Tables over bullet lists for comparisons.

## Never
No gradient backgrounds. No emoji in headings. No stock-photo aesthetic.
No "it's not X, it's Y" constructions in the copy.

## Look at these
examples/good-one-pager.html · examples/board-brief.html
```

Point your orientation file at it and every visual output starts from your house style rather than the default one. It's an emerging convention — organisations are increasingly keeping a standalone file like this for agents to reference — and it turns "steer it every time" into "steer it once."

The same idea applies to prose: these tools have recognisable writing habits (overuse of em dashes, the *"it's not this, it's that"* construction, a certain relentless balance). Name the ones that bother you in the file, and they stop appearing.

## Publishing with `here-now`

`here-now` takes the local file and puts it on a real, shareable web address at `{slug}.here.now`.

**Three things to know before you publish anything, and the first one has ruined a good afternoon for somebody:**

> ⚠️ **Published without an account, a site expires in 24 hours — and the claim URL that makes it permanent is returned ONCE and cannot be recovered.** If it scrolls past and you close the session, the page is gone tomorrow and there is no way back. Save the claim URL the moment you see it, or sign in first.

> ⚠️ **Sites are public by default. No password.** Anyone with the link can open it, and links are guessable enough that "nobody will find it" is not a security model. **Do not publish client material, anything under NDA, or anything you'd need to defend having put on the open web.** Pick your document with that in mind — and if you're unsure, don't.

> ✅ **Publishing is optional.** The exercise works perfectly well if you stop at the HTML file and open it locally in your browser. If you work with sensitive material and would rather not install a publishing tool at all, that is a completely reasonable call — one participant made exactly that decision, and noted their agent had advised the same when they talked the risk through with it.

With a free account, pages persist rather than expiring. On a paid account you can **pin or password-gate** a page — a code you hand to specific recipients, effectively a private link — and **attach your own domain**, so the address looks like `insights.yourcompany.com` rather than a random subdomain.

## Turning it into a document

- **HTML → PDF.** Build and iterate as HTML — where it's fast and cheap to change things — then export to PDF only at the end, when it's right. The **`pdf-create`** skill does this, or your browser's print dialogue will. Doing it the other way round means re-doing the layout every time you change a word.
- **A confidential document workflow, without Word.** Text-heavy internal documents can move to gated HTML: publish behind a pin, attach your own domain, and export to PDF whenever you need the document form.
- **A useful first-draft combination:** a retrieval tool like NotebookLM is strong at a fast first pass (a deck, a visual) and weak at iterating. Take its first pass, then hand it to your agent to develop.
- **Slides:** the **`slides`** skill builds HTML decks. Course decks are themselves HTML files.

## Try this

> Take a document I care about. Turn it into a visual HTML explainer — but before you start,
> ask me three questions about how it should look and who it's for, and tell me what forms
> (chart types, layouts) would suit this content. Iterate with me until it's right. Then ask
> whether it's safe to publish publicly before you publish anything — and if it is, save the
> claim URL somewhere I'll find it.
