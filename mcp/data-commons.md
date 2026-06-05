# Add Data Commons — for the agent

**You are an AI coding agent (Claude Code or Codex). The user wants to add Google
Data Commons — one connection to ~240 harmonised public datasets (World Bank, WHO,
UN, US Census, the Australian Bureau of Statistics and more) so they can ask for
real statistics and get sourced numbers back.** This connects the `datacommons-mcp`
server, which powers the **public statistics** lane of the `web-searcher` agent in
this kit.

**A free API key is required** (Step 2). The only other requirement is `uv`; if
it's missing, install it in Step 1.

Explain each step to the user in plain English before you run it, and ask them to
approve any command. Then work through the steps for their runtime.

---

## Step 1 — Ensure `uv` is installed (both runtimes)

`datacommons-mcp` is a Python tool, and `uv` runs it without a manual install.
(If you already set up Paper Search, `uv` is in place — skip ahead.)

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

## Step 2 — Get the free API key (user, in browser)

Send the user to **https://apikeys.datacommons.org** — they sign in with Google,
create a key for the **datacommons.org** domain, and copy it. Free; no card.

## Step 3 (Claude Code) — add the server

The server launches with: `uvx datacommons-mcp@latest serve stdio`, and reads the
key from the `DC_API_KEY` environment variable.

**Preferred — use the CLI if it's available:**

```bash
claude mcp add datacommons --scope user --env DC_API_KEY=THEIR-KEY -- uvx datacommons-mcp@latest serve stdio
```

**If you get `claude: command not found`** (common when only the Claude Code
*desktop app* is installed, not the terminal CLI), add it by editing
`~/.claude.json` directly. Find the top-level `"mcpServers"` object (create it if
it isn't there) and add this entry **without disturbing anything else in the file**:

```json
"datacommons": {
  "type": "stdio",
  "command": "uvx",
  "args": ["datacommons-mcp@latest", "serve", "stdio"],
  "env": { "DC_API_KEY": "THEIR-KEY" }
}
```

If `uvx` isn't on PATH, replace `"uvx"` with its full path, e.g.
`"/Users/NAME/.local/bin/uvx"`.

The same `~/.claude.json` is read by **both** the Claude Code CLI and the Claude
Code desktop app, so this works in either.

## Step 3 (Codex) — add the server

Add the server to `~/.codex/config.toml`. Do **not** overwrite the file — append
this block (create the section if it isn't there):

```toml
[mcp_servers.datacommons]
command = "uvx"
args = ["datacommons-mcp@latest", "serve", "stdio"]
env = { DC_API_KEY = "THEIR-KEY" }
```

If `uvx` isn't on PATH, use its full path for `command`.

## Step 4 — Restart, then verify

MCP servers load at **startup**, so the new tools will **not** appear in the
current session.

1. Tell the user to fully **quit and reopen** Claude Code / Codex (a new session
   isn't enough in the desktop app — quit the app).
2. Then have them try:
   > *"Using Data Commons, what's the population trend of Australia over the last
   > 20 years? Cite the source."*
3. Confirm real figures with a source come back. Once they do, the `web-searcher`
   agent will also route statistics queries here automatically.

---

## Notes

- The key ends up in a config file (`~/.claude.json` / `~/.codex/config.toml`) —
  that's the supported pattern for MCP servers and those files stay on the user's
  machine. Still: never copy it into `CLAUDE.md` / `AGENTS.md`, a skill, or any
  synced/git-tracked folder.
- Good demo asks: unemployment by country, life expectancy comparisons,
  city-level census data, CO₂ emissions over time.
- **Sibling sources:** [`paper-search.md`](paper-search.md) covers academic
  literature (free, no key); [`openrouter.md`](openrouter.md) covers image
  generation + live/social search (one paid key). Together they fill out all of
  `web-searcher`'s lanes.
- Docs: <https://docs.datacommons.org/mcp> · PyPI: `datacommons-mcp`.
