# VS Code Setup — the shared workspace, with the recommended extensions

**Why bother:** VS Code, Claude Code and Codex are all just **windows into the
same folder**. Working in VS Code doesn't replace your agent — it puts you *next
to it*: you see every file it touches, make the last-15% edits yourself, and
preview Markdown, PDFs and spreadsheets in place instead of round-tripping
through other apps.

You can follow this yourself in ten minutes, or point your agent at it:
*"read `guides/vscode-setup.md` and set me up."*

---

## 1. Install VS Code and open your workspace

1. Download from [code.visualstudio.com](https://code.visualstudio.com) (free,
   Mac/Windows/Linux).
2. **File → Open Folder…** and choose your workspace folder — the same one you
   point Claude/Codex at. The **file tree** on the left now mirrors your folder:
   click to open anything, right-click to create files and folders.

## 2. The recommended extensions

Install from the Extensions icon in the left sidebar (the four squares) — search
the name, click Install. Or have your agent do it in one go with the IDs below.

| Extension | What it does | ID |
|---|---|---|
| **Claude Code** (Anthropic — verified publisher) | The full agent as a sidebar in your workspace | `anthropic.claude-code` |
| **Codex** (OpenAI — verified publisher) | Same, for Codex | `openai.chatgpt` |
| **Office Viewer** | Open **Word, Excel, PowerPoint and PDF** files in place | `cweijan.vscode-office` |
| **Rainbow CSV** | Makes CSV files readable (colour-codes the columns) | `mechatroner.rainbow-csv` |
| **PDF viewer** *(optional — Office Viewer already covers PDFs)* | A dedicated, snappier PDF tab | `tomoki1207.pdf` |

**Markdown preview needs no extension** — it's built in. With a `.md` file open,
press **⌘⇧V** (Mac) / **Ctrl+Shift+V** (Windows), or click the preview icon
(magnifying-glass-on-page, top right) for a side-by-side view.

Agent-followable install (one line per extension, from a terminal):

```bash
code --install-extension anthropic.claude-code
code --install-extension openai.chatgpt
code --install-extension cweijan.vscode-office
code --install-extension mechatroner.rainbow-csv
```

(If `code` isn't recognised: in VS Code, ⌘⇧P / Ctrl+Shift+P → *"Shell Command:
Install 'code' command in PATH"* — then retry.)

## 3. The workflow that makes it worth it

- **Agent in the sidebar, files in the middle.** Open the Claude or Codex panel;
  everything it does happens in the tree in front of you, live.
- **Draft in Markdown where the agent can see it.** Create `writing.md`, brain-dump
  or scaffold, then: *"read my `writing.md` and turn it into a report in this
  style."* No copy-paste shuffle — and when the output is 85% right, you edit the
  remaining 15% directly instead of prompting for it.
- **Copy Path** (right-click any file) to hand the agent an exact address, or
  **@-tag** the file by name in the chat — faster and more reliable than making it
  search.
- **Preview everything in place**: the PDF the agent just made, the CSV it
  produced, your Markdown notes — no leaving the window.

## 4. Two small settings worth making

- **Autosave**: File → Auto Save (tick it). The agent reads files from disk —
  autosave means it always sees your latest edits.
- **Word wrap** for prose: ⌘⇧P / Ctrl+Shift+P → *"Toggle Word Wrap"* — so long
  paragraphs wrap instead of scrolling sideways.

---

*All five extension IDs above re-verified on the VS Code marketplace on 2026-09-01
— every one still resolves under the ID given, from the publisher named. (Note
`openai.chatgpt` now displays as "Codex — OpenAI's coding agent"; the ID is
unchanged.) If one won't install, search the name in the Extensions panel rather
than assuming the guide is broken — publishers occasionally rename.*
