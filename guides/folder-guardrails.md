# Folder Guardrails — actually blocking your agent from sensitive folders

**The problem:** you want to use your agent across your computer, but some folders
are genuinely off-limits — client files under NDA, HR records, personal finances.
A line in your `AGENTS.md` / `CLAUDE.md` saying "never open `~/Private`" is worth
having, but it's *asking* — like giving someone a key and requesting they stay out
of one room. A **guardrail** is configuration that *blocks* the action before it
runs: locking the door. Do both.

**Point your agent at this guide** and say: *"follow this and set up a guardrail
around <folder> for me."* It knows how to do the rest — the sections below are
written for it as much as for you.

### Who are you protecting the folder from?

The layers below stop different things, and it's worth being honest about which
is which before you pick one:

| The agent is… | What stops it |
|---|---|
| **Careless** — wandered in while doing something adjacent | Layer 1 (the instruction) |
| **Confused** — decided the folder was genuinely relevant to your task | Layer 2 (deny rules) |
| **Hijacked** — following instructions hidden in a web page or a file it read | Layer 2b (sandbox) or Layer 3 (OS) |

Layer 1 and Layer 2 both run *through* the agent's decision-making. If something
has subverted that decision-making, only a boundary enforced outside the agent —
the operating system — still holds. That's the whole reason this guide has three
layers rather than one.

---

## Layer 1 — the instruction (both runtimes, 30 seconds)

Add to your global `CLAUDE.md` / `AGENTS.md`:

```markdown
## Out of bounds
- Never read, list, edit, or run commands that touch `~/Private/` (or anything inside it).
- If a task seems to need something from there, stop and ask me instead.
```

Cheap, portable, and covers the honest-mistake cases. Not foolproof on its own —
that's what Layer 2 is for.

## Layer 2 (Claude Code) — deny rules: the lock on the door

Claude Code has a built-in **permission system** with allow/deny rules, and deny
rules can fence off paths. This is the simple, supported way — no code required.

**You are an AI agent setting this up: edit the user's `~/.claude/settings.json`
(create it if missing), preserving anything already in the file.** Add deny rules
for each protected folder:

```json
{
  "permissions": {
    "deny": [
      "Read(//Users/NAME/Private/**)",
      "Edit(//Users/NAME/Private/**)",
      "Bash(*Private*)"
    ]
  }
}
```

Notes for the agent doing the setup:

- Replace `NAME`/the path with the user's real folder. The `//` prefix means an
  **absolute** path; `**` covers everything inside, at any depth. A single leading
  slash is *not* absolute — `/Users/...` anchors at the settings file's own
  directory, which is a common and silent mistake.
- **Only `Read(...)` and `Edit(...)` are matched for file paths.** A
  `Write(path)`, `NotebookEdit(path)` or `Glob(path)` rule is accepted, does
  nothing, and prints a startup warning. `Edit` already covers every file-editing
  tool, so those two rules are the complete set.
- `Read` deny covers more than the Read tool: it applies to Grep and Glob, to
  `@file` mentions in your prompts, to the file context an IDE shares with Claude,
  and to file commands Claude Code recognises in Bash such as `cat`, `head`,
  `tail` and `sed`.
- The `Bash` pattern is a blunt backstop for shell commands the file-command
  recognition doesn't cover (`rsync`, `zip`, `python …`). It matches on the text
  of the command, so it also blocks innocent commands that merely *mention* the
  word — pick a distinctive folder name, and expect the occasional false alarm.
- Deny rules **override** allow rules, and rules in the global
  `~/.claude/settings.json` apply in every project.
- **Protect the guardrail itself.** These rules live in a file the agent can edit.
  Add `"Edit(//Users/NAME/.claude/**)"` to the deny list so it can't quietly
  remove its own restrictions.

### Verify it — five tests, not one

Start a fresh session (rules load at startup) and try each of these against the
protected folder. The last one is the interesting one:

| Try | Expected |
|---|---|
| Ask it to **read** a file inside the folder | refused |
| Ask it to **search** the folder for a word (Grep) | refused |
| Ask it to run **`cat`** on a file inside | refused |
| Point a **symlink** from your project into the folder, ask it to read that | refused — deny rules check both the link and its target |
| Ask it to run `python3 -c "print(open('/Users/NAME/Private/x.txt').read())"` | **succeeds** — unless you've done Layer 2b |

If any of the first four succeeds, the rule isn't matching — check the path
syntax. The fifth one is not a bug: permission rules govern what *Claude* does,
and a Python script that opens a file itself is doing it below that layer. That
gap is what Layer 2b closes.

### Layer 2b (Claude Code) — the sandbox: enforced by the operating system

Claude Code ships an OS-level sandbox for shell commands. Unlike deny rules, it
isn't a decision the agent makes — the operating system enforces it on the running
process and every child process it spawns, so it holds even if a prompt injection
has taken the wheel.

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "denyRead": ["~/Private"]
    }
  }
}
```

Notes for the agent doing the setup:

- **`enabled: true` alone is not enough.** The sandbox's default read policy is
  "the whole computer" — the `denyRead` entry is what protects the folder.
- Sandbox paths use ordinary conventions (`~/Private`, `/absolute/path`) — *not*
  the `//` prefix that permission rules use. Don't copy the syntax across.
- macOS, Linux and WSL2 only. There is no native Windows sandbox; on Windows, run
  Claude Code inside WSL2, or rely on Layer 3.
- It covers **Bash commands and their children**. Claude's built-in Read/Edit
  tools go through the permission system instead — which is why you want both
  Layer 2 and Layer 2b, not one or the other.
- Turn it on interactively with `/sandbox`, or set the keys above in
  `~/.claude/settings.json` to apply it everywhere.

### For a work machine — put the rules where the agent can't reach them

Everything above lives in files your agent can edit. If the folder matters
because someone else says it matters — a client contract, an employer's policy —
put the deny rules in **managed settings** instead:

- **macOS:** `/Library/Application Support/ClaudeCode/managed-settings.json`
- **Linux/WSL:** `/etc/claude-code/managed-settings.json`
- **Windows:** `C:\Program Files\ClaudeCode\managed-settings.json`

Same JSON shape. Writing there needs admin rights, and no user or project setting
can override a deny rule that lives in it. This is the difference between a lock
and a lock that can't be unscrewed from the inside.

### One thing none of this covers — MCP servers

Path-based deny rules match MCP tools by *name*, not by the paths they touch. If
you connect a filesystem MCP server, it can read your protected folder through its
own tools regardless of every rule above. Either don't connect one alongside a
protected folder, or deny the server explicitly (e.g. `"mcp__filesystem__*"`).

### Going further — the `guard-folders` hook (shipped in this kit)

For belt-and-braces, both runtimes support **hooks**: tiny programs that run
*before* each tool call and can veto it. This kit ships a worked v1 —
[`guard-folders/`](guard-folders/) — a small Python script that blocks any tool
call touching folders you list in a plain `protected-folders.txt`. Point your
agent at [`guard-folders/README.md`](guard-folders/README.md) and say *"install
this for me"*; it wires the hook, then you verify in a fresh session by asking the
agent to read something inside a protected folder (correct answer: a refusal
naming guard-folders). It fails open on errors, so a broken guard never bricks
your agent.

The hook's real value is on **Codex**, which has no read-side deny rules of its
own (see below). On Claude Code it's a useful third opinion, but the permission
rules and the sandbox are the load-bearing layers.

**Know what the hook cannot see.** It reads the *text of the tool call*, so it
catches a path written out plainly and — because it resolves paths — a symlink
pointing into the folder. It does **not** catch a shell command that reaches the
same file by another spelling. We tested these; all four get through:

| Slips past the hook | Example |
|---|---|
| A glob | `cat ~/Priv*te/notes.txt` |
| Split quoting | `cat ~/'Pri''vate'/notes.txt` |
| `cd` then a relative path | `cd ~ && cat Private/notes.txt` |
| A script that opens the file itself | `python3 analyse.py` |

None of these is fixable by inspecting commands — that's the ceiling of the
technique, not a bug we haven't got to. It's why the hook is a *layer* and not
the answer, and why anything genuinely sensitive belongs behind Layer 2b's
sandbox or Layer 3.

**Related tool, different axis:** [destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard)
pattern-checks *dangerous shell commands* (`rm -rf`, forced pushes…) before they run —
it guards destructive **actions** anywhere, where guard-folders guards **places**.
They stack nicely.

## Layer 2 (Codex) — the sandbox, and what it does *not* do

Codex's idiomatic guardrail is its **sandbox**, configured in
`~/.codex/config.toml`:

- `sandbox_mode` — `"read-only"`, `"workspace-write"` (the usual setting), or
  `"danger-full-access"` (avoid).
- `sandbox_workspace_write.writable_roots = [...]` — pins **exactly which folders
  the agent may write to**.
- `approval_policy` — controls what still asks you first.

> **Read this before relying on it.** Codex's sandbox is a guardrail on *writing*,
> not on *reading*. In `workspace-write` mode the agent can read the entire disk
> and write only to your workspace; `"read-only"` mode means "may only read" —
> not "may only read *these places*". There is no configuration key in Codex that
> restricts which folders it can read. So for NDA or HR material, where the risk
> is someone *seeing* the file, `writable_roots` gives you nothing.

What that leaves you on Codex:

- **Don't open Codex at your home directory** — open it at the folder you're
  actually working in. This doesn't stop reads either, but it keeps the folder out
  of the agent's line of sight for ordinary work. Check the current settings any
  time with `/status`.
- **Install the `guard-folders` hook** — on Codex this is the read-side veto, not
  a nice-to-have. Codex supports hooks under `[hooks]` in `config.toml`, using the
  same event schema as Claude Code. Hooks are still a young feature there and the
  config shape has changed between releases — the [installer](guard-folders/README.md)
  records the version it was verified against; re-run the verify test after a
  Codex upgrade.
- **For anything genuinely sensitive, go to Layer 3.** On Codex that's not
  belt-and-braces, it's the only boundary the agent can't reason its way around.

## Layer 3 — the OS-level option (any tool, strongest)

If a folder must be untouchable by *any* agent, take the decision out of the
agents' hands entirely. The thing to keep in mind: **your agent runs as you**. Any
protection you can undo by clicking through a dialog, it can undo too — so
`chmod`-ing your own folder to be unreadable is a speed bump, not a wall. These
three are real:

- **Keep it in an encrypted container that stays closed.** macOS: Disk Utility →
  New Image → encrypted disk image. Windows: BitLocker or VeraCrypt. Mount it when
  you need it, unmount it before you start an agent. Nothing can read a volume
  that isn't mounted.
- **Put it in Documents, then revoke that app's access to Documents (macOS).**
  Order matters here, and this is the step people get wrong. macOS only asks
  permission for a **specific set of locations** — Desktop, Documents and
  Downloads, plus removable and network volumes and iCloud Drive. A folder you
  made yourself at `~/Private` is **not** in that set, so revoking file access
  protects it not at all. Move the material into one of the covered folders
  *first*; then, in System Settings → Privacy & Security → Files and Folders,
  turn off that folder's access for the app you run your agent in (Terminal,
  iTerm, VS Code), and turn off Full Disk Access for it too. Your agent inherits
  its terminal's permissions and cannot grant itself more — macOS requires *you*
  to approve that, in an interface the agent can't reach. If you'd rather not
  move the folder, skip this one and use the encrypted container or a separate
  account, which work anywhere on disk.
- **Run the agent as a different user account.** Create a second macOS or Windows
  account for agent work, and leave the sensitive folder owned by — and readable
  only by — your main account. This is the strongest of the three and the least
  convenient.

An agent cannot read what the operating system won't show it — no configuration,
prompt, or injection can route around that.

---

## Which layers do I actually need?

| Situation | Recommendation |
|---|---|
| "I'd just rather it didn't wander" | Layer 1 |
| Client/NDA or HR material on a work machine | Layers 1 + 2 + 2b, verified — and managed settings if someone else sets the policy |
| Using Codex rather than Claude Code | Layer 1 + the `guard-folders` hook + Layer 3 — Codex's sandbox does not restrict reads |
| Regulated or truly sensitive data | Layer 3 — or keep it off the machine agents run on entirely |

One honest note from the course: for genuinely high-stakes data (health records
and the like), the current best practice is still **don't expose it to coding
agents at all** — a guardrail protects a folder, but the safest folder is one on
a machine the agent never sees.

---

*Runtimes move fast. The Claude Code behaviour here was checked against the
permissions and sandboxing documentation, and the Codex sandbox behaviour against
the Codex source, in July 2026. Re-run the verification tests after a major
upgrade of either tool rather than assuming a rule still bites.*
