# Converting Documents — PDF, Word, PowerPoint ↔ Markdown

**Why this matters:** agents work best on plain text. A content-heavy PDF or Word
doc becomes far more useful — searchable, quotable, editable, cheap in tokens —
once it's Markdown. Renaming a file to `.md` does **not** convert it; the routes
below do. (For going the *other* way — Markdown out to polished PDF or slides —
see the end.)

**The short version: just ask.** The kit's **`convert-docs`** skill does all of
this — it picks the right route below, warns you before anything costs money, and
needs nothing installed to work the first time. *"Convert these to markdown"* is
enough. Read on if you want to know what it's doing, or to do it by hand.

---

## Route 1 — anydoc, on your machine (start here)

[**anydoc**](https://github.com/firecrawl/anydoc) converts Word, PowerPoint,
Excel, OpenDocument, RTF, EPUB, CSV and text-based PDFs into clean Markdown in
milliseconds. It runs **entirely on your computer** — no API key, no account,
nothing sent anywhere, no cost. Headings, tables, lists, links and footnotes all
survive.

**Nothing to install.** Your agent runs it with `npx`, which fetches the tool and
runs it in one go:

```bash
npx -y @firecrawl/anydoc report.docx -o report.md
```

If you convert documents often, ask your agent to install it permanently
(`npm install -g @firecrawl/anydoc`) so every run is instant. Either way, your
agent handles it — you don't need to touch a terminal.

> **Needs Node 20+.** Many people who've installed Claude Code or Codex already
> have it. If you don't, you have two options that need nothing at all — the
> browser version below, or letting your agent read the file directly (Route 1b).
> Your agent will pick one and finish the job, then offer to set Node up for next
> time. **Nothing blocks.**
>
> **Agents:** the `-y` flag is required. Without it `npx` waits for a keypress
> that never comes and the command hangs.

### Nothing installed? Same tool, in a browser tab

anydoc also runs at **[firecrawl.github.io/anydoc](https://firecrawl.github.io/anydoc/)** with
nothing to install. It runs *inside the page* — your files never leave your computer, exactly as
with the command-line version. Drag a document in, get Markdown out, save it into your workspace.

Best for one or two files when you'd rather not install anything. For a folder of fifty, it's
worth the two-minute Node setup — or just ask your agent to read them (Route 1b).

**Batch tip:** for a folder of many documents this is a perfect
**routine** — *"each night, convert any new documents in `~/Inbox` to Markdown"* —
or a one-off: *"convert all 70 PDFs in this folder; keep a progress log as you go."*

**Use the original file, not a PDF of it.** If you have both `deck.pptx` and
`deck.pdf`, convert the PowerPoint. A PDF has already thrown the structure away, so
anything in columns — slides especially — can come out with the columns read *across*
instead of down, which scrambles the sentences. We tested this: the same content
converted cleanly from `.pptx` and came back interleaved from the PDF export. Same
logic for `.docx` over a printed PDF of it.

**Where Route 1 falls short:** scanned documents (photos of text) and multi-column
PDF layouts, as above. anydoc is also young software (0.1.x) — so glance at the
output rather than assuming. If it comes out empty or garbled, escalate.

## Route 1b — let the agent read it directly

For a digitally-created PDF or Word file, your agent can also just read the file
and write the Markdown out itself. Slower and it uses up context on a long
document, but it needs absolutely nothing installed. This is the automatic
fallback when Route 1 isn't available.

## Route 2 — the one-key route: OpenRouter (recommended)

If you set up **OpenRouter** from this kit ([`../mcp/openrouter.md`](../mcp/openrouter.md)
— the same single key that powers image generation and live search), that key
also does professional PDF conversion. Note this is a **recipe, not a command**:
the kit's `openrouter.py` engine script covers images and search, but has no PDF
path, so the agent makes this request itself. OpenRouter's **`file-parser`**
feature attaches a PDF to any model request, with a choice of engine:

| Engine | What it's for | Cost |
|---|---|---|
| **`cloudflare-ai`** | Converts ordinary PDFs to **Markdown** | **Free** |
| **`mistral-ocr`** | True OCR for **scanned/image-heavy** documents | **$2 per 1,000 pages** |
| **`native`** | The model reads the PDF itself, where it can | Input tokens only |

> ⚠️ **Always set `engine` explicitly — the fallback is the paid one.** If the
> request omits `engine`, OpenRouter tries the model's native file handling and
> then falls back to **`mistral-ocr`**, which bills. The free route is only free
> if you name it. This matters most exactly where it's easiest to forget: the
> batch case below, where "convert all 70 PDFs" is the difference between $0 and
> a real invoice. If you wrap this in a script, hard-code the engine.

The key lives at `~/.fluency/openrouter.key` (see
[`../mcp/openrouter.md`](../mcp/openrouter.md)) — read it from there rather than
asking the user for it again.

**You are an AI agent doing this for the user — the request shape** (docs:
[openrouter.ai/docs → Multimodal → PDFs](https://openrouter.ai/docs/guides/overview/multimodal/pdfs)):
a normal `/chat/completions` call with the PDF attached as a file part
(`{"type": "file", "file": {"filename": "doc.pdf", "file_data": "<url or base64>"}}`),
plus:

```json
"plugins": [
  { "id": "file-parser", "pdf": { "engine": "cloudflare-ai" } }
]
```

Prompt the model with *"return the full document as clean Markdown, preserving
headings and tables"* and save the reply as the `.md` file. Two practical notes:

- Responses include an **`annotations`** object — send it back on follow-up
  requests about the same PDF to skip re-parsing (and re-billing on `mistral-ocr`).
- On the `mistral-ocr` path OpenRouter forwards **at most 8 images per PDF** (all
  *text* is preserved in full). Fine for most documents; for genuinely
  image-heavy ones, use Route 3.

Offer to wrap this in a small script — and then **package it as a skill** with
`skill-creator`, so next time it's one command.

## Route 3 — Mistral OCR direct (image-heavy & maximum fidelity)

The engine behind Route 2's OCR is **Mistral OCR**, and you can use it directly —
worth it when a document's images and figures all need to survive, since the
direct API returns every image (not capped at 8) alongside the Markdown. Handles
PDF, DOCX and PPTX, including scans. Requires its own key (so it breaks the
one-key principle — that's the trade): create one at
[console.mistral.ai](https://console.mistral.ai), store it as an environment
variable (**never in a tracked file**), `pip install mistralai`, then per the
[official docs](https://docs.mistral.ai/studio-api/document-processing/basic_ocr):

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={"type": "document_url", "document_url": "https://arxiv.org/pdf/2201.04234"},
    include_image_base64=True,   # also return the document's images
)
```

Each page comes back as Markdown; write returned images into an `_assets/` folder
next to the `.md` and the links keep working. Priced per page — a few dollars per
*thousand* pages (check [mistral.ai/pricing](https://mistral.ai/pricing) for the
current rate).

## Which route when?

| Document | Route | Cost |
|---|---|---|
| Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV | **1** — anydoc | free |
| Exported PDF (real text, not a scan) | **1** — anydoc, else **1b** | free |
| No Node, a few files | **1** — anydoc in the browser | free |
| No Node, a whole folder | **1b** — agent reads it, or install Node once | free |
| Scanned pages, photographed documents | **2** with `mistral-ocr` | $2 / 1,000 pages |
| Image/figure-heavy documents where everything must survive | **3** — Mistral direct | per page |
| Hundreds of documents on a budget | **1** for all of them; escalate only the ones that come out mangled | free |

## Going the other way — Markdown out to polished formats

- **Markdown → PDF:** the **`pdf-create`** skill in this kit produces a designed
  PDF; or use the pattern that works better in practice — agent writes **HTML**,
  you iterate on it visually, then *"turn this into a PDF"*.
- **Markdown → slides:** the **`slides`** skill.
- **Markdown → Word:** just ask — *"save this as a `.docx` I can send to legal"*
  (agents use `pandoc` for this; installing it once is fine).
- **Share instead of send:** `here-now` publishes any of it to a live URL.
