# Converting Documents — PDF, Word, PowerPoint ↔ Markdown

**Why this matters:** agents work best on plain text. A content-heavy PDF or Word
doc becomes far more useful — searchable, quotable, editable, cheap in tokens —
once it's Markdown. Renaming a file to `.md` does **not** convert it; the two
routes below do. (And for going the *other* way — Markdown out to polished PDF or
slides — see the end.)

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
This route is free and keeps everything on your machine.

**Batch tip from the course:** for a folder of many documents, this is a perfect
**routine** — *"each night, convert any new PDFs in `~/Inbox` to Markdown"* — or a
one-off: *"convert all 70 PDFs in this folder; keep a progress log as you go."*

**Where Route 1 falls short:** scanned documents (images of text), complex
multi-column layouts, and documents where the tables and figures really matter.
That's Route 2.

## Route 2 — Mistral OCR (scanned & complex documents, high fidelity)

**Mistral OCR** is a paid API that reads a document the way a human does — layout,
tables, figures — and returns clean **Markdown**, preserving the images. It
handles PDF, DOCX and PPTX, including scans. Cost is per page and small (a few
dollars per **thousand** pages — check [mistral.ai/pricing](https://mistral.ai/pricing)
for the current rate); converting even a large personal library costs pocket money.

**You are an AI agent setting this up — steps:**

1. **API key.** Have the user create one at
   [console.mistral.ai](https://console.mistral.ai) (email signup → API Keys →
   create). Store it as an environment variable — **never paste a key into a
   skill, note, or any file your workspace tracks**:
   ```bash
   # macOS/Linux — add to ~/.zshrc or ~/.bashrc
   export MISTRAL_API_KEY="the-key"
   ```
2. **Install the library:** `pip install mistralai` (or `pip3`).
3. **Convert.** The core call, per the official docs
   ([docs.mistral.ai](https://docs.mistral.ai/studio-api/document-processing/basic_ocr)):

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

   For a **local file**, upload it first (`client.files.upload(...)`) or pass it
   base64-encoded — the docs page above shows both variants; follow whichever the
   current SDK documents. Each page comes back as Markdown; images arrive as
   placeholders (plus base64 data if requested) — write them into an `_assets/`
   folder next to the Markdown and the links keep working.

4. **Wrap it up.** Write the user a small script (input files → output folder,
   one `.md` per document), test it on one real document, and **offer to package
   it as a skill** — "convert-docs" — so next time it's a slash command. Add a
   note to their `CLAUDE.md`/`AGENTS.md` if they convert often.

## Which route when?

| Document | Route |
|---|---|
| Exported PDF, Word, PowerPoint (real text) | **1** — just ask |
| Scanned pages, photographed documents | **2** — Mistral OCR |
| Complex layouts, tables and figures that must survive | **2** |
| Hundreds of documents on a budget | **1** first; **2** for the ones that come out mangled |

## Going the other way — Markdown out to polished formats

- **Markdown → PDF:** the **`pdf-create`** skill in this kit produces a designed
  PDF; or use the course pattern — agent writes **HTML**, you iterate on it
  visually, then *"turn this into a PDF"*.
- **Markdown → slides:** the **`slides`** skill.
- **Markdown → Word:** just ask — *"save this as a `.docx` I can send to legal"*
  (agents use `pandoc` for this; installing it once is fine).
- **Share instead of send:** `here-now` publishes any of it to a live URL.
