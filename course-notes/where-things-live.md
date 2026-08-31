# Where Things Live

*Global versus project, hidden folders, and the placement rule that decides whether your agent can see the thing you just installed.*

This is the most confusing part of working this way, and it is confusing for a single reason: **everything is a folder.** Your workspace is a folder. A project is a folder. The agent's own configuration is a folder. They look identical and they do completely different jobs. Once the layout is clear, half the mysterious failures stop being mysterious.

---

## Everything is a file on your computer

- **A workspace, a project and a folder are the same thing.** The words get used interchangeably; they all mean a folder you have pointed an agent at. When a tool shows "working directory" at the top of the chat, *directory* just means folder.
- **The apps are windows onto the same files.** Claude, Codex, your file explorer, a markdown editor — all looking at the same folder on disk. Nothing is duplicated per tool, and nothing is uploaded. **Your setup is not locked to one AI**: switching tools does not mean rebuilding.
- **The work stays on the machine it was made on** until you deliberately put it somewhere else. If you change laptops, it does not follow you. That is what [`../guides/github-basics.md`](../guides/github-basics.md) is for — and note that your `.claude` / `.codex` folder is *not* included in a backup of your project folder. It is the thing people lose.

## The hidden dot-folders

- Configuration lives in folders whose names start with a dot: **`.claude`** and **`.codex`**. The leading dot makes them **hidden** — your file explorer won't show them without changing a setting.
- Hidden does not mean temporary. They are permanent, they are yours, and you can open and edit them like anything else.
- **Don't hunt for them.** Just ask: *"open my global `.claude` folder for me."*

## Global and project — they stack

You have a **global** setup in your home folder that applies everywhere, and **project** ones inside specific folders that apply only there.

| | Global | Project |
|---|---|---|
| Orientation file | `~/.claude/CLAUDE.md` · `~/.codex/AGENTS.md` | `CLAUDE.md` / `AGENTS.md` in the folder |
| Subagents | `~/.claude/agents/` · `~/.codex/agents/` | `.claude/agents/` · `.codex/agents/` |
| Skills | `~/.claude/skills/` · `~/.codex/skills/` | `.claude/skills/` · `.codex/skills/` |
| Available | Everywhere | Only inside that folder |

**The key point, and it is the one people get backwards: they add together.** When you start a session in a folder, the agent reads every orientation file from that folder all the way up to your home directory and **concatenates** them. Global first, then each one below it. So:

- **"How I work" goes global** — who you are, British English, your conventions. Write it once and never repeat it.
- **"What this project is" goes local** — this client, this deadline, these files.
- If two files *directly* contradict each other, the closest and most specific one wins. But that is the exception. **Stacking, not overriding, is the everyday case**, and designing your files as though local replaces global will leave you duplicating things you never needed to.

A rough analogy: global is federal law, project is state law — except they mostly just add up rather than compete.

## ⚠️ The spawn-location trap

**An agent started in a subfolder cannot see the skills and subagents sitting in the parent folder.** It sees its own folder, plus anything global. Nothing else.

This is the single commonest reason someone types `/` and finds an empty list after a successful install.

- **If you installed the kit into a subfolder of your workspace, start your session in that subfolder.**
- Or — better — install to the **global** location so it follows you everywhere. That is what the kit's install playbook does by default.
- The fix, if you're stuck: *"check whether the kit's skills are installed globally or just in this project, and move them to global."* Then **start a new session** — new skills and subagents are picked up at session start, not mid-conversation.

The same rule covers skills *and* subagents. Learn it once; it explains both.

## Two ways to lay out your work

Neither is right. Pick the one that matches how you think.

- **One parent folder, projects as subfolders.** You always open the parent. The upside is **cross-project work** — the agent can look at two projects at once and spot the overlap.
- **A separate parent folder per project.** You open the one you're working in. The upside is **separation**: if the agent can only see this folder, it cannot wander into another client's material. This is the sandbox option.

**A ceiling worth respecting: three or four levels of subfolder, maximum.** Nest deeper and the agent has a harder time locating the relevant file efficiently — it has more places to look and less signal about which one matters. If you find yourself going deeper, **promote a subfolder up a level** rather than adding another layer.

Whichever you choose, **write the structure into your orientation file** so the agent knows what it's looking at rather than working it out each time.

## Telling the agent where something is

Three ways, in order of how often you'll use them:

1. **`@`-tag it.** Type `@` in your message and pick the file. Fastest, and it works for folders too.
2. **Relative path** — the address *from the folder you've opened*: `projects/q3-launch/plan.md`. Enough for anything inside your workspace, and this is what you want in a chat session.
3. **Absolute path** — the address on your whole computer: `/Users/you/Documents/work/projects/...`. Use it to point at something *outside* the current folder, or to open a file in your browser.

> **The analogy that makes it stick:** telling someone in another country where you live means naming the country, the city and the street. Telling a friend across town, you just give the street. Absolute is the first; relative is the second.

⚠️ **An absolute path is yours alone.** Send `/Users/yourname/...` to a colleague and it means nothing on their machine — their home folder has a different name. Share relative paths when you're collaborating.

**Finding a path:** in Finder, turn on **View → Show Path Bar** so you can always see where you are, then right-click a file → *Copy as Pathname*. On Windows, copy from the address bar in File Explorer. In the chat, the three-dot menu on the file panel will copy either form. Or just ask the agent to open or locate it for you.

## Seeing the structure

The commonest complaint in a first week is *"I can't see what's going on."* Two fixes:

- **Show the file panel** in your agent's interface (usually a three-dot menu → Files) so you watch files appear as they're created.
- **Open the same folder in a markdown editor** — [Obsidian](https://obsidian.md/) is the usual choice, free, and it stores nothing of its own: your notes *are* the markdown files already on your computer, and Obsidian is a second window onto them. It also shows [front matter as editable fields](https://obsidian.md/help/properties) rather than raw text, which is the fastest way to check whether the properties you added actually took. Point it at one project folder to start with, not everything you own.

## Try this

> Draw me a map of my current setup: where my global config lives, which orientation files
> exist and in what order they'd stack for the folder I'm in right now, and where my skills
> and subagents are installed. Tell me if anything is in a place where you wouldn't find it.
