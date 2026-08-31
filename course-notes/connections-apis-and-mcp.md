# Connections, APIs & MCP

*Reaching outside the building — letting your agent talk to the services and data sources you already use.*

Everything so far has happened **inside your own machine**: an agent in your folders, working on your files, with the procedures and specialists you gave it. This is about the other direction — connecting it to things that live elsewhere, so it can fetch its own inputs rather than waiting for you to paste them in.

The good news is that you don't need to understand any of the plumbing. You need three words and one habit.

---

## Three words

- **API** — the way one piece of software talks to another. Think of a restaurant with two doors: humans walk in and order at the counter; other software calls the kitchen directly through the side window. Almost every service that delivers something has one.
- **API key** — your account identifier. It tells the service who's calling, what they're allowed to reach, and who to bill. Some services need one; many don't.
- **MCP** (Model Context Protocol) — a newer standard *on top of* APIs that makes it easy for agents specifically to discover and use external tools. You'll see the acronym everywhere. You never need to understand the protocol; your agent does.

**The habit:** when you want to connect something, search *"[tool name] MCP"* — and if that comes up empty, *"[tool name] API"*. The API is the plumbing underneath; the MCP sits on top and is the agent-friendly path. **Prefer the MCP where one exists.**

Then just say: *"set this up for me."* The setup is the agent's job, not yours.

## The connector menu

Before you go looking for anything, check what's already one click away.

- **Claude Desktop:** **Customize → Connectors** in the sidebar. Browse, click "+" to add. Most are a login and nothing else.
- **Codex:** the **Plugins** menu. Same experience, different name.

Gmail, Outlook, Google Drive, SharePoint, Notion and similar are usually here, pre-built. On a managed work laptop, some of these will need your administrator to approve the permission — which is itself worth knowing before you promise anyone a demo.

## What connecting actually buys you

It is easy to overstate this, so here is the honest version.

**An unconnected agent is not helpless.** Ask it a statistical question and it will go and *search the web* — it does not answer from memory. What you get back is a slow, unreliable search: possibly the wrong year, possibly a secondary source quoting a figure it has itself misread, possibly nothing usable.

**A connected agent queries the source.** Fast, authoritative, the right year, with an identifier you can check — and it works across a whole range of subjects rather than one lucky search.

That's the trade. Not *impossible* versus *possible*; **unreliable and slow** versus **authoritative and fast**. Which matters enormously when the number ends up in something you send.

## A worked example — Data Commons

[Data Commons](https://datacommons.org) is Google's harmonised aggregator across **180+ public datasets from 85+ official sources** — World Bank, WHO, UN, OECD, US Census, national statistics agencies, NOAA. It is free, and it is the connection most likely to be immediately useful to people doing research or analysis.

Full agent-followable setup: **[`../mcp/data-commons.md`](../mcp/data-commons.md)** — point your agent at that page and say *"follow this and set it up for me."* The shape of it:

1. **Create an account** and generate a free key at `apikeys.datacommons.org` — *New app*, name it, copy the key.
2. ⚠️ **Scope the key to `api.datacommons.org`, not `datacommons.org`.** The wrong domain fails as `✘ Failed to connect` with no explanation, and you will not guess it.
3. **Let your agent do the install**, following the guide.
4. **Test it properly.** Ask a real question and require a **DCID** — Data Commons' own identifier for the thing you asked about — in the answer. Don't accept a source URL as proof: a plain web search returns one of those too. A DCID is the one thing a search cannot produce, so it's the only test that actually distinguishes "connected" from "searched".

## Other free public-data connections

| Connection | What it unlocks | Key? |
|---|---|---|
| [`../mcp/data-commons.md`](../mcp/data-commons.md) | 180+ public datasets from 85+ official statistical sources | Free key |
| [`../mcp/paper-search.md`](../mcp/paper-search.md) | Academic literature — arXiv, PubMed, Semantic Scholar, OpenAlex, Crossref, SSRN and more | None to start |
| [`../mcp/openrouter.md`](../mcp/openrouter.md) | Live cited search, social search, image generation, high-fidelity PDF conversion | One paid key |

> ⚠️ **Read the warning at the top of the Paper Search guide before installing it.** The server it connects to includes tools that download from **Sci-Hub**, reached **automatically as a fallback** rather than only when you ask for it. Whether that is fine or a serious problem depends entirely on whose machine you're on and what your organisation's position is. The guide explains it and shows how to block those two tools if you'd rather they couldn't run. Make the call with the facts.

Together these fill out the kit's `web-searcher` subagent's lanes — it routes a query to whichever source fits and falls back to ordinary web search when a lane isn't set up.

## Connections compose into skills

This is where it stops being a party trick. Just as a [skill](skills.md) can dispatch a [subagent](subagents.md), a skill can **bake a connection into its instructions**: *"when researching, pull statistics from these sources I've already connected."*

So the connection stops being something you remember to use and becomes part of a recipe that fires automatically. That's the composition that makes a genuinely capable setup: procedure → specialist → data source, chained, with you describing the job in plain English.

## Security, honestly

Connecting an agent to external services expands what it can reach, and that is exactly what makes **prompt injection** a live concern rather than a theoretical one — a page it fetches is text aimed at your agent, and it can carry instructions. Read [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md) § *Prompt injection* before you connect anything to your email, and apply the limit it lands on: **it drafts, you send.**

- **Keys are credentials.** Never write one into a file your agent might publish or sync. If you paste one into a chat, ask where it should actually live.
- **Scope keys narrowly** where the service lets you, and delete ones you stop using.
- **You don't need the terminal for any of this**, but it occasionally surfaces — when the agent is blocked and asks you to run something yourself, or when wiring up a tool that has no first-class connector. It's a window under the hood of your computer, and the agent will tell you exactly what to type.

## Try this

> Look at what I actually work on. Search for whether there's an MCP or an API for the two
> or three tools and data sources I'd most benefit from reaching — tell me what you find,
> including where you found nothing. Then set up the easiest useful one with me, and prove
> it's working with a query I can check.
