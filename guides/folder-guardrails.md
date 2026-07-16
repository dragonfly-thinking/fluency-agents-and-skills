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
      "Write(//Users/NAME/Private/**)",
      "Bash(*Private*)"
    ]
  }
}
```

Notes for the agent doing the setup:

- Replace `NAME`/the path with the user's real folder. The `//` prefix means an
  **absolute** path; `**` covers everything inside, at any depth.
- The `Read`/`Edit`/`Write` rules stop the file tools; the `Bash` pattern is a
  blunt backstop that blocks shell commands mentioning the folder (pattern-based,
  so it can be worked around in principle — see the hook option below for
  something stronger, and note a determined prompt-injection is exactly the case
  hooks exist for).
- Deny rules **override** allow rules and apply in every project when set in the
  global `~/.claude/settings.json`.
- **Verify it**: start a new session and ask Claude to read a file inside the
  protected folder. The correct outcome is a **permission refusal**. If it reads
  the file, the rule isn't matching — check the path syntax.

### Going further (Claude) — a hook

For belt-and-braces, Claude Code also supports **hooks**: tiny programs that run
*before* each tool call and can veto it (a `PreToolUse` hook whose matcher checks
whether the target path is inside a protected folder, exiting with a block). Hooks
catch edge cases pattern rules miss, but they're a step up in complexity — start
with deny rules, and if you want the hook version, ask your agent to *"write a
PreToolUse hook that blocks any tool call touching `~/Private`, following the
official hooks docs at code.claude.com/docs"* and test it the same way.

## Layer 2 (Codex) — the sandbox (and yes, Codex has hooks too)

Codex's idiomatic guardrail is its **sandbox**, configured in
`~/.codex/config.toml`:

- `sandbox_mode` — `"read-only"`, `"workspace-write"` (the usual setting: the
  agent can only *write* inside the workspace), or `"danger-full-access"` (avoid).
- `sandbox_workspace_write.writable_roots = [...]` — pins **exactly which folders**
  the agent may write to. Keep sensitive folders off this list and out of the
  workspace you open.
- `approval_policy` — controls what still asks you first.

Practical guidance: don't open Codex at your home directory — open it at the
folders you actually work in, so the sandbox boundary *is* the guardrail. Check
the current settings any time with `/status` in a session.

Codex also supports **hooks** — the same event-interception mechanism as Claude
(`PreToolUse` and friends, same schema), configured under `[hooks]` in
`config.toml` — so the "small program that vetoes an action before it runs"
pattern from the session works in both tools. Sandbox first, hooks for the edge
cases.

## Layer 3 — the OS-level option (any tool, strongest)

If a folder must be untouchable by *any* agent, take the decision out of the
agents' hands entirely:

- **macOS:** remove your user's read permission from the folder and require an
  admin prompt to open it (right-click → Get Info → Sharing & Permissions), or
  keep the material in an **encrypted disk image** (Disk Utility → New Image →
  encrypted) that stays unmounted while agents run.
- **Windows:** right-click → Properties → Security, and remove access for the
  account the agent runs under; or keep it in a **BitLocker/VeraCrypt** container.

An agent cannot read what the operating system won't show it — no configuration,
prompt, or injection can route around that.

---

## Which layers do I actually need?

| Situation | Recommendation |
|---|---|
| "I'd just rather it didn't wander" | Layer 1 |
| Client/NDA or HR material on a work machine | Layers 1 + 2, verified |
| Regulated or truly sensitive data | Layer 3 — or keep it off the machine agents run on entirely |

One honest note from the course: for genuinely high-stakes data (health records
and the like), the current best practice is still **don't expose it to coding
agents at all** — a guardrail protects a folder, but the safest folder is one on
a machine the agent never sees.
