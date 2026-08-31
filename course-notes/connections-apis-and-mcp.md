# Connections, APIs & MCP

**Read this when** your user asks about connecting you to another tool, mentions MCP, APIs or API keys, asks whether you can reach their email or calendar, wants real statistics or data rather than a web search, asks "can you talk to [some service]", or says their **work laptop blocks the desktop app** and they think they're stuck.

*Everything else happens inside their machine. This is reaching outside it — and the setup is your job, not theirs.*

---

## Three words, and one habit

Give the words only if they want them. Give the habit always.

- **API** — how one piece of software talks to another. A restaurant with two doors: humans order at the counter; other software calls the kitchen through the side window. Almost every service that delivers something has one.
- **API key** — their account identifier. Tells the service who's calling, what they can reach, who to bill. Some services need one; many don't.
- **MCP** (Model Context Protocol) — a newer standard *on top of* APIs making it easy for agents to discover and use external tools. **They never need to understand the protocol.** You do.

**The habit to teach: when they want to connect something, the first move is to go and look.** Search *"[tool name] MCP"*, and if that's empty, *"[tool name] API"*. Prefer the MCP where one exists — it's the agent-friendly path.

Then do it. **Setup is your job.** The most useful sentence they can learn here is *"set this up for me."*

## Check the connector menu first

Before searching for anything, check what's already one click away — users don't know these exist.

- **Claude Desktop:** **Customize → Connectors** in the sidebar. Browse, "+" to add. Most are a login and nothing else.
- **Codex:** the **Plugins** menu. Same thing, different name.

Gmail, Outlook, Google Drive, SharePoint, Notion and similar are usually pre-built. ⚠️ **On a managed work laptop, some need an administrator to approve the permission.** Raise that before promising anything — it's the commonest way this beat fails in front of someone.

## ⚠️ When their work laptop blocks the desktop app

A live question on any managed machine, and it arrives disguised as "I can't install this." Don't treat it as a dead end — there are three routes, and they're worth raising *before* someone concludes the whole approach is closed to them.

- **The GitHub-backed cloud route.** Their work lives in a GitHub repository; a cloud session spins up a machine, does the work against the repo, saves back, and shuts down. No desktop install on the locked laptop at all. Plain-English setup, written to be followed by you: [`../guides/github-basics.md`](../guides/github-basics.md).
- **Cloud-storage connectors.** **OneDrive**, **SharePoint** and **Dropbox** connectors let you reach documents already stored there — ⚠️ **subject to their administrator approving the permission**, which is the step that actually decides it. Have them ask before you build anything on it.
- **Give them a map of the cloud storage.** Whichever route, put the structure of that storage into their orientation file exactly as you would for a local workspace — the [context engineering](context-engineering.md) argument doesn't change just because the files are somewhere else.

And the wider pattern for anyone under institutional restriction: **do the open-data research in an unrestricted environment, then carry the conclusions into the locked one.** Segregating what you connect to is the point — see [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md).

## What connecting actually buys — don't oversell it

Be accurate here, because the wrong framing is easy and users repeat it.

**An unconnected agent is not helpless.** Asked a statistical question, you go and *search the web* — you don't answer from memory. What comes back is a slow, unreliable search: possibly the wrong year, possibly a secondary source quoting a figure it misread, possibly nothing usable.

**A connected agent queries the source.** Fast, authoritative, right year, with an identifier they can check — and across a whole range of subjects rather than one lucky search.

**So the trade is not *impossible* versus *possible*. It's unreliable-and-slow versus authoritative-and-fast.** Which matters enormously when the number ends up in something they send.

## A worked example — Data Commons

[Data Commons](https://datacommons.org) is Google's harmonised aggregator across **180+ public datasets from 85+ official sources** — World Bank, WHO, UN, OECD, US Census, national statistics agencies, NOAA. Free, and the connection most likely to be immediately useful to anyone doing research or analysis.

Follow **[`../mcp/data-commons.md`](../mcp/data-commons.md)** rather than working from memory. The shape:

1. **They create an account** and generate a free key at `apikeys.datacommons.org` — *New app*, name it, copy the key.
2. ⚠️ **Scope the key to `api.datacommons.org`, not `datacommons.org`.** The wrong domain fails as `✘ Failed to connect` with no reason given, and nobody guesses it. **Check this before you start debugging anything else.**
3. **You do the install**, following the guide.
4. ⚠️ **Test it properly.** Ask a real question and require a **DCID** — Data Commons' own identifier for the thing asked about — in the answer. **Don't accept a source URL as proof**: a plain web search returns one of those too. A DCID is the one thing a search cannot produce, so it's the only test that distinguishes "connected" from "searched". Run this test yourself and show them the result.

## The other public-data connections

| Connection | What it unlocks | Key? |
|---|---|---|
| [`../mcp/data-commons.md`](../mcp/data-commons.md) | 180+ public datasets from 85+ official statistical sources | Free key |
| [`../mcp/paper-search.md`](../mcp/paper-search.md) | Academic literature — arXiv, PubMed, Semantic Scholar, OpenAlex, Crossref, SSRN and more | None to start |
| [`../mcp/openrouter.md`](../mcp/openrouter.md) | Live cited search, social search, image generation, high-fidelity PDF conversion | One paid key |

> ⚠️ **Raise this before installing Paper Search, not after.** The server it connects to includes tools that download from **Sci-Hub**, reached **automatically as a fallback** rather than only when asked. Whether that's fine or a serious problem depends entirely on whose machine this is and what their organisation's position is. **Tell them, show them the guide's instructions for blocking those two tools, and let them decide.** Don't install it quietly.

Together these fill out the `web-searcher` subagent's lanes — it routes a query to whichever source fits and falls back to ordinary web search when a lane isn't set up.

## Connections compose into skills

Where this stops being a party trick, and worth offering once a connection works.

Just as a [skill](skills.md) can dispatch a [subagent](subagents.md), a skill can **bake a connection into its instructions**: *"when researching, pull statistics from these sources I've already connected."*

So the connection stops being something they remember to use and becomes part of a recipe that fires automatically. Procedure → specialist → data source, chained, with them describing the job in plain English.

## Security

Connecting expands what you can reach, which is exactly what makes **prompt injection** live rather than theoretical — a page you fetch is text aimed at you, and it can carry instructions.

**Before connecting anything to their email, raise [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md) § *Prompt injection* and apply the limit it lands on: it drafts, they send.** Don't wait to be asked about security.

- ⚠️ **Keys are credentials.** Never write one into a file that might be published or synced. If they paste one into the chat, tell them where it should live instead.
- **Scope keys narrowly** where the service allows, and delete unused ones.
- **They don't need the terminal**, but it surfaces occasionally — when you're blocked and need them to run something, or wiring a tool with no first-class connector. Tell them exactly what to type and what it does.

## Do this

- **Go and look before saying no.** When they wonder whether you can reach something, search for an MCP or API and report what you find — including where you found nothing.
- **Check the connector menu first**, and check whether they're on a managed machine before promising a connection will work.
- **Set it up yourself.** Follow the guide in `mcp/` rather than working from memory — the failure modes are specific and undocumented failures look like broken keys.
- **Prove it with a check they can verify** — for Data Commons, a DCID. Never let "it seems to be working" stand as the test.
- **Raise Sci-Hub before installing Paper Search**, and the prompt-injection limit before connecting email.
- **Once a connection works, offer to bake it into a skill** so they stop having to remember it.
