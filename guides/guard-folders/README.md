# guard-folders v1 — install

The worked folder-guardrail from the course: a small hook that **vetoes any agent
tool call touching folders you list** — reading, editing, or shell commands — before
it runs. Concept and layered strategy: [`../folder-guardrails.md`](../folder-guardrails.md).

**You are an AI agent installing this. Steps (Claude Code):**

1. Copy the script and make it executable:
   ```bash
   mkdir -p ~/.claude/hooks
   cp guard_folders.py ~/.claude/hooks/guard_folders.py
   chmod +x ~/.claude/hooks/guard_folders.py
   ```
2. Create the protected list — **ask the user which folders**, then write
   `~/.claude/protected-folders.txt` (copy `protected-folders.example.txt` as a
   start), one folder per line, `#` for comments.
3. Wire the hook into `~/.claude/settings.json` — **merge, don't overwrite**. Add
   this to the top-level `"hooks"` object (create it if absent):
   ```json
   "hooks": {
     "PreToolUse": [
       {
         "matcher": ".*",
         "hooks": [
           { "type": "command", "command": "python3 ~/.claude/hooks/guard_folders.py" }
         ]
       }
     ]
   }
   ```
   Validate the file is still valid JSON afterwards. The `.*` matcher is
   deliberate: it catches MCP-server tools (`mcp__…`) too, which named matchers
   like `Read|Edit|Bash` would miss.
4. **Restart** — hooks load at session start. Then verify: ask the agent to read a
   file inside a protected folder. Correct result: a refusal that names
   guard-folders. Also verify normal work still succeeds (fail-open check).

**Codex:** the script is identical (it also reads `~/.codex/protected-folders.txt` —
create it, and copy the script to `~/.codex/hooks/`). Registration in
`~/.codex/config.toml` (this exact shape parses on codex-cli 0.144; note the
required `type` field — Codex hooks are a young feature and the shape has changed
between releases, so re-run the verify test after upgrading):

```toml
[features]
hooks = true

[[hooks.PreToolUse]]
matcher = ".*"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/guard_folders.py"
```

Restart Codex and run the same verify test. On Codex this hook is doing real work
rather than adding belt-and-braces: Codex's sandbox restricts **writing** only —
`workspace-write` can read the entire disk, and there is no config key that
restricts reads — so the hook is the read-side veto there.

**Honest limits (v1) — these were tested, not guessed:**

- **Bash is matched by path substring**, so a command that spells the path any
  other way slips past. All four of these get through:
  | Slips past | Example |
  |---|---|
  | a glob | `cat ~/Priv*te/notes.txt` |
  | split quoting | `cat ~/'Pri''vate'/notes.txt` |
  | `cd` then a relative path | `cd ~ && cat Private/notes.txt` |
  | a shell variable | `P=~/Pri; cat ${P}vate/notes.txt` |
- **A script that opens the file itself is invisible to this hook.** The hook sees
  `python3 analyse.py`, not the file that script goes on to read. Nothing that
  inspects the *command* can close this — only an OS-enforced boundary can
  (Claude Code's `sandbox.filesystem.denyRead`, or Layer 3 in the guide).
- **It fails open** on any internal error, so a broken guard never bricks your
  agent — which also means a broken guard is silent. Test it after install rather
  than assuming, and re-test after upgrading either runtime.

What it *does* catch: paths written out plainly, in any letter case — macOS and
Windows filesystems ignore case, so `~/private` and `~/Private` are the same
folder and the hook treats them as one; accented folder names in either Unicode
form; symlinks pointing into a protected folder, and symlinked parent
directories; Codex's argv-list command shape; and MCP-server tools.

That's why the guide teaches layers rather than selling this hook as the answer:
this hook + permission deny rules + the sandbox + (for the genuinely sensitive)
OS-level locks.
