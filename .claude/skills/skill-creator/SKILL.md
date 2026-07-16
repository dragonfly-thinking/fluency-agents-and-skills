---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. Also use when the user says "make a skill", "turn this into a skill", "create a skill for X", "skill for Y", or wants to package a repeatable workflow.
---

# Skill Creator

Create effective, reusable skills — modular packages that extend Claude with specialized knowledge, workflows, and tools.

A skill is **a folder, not just a markdown file**. The most powerful skills use their folder structure creatively: scripts Claude can compose, reference docs it reads on demand, assets it copies into output, config files it populates during setup, and data files it appends to across invocations.

## Types of Skills

Before building, identify which category the skill fits. The best skills fit cleanly into one; confusing ones straddle several.

| Category | What It Does | Examples |
|----------|-------------|----------|
| **Library & API Reference** | Explains how to correctly use a library, CLI, or SDK — internal or external. Often includes a folder of code snippets and a gotchas list. | `billing-lib`, `internal-platform-cli`, `frontend-design` |
| **Product Verification** | Describes how to test/verify that code works. Often paired with tools (Playwright, tmux). Worth investing heavily in — verification skills ensure Claude's output is correct. | `signup-flow-driver`, `checkout-verifier`, `tmux-cli-driver` |
| **Data Fetching & Analysis** | Connects to data and monitoring stacks. May include helper libraries with credentials, dashboard IDs, common query patterns. | `funnel-query`, `cohort-compare`, `grafana` |
| **Business Process & Automation** | Automates repetitive workflows into one command. Often simple instructions with dependencies on other skills/MCPs. Saving results in log files helps the model stay consistent. | `standup-post`, `create-ticket`, `weekly-recap` |
| **Code Scaffolding & Templates** | Generates framework boilerplate. Especially useful when scaffolding has natural-language requirements that pure code can't cover. | `new-workflow`, `new-migration`, `create-app` |
| **Code Quality & Review** | Enforces code quality standards. Can include deterministic scripts for maximum robustness. Can run automatically via hooks or GitHub Actions. | `adversarial-review`, `code-style`, `testing-practices` |
| **CI/CD & Deployment** | Helps fetch, push, and deploy code. May reference other skills to collect data. | `babysit-pr`, `deploy-service`, `cherry-pick-prod` |
| **Runbooks** | Takes a symptom (alert, error, Slack thread), walks through investigation, produces structured findings. | `api-debugging`, `oncall-runner`, `log-correlator` |
| **Infrastructure Operations** | Performs routine maintenance — some involving destructive actions that benefit from guardrails. | `orphan-cleanup`, `dependency-management`, `cost-investigation` |

## Anatomy of a Skill

```
skill-name/
├── SKILL.md              # Required — instructions + frontmatter
├── scripts/              # Executable code (Python/Bash/etc.)
├── references/           # Docs loaded into context as needed
├── assets/               # Files used in output (templates, fonts, etc.)
├── config.json           # Optional — user-specific setup data
└── data/                 # Optional — persistent skill memory
```

### Progressive Disclosure

Skills use a three-level loading system:

1. **Metadata** (name + description) — always in context (~100 words)
2. **SKILL.md body** — loaded when skill triggers (<500 lines ideal)
3. **Bundled resources** — loaded as needed (unlimited; scripts can execute without reading)

Tell Claude what files exist in the skill folder and when to read them. It will load them at the right time.

## Writing Effective Skills

### Don't State the Obvious

Claude knows a lot about coding and your codebase. Focus on information that pushes Claude **out of its normal way of thinking** — the non-obvious stuff. If Claude would do it correctly without the skill, don't waste tokens on it.

### Build a Gotchas Section

The highest-signal content in any skill is the **Gotchas** section. Build it up from common failure points Claude encounters when using the skill. Update it over time as new failure modes appear. This is a living document.

```markdown
## Gotchas

- The `created_at` column is UTC but `report_date` is Pacific — always convert before joining
- Don't use `rm -rf` on the build directory; the symlinks point to the source
- The v2 API returns paginated results even though the docs say otherwise — always check `next_cursor`
```

### Explain the Why, Not Just the What

Claude has good theory of mind. When given reasoning, it can adapt to situations the instructions didn't anticipate. Instead of rigid `ALWAYS`/`NEVER` directives, explain **why** something matters:

```markdown
# Rigid (fragile)
ALWAYS use prepared statements. NEVER concatenate SQL strings.

# Better (robust)
Use prepared statements for all database queries. Raw string concatenation
opens SQL injection vectors, and our WAF won't catch parameterized
attack patterns that bypass simple escaping.
```

### Avoid Railroading

Skills are reusable across many situations. Give Claude the information it needs but the flexibility to adapt. Overly specific instructions that work for your three test cases will break on the fourth.

### Think Through Setup

Some skills need user-specific context (which Slack channel, which database, API keys). Use a `config.json` pattern:

```markdown
## First Run Setup

If `config.json` doesn't exist in this skill directory, ask the user:
1. Which Slack channel to post standups to
2. Their GitHub username for activity aggregation

Save to `config.json`:
```json
{ "slack_channel": "#team-standups", "github_user": "samdev" }
```

Subsequent runs read the config automatically.
```

To present structured choices, instruct Claude to use the `AskUserQuestion` tool.

### The Description Field Is for the Model

When Claude starts a session, it scans every skill's `name + description` to decide relevance. The description isn't a summary — it's a **trigger specification**. Be specific about when to activate, and slightly "pushy" to counter Claude's tendency to under-trigger:

```yaml
# Weak
description: Helps with data analysis

# Strong
description: >
  Query and analyze data from our BigQuery warehouse. Use when the user
  mentions data analysis, metrics, cohort comparisons, funnel queries,
  SQL against our warehouse, or asks questions like "how many users..."
  or "what happened on Tuesday" — even if they don't mention BigQuery.
```

### Store Scripts & Composable Code

One of the most powerful things to give Claude is code. Scripts and helper libraries let Claude spend its turns on **composition** — deciding what to do — rather than reconstructing boilerplate.

```
data-analysis/
├── SKILL.md
└── scripts/
    ├── fetch_events.py      # Fetch from event source with auth
    ├── compute_retention.py  # Retention curve calculation
    └── plot_funnel.py       # Funnel visualization
```

Claude can then generate scripts on the fly that import and compose these helpers for complex queries.

### Memory & Persistent Data

Skills can maintain state across invocations. Use `${CLAUDE_PLUGIN_DATA}` for a stable per-plugin data directory that survives skill upgrades (data stored in the skill directory itself may be deleted on upgrade).

```markdown
## Logging

After each standup post, append an entry to `${CLAUDE_PLUGIN_DATA}/standups.log`.
Next run, read the log to identify what changed since yesterday.
```

Options range from simple (append-only text log, JSON file) to advanced (SQLite database).

### On-Demand Hooks

Skills can register hooks that activate only when the skill is called and last for the session. Use this for opinionated guardrails that would be annoying if always-on:

- `/careful` — blocks `rm -rf`, `DROP TABLE`, force-push via PreToolUse matcher. Only want this when touching prod.
- `/freeze` — blocks Edit/Write outside a specific directory. Useful when debugging: "add logs but don't accidentally 'fix' unrelated code."

### Composing Skills

Reference other skills by name in your instructions. Claude will invoke them if installed:

```markdown
After generating the CSV, use the `file-upload` skill to upload it to the shared drive.
```

Formal dependency management isn't built in yet, but name-based references work well in practice.

## Skill Creation Process

### Step 1: Understand with Concrete Examples

Skip only when usage patterns are already clear.

Get concrete examples of how the skill will be used — either from the user or generated and validated:

- "What should this skill enable?"
- "Can you give examples of prompts that should trigger it?"
- "What's the expected output?"

If the conversation already contains a workflow ("turn this into a skill"), extract answers from conversation history first: tools used, sequence of steps, corrections made, input/output formats observed.

Avoid overwhelming with questions — start with the most important, follow up as needed.

### Step 2: Plan Reusable Contents

Analyze each concrete example:

1. What code gets rewritten every time? → `scripts/`
2. What documentation gets rediscovered every time? → `references/`
3. What boilerplate gets recreated every time? → `assets/`
4. What user-specific context is needed? → `config.json` pattern
5. What data should persist across runs? → `data/` or `${CLAUDE_PLUGIN_DATA}`

Look for repeated work across examples — if all test cases result in writing a similar helper script, that script belongs in `scripts/`.

### Step 3: Initialize

For new skills, run the init script:

```bash
python scripts/init_skill.py <skill-name> --path <output-directory>
```

This creates the directory structure with SKILL.md template and example resource directories. Customize or delete the generated examples as needed.

Skip this step if iterating on an existing skill.

### Step 4: Write the Skill

Write for another instance of Claude, not for a human. Focus on information that is **beneficial and non-obvious**.

#### SKILL.md Structure

1. **Frontmatter** — `name` (required), `description` (required, trigger-optimized)
2. **One-line purpose** — what this skill enables
3. **Core instructions** — how to use it, referencing bundled resources
4. **Gotchas** — failure modes to avoid (add to this over time)

**Writing style:** Imperative/infinitive form ("To accomplish X, do Y"), not second person. Keep SKILL.md under 500 lines — if approaching the limit, split detail into `references/` with clear pointers about when to read them.

#### Bundled Resources

Start with the resources identified in Step 2. This may require user input (e.g., brand assets, API docs, templates).

| Directory | Purpose | When to Include |
|-----------|---------|-----------------|
| `scripts/` | Deterministic, reusable code | Same code rewritten repeatedly |
| `references/` | Docs loaded on demand | Detailed info too large for SKILL.md |
| `assets/` | Files used in output | Templates, images, boilerplate |

For large reference files (>300 lines), include a table of contents. For very large ones (>10k words), include grep search patterns in SKILL.md.

### Step 5: Validate & Package

```bash
python scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

Validates (frontmatter, naming, structure) then creates a distributable zip.

### Step 6: Iterate

The best skills start as a few lines and a single gotcha, then improve as Claude hits new edge cases.

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Update SKILL.md or bundled resources
4. Test again

When improving: keep the prompt lean (remove what isn't pulling its weight), read transcripts (not just outputs) to spot unproductive loops, and generalize from feedback rather than overfitting to test cases.

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

---

*Adapted from Anthropic's public [skill-creator](https://github.com/anthropics/skills) (Apache-2.0 — see `LICENSE.txt`). Works in both Claude Code and Codex; where the text says "Claude", read "your agent".*
