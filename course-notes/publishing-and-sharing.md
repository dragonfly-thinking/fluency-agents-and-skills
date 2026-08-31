# Publishing & Sharing

**Read this when** your user wants to share something, asks for a web page or a one-pager, says an output looks generic or "like AI", asks about HTML, wants a PDF that looks designed, asks to publish something online, or wants their brand applied to what you produce.

*Two things matter here: the vocabulary they use to ask, and the warnings you give before they publish.*

---

## What HTML is, in their terms

Your natural output format isn't Word. It's **HTML** — a web page. Not a technical detail: it's why you can produce an interactive chart, a timeline, a diagram and a designed layout in the time it takes to format a document badly.

Two things to tell them:

- **It can be genuinely interactive.** Flowcharts, toggles, tabs, charts they can hover over. Not a picture of a diagram — a real one.
- ⚠️ **It's a file on their computer.** Opening it looks like a web page and even shows an address, but it is *not* on the internet. **Email that address and nothing happens for the recipient.** Say this before they try — it's a confusing failure and a common one.

Markdown also supports **Mermaid**, diagrams written as plain text, so you produce flowcharts and mind-maps directly with no drawing tool.

## The workflow

1. **`/visual-explainer`** — turns content into a self-contained HTML one-pager with diagrams pulled out of the prose. It's good at finding structure that was only implied: a text-only article with no charts comes back with charts and a timeline built from data buried in the sentences.
2. **Iterate.** The first attempt is rarely the best. Tell them that up front, so they push back instead of accepting it.
3. **`/here-now`** — publishes to a live, shareable URL.

They don't need to name either skill — describe the job and you pick them up. Let that happen; it's [progressive disclosure](skills.md) paying off visibly.

## ⚠️ Ask for more — the part that decides whether it's theirs

**The biggest lever on whether output is *theirs* or generic is the vocabulary used to ask.** And they don't have that vocabulary yet — so supply it rather than waiting.

Asked for "a nice summary page", you produce the default: everything in shades of blue, an oatmeal-beige aesthetic, the title-then-*italicised-coloured-emphasis* pattern. That look is recognisable now and reads as unconsidered.

**Offer the options rather than executing the vague request.** Before you build, ask two or three questions and tell them what's available:

- **Name the form.** A spider chart. A timeline. A comparison table with tradeoffs called out. **Knowing a spider chart exists is what lets someone ask for one** — so list the forms that would suit their content. This is the single most useful thing you can do here.
- **Name the style.** "Brown ink, da Vinci-style line drawings." "Two colours only." "Editorial, lots of white space." Anything specific beats "make it look good".
- **Name their brand.** Their colours, logo, fonts. Highest-return input available for anything visual — ask whether they have a style guide.
- **Movement, if they want it.** Animation, transitions, a reveal — available, and you won't offer it unless asked. So offer it.
- **Ask what their options are.** Genuinely useful as a thought-partner move: *"here are three different ways this could be presented."*

## Offer them a `DESIGN.md`

Then they stop doing that every time.

Exactly like their [orientation file](your-orientation-file.md), but for how output should **look**: colours, fonts, layout preferences, things they never want, and links to a couple of examples they're happy with.

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

Point their orientation file at it and every visual output starts from their house style rather than the default. It's an emerging convention — organisations increasingly keep a standalone file like this for agents to reference. **The moment to offer it is the first time they say an output looks generic.**

Same idea applies to prose: you have recognisable writing habits (overuse of em dashes, the *"it's not this, it's that"* construction, a relentless balance). Ask which ones bother them and put those in the file.

## Publishing with `here-now`

`here-now` takes the local file and puts it on a real address at `{slug}.here.now`.

**Three things to say before you publish anything. The first has ruined someone's afternoon:**

> ⚠️ **Published without an account, a site expires in 24 hours — and the claim URL that makes it permanent is returned ONCE and cannot be recovered.** If it scrolls past and the session closes, the page is gone tomorrow with no way back. **Save the claim URL somewhere they'll find it, and tell them you've done so** — or get them signed in first.

> ⚠️ **Sites are public by default.** Anyone with the link can open it, and "nobody will find it" is not a security model. A password can be set afterwards, but the default is open — and a signed-in user's sites can also surface on their public here.now profile. **Ask before publishing whether the document is safe to put on the open web** — client material, anything under NDA, anything they'd have to defend. Don't publish and then mention it.

> ✅ **Publishing is optional, and say so.** The whole thing works if you stop at the HTML file and they open it locally. If they work with sensitive material and would rather not install a publishing tool at all, that is a completely reasonable call — and worth saying out loud, because people assume the exercise requires it.

**What a free account changes**, and it changes more than people expect. Signed in, **pages persist** rather than expiring, they can set a **custom expiry** instead, they can **password-protect** a page, and they get **one custom domain** — so the address reads `insights.theircompany.com` rather than a random subdomain. Paid plans raise the domain and storage limits; they don't unlock passwords or persistence.

⚠️ **There is no "PIN" feature — don't call it one.** Password protection is a setting on a published site, applied after publishing. And a site with no password is **public**, including to a signed-in user's public here.now profile.

## Turning it into a document

- **HTML → PDF.** Build and iterate as HTML, where changes are fast and cheap, then export **only at the end** when it's right. The **`pdf-create`** skill, or their browser's print dialogue. ⚠️ Doing it the other way round means re-doing the layout on every wording change — steer them away from it.
- **A document workflow without Word:** password-protected HTML on their own domain, exported to PDF when a document is needed. ⚠️ **Don't sell this as a route for genuinely confidential material.** A password on a public host is access control, not confidentiality — it's fine for "don't want this indexed and shared onward", wrong for client-privileged or regulated content. For that, keep it local and export to PDF.
- **First-draft combination:** a retrieval tool like NotebookLM is strong at a fast first pass and weak at iterating. Take its first pass, then develop it properly.
- **Slides:** the **`slides`** skill builds HTML decks.

## Do this

- **Ask before you build**, not after: who's it for, how should it look, what forms would suit this content. Two or three questions, then build.
- **Name the chart types and layouts available** for their material. Supplying vocabulary is the job here.
- **Ask whether they have brand colours or a style guide** the first time you produce anything visual.
- **Offer a `DESIGN.md`** the first time they call an output generic — and write it from their answers rather than handing over the template.
- **Ask "is this safe to put on the open web?" before publishing.** Every time.
- **Save the claim URL and tell them where it is.** Don't let it scroll past.
- **Tell them the first version won't be the best one**, so they iterate instead of settling.
