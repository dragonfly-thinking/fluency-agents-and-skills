# Your Agent in the Browser — filling forms, reading pages, clicking buttons

**Why this matters:** a lot of your work lives in web apps that have no export button
and no API — portals, forms, dashboards, booking systems. A **browser agent** lets
your AI drive a real browser: navigate, read pages, click, and fill forms, while you
watch it happen. The kit's `browser-agent` skill teaches your agent the workflow;
this guide gets the tool installed and tells you the one safety rule that matters.

**Point your agent at this guide** and say: *"set up browser automation for me
following this."*

---

## ⚠️ The one safety rule, before anything else

A browser agent inherits **every login of the browser profile it runs in**. If it
browses arbitrary pages while logged into your email, a malicious page's hidden
instructions become a real attack (this is *prompt injection*, now with your logins
attached).

**Rule: browser agents get their own browser.** The tool below launches its own
clean browser by default — logged into nothing — which is exactly what you want.
Don't connect it to your daily browser profile unless you've thought hard about why.

## Install (agent-followable)

The tool is **`agent-browser`** — a free command-line tool that works identically
under Claude Code and Codex (it's just a command; no per-runtime setup).

**You are an AI agent installing this — steps, verifying each:**

1. **Node.js** — check `node --version`. If missing, install it (macOS:
   `brew install node`; Windows: `winget install OpenJS.NodeJS.LTS`; or
   [nodejs.org](https://nodejs.org)).
2. **The CLI** — `npm install -g agent-browser`, then check `agent-browser --version`.
3. **The browser engine** — run `agent-browser install`. ⚠️ **Known trap:** on some
   machines this fetches the wrong build and later commands fail with *"Executable
   doesn't exist… chromium-XXXX"*. The reliable fix: check the pinned Playwright
   version (`npm ls -g agent-browser` → its `playwright` dependency, e.g. `1.57.0`)
   and run `npx playwright@<that version> install chromium` (~160 MB, one-time).
4. **Verify end-to-end** (a visible browser window should open):
   ```bash
   agent-browser open --headed https://example.com
   agent-browser snapshot -i -c    # should list the page's links with @refs
   agent-browser close
   ```

## The workflow (what the skill automates)

```bash
agent-browser open --headed <url>   # --headed = visible browser, watch it work
agent-browser snapshot -i           # THE key step: lists interactive elements as @e1, @e2…
agent-browser click @e3             # act using refs from the snapshot
agent-browser fill @e5 "text"
agent-browser close
```

Two rules the whole thing hinges on:
- **Snapshot before refs.** `@e1` only exists after a `snapshot` — and refs go stale
  when the page changes, so re-snapshot after navigating or submitting.
- **Headed while you're learning.** Watching the browser is both the demo and the
  debugging.

## Three things to try

1. **Fill a form from a file** — the course demo. Write a messy notes file about a
   (fictional!) person, then: *"Open
   https://courses-visuals.dragonflythinking.com/fluency-demo-form/ and fill it out
   based on my notes file."* That form is a safe practice target: it's a dead demo
   page that submits nothing and shows a confirmation code your agent can report back.
   Notice the agent doesn't copy — it *composes* the bio and *decides* the dropdowns.
2. **Extract what a page won't give you** — *"open this dashboard, snapshot it, and
   give me the table as Markdown."*
3. **A repeating check** — *"each morning, open the grants portal and tell me if
   anything new is listed"* (pairs with routines — see the Session 4 notes).

## Troubleshooting

| Symptom | Fix |
|---|---|
| `Executable doesn't exist… chromium-XXXX` | Step 3's pinned-Playwright fix |
| `Unsupported token "@e1"` | You skipped `snapshot` — snapshot first, then act |
| Element not found after clicking around | Refs went stale — re-snapshot |
| A login wall | Stop and ask the user — don't have the agent handle credentials; log in yourself in the agent's browser window, then let it continue |
| CAPTCHA | That's the site saying "humans only" — respect it; do that step yourself |

**Where it doesn't belong:** sites you're logged into with real money or real
sensitivity (banking, patient records), and anything a site's terms forbid
automating. When in doubt, drive; let the agent navigate.
