# Init Interview — full setup of a new workspace

This is the canonical interview that produces a fresh agentic workspace for the user. Follow it exactly. **The parent skill (`setup-workspace`) routes here when no workspace is detected anywhere — global or project scope.**

---

You're going to interview the user to set up a personalised workspace that future AI agents they work with will use to understand who they are and how they work.

This is the **quick version** — keep it under 10 minutes. The user can do a deeper one later.

The output is **NOT** a single file. It's a small workspace:

```
AGENTS.md or CLAUDE.md             (router file — output ONLY ONE, based on the tool they're using)
context/bio.md                     (who they are — background, role, audiences)
context/work.md                    (what they do — recurring work + working style)
context/company.md                 (only if they work for an organisation — what it does, who it serves)
projects/<project-name>/index.md   (only if they have a current project worth scoping — one file per project)
```

**Which router filename to use:**
- If they're using **Claude Code / Claude workflows:** `CLAUDE.md`
- If they're using **Codex / Cursor / Aider workflows:** `AGENTS.md`
- If unclear, ask.

---

## How this runs

### 1. INTAKE

Start by asking if the user has any links (LinkedIn, their website, their company's website, a bio) or files (a recent email, an "about me" doc, a CV) to share.

**If they share any, READ THEM FIRST** and treat them as equivalent to the user answering several questions. Extract what you can, then only ask about what's missing.

### 2. ONE QUESTION AT A TIME

Wait for an answer before asking the next one. **Never batch.**

### 3. BUDGET: 5 QUESTIONS MAXIMUM

Use them wisely. If the user's shared materials cover an area, skip the question for it.

### 4. ANCHOR ON EXAMPLES, NOT ADJECTIVES

If you want their voice, ask them to write or paste one real sentence. If you want their work, ask for a specific recent example.

### 5. AREAS TO COVER

Adapt order to what the user already shared. Cover:

- **Role + organisation + who they serve** (drives `bio.md` + `company.md`)
- **One sentence in their own voice** describing what they do (voice anchor for the router file's identity line)
- **Top 1-2 recurring things they do every week** (`work.md`)
- **Main current project + one-line status** — only if they have one worth scoping; skip if not
- **One guardrail** — something an AI should always check with them before doing, or never do

### 6. AFTER 5 QUESTIONS (or sooner if materials covered enough)

Stop asking. Produce **exactly ONE code block total** that contains all file contents. Inside that single code block, clearly label each file and its content. **Do NOT output multiple separate code blocks.**

Use this exact format:

```
[ROUTER FILE — output only ONE of these, based on the tool the user is using]
Save to: CLAUDE.md
---
[router content — see structure below]

OR

Save to: AGENTS.md
---
[router content — see structure below]


[context/bio.md]
---
[content]


[context/work.md]
---
[content]


[context/company.md]  (ONLY if they work for an organisation)
---
[content]


[projects/<project-name>/index.md]  (ONLY if they named a current project)
---
[content]
```

Use a kebab-case project name (`mobile-app-relaunch`, not `Mobile App Relaunch`).

---

## STRUCTURE OF EACH FILE

### The router file (CLAUDE.md or AGENTS.md) — SHORT, under 25 lines

Template:

```markdown
# Who I am

[One sentence in the user's own voice — verbatim from their answer.]

## Workspace map

Detail lives in `context/` (about me) and `projects/` (about what I'm working on). Read the file that matches what you're doing — don't load all of them at once.

**About me**
- `context/bio.md` — background, role, audiences I serve
- `context/work.md` — what I do every week, how I like it approached

[IF company.md was produced:]
**About my company**
- `context/company.md` — [company name]: what we do, who we serve

[IF a project was produced:]
**Projects**
- `projects/<project-name>/` — [one-line description]

## Always remember

[3-5 lines covering the user's most important guardrails. These need to be in context every session. Examples:
- Never auto-send email or post publicly under my name — drafts only.
- No sycophancy. Have an opinion. If you disagree with me, say so.
- Confirm before destructive actions (deletes, force pushes, etc).
- Default to terse responses.

Adapt to what the user told you about guardrails. **Always include the safety floor: no auto-send, confirm destructive.**]
```

### context/bio.md

Who the user is, longer form (150-250 words). Their role, organisation, audiences they serve, how they sit in their field. Use their own voice sentences verbatim.

### context/work.md

3-5 bullets on weekly recurring work, each with a one-line note on how they like it approached. Plus a short paragraph on their working style (async/sync, time pressures, when they're at their best).

### context/company.md

**Only include if the user works for an organisation.**

~150-250 words on what the company does, who it serves, how engagements are structured. Use info they gave you or extracted from their materials. Don't invent details — if you don't know something, mark it for them to fill in with `<TODO: ...>`.

### projects/<project-name>/index.md

**Only include if the user named a current project worth scoping.**

Sections:
- **What it is** (1-2 sentences)
- **Status** (where we are right now)
- **Key people / stakeholders** (if mentioned, otherwise omit)
- **Current focus**
- **How I want agents to help here** (project-specific guidance, if any)

---

## 7. VALIDATE WITH A NEGATIVE FRAME

After showing the code block, ask:

> *"What's wrong with this?"*

Not *"does this look right?"* — the negative frame surfaces real objections.

## 8. ONE ROUND OF EDITS, THEN DONE

Make one round of edits based on the user's answer. Then tell them where to save the files:

- **Claude Code:** at their workspace root or `~/.claude/`. Save the router content as `CLAUDE.md`. Keep the folder structure (router file at root, `context/` and `projects/` as subfolders).
- **Codex:** at their workspace root or `~/.codex/`. Save the router content as `AGENTS.md`.
- **Claude Desktop (Cowork):** paste all files (clearly labelled by filename) into Custom Instructions, OR upload them as attached files to a Claude Project and reference the project for future chats.

---

## Start now

Begin by asking if the user has any links or files to share, or if they'd rather just answer questions.
