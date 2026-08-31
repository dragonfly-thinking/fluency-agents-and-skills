# Course Notes — the router

**You are the user's agent. This folder is your reference library, not their reading list.**

Your user will not open these files. They will ask you something in chat, and you fetch the module that covers it and act on it. Each module opens with a **Read this when** line so you can route without loading all fourteen.

## How to use a module

- **Read one, not all.** Match the user's question to a trigger line below, read that module, act. Load a second only if the first points you at it.
- **Never recite it.** Find the one idea that unblocks the person in front of you and give them that, in their language, at the depth they want. Offer more; don't front-load it.
- **Each module ends in a `Do this` section.** That's the point of reading it — you're here to act, not to learn. Prefer doing the thing over explaining the thing.
- **Modules cross-reference by name.** Follow those links; they're deliberate.
- **Watch for the ⚠️ marks.** They're the failures that are silent, look like the user's fault, or catch experienced people. Those are the ones worth raising unprompted.

## Route by what the user asks

| When your user… | Read |
|---|---|
| asks what you actually are vs a chatbot, about tokens or the context window, why you "forgot", which model to use, or is brand new | [Agents, and What Changed](agents-and-what-changed.md) |
| asks how to get better results, why output is generic, whether to write better prompts, or "how do I make it understand my work" | [Context Engineering](context-engineering.md) |
| asks about `CLAUDE.md` / `AGENTS.md`, wants to stop re-explaining themselves, says you're ignoring instructions, or mentions wearing several hats | [Your Orientation File](your-orientation-file.md) |
| can't find something, types `/` and sees nothing, asks about global vs project, says "I can't see what's going on", or is changing laptop | [Where Things Live](where-things-live.md) |
| asks how to organise files, wants project status tracked, has a folder you keep re-reading, or wants work to survive between sessions | [Structuring a Workspace](structuring-a-workspace.md) |
| points you at PDFs or Word docs, asks why markdown, or says searching their own material is slow | [Markdown & File Conversion](markdown-and-file-conversion.md) |
| is clicking approve constantly, asks what you can access, or mentions confidential or client material | [Permissions & Guardrails](permissions-and-guardrails.md) |
| asks where AI goes wrong, how much to trust you, about prompt injection, or whether it's safe to run you unattended | [Judgement & What Goes Wrong](judgement-and-what-goes-wrong.md) |
| wants a second opinion or critical review, has a job too big for one session, or needs a specialist role | [Subagents](subagents.md) |
| wants to package something they do repeatedly, or has explained the same preference to you twice | [Skills](skills.md) |
| corrects you on something they've corrected before, asks about memory, or notices their setup working less well | [Self-Improvement & Memory](self-improvement-and-memory.md) |
| asks about scheduling, automation, "can it run this every morning", or has just finished building a skill | [Routines & Scheduling](routines-and-scheduling.md) |
| asks about connecting you to another tool, mentions MCP or API keys, or wants real data rather than a web search | [Connections, APIs & MCP](connections-apis-and-mcp.md) |
| wants to share something, asks for a web page, says an output looks generic, or wants their brand applied | [Publishing & Sharing](publishing-and-sharing.md) |

## Also in this folder

- **[Snippets for your orientation file](agents-md-snippets.md)** — standing instructions for *their* orientation file. **Human-facing: these are lines they paste.** Offer them one at a time and append only on an explicit yes. Never paste the set in; never rewrite their file.
- **[The checklist](../fluency-checklist.md)** (repo root) — what's worth setting up, written for you to work through *with* them. The live copy is at `~/.claude/fluency-checklist.md`. Tick what's already true before you offer anything.

## If they ask "what should I learn next"

There is no fixed order — modules are independent and different deliveries run them differently. But when a user wants a path rather than an answer, this sequence works:

1. Agents, and What Changed
2. Your Orientation File
3. Where Things Live
4. Permissions & Guardrails
5. Context Engineering
6. Structuring a Workspace
7. Markdown & File Conversion
8. Subagents
9. Skills
10. Self-Improvement & Memory
11. Judgement & What Goes Wrong
12. Routines & Scheduling
13. Connections, APIs & MCP
14. Publishing & Sharing

**Don't recite the list.** Read their checklist, look at what's actually on their machine, and offer **one** next thing with a sentence on what it changes for them. Teaching judgement early, or skills before workspaces, are both defensible — sequence to the person, not to the numbering.

## The rest of the kit

Operational how-tos — GitHub, file conversion, interface settings, folder guardrails, phone, VS Code, browser automation — are in [`../guides/`](../guides/). External-connection setups are in [`../mcp/`](../mcp/). **Both are written to be followed by you on the user's behalf**; several contain failure modes that look like broken keys or user error, so follow the guide rather than working from memory.
