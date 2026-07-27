# Add Paper Search — for the agent

**You are an AI coding agent (Claude Code or Codex). The user wants to add the
Paper Search data source so they can search academic literature — arXiv, PubMed,
bioRxiv, Semantic Scholar and around twenty more — just by asking.** This connects
the `paper-search` MCP server, which powers the **academic / papers** lane of the
`web-searcher` agent in this kit.

**No API key is needed to get started.** The only requirement is `uv` (a fast
Python runner); if it's missing, install it in Step 1.

Explain each step to the user in plain English before you run it, and ask them to
approve any command. Then work through the steps for their runtime.

---

## ⚠️ Read this to the user before installing — it's their call to make

This server is genuinely useful, and it also ships **two tools that download
papers from Sci-Hub**, the paywall-bypass site. We're telling you rather than
deciding for you, but you need one detail to decide properly:

**It isn't a button you choose to press. It's an automatic fallback.** The
server's `download_with_fallback` tool has Sci-Hub **on by default**
(`use_scihub=True`). Ask your agent for a paper's full text, and if the
open-access routes fail, it goes to Sci-Hub on its own — without asking you.
There's also a standalone `download_scihub` tool. Neither can be switched off
from the server's own settings.

**Whether that matters is about where you work, not about the tool.** On a
university or law-firm machine this can breach IT policy, publisher licence
terms, or your institution's copyright position — and in some jurisdictions it's
a legal question, not just a policy one. On your own machine for your own reading,
you may take a different view. That's yours to take.

**If you'd rather it simply couldn't happen**, block the two tools. In Claude Code
this is enforced, not advisory — add to `~/.claude/settings.json`:

```json
{
  "permissions": {
    "deny": [
      "mcp__paper-search__download_scihub",
      "mcp__paper-search__download_with_fallback"
    ]
  }
}
```

Searching, reading abstracts, and the direct per-source downloads
(`download_arxiv`, `download_pubmed`, and so on) all keep working — you lose the
one convenience function that chains through fallbacks. Worth it if you're on an
institutional machine.

> **On Codex there is no equivalent enforcement.** Codex has no per-tool deny
> rules, so the only lever is instruction: tell your agent, in your `AGENTS.md`,
> never to call `download_scihub` and to pass `use_scihub=False` if it uses
> `download_with_fallback`. That's a request, not a block — if that isn't good
> enough for your setting, don't install this server on the Codex side.

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

`uv` / `uvx` normally lands in `~/.local/bin`. Run `which uvx` to find it — if it
isn't on PATH, use the full path wherever `uvx` appears below.

---

## Step 2 (Claude Code) — add the server

```bash
claude mcp add paper-search --scope user -- uvx --from paper-search-mcp python -m paper_search_mcp.server
```

**If you get `claude: command not found`**, check the Claude Code desktop app's
built-in terminal (Ctrl-`) — the desktop app ships the CLI, so the command above
usually works there.

Failing that, edit `~/.claude.json` directly. **Back it up first** — that file
also holds your login session, so a stray comma logs you out:

```bash
cp ~/.claude.json ~/.claude.json.bak
```

Find the top-level `"mcpServers"` object (create it if absent) and add:

```json
"paper-search": {
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "paper-search-mcp", "python", "-m", "paper_search_mcp.server"],
  "env": {}
}
```

Use the **full path** to `uvx` rather than the bare command — an app launched from
the Dock doesn't inherit your terminal's PATH, and that's a common cause of a
server that silently won't start.

> **Which app do they have?** `~/.claude.json` is right for **Claude Code** (the
> CLI, or the Code tab of the desktop app). The **Claude chat app** uses a
> different file — `~/Library/Application Support/Claude/claude_desktop_config.json`
> (Windows: `%APPDATA%\Claude\`). Someone saying "the Claude desktop app" usually
> means the chat one, and editing the wrong file does nothing at all, silently.

---

## Step 2 (Codex) — add the server

Use the CLI — it edits the file safely:

```bash
codex mcp add paper-search -- uvx --from paper-search-mcp python -m paper_search_mcp.server
```

If you're editing `~/.codex/config.toml` by hand instead, **paste at the very end
of the file**. TOML keys that follow a `[table]` header belong to that table, so
pasting mid-file can silently swallow settings that come after it:

```toml
[mcp_servers.paper-search]
command = "uvx"
args = ["--from", "paper-search-mcp", "python", "-m", "paper_search_mcp.server"]
```

---

## Step 3 — Restart, then verify

MCP servers load at **startup**, so new tools will **not** appear in the current
session. Have the user fully **quit and reopen** Claude Code / Codex.

**1. Check the connection first.**
- *Claude Code:* run `/mcp`. `paper-search` should be listed with its tools. If it
  says failed to connect, stop and troubleshoot — don't proceed to the query.
- *Codex:* `codex mcp list` only proves the config was written, not that the server
  runs. Instead run the launch command in a terminal and confirm it starts; Ctrl-C
  to stop.

**2. Then ask for something the model cannot already know**, and require a link:

> *"Using Paper Search, find me three arXiv papers from the last two months on
> [their niche topic]. Give me the arXiv ID and URL for each."*

IDs and URLs can only come from the tool. A fluent answer with no IDs means the
agent answered from memory — the server isn't connected. A general question like
"find papers on large language models" can't tell the difference, because the
model can answer that unaided.

---

## Troubleshooting

| Symptom | Cause |
|---|---|
| `command not found: uvx` | Not on PATH — use the full path from `which uvx` |
| Server won't start | Run the launch command in a terminal and read the actual error |
| Startup warnings about CORE / DOAJ / Unpaywall keys | Normal and ignorable — those are optional extras (see below) |
| Searches return nothing, repeatedly | Often rate-limiting rather than absence — see the honesty note below |

---

## Notes — what to expect, honestly

- **"No key needed" is true to get started, not the whole story.** arXiv, Crossref,
  OpenAlex, Europe PMC, bioRxiv and medRxiv work keyless and well. **Semantic
  Scholar** shares one rate limit across every unauthenticated user worldwide and
  is frequently exhausted; **PubMed** throttles unkeyed traffic. Free keys lift
  both (`SEMANTIC_SCHOLAR_API_KEY`, and `CORE_API_KEY` / `UNPAYWALL_EMAIL` for
  those sources) — pass them with `claude mcp add … -e KEY=value`.

- **A rate-limited search returns "nothing found", not an error.** This is the
  single most important thing on this page. The server hands the agent an empty
  result marked as success, so **your agent cannot tell "I was throttled" from
  "no such work exists."** If a search comes back empty, treat it as *unknown*,
  not as absence — retry, and ask which sources actually responded.

- **Never cite a paper you haven't opened.** An agent with nothing to cite is an
  agent tempted to produce a plausible-looking reference. Open the DOI or arXiv
  link and check the title matches before anything goes in a footnote. This
  matters more here than anywhere else in the kit.

- **Coverage is uneven.** Around twenty sources are wired up, but a given search
  typically gets useful results from a handful. It skews STEM and preprints —
  arXiv, bioRxiv, medRxiv, PubMed. Law, humanities and social science are thin,
  and IACR is cryptography only. Absence of results is weak evidence of absence.

- **Full text is often unavailable.** Open-access preprints can be read in full;
  paywalled journal articles usually give you title, abstract and metadata only.

- **Sibling sources:** [`data-commons.md`](data-commons.md) covers public
  statistics (free key); [`openrouter.md`](openrouter.md) covers image generation
  and live/social search (one paid key).

- Source repo: <https://github.com/openags/paper-search-mcp>. Its README carries
  the maintainers' own note on the Sci-Hub connector — worth reading alongside the
  warning at the top of this page.
