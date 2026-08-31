# Markdown & File Conversion

**Read this when** your user points you at PDFs or Word documents, asks why markdown, asks about converting files, says searching their own material is slow or expensive, asks how to get something back into Word or PDF, or is working from a folder of documents you can't search properly.

*Your user's file formats decide how good you are. This is usually the highest-return hour of setup available, and they will not think to ask for it.*

---

## The pattern to establish

**Convert in, work in markdown, publish out.** Whatever arrives — Word, PDF, PowerPoint, a spreadsheet — gets converted to markdown, the work happens there, and at the end you produce whatever polished format the recipient needs.

Markdown is the workbench, not the deliverable. Say it that way; users worry they're being asked to abandon Word.

**Reassure them about the format itself.** Markdown is just text with light symbols — `#` for a heading, `**bold**` for bold. They don't learn the symbols: you write them, and a markdown editor lets them type normally.

## Why it matters — two reasons, and the second is bigger

**1 · Cost.** A PDF gets handled one of two ways — imaging each page and interpreting the picture, or extracting the text — and in practice **both happen**. Anthropic's own PDF documentation puts the text cost at roughly **1,500–3,000 tokens per page depending on density**, then adds that *because each page is converted into an image, the same image-based cost calculations are applied*.

> **Give them the mechanism, not a number: you pay for a PDF page twice — once as text, once as an image.** That stays true whatever the pricing does. Don't quote a single headline figure; it dates and users repeat it in their own organisations.

**2 · Searchability — this is the one that actually changes their working life.**

You search using the same tools a programmer would: **across tens of thousands of files for a phrase, almost instantly**, finding every occurrence and reading the lines *around* each one to judge relevance. Needle, haystack, no effort.

Locked inside PDFs and Word documents, that text isn't searchable the same way. You'd have to open and interpret documents one at a time — slower, far more expensive, and you'll often stop before reading everything relevant. **Converting their archive is what makes their own material searchable to you at all.**

- **CSV instead of Excel**, same reason — a CSV is just text.
- **Spreadsheets and tables** convert well into markdown tables: cheap to read, easy to reason over.

## The conversion routes

- **The `convert-docs` skill.** Point it at a file or a folder. It uses **[anydoc](https://github.com/firecrawl/anydoc)** — free, open source, running **on their own machine**, so nothing is uploaded. Covers Word, PowerPoint, Excel, PDF, EPUB, CSV, OpenDocument, RTF, and it's fast enough to batch a folder. **Say the "nothing is uploaded" part unprompted** — it's the objection people don't voice.
- **Nothing installed at all?** The same converter [runs in a browser tab](https://firecrawl.github.io/anydoc/) — drag a file in, and it still never leaves their computer. Good for one or two files, and the right suggestion for anyone on a locked-down machine.
- **You can convert natively**, no tooling. It works; it's slower and costs more tokens. Fine for a handful, wasteful for fifty.
- **Scanned or layout-critical PDFs** need a higher-fidelity route. Options and cost trade-offs: [`../guides/file-conversion.md`](../guides/file-conversion.md).
- **Convert the original, not a PDF of it.** If both `deck.pptx` and `deck.pdf` exist, take the PowerPoint — a PDF has already thrown the structure away.

⚠️ **anydoc is very new.** Look at the output before relying on it — tables and multi-column layouts are where converters slip. Tell the user what you checked.

## Keep the original, and say what didn't survive

Conversion is lossy in predictable ways. Handle it in the file itself, every time, without being asked:

- **Keep the source document** and link to it from the top of the markdown twin.
- **Note what didn't convert** — images, charts, complex tables — so a future session knows when to open the original.
- **Don't re-convert** a file that already has an up-to-date markdown twin.

## Make it automatic

They shouldn't have to ask each time. Offer this for their orientation file:

```markdown
## Working with documents
- When I point you at a PDF, Word doc, PowerPoint or spreadsheet and there's no Markdown
  version next to it, convert it first and work from the Markdown. Use the `convert-docs` skill.
- Keep the original. Link to it from the top of the Markdown, and note anything that didn't
  survive the conversion — images, charts, complex tables — so you know when to open the source.
- Don't re-convert a file that already has an up-to-date Markdown twin.
```

For a folder that keeps growing, offer a [routine](routines-and-scheduling.md) instead: *"each night, convert any new documents in `~/Inbox` to markdown."*

## Getting back out

- **Markdown → Word.** Just do it when asked. Two things worth mentioning: Word has a **paste-as-markdown setting** that interprets `#` and `**` properly instead of pasting raw symbols — worth turning on if they move text by hand. And third-party Word add-ins do the job more thoroughly; **look up a current one rather than naming one from memory**, because they come and go.
- ⚠️ **On cost, be straight with them.** For a *large* document on an entry-level plan, copying and pasting the text themselves is genuinely sometimes cheaper than having you rewrite it. Not a rule, but say it rather than burning their afternoon's usage reformatting a report.
- **Markdown → PDF.** The **`pdf-create`** skill. For anything visual, build as **HTML** first, iterate until it's right, then export — see [Publishing & Sharing](publishing-and-sharing.md).
- **Markdown → slides.** The **`slides`** skill.
- **A pattern worth offering:** wordy PowerPoint → save as PDF → turn it into a visual HTML page → iterate → distribute as PDF or a link.

⚠️ **Renaming a file to `.md` does not convert it.** If a user does this, tell them — it just gives a Word document a misleading extension, and the failure afterwards is confusing.

## Do this

- **Find a real folder of their PDFs or Word files** — not a sample, their actual work — and offer to convert it. This is the demonstration, and it's worth more than the explanation.
- **After converting, prove the difference:** search across the converted folder for something and tell them what you found and how fast. That's the moment the argument lands.
- **Keep originals and note the losses in every file**, without being asked.
- **Offer the standing instruction** as soon as they've converted anything, so they never ask again.
- **Suggest the browser converter** rather than an install if they're on a managed machine.
- **Warn about token cost** before a large Word round-trip, not after.
