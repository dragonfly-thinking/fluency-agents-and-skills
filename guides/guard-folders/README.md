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
         "matcher": "Read|Edit|Write|Glob|Grep|Bash|NotebookEdit",
         "hooks": [
           { "type": "command", "command": "python3 ~/.claude/hooks/guard_folders.py" }
         ]
       }
     ]
   }
   ```
   Validate the file is still valid JSON afterwards.
4. **Restart** — hooks load at session start. Then verify: ask the agent to read a
   file inside a protected folder. Correct result: a refusal that names
   guard-folders. Also verify normal work still succeeds (fail-open check).

**Codex:** the script is identical (it also reads `~/.codex/protected-folders.txt` —
create it, and copy the script to `~/.codex/hooks/`). Registration in
`~/.codex/config.toml` (this exact shape parses on codex-cli 0.144; note the
required `type` field):

```toml
[features]
hooks = true

[[hooks.PreToolUse]]
matcher = ".*"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/guard_folders.py"
```

Restart Codex and run the same verify test. Codex's built-in sandbox
(`writable_roots`) remains the first line there — this hook adds the read-side veto.

**Honest limits (v1):** Bash commands are matched by path substring — a command
using a *relative* path or a variable can slip past. That's why the guide teaches
layers: this hook + permission deny rules + (for the genuinely sensitive) OS-level
locks. And the script **fails open** on any internal error, so a broken guard never
bricks your agent — test it after install rather than assuming.
