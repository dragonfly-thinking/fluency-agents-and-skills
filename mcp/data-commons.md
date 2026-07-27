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
(If `uv` is already in place from something else, skip ahead.)

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
create a key for the **`api.datacommons.org`** domain, and copy it. Free; no card.

> ⚠️ **The domain must be `api.datacommons.org`, not `datacommons.org`.** The
> server validates the key against `https://api.datacommons.org/...` at startup,
> so a key scoped to the wrong domain fails with a 401 — which, inside Claude
> Code, shows up only as `✘ Failed to connect` with no reason given. Don't
> "simplify" this to `datacommons.org`.

## Step 3 (Claude Code) — add the server

The server launches with: `uvx datacommons-mcp@latest serve stdio`, and reads the
key from the `DC_API_KEY` environment variable.

**Preferred — use the CLI if it's available:**

```bash
claude mcp add datacommons --scope user --env DC_API_KEY=THEIR-KEY -- uvx datacommons-mcp@latest serve stdio
```

**If you get `claude: command not found`**, first check the Claude Code desktop
app's built-in terminal (Ctrl-`) — the desktop app ships the CLI, so `claude mcp
add` is usually available there and the command above is still the safest route.

If you genuinely have no CLI, edit `~/.claude.json` directly. **Back it up first**
— that file also holds your login session, so a stray comma logs you out, not
just breaks the server:

```bash
cp ~/.claude.json ~/.claude.json.bak
```

Find the top-level `"mcpServers"` object (create it if it isn't there) and add
this entry **without disturbing anything else in the file**:

```json
"datacommons": {
  "type": "stdio",
  "command": "uvx",
  "args": ["datacommons-mcp@latest", "serve", "stdio"],
  "env": { "DC_API_KEY": "THEIR-KEY" }
}
```

**Use the full path to `uvx`, not the bare command** — e.g.
`"/Users/NAME/.local/bin/uvx"` (run `which uvx` to find it). An app launched from
the Dock doesn't inherit your terminal's PATH, so a bare `"uvx"` is a common cause
of `✘ Failed to connect` for exactly the people using this fallback.

> ⚠️ **Which app do they actually have?** This matters and is easy to get wrong:
> - **Claude Code** — the CLI, or the Code tab of the desktop app → `~/.claude.json`, as above. ✅
> - **The Claude chat app** (the everyday Claude desktop app) → a *different*
>   file: `~/Library/Application Support/Claude/claude_desktop_config.json`
>   (Windows: `%APPDATA%\Claude\`), with its own `mcpServers` key.
>
> Someone who says "I have the Claude desktop app" usually means the chat app.
> Editing `~/.claude.json` for them does nothing at all, with no error. Ask which
> one before you edit anything.

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

2. **Check the connection structurally — do this before asking any question.**
   - *Claude Code:* run `/mcp` in a fresh session. `datacommons` must be listed
     with 2 tools. `✘ Failed to connect` means it did **not** work — go to
     Troubleshooting; don't proceed.
   - *Codex:* `codex mcp list` only proves the config was written, **not** that
     the server runs. Instead run this in a terminal:
     ```bash
     DC_API_KEY=THEIR-KEY uvx datacommons-mcp@latest serve stdio
     ```
     A working key prints that the server is ready; a broken one prints the real
     reason and exits. Ctrl-C to stop it, then carry on.

3. **Then ask something the model cannot already know**, and demand provenance:
   > *"Using Data Commons, get the latest unemployment rate for Ballarat,
   > Victoria. Give me the exact variable DCID and the provenance URL the tool
   > returned."*

   A DCID and a provenance URL can only come from the tool. Prose without them
   means the agent answered from memory and the server is **not** connected.

> ⚠️ **Why not just ask about Australia's population?** Because Claude already
> knows it. With the server completely broken, it will answer from memory, cite
> "the ABS", and look exactly like success. A check that passes when the thing is
> broken is worse than no check — it manufactures false confidence. Always verify
> with something only the tool could have produced.

Once that passes, the `web-searcher` agent will also route statistics queries
here automatically.

## Troubleshooting

Inside Claude Code every failure looks identical — `✘ Failed to connect` — so run
the server by hand (the Codex command in step 2 above works on any machine) and
read the real error:

| What the server prints | What it means |
|---|---|
| `command not found: uvx` | `uv` isn't on your PATH — use the full path, e.g. `~/.local/bin/uvx` |
| `DC_API_KEY is not set` | The `env` block didn't reach the server — check the config entry |
| `API key is invalid or has expired. Status: 401` | Mistyped key, **or a key created for the wrong domain** (see Step 2) |
| Server says it's ready, but tools still missing | The server is fine — the problem is the config file or you didn't fully quit the app |

> ⚠️ **Don't add `--skip-api-key-validation`.** It's the first thing a search
> result will suggest, and it makes things worse: the server then reports
> `✔ Connected` with a completely invalid key, and every query fails silently
> instead. If you're tempted to add it, the key is the problem — fix the key.

---

## Notes

- The key ends up in a config file (`~/.claude.json` / `~/.codex/config.toml`) —
  that's the supported pattern for MCP servers and those files stay on the user's
  machine. Still: never copy it into `CLAUDE.md` / `AGENTS.md`, a skill, or any
  synced/git-tracked folder.
- Good demo asks: unemployment by country, life expectancy comparisons,
  city-level census data, CO₂ emissions over time.
- **Name it `datacommons`.** The `web-searcher` agent is wired to that exact
  name — calling it `data-commons` breaks the integration silently.
- **What the numbers are, and aren't.** Data Commons harmonises **180+ datasets
  from 85+ official sources** — genuinely broad, but not complete or uniform:
  - **Coverage is uneven and the maintainers say so** — some surveys are only
    partially imported. A gap is not evidence that the statistic doesn't exist.
  - **Vintage varies by source.** "Latest" can mean last year or five years ago.
    Ask for the observation date rather than assuming it's current.
  - **Most variables have competing sources, and the server picks one for you.**
    It returns a primary source plus `alternative_sources` — chosen by an
    internal heuristic, not by authority. So "cite the source" gives you *a*
    source, while others with different numbers sit in the same response. For
    anything consequential, ask what the alternatives said.
  - **The headline source list is not proportional.** World Bank, UN and US
    Census are deep; **WHO is essentially one COVID-19 dataset**. A health
    question will usually be answered from World Bank or UN data, not WHO.
  - **No data returns empty, not an error** — the same shape as a working query
    that found nothing.
  - **The rule that covers all of it:** if an answer has no DCID and no
    provenance URL, it came from the model's memory, not from Data Commons.
- **Where your queries go:** every request hits Google's `api.datacommons.org`
  carrying your key. Worth knowing on a firm or government machine.
- **Sibling source:** [`openrouter.md`](openrouter.md) covers image generation +
  live/social search (one paid key). Academic literature is handled by ordinary
  web search for now (see the README).
- Docs: <https://docs.datacommons.org/mcp> · PyPI: `datacommons-mcp`.
