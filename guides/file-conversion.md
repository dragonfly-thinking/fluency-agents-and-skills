# Converting Documents — PDF, Word, PowerPoint ↔ Markdown

**Why this matters:** agents work best on plain text. A content-heavy PDF or Word
doc becomes far more useful — searchable, quotable, editable, cheap in tokens —
once it's Markdown. Renaming a file to `.md` does **not** convert it; the routes
below do. (For going the *other* way — Markdown out to polished PDF or slides —
see the end.)

You can read this yourself, or point your agent at it: *"read
`guides/file-conversion.md` and convert the PDFs in this folder for me."*

---

## Route 1 — just ask your agent (start here)

For most **digitally-created** documents (exported PDFs, Word docs, PowerPoints —
anything where the text is real text, not a photo of text), your agent can convert
without any external service:

> *"Convert `report.pdf` to Markdown, save it next to the original, and keep the
> heading structure."*

Under the hood it will read the file directly or use a small free tool (it may ask
to install a Python library or `pandoc` the first time — that's normal and safe).
Free, and everything stays on your machine.

**Batch tip from the course:** for a folder of many documents this is a perfect
**routine** — *"each night, convert any new PDFs in `~/Inbox` to Markdown"* — or a
one-off: *"convert all 70 PDFs in this folder; keep a progress log as you go."*

**Where Route 1 falls short:** scanned documents (images of text) and complex
multi-column layouts. That's Route 2.

## Route 2 — the one-key route: OpenRouter (recommended)

If you set up **OpenRouter** from this kit ([`../mcp/openrouter.md`](../mcp/openrouter.md)
— the same single key that powers image generation and live search), you already
have professional PDF conversion. OpenRouter's **`file-parser`** feature attaches
a PDF to any model request, with a choice of engine:

| Engine | What it's for | Cost |
|---|---|---|
| **`cloudflare-ai`** | Converts ordinary PDFs to **Markdown** | **Free** |
| **`mistral-ocr`** | True OCR for **scanned/image-heavy** documents | **$2 per 1,000 pages** |

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

| Document | Route |
|---|---|
| Exported PDF, Word, PowerPoint (real text) | **1** — just ask |
| Ordinary PDF you want as clean Markdown | **2** with `cloudflare-ai` (free) |
| Scanned pages, photographed documents | **2** with `mistral-ocr` |
| Image/figure-heavy documents where everything must survive | **3** — Mistral direct |
| Hundreds of documents on a budget | **1** first; **2** for the ones that come out mangled |

## Going the other way — Markdown out to polished formats

- **Markdown → PDF:** the **`pdf-create`** skill in this kit produces a designed
  PDF; or use the course pattern — agent writes **HTML**, you iterate on it
  visually, then *"turn this into a PDF"*.
- **Markdown → slides:** the **`slides`** skill.
- **Markdown → Word:** just ask — *"save this as a `.docx` I can send to legal"*
  (agents use `pandoc` for this; installing it once is fine).
- **Share instead of send:** `here-now` publishes any of it to a live URL.
