#!/usr/bin/env python3
"""guard-folders v1 — a PreToolUse hook that BLOCKS agent access to protected folders.

Shared as part of the Dragonfly AI Fluency kit (see guides/folder-guardrails.md).

How it works: Claude Code (and Codex, which uses the same hook event schema) runs
this script before each tool call, passing the call as JSON on stdin. If the call
touches any folder listed in your protected-folders.txt, the script exits with
code 2, which vetoes the call before it runs. Anything else — including any
unexpected error in this script — lets the call through (fail-open by design:
a broken guard should never brick your agent).

Protected folders are listed one per line in:
    ~/.claude/protected-folders.txt   (and/or ~/.codex/protected-folders.txt)
Lines starting with # are comments. ~ is expanded. Symlinks are resolved.

Known limits (v1, by design — see the guide):
- Bash commands are checked by substring (absolute and ~ forms of each protected
  path). A command that reaches a folder by *relative* path or via a variable can
  slip past. Pair this hook with permission deny rules and, for the truly
  sensitive, OS-level locks. Layers, not silver bullets.
"""

import json
import os
import sys

CONFIG_FILES = [
    os.path.expanduser("~/.claude/protected-folders.txt"),
    os.path.expanduser("~/.codex/protected-folders.txt"),
]

# tool_input keys that carry filesystem paths across common tools
PATH_KEYS = (
    "file_path", "path", "notebook_path", "directory", "cwd",
    "old_path", "new_path", "target_file", "source_file",
)


def load_protected():
    folders = []
    for cfg in CONFIG_FILES:
        try:
            with open(cfg, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    folders.append(os.path.realpath(os.path.expanduser(line)))
        except OSError:
            continue
    return folders


def block(folder, tool):
    sys.stderr.write(
        f"BLOCKED by guard-folders: {tool} tried to touch the protected folder "
        f"{folder}. That folder is off-limits to agents. Do not retry or work "
        f"around this; tell the user it is protected and continue without it.\n"
    )
    sys.exit(2)


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed input → fail open

    protected = load_protected()
    if not protected:
        sys.exit(0)

    tool = event.get("tool_name", "unknown-tool")
    tool_input = event.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        sys.exit(0)

    home = os.path.expanduser("~")

    for folder in protected:
        # 1) explicit path arguments (Read, Edit, Write, Glob, Grep, ...)
        for key in PATH_KEYS:
            value = tool_input.get(key)
            if not isinstance(value, str) or not value:
                continue
            resolved = os.path.realpath(os.path.expanduser(value))
            if resolved == folder or resolved.startswith(folder + os.sep):
                block(folder, tool)

        # 2) shell commands (Bash) — substring match on abs and ~ forms
        command = tool_input.get("command")
        if isinstance(command, str) and command:
            tilde_form = folder.replace(home, "~", 1) if folder.startswith(home) else None
            if folder in command or (tilde_form and tilde_form in command):
                block(folder, tool)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)  # any unexpected error → fail open
