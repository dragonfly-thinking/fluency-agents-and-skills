# Markdown & File Conversion

*Why the format your documents are in decides how good your agent is, and how to fix it in one instruction.*

Agents work best with **text**. Markdown is text with light symbols standing in for formatting — `#` is a heading, `**bold**` is bold. That is the whole of it. You do not need to learn the symbols; the agent writes them, and any markdown editor will let you type normally and produce them for you.

The pattern to internalise: **convert in, work in markdown, publish out.** Whatever arrives — Word, PDF, PowerPoint, a spreadsheet — gets converted to markdown, the work happens there, and at the end you produce whatever polished format the recipient needs. Markdown is the workbench, not the deliverable.

---

## Why markdown wins

Two reasons, and the second is the bigger one.

**1 · It costs less to read.** A PDF has to be handled one of two ways — the agent takes a picture of each page and interprets the image, or it extracts the text — and in practice **it does both**. Anthropic's own PDF documentation puts the text cost at roughly **1,500–3,000 tokens per page depending on density**, and then adds: *"because each page is converted into an image, the same image-based cost calculations are applied."* So you pay twice for every page. The same content as markdown costs a fraction of that, and it costs it once.

> The mechanism is the point, not any particular number. **You pay for a PDF page twice — once as text, once as an image.** That is the argument for converting, and it is true whatever the current pricing is.

**2 · It is searchable, and a PDF isn't.** This matters more than the cost.

An agent searching for information uses the same tools a programmer would: it can search **across tens of thousands of files for a phrase in the blink of an eye**, find every occurrence, and read the lines *around* each one to judge whether it's relevant. Needle, haystack, no effort.

Locked inside PDFs and Word documents, that text is not searchable in the same way. The agent has to open and interpret documents one at a time to find out whether they were relevant — slower, far more expensive, and it will often give up before it has read everything. **Converting your archive to markdown is what makes your own material searchable to your agent at all.**

- **CSV instead of Excel**, for the same reason — a CSV is just text. A spreadsheet is not.
- **Spreadsheets and tables** convert well into markdown tables, which are cheap to read and easy for the agent to reason over.

## Converting — the practical routes

- **The `convert-docs` skill** in this kit. Point it at a file or a folder and it handles the rest. It uses **[anydoc](https://github.com/firecrawl/anydoc)** — free, open source, and it runs **on your own machine**, so nothing is uploaded anywhere. It covers Word, PowerPoint, Excel, PDF, EPUB, CSV, OpenDocument and RTF, and it is fast enough to batch a whole folder.
- **No installation at all?** The same converter [runs in a browser tab](https://firecrawl.github.io/anydoc/) — drag a file in, get markdown out, and it still never leaves your computer. Good for one or two files.
- **The agent can also just do it natively**, with no tooling. It works; it takes longer and costs more tokens. Fine for a handful of files, wasteful for fifty.
- **Scanned or complex PDFs** — anything where the layout, images or figures genuinely matter — want a higher-fidelity route. Options and the cost trade-offs are in [`../guides/file-conversion.md`](../guides/file-conversion.md).
- **Convert the original, not a PDF of it.** If you have both `deck.pptx` and `deck.pdf`, convert the PowerPoint. A PDF has already thrown the structure away.

⚠️ **anydoc is very new.** Open the output and look at it before you rely on it — tables and multi-column layouts are where converters slip.

## Keep the original, and say what didn't survive

Conversion is lossy in specific, predictable ways. Handle it once, in the file itself:

- **Keep the source document**, and link to it from the top of the markdown twin.
- **Note what didn't convert** — images, charts, complex tables — so a future session knows when to go and open the original.
- **Don't re-convert** a file that already has an up-to-date markdown twin.

## Make it automatic

You do not want to ask for this every time. Put it in your orientation file once:

```markdown
## Working with documents
- When I point you at a PDF, Word doc, PowerPoint or spreadsheet and there's no Markdown
  version next to it, convert it first and work from the Markdown. Use the `convert-docs` skill.
- Keep the original. Link to it from the top of the Markdown, and note anything that didn't
  survive the conversion — images, charts, complex tables — so you know when to open the source.
- Don't re-convert a file that already has an up-to-date Markdown twin.
```

For a folder that keeps growing, this is also a natural [routine](routines-and-scheduling.md): *"each night, convert any new documents in `~/Inbox` to markdown."*

## Going back out — markdown to something you can send

- **Markdown → Word.** Just ask: *"save this as a `.docx` I can send."* Two things worth knowing. Word itself has a **paste-as-markdown setting** that will interpret `#` and `**` correctly instead of pasting the raw symbols — worth turning on if you move text by hand a lot. And there are third-party Word add-ins that do the same job more thoroughly; ask your agent to find a current one rather than trusting a name from a document like this, because they come and go.
- **On the token cost of conversion:** for a *large* document on an entry-level plan, copying and pasting the text yourself is genuinely sometimes cheaper than having the agent rewrite it. Not a rule, but worth knowing before you burn an afternoon's usage reformatting a report.
- **Markdown → PDF.** The **`pdf-create`** skill produces a designed PDF. The better route for anything visual is to build it as **HTML** first, iterate on it until it looks right, then export to PDF — see [Publishing & Sharing](publishing-and-sharing.md).
- **Markdown → slides.** The **`slides`** skill.
- **A practical pattern:** wordy PowerPoint → save as PDF → agent turns it into a visual HTML page → iterate → distribute as PDF or a link.

⚠️ **Renaming a file to `.md` does not convert it.** It just gives a Word document a misleading extension. Ask the agent to convert it.

## Try this

> Find a folder of my PDFs or Word documents — a real one I actually use, not a sample.
> Convert it to markdown, keep the originals, and note in each file anything that didn't
> survive. Then show me: search across the converted folder for something and tell me how
> long it took, so I can see the difference.
