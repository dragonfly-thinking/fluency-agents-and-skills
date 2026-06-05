# Add Paper Search — for the agent

**You are an AI coding agent (Claude Code or Codex). The user wants to add the
Paper Search data source so they can search academic literature — arXiv, PubMed,
bioRxiv, Semantic Scholar and ~20 more — just by asking.** This connects the
`paper-search` MCP server, which powers the **academic / papers** lane of the
`web-searcher` agent in this kit.

**No API key is needed.** The only requirement is `uv` (a fast Python runner); if
it's missing, install it in Step 1.

Explain each step to the user in plain English before you run it, and ask them to
approve any command. Then work through the steps for their runtime.

---

## Step 1 — Ensure `uv` is installed (both runtimes)

`paper-search-mcp` is a Python tool, and `uv` runs it without a manual install.

Check first:

```bash
uv --version || echo "uv not found"
```

If it's not found, install it:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing, `uv` / `uvx` lives in `~/.local/bin`. If `uvx` still isn't found
on PATH, use the full path `~/.local/bin/uvx` wherever `uvx` appears below.

> ⚠️ Do **not** run `uvx paper-search-mcp` on its own — the package ships no
> executable and errors with *"does not provide any executables."* You must use
> the `--from paper-search-mcp python -m paper_search_mcp.server` form below.

---

## Step 2 (Claude Code) — add the server

The server launches with: `uvx --from paper-search-mcp python -m paper_search_mcp.server`

**Preferred — use the CLI if it's available:**

```bash
claude mcp add paper-search --scope user -- uvx --from paper-search-mcp python -m paper_search_mcp.server
```

**If you get `claude: command not found`** (common when only the Claude Code
*desktop app* is installed, not the terminal CLI), add it by editing
`~/.claude.json` directly. Find the top-level `"mcpServers"` object (create it if
it isn't there) and add this entry **without disturbing anything else in the file**:

```json
"paper-search": {
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "paper-search-mcp", "python", "-m", "paper_search_mcp.server"],
  "env": {}
}
```

If `uvx` isn't on PATH, replace `"uvx"` with its full path, e.g.
`"/Users/NAME/.local/bin/uvx"`.

> Do **not** use the Smithery `--client claude` install command — it targets
> *Claude Desktop* (the chat app), not Claude Code, so the server won't appear in
> the user's sessions.

The same `~/.claude.json` is read by **both** the Claude Code CLI and the Claude
Code desktop app, so this works in either.

---

## Step 2 (Codex) — add the server

Add the server to `~/.codex/config.toml`. Do **not** overwrite the file — append
this block (create the section if it isn't there):

```toml
[mcp_servers.paper-search]
command = "uvx"
args = ["--from", "paper-search-mcp", "python", "-m", "paper_search_mcp.server"]
```

If `uvx` isn't on PATH, use its full path for `command`.

---

## Step 3 — Restart, then verify

MCP servers load at **startup**, so the new tools will **not** appear in the
current session.

1. Tell the user to fully **quit and reopen** Claude Code / Codex (a new session
   isn't enough in the desktop app — quit the app).
2. Then have them try:
   > *"Search arXiv for recent papers on large language models — show me 3, with
   > titles and abstracts."*
3. Confirm real paper titles and abstracts come back. Once they do, the
   `web-searcher` agent will also route academic queries here automatically.

---

## Notes

- **Free, no key:** arXiv, PubMed, bioRxiv, medRxiv, Semantic Scholar, Crossref,
  IACR and more.
- **Sibling sources:** for public statistics — population, economy, health,
  demographics — [`data-commons.md`](data-commons.md) fills the other lane of
  `web-searcher` (free API key). For image generation and live/social search,
  see [`openrouter.md`](openrouter.md).
- Source repo: <https://github.com/openags/paper-search-mcp>. Follow **this**
  guide, not the repo's README — its `uvx` and Smithery commands have the traps
  noted above.
