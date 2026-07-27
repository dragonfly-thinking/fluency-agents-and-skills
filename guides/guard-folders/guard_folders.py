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

Known limits (v1, by design — see the guide). These are tested, not assumed:
- Bash commands are checked by substring (absolute and ~ forms of each protected
  path), so a command that spells the path another way slips past — a glob
  (cat ~/Priv*te/x), split quoting (cat ~/'Pri''vate'/x), cd plus a relative
  path, or a shell variable.
- A script that opens the file itself is invisible here: this hook sees
  `python3 analyse.py`, not what that script goes on to read. No hook that
  inspects the command can close that gap — only an OS-enforced boundary can
  (Claude Code's sandbox.filesystem.denyRead, or the OS-level options in the
  guide).
Pair this hook with permission deny rules, the sandbox, and — for the truly
sensitive — OS-level locks. Layers, not silver bullets.
"""

import json
import os
import sys
import unicodedata

CONFIG_FILES = [
    os.path.expanduser("~/.claude/protected-folders.txt"),
    os.path.expanduser("~/.codex/protected-folders.txt"),
]

# tool_input keys that carry filesystem paths across common tools
PATH_KEYS = (
    "file_path", "path", "notebook_path", "directory", "cwd",
    "old_path", "new_path", "target_file", "source_file",
)

# macOS and Windows are case-insensitive by default: ~/Private and ~/private are
# the SAME folder, but a plain string compare treats them as different, which
# would let a trivial case change walk straight past this guard. macOS also
# stores filenames decomposed (NFD), so an accented folder name can arrive in a
# different byte form than the one in protected-folders.txt.
FOLD_CASE = sys.platform in ("darwin", "win32")


def norm(text):
    """Normalise for comparison: Unicode form, then case where the OS ignores it."""
    text = unicodedata.normalize("NFC", text)
    return text.casefold() if FOLD_CASE else text


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

    # Flatten every string in tool_input (Codex's shell passes argv as a LIST of
    # strings, and tool schemas differ between runtimes — so inspect everything).
    path_values, other_values = [], []
    for key, value in tool_input.items():
        values = value if isinstance(value, list) else [value]
        for v in values:
            if isinstance(v, str) and v:
                (path_values if key in PATH_KEYS else other_values).append(v)

    for folder in protected:
        folder_n = norm(folder)

        # 1) known path arguments — resolved-prefix match (catches ../ and symlinks)
        for value in path_values:
            resolved = norm(os.path.realpath(os.path.expanduser(value)))
            if resolved == folder_n or resolved.startswith(folder_n + os.sep):
                block(folder, tool)

        # 2) everything else (shell commands, argv items, unknown fields) —
        #    substring match on absolute and ~ forms
        tilde_form = folder.replace(home, "~", 1) if folder.startswith(home) else None
        tilde_n = norm(tilde_form) if tilde_form else None
        for value in other_values:
            value_n = norm(value)
            if folder_n in value_n or (tilde_n and tilde_n in value_n):
                block(folder, tool)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)  # any unexpected error → fail open
