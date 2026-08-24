# Install guide — for the agent

**You are an AI coding agent (Claude Code or Codex). The user has asked you to set up this kit. Follow the steps for the user's runtime below.** This installs 6 specialist subagents and 16 skills into the user's environment so they're available in every session, not just this folder.

If you don't know which runtime you're in: you're **Claude Code** if you read `CLAUDE.md` and use `.claude/`; you're **Codex** if you read `AGENTS.md` and use `.codex/`. If unsure, ask the user.

**If the user already has a workspace set up** — a `CLAUDE.md` / `AGENTS.md`, a `context/` folder, their own agents or skills — that is normal, and it is *not* a conflict. Installing the kit adds capabilities to `~/.claude/` (or `~/.codex/`); it does not touch their workspace files. So don't present this as an either/or, don't report that their skills "aren't live", and don't offer to skip the install because you've spotted an overlap. Install the kit, leave their workspace alone, and mention afterwards that the `setup-workspace` skill can fill any gaps later if they want it.

---

## 🚫 Never overwrite these — read before you copy anything

**This is an install, and it is also an *update*.** Returning users have files they built
themselves, some of them in a live session with an instructor. Losing one is worse than any
capability this kit adds. **These are never yours to replace:**

| File | Why it matters | What you do instead |
|---|---|---|
| **Their orientation file** — `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or any `CLAUDE.md`/`AGENTS.md` in a project | They wrote it, usually by interview. It is the single most personal file in their setup. | **Never write to it during install.** Snippets from `course-notes/agents-md-snippets.md` are *offered* after the install, one at a time, and appended only on an explicit yes. |
| **Their checklist** — `~/.claude/fluency-checklist.md` | Holds their ticked progress and notes. | If it exists, leave it. Add only genuinely new items from the template, unticked, at the end. |
| **Skills they've tailored** | The course told them to shape these. Theirs is the version tuned to their work. | The MODIFIED check below catches these. Ask before touching any of them. |
| **`~/.codex/config.toml`** | Contains config that isn't ours. | Back it up, then *merge* the `[agents.*]` blocks. Never overwrite the file. |
| **`context/`, `projects/`, `user.md`, and anything else in their workspace** | Their actual work. | Don't touch it. Don't tidy it. Don't reorganise it. |

If you are ever unsure whether a file is theirs or ours: **it's theirs.** Ask.

---

## What gets installed

- **6 agents** (specialists a skill can delegate to): `critical-friend`, `fact-checker`, `writing-editor`, `project-planner`, `vault-librarian`, `web-searcher`
- **16 skills** (verbs the user invokes): `setup-workspace`, `new-project`, `proofread`, `critical-review`, `research-brief`, `premortem`, `daily-brief`, `visual-explainer`, `slides`, `canvas-design`, `pdf-create`, `here-now`, `verify-work`, `convert-docs`, `skill-creator` *(Claude only — Codex has its own built in)*, `browser-agent`

The repo ships both `.claude/` (Claude Code format) and `.codex/` (Codex format). Install the one matching the runtime. The repo also carries `course-notes/` (the reference library, plus `agents-md-snippets.md` — standing instructions for their orientation file), `guides/` (plain-English how-tos: GitHub, file conversion, folder guardrails, phone, VS Code, browser automation), and `mcp/` (external-connection setup guides) — these stay in the repo rather than being installed; see the wrap-up step.

**One file *is* copied out of the repo:** `fluency-checklist.md` → `~/.claude/fluency-checklist.md` (or `~/.codex/`). It lives outside the kit folder deliberately, so updating the kit never wipes the user's progress. See the wrap-up step for the copy rule.

---

## Step 0 — get the repo onto disk

You may have been given only this repo's **URL**. The install commands below assume the repo's files are on the user's machine, so get them there first. **Do not install by fetching files one at a time over the web** — you'll miss scripts and subfolders.

No GitHub account is needed for any of this; the repo is public.

- **If the repo is already on disk** (you're reading this file locally): it's ready to install — **but the kit gets updated between sessions, so if this might be an older copy from a previous course session, re-download the current version first** (see below) and install that, not stale files.
- **If the user downloaded it themselves** (e.g. they say "I downloaded it"): look for `fluency-agents-and-skills-main` — usually in `~/Downloads`, possibly still zipped. Unzip if needed, then **move it somewhere durable** before installing, e.g. `mv ~/Downloads/fluency-agents-and-skills-main ~/fluency-agents-and-skills`. Downloads folders get purged, and `course-notes/` + `mcp/` need to live on after install. (If their download is from an earlier session, prefer re-fetching the latest as below.)
- **Otherwise, fetch it yourself — don't assume `git` is installed.** Most course participants won't have it (on a fresh Mac, even running `git` triggers an install prompt that can hang you). Default to the plain **ZIP download** — no git, no account. This is also the **update path**: re-downloading always gets the latest and replaces an older copy.

**Never delete their existing copy until the new one is safely extracted.** A plain `curl -L`
**exits 0 on a 404** and writes a tiny error file, so "download then delete then unzip" destroys
a working kit whenever the network hiccups or a proxy intercepts — and the user may have saved
their own files in that folder. Use this, which only swaps at the very end:

```bash
cd ~   # never run this from inside the folder you're about to replace

# 1. Download, and STOP if it failed (-f makes curl fail loudly on 404/5xx)
curl -fL https://github.com/dragonfly-thinking/fluency-agents-and-skills/archive/refs/heads/main.zip \
  -o /tmp/fluency-kit.zip || { echo "Download failed — existing kit left untouched."; exit 1; }

# 2. Extract to a clean temp folder (NOT over the top of anything)
rm -rf /tmp/fluency-kit-unpack && mkdir -p /tmp/fluency-kit-unpack
unzip -qo /tmp/fluency-kit.zip -d /tmp/fluency-kit-unpack \
  || tar -xf /tmp/fluency-kit.zip -C /tmp/fluency-kit-unpack \
  || python3 -m zipfile -e /tmp/fluency-kit.zip /tmp/fluency-kit-unpack \
  || { echo "Could not extract the zip — existing kit left untouched."; exit 1; }

# 3. Only now swap it into place, keeping the old copy until the move succeeds
rm -rf ~/fluency-agents-and-skills.previous
[ -d ~/fluency-agents-and-skills ] && mv ~/fluency-agents-and-skills ~/fluency-agents-and-skills.previous
mv /tmp/fluency-kit-unpack/fluency-agents-and-skills-main ~/fluency-agents-and-skills
```

Three things that command is deliberately doing, so don't "simplify" them away:

- **`-qo` on `unzip`**, not `-q`. Plain `-q` stops and *asks* about each existing file, which on a
  real terminal blocks on a keypress and looks like a freeze.
- **Three extraction attempts.** `unzip` is **not present on Windows Git Bash** (it was dropped
  from Git for Windows), so `tar` and then Python are tried in turn. Keep `unzip` first — GNU tar
  on Linux can't read zips.
- **`cd ~` first.** Deleting the folder your shell is currently sitting in breaks every later
  command in the session with `getcwd` errors, and recreating the path does not fix it.

Afterwards, tell the user their previous copy is at `~/fluency-agents-and-skills.previous` and
offer to delete it once they're happy. Don't delete it yourself without asking.

> **On Windows:** all of the above runs in Git Bash, which is what the agent's shell will normally
> be. `$HOME` correctly maps to `C:\Users\<name>`, so `~/.claude` is the right place. If you find
> yourself in PowerShell instead, `curl` is an alias for `Invoke-WebRequest` and `-L` will fail —
> use `Invoke-WebRequest -Uri <url> -OutFile <path>` and `Expand-Archive` instead.

Only if `git` is *already* installed, cloning is a fine alternative (and makes later updates a `git pull`):

```bash
git clone https://github.com/dragonfly-thinking/fluency-agents-and-skills.git ~/fluency-agents-and-skills
```

Use `~/fluency-agents-and-skills` as the standard location — the course materials assume the repo lives somewhere predictable. Run the install commands below from inside it.

---

## Claude Code install

**Check what's already there before you copy anything.** `cp -R` overwrites silently, and this is the *update* path as much as the first-install path — a returning participant may have tailored a kit skill exactly as the course told them to, and a careless copy destroys that work. Check every time:

**Compare contents, not just names** — otherwise every re-install flags all 16 skills as
"existing", the user gets asked an unanswerable question about each, and the update they re-ran
the install *for* never happens. Only genuinely **modified** files deserve a question:

```bash
cd ~/fluency-agents-and-skills || { echo "Not in the kit folder — get the repo first (Step 0)"; exit 1; }
[ -d .claude/skills ] || { echo "This doesn't look like the kit folder — no .claude/skills inside"; exit 1; }
mkdir -p ~/.claude/agents ~/.claude/skills

# Only report things the user has actually CHANGED
for f in .claude/agents/* .claude/skills/*; do
  n=$(basename "$f"); d=$(dirname "$f"); t="$HOME/$d/$n"
  [ -e "$t" ] && ! diff -rq "$f" "$t" >/dev/null 2>&1 && echo "MODIFIED: $d/$n"
done
echo "--- check complete"
```

**Nothing listed as MODIFIED** — nothing of theirs is at risk. Copy everything straight over;
identical files are unchanged and older ones get the update they wanted. Don't ask a question here:

```bash
cp -R .claude/agents/*  ~/.claude/agents/
cp -R .claude/skills/*  ~/.claude/skills/
```

**Something listed as MODIFIED** — that's a skill they've tailored. Name just those, and ask
before touching them. Don't assume the kit's copy is better; theirs is the one tuned to their
work. Three choices:

- **Keep mine** — skip those, install everything else.
- **Take the kit's** — back their version up **outside** the skills folder first, then copy:
  `mkdir -p ~/.claude/skills-backup && cp -R "$HOME/.claude/skills/<name>" ~/.claude/skills-backup/`
  (Keep the quotes — skill names can contain spaces. And never leave a `<name>.backup` folder
  *inside* `~/.claude/skills/`; it would load as a second copy of the same skill.)
- **Show me what's different** — summarise the changes in plain English. Don't paste raw `diff`
  output at someone who's never seen one.

Install everything not listed either way. And anything in `~/.claude/` that isn't part of the
kit, leave completely alone — the user's own agents and skills are not yours to tidy up.

> Note the check only sees `~/.claude/skills/`. If a kit skill name is also installed as a
> **plugin**, that copy is invisible here — if a skill misbehaves after install, that's worth
> checking.

Claude Code auto-discovers `~/.claude/agents/` and `~/.claude/skills/`. Restart the session (or start a new one) and the skills/agents are live. Skills route automatically when the user describes the task.

**Verify:** in the new session, have the user type `/` — the installed skills (`proofread`, `slides`, `new-project`, …) should appear in the list — and run `/agents` to confirm the six subagents are registered. If they don't appear, check the files actually landed (`ls ~/.claude/skills ~/.claude/agents`) and that the session was fully restarted.

---

## Codex install

Codex needs three things: the skills, the agent role files, and the `[agents.*]` registrations merged into the user's config.

**Run the same collision check as the Claude section above** — against `~/.codex/skills` and `~/.codex/agents` — before copying. Same reasoning, same three choices to offer.

```bash
mkdir -p ~/.codex/skills ~/.codex/agents
cp -R .codex/skills/*  ~/.codex/skills/
cp -R .codex/agents/*  ~/.codex/agents/
```

Then **merge** the agent registrations into `~/.codex/config.toml`. This is the only step that
hand-edits an existing config file, so **back it up first** — if the file ends up malformed,
Codex may not start, and the user is mid-session with no way back:

```bash
[ -f ~/.codex/config.toml ] && cp ~/.codex/config.toml "$HOME/.codex/config.toml.bak-$(date +%Y%m%d-%H%M%S)"
```

Do NOT overwrite the file — the user may already have config. Ensure `[features] multi_agent = true` is present, then append any `[agents.*]` blocks from this repo's `.codex/config.toml` that aren't already there. The blocks look like:

```toml
[features]
multi_agent = true

[agents.critical_friend]
description = "..."
config_file = "agents/critical-friend.toml"
# ...and the other five agents
```

Read `.codex/config.toml` for the exact blocks and copy them verbatim.

**One more block, and it needs the user's permission.** `.codex/config.toml` also contains:

```toml
[sandbox_workspace_write]
network_access = true
```

Without it, the premium search lanes fail with connection errors that look like a broken API key.
With it, Codex can reach the network from inside its workspace sandbox. **That is a real change to
how sandboxed their machine is, so say so in plain English and ask** — something like: *"The kit
needs one setting changed so the research tools can reach the internet from inside Codex's
sandbox. It's needed for web search to work. Happy for me to set it?"* If they'd rather not, skip
it and tell them which skills won't work (`research-brief`, `daily-brief`, and the
`web-searcher` agent's paid lanes). Never set it silently — some participants are on managed work
laptops where that isn't their decision to make.

**Verify** by reading the merged file back (`grep -A2 '^\[agents\.' ~/.codex/config.toml`) and
confirming all six agents plus `multi_agent = true` are present. Don't tell the user to run
`/status` — that's a slash command inside the Codex interface, and you're already inside it.
In Codex, subagents are invoked **explicitly** — e.g. *"use the web_searcher agent to find sources on X"*. See `.codex/AGENTS.md` for the full Codex mapping.

---

## The here-now skill (special)

`here-now` publishes files to a live URL. It ships with working scripts (`scripts/publish.sh`, `scripts/drive.sh`), so copying it as above is enough. Alternatively, install the always-current upstream version directly:

```bash
npx skills add heredotnow/skill --skill here-now -g
```

No API key is needed for anonymous publishing (URLs expire in 24h). For permanent URLs, the skill walks the user through an email sign-in to get a key — see `.codex/skills/here-now/SKILL.md`.

---

## After installing — verify

Tell the user it's done and give them something to try:

> "Installed 6 agents and 16 skills. **First time?** Run *`setup-workspace`* — it'll interview you and create your `CLAUDE.md` / `AGENTS.md` + `context/` + `projects/` for you. **Been here before?** Run *`setup-workspace`* again — it'll spot what's missing from your setup and fill just those gaps. Or try: *start a new project with `new-project`* (it opens by asking what you'd like to work on), *build me slides on X*, *research-brief on Y*, or *publish something with here-now*."

Then four more things:

1. **Set up their checklist.** The kit ships a lot that people never get round to using; this is what stops that.

   ```bash
   mkdir -p ~/.claude   # or ~/.codex
   [ -f ~/.claude/fluency-checklist.md ] \
     && echo "EXISTS — do not overwrite; merge new items only" \
     || cp fluency-checklist.md ~/.claude/fluency-checklist.md
   ```

   **If it already exists, leave it alone.** Read it, and add only genuinely new items from the
   template, unticked, at the end. Their ticks and notes are theirs.

   Then *use* it, don't just announce it: look at what's actually on their machine, tick what's
   already true, and tell them. **Offer one next thing, not thirteen** — the header inside the
   file explains why. Say: *"I've started a checklist at `~/.claude/fluency-checklist.md` of the
   things in this kit worth doing. You've already got three of them. Want to do the next one now?"*

2. **Point at the course notes.** Tell the user where the repo lives on their machine (normally `~/fluency-agents-and-skills` — see Step 0) and that `course-notes/` there holds the reference library, `guides/` the plain-English how-tos, and `mcp/` the external-connection setup guides. Flag `course-notes/agents-md-snippets.md` specifically — standing instructions they can add to their orientation file so they stop asking for the same things by hand. Offer: *"Want me to read those and suggest two or three that fit how you work?"*

   ⚠️ **Offering is where this goes wrong.** Do not paste snippets into their orientation file as part of the install, do not add several at once, and do not rewrite the file to "tidy it up". Show one, say what it changes, append it if they say yes. Re-read the *Never overwrite these* table above if you're about to touch that file.
3. **Tell them the kit is theirs to shape.** One line is enough: *"If a skill ever gets something wrong, just tell me — I can update the skill so it doesn't happen again. And if you notice a task you repeat, I can turn it into a new skill."* (If they do tailor a skill, mention that re-installing the kit later will ask before overwriting it — it won't wipe their changes.)

4. **Offer to sort out permissions now.** This is the single most common frustration in the first hour: the skills that fetch from the web (`research-brief`, `daily-brief`, `fact-checker`) and the ones that write files will otherwise ask for approval over and over — one prompt per site on a batch job. Ask: *"Want me to set up a sensible always-allow list so you're not approving every web fetch?"* If yes, read [`guides/interface-and-settings.md`](guides/interface-and-settings.md) § *Always-allow* — it gives the safe-vs-keep-asking split in principle, and [`guides/folder-guardrails.md`](guides/folder-guardrails.md) shows the actual `permissions` file shape to write it into. Note the guide's "review what you've been approving" method **won't work for a brand-new user** — they haven't approved anything yet — so for a first install, propose a starting list from the guide's table (web search and fetching yes; deleting files no) and explain each line in one sentence rather than writing a config they can't read.

## Runtime dependencies to mention

- **Web search** must be enabled for `fact-checker`, `web-searcher`, `research-brief`, and `daily-brief` to verify/retrieve from the web. If it's off, they'll say so rather than invent.
- **here-now** needs `curl`, `file`, and `jq` on PATH (standard on macOS/Linux).
- **pdf-create** uses an already-installed Chrome/Edge; if none is found it falls back to "open the HTML and Cmd/Ctrl+P → Save as PDF" — no installs.
- **browser-agent** needs Node.js plus a one-time browser download on first use — the skill (and `guides/browser-agent.md`) walks through it; nothing to do at install time.

---

For what each skill and agent does, see [`README.md`](README.md).
