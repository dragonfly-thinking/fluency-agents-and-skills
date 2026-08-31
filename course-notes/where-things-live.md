# Where Things Live

**Read this when** your user can't find something, asks where their files or config actually are, types `/` and sees an empty list, asks about global versus project, says "I can't see what's going on", is deciding how to lay out folders, or is about to change laptop. Also read it whenever a skill or subagent you expect to exist isn't showing up — the answer is usually here.

*This is the module that resolves the most mysterious failures. Most of them are placement, not breakage.*

---

## The confusion to clear first

Everything is a folder. Their workspace is a folder, a project is a folder, your own configuration is a folder. They look identical and do completely different jobs, and that is why this feels impenetrable to new users.

- **Workspace, project and folder mean the same thing here.** When the interface says "working directory", *directory* means folder. Say so; the vocabulary alone blocks people.
- **The apps are windows onto the same files.** Claude, Codex, their file explorer, a markdown editor — all looking at one folder on disk. **Their setup is not locked to one AI**; switching tools doesn't mean rebuilding. Users find this genuinely reassuring and rarely think to ask.
- **Work stays on the machine it was made on** until they deliberately put it somewhere else. ⚠️ **Raise this before they change laptop, not after** — and note that their `.claude` / `.codex` folder is *not* included when they back up a project folder. That's the thing people lose. [`../guides/github-basics.md`](../guides/github-basics.md).

## The hidden dot-folders

- Configuration lives in **`.claude`** and **`.codex`**. The leading dot makes them hidden — their file explorer won't show them without a settings change.
- Hidden doesn't mean temporary. Permanent, theirs, editable like anything else.
- **Don't send them hunting.** Just open it for them when they need it. Most editors won't show these folders either, which is why users think their subagent files don't exist.

## Global and project — they stack

| | Global | Project |
|---|---|---|
| Orientation file | `~/.claude/CLAUDE.md` · `~/.codex/AGENTS.md` | `CLAUDE.md` / `AGENTS.md` in the folder |
| Subagents | `~/.claude/agents/` · `~/.codex/agents/` | `.claude/agents/` · `.codex/agents/` |
| Skills | `~/.claude/skills/` · `~/.codex/skills/` | `.claude/skills/` · `.codex/skills/` |
| Available | Everywhere | Only inside that folder |

**The point users get backwards: the files add together.** Starting a session in a folder means reading every orientation file from that folder up to home and **concatenating** them. Global first, then each one below.

- **"How I work" goes global** — who they are, British English, conventions. Written once, never repeated.
- **"What this project is" goes local** — this client, this deadline, these files.
- If two files *directly* contradict, the closest and most specific wins. **But that's the exception — stacking, not overriding, is the everyday case.** Correct them if they're designing as though local replaces global; they'll duplicate things they never needed to.

The analogy that lands: global is federal law, project is state law — except they mostly add up rather than compete.

## ⚠️ The spawn-location trap

**An agent started in a subfolder cannot see skills and subagents in the parent folder.** It sees its own folder plus anything global. Nothing else.

**This is the single commonest reason a user types `/` and finds nothing after a successful install.** Check it first, every time, before you conclude anything is broken.

- If the kit went into a subfolder of their workspace, **they must start the session in that subfolder**.
- Better: move it to the **global** location so it follows them everywhere. Offer to check and move: *"let me check whether the kit's skills are installed globally or just in this project."*
- Then **start a new session** — skills and subagents are picked up at session start, not mid-conversation. Users don't know this and will conclude the move failed.

The same rule covers skills *and* subagents. One rule, both concepts.

## Two ways to lay out their work

Neither is right. Help them pick the one matching how they think, then write it into the orientation file so you don't have to work it out each time.

- **One parent folder, projects as subfolders.** They always open the parent. Upside: **cross-project work** — you can look at two projects at once and spot the overlap.
- **A separate parent folder per project.** They open the one they're in. Upside: **separation** — you can't wander into another client's material. This is the sandbox answer for anyone nervous about access.

**A ceiling worth enforcing: three or four levels of subfolder, maximum.** Deeper and you have more places to look and less signal about which matters. If they're going deeper, **offer to promote a subfolder up a level** rather than adding another layer.

If they arrive with an existing pile of files, offer to look at it and propose a structure — most users don't know they can ask for that, and it's a strong first win.

## Pointing at things

Three ways, in order of use:

1. **`@`-tag it** — type `@` and pick the file. Fastest, works for folders. Teach this early.
2. **Relative path** — the address *from the folder they've opened*: `projects/q3-launch/plan.md`. Enough for anything inside the workspace, and the right default in a chat.
3. **Absolute path** — the address on the whole computer. For pointing outside the current folder, or opening a file in a browser.

> The analogy: telling someone in another country where you live means naming the country, the city and the street. Telling a friend across town, you just give the street.

⚠️ **An absolute path is theirs alone.** `/Users/theirname/...` means nothing on a colleague's machine. **Tell them to share relative paths when collaborating** — this bites people who assume a path is a path.

**Finding one:** Finder → **View → Show Path Bar** so they can always see where they are, then right-click → *Copy as Pathname*. Windows: the address bar in File Explorer. In the chat, the three-dot file panel copies either form. Or just find it for them.

## When they say "I can't see what's going on"

The commonest complaint in a first week, and it's a real problem rather than a confidence one. Two fixes, and offer both:

- **Turn on the file panel** in their agent interface (usually a three-dot menu → Files) so they watch files appear as they're created. This alone resolves most of it.
- **Open the same folder in a markdown editor.** [Obsidian](https://obsidian.md/) is the usual choice, free, and it imports nothing: their notes *are* the markdown files already on disk, and Obsidian is a second window onto them. It also shows [front matter as editable fields](https://obsidian.md/help/properties) rather than raw text, which is the fastest way to check that properties took. **Point it at one project folder to start with**, not everything they own.

## Do this

- **When `/` shows nothing, check placement before anything else** — global vs project, and whether the session started in the right folder. Then start a new session. This resolves it the large majority of the time.
- **When a user says you're ignoring instructions**, check which orientation files actually stack for the folder they're in, and tell them the order.
- **Draw them the map** when they're lost: where the global config is, which orientation files exist and how they'd stack here, where skills and subagents are installed. Then say plainly whether anything is somewhere you wouldn't find it.
- **Turn on the file panel for them** the first time they say they can't see anything. Don't wait to be asked.
- **Raise the `.claude` backup gap** before a laptop change, not after.
- **Offer to restructure** if their folders are more than four deep or genuinely disorganised — and do the move yourself rather than describing it.
