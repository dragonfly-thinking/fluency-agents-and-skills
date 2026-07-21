# Skill Creator — advanced topics

Moved out of SKILL.md to keep the always-loaded body lean. Read this when a skill
needs to persist state across runs, register session-scoped guardrail hooks, or
ship beyond a single repo. These features are Claude Code-specific.

---

## Memory & Persistent Data

Skills can maintain state across invocations. Use `${CLAUDE_PLUGIN_DATA}` for a stable per-plugin data directory that survives skill upgrades (data stored in the skill directory itself may be deleted on upgrade).

```markdown
## Logging

After each standup post, append an entry to `${CLAUDE_PLUGIN_DATA}/standups.log`.
Next run, read the log to identify what changed since yesterday.
```

Options range from simple (append-only text log, JSON file) to advanced (SQLite database).

## On-Demand Hooks

Skills can register hooks that activate only when the skill is called and last for the session. Use this for opinionated guardrails that would be annoying if always-on:

- `/careful` — blocks `rm -rf`, `DROP TABLE`, force-push via PreToolUse matcher. Only want this when touching prod.
- `/freeze` — blocks Edit/Write outside a specific directory. Useful when debugging: "add logs but don't accidentally 'fix' unrelated code."

## Distribution

Two paths for sharing skills:

| Method | Best For | Tradeoff |
|--------|----------|----------|
| **Check into repo** (`.claude/skills/`) | Small teams, few repos | Every skill adds to context scan; doesn't scale |
| **Plugin marketplace** | Larger orgs, many repos | Users choose what to install; needs curation |

For marketplaces: let skills emerge organically. Sandbox folder → traction → PR to marketplace. Curation before release matters — bad or redundant skills degrade the experience.

## Measuring Skills

Track skill usage with a PreToolUse hook that logs when skills trigger. This reveals:
- Popular skills (invest in improving them)
- Under-triggering skills (fix the description)
- Unused skills (retire or rework them)
