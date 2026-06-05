---
name: new-project
description: Interviews the user to find and shape their next project, then scaffolds
  it as a properly-tracked piece of work. Kicks off the interview the moment
  it's invoked — opening with "what would you like to work on?" — and guides
  the user from there: offering example project types or scanning the workspace
  for candidates if they want ideas, then shaping the goal, constraints, and
  scope. Scaffolds the chosen project — its own folder under projects/ with
  overview.md, plan.md, and progress.md, plus a one-line entry in the router
  file (CLAUDE.md / AGENTS.md) — writing files only once the user approves. Use
  when the user invokes /new-project (with or without any other text), says
  "start a new project", "set this up as a project", "set up my work on Y
  properly", or "I don't know what to work on next".
version: 2.0.0
---

# New Project

Interview the user to find and shape their next project, then set it up properly: a
small, self-tracking structure that an agent — or the user, next week — can pick up cold.
The interview meets them wherever they are — a fully-formed plan, half an idea, or
nothing yet — and guides them through fleshing out the workspace for it.

**The moment this skill is invoked, start the interview (Step 2).** Don't wait for further
instruction, don't list the workspace contents, don't ask "what would you like me to do?"
— ask the first interview question. If the invocation already carries an idea
("/new-project for my Q3 report"), skip the exploration and go straight to shaping it.

**Don't use it when:**
- The user just needs a one-off answer or a single file → don't make a project; just do
  the thing.

---

## The principle (this is what the skill is really teaching)

1. **You stay the director.** Propose the structure and get a nod *before* writing files —
   plan first, act second.
2. **Every file earns its place.** Start with three. Don't bury the work under ceremony.
3. **The work tracks itself.** A running log means any new session can pick up exactly
   where the last one left off.

A "project" here is nothing technical: **a folder that keeps its own notes** about what
the work is, how it'll get done, and where it's up to. Say so, in roughly those words, if
the user seems unsure what they're making.

The default output is **three files**, populated from the interview. The fuller structure
is *offered*, never imposed.

---

## Step 1 — Find where projects live (don't assume)

Locate the **workspace root** — the folder holding the router file (`CLAUDE.md` for Claude
Code, `AGENTS.md` for Codex). Projects go in a `projects/` folder *there*, next to the
router — **not** wherever the terminal happens to be sitting. Use `ls` / `Read` to check;
never guess. Do this quietly — the user doesn't need a narration of the folder hunt.

- **Has a router + `projects/`** → use it. Note which router file(s) are present (Step 6).
- **No workspace at all** (no router file, no `projects/`) → say so and suggest running
  **`setup-workspace`** first, so this skill has somewhere to put the project. If the user
  would rather just start, create a `projects/` folder in the current directory and carry
  on.

## Step 2 — Find the project

Open the conversation here. One warm question:

> *"What would you like to work on? It can be anything — a piece of work, something
> personal, a nagging thing you keep meaning to sort out."*

Then branch on what comes back:

- **They have an answer** → go to Step 3 and shape it.
- **They're not sure, or ask what a project could be** → help them find one. Two moves,
  in this order:
  1. **Offer the shapes projects usually take** — present these as a clear choice (use
     the AskUserQuestion tool if available, otherwise a short list):
     *something to produce* (a report, a deck, a piece of writing), *something to
     organise* (an event, a trip, a move), *a recurring headache to systematise* (the
     admin task they redo every month), *something to research or learn*, or *a process
     to hand to an agent* (a workflow they'd love to stop doing by hand).
  2. **Offer to look for candidates:** *"Want me to look at what's already in this
     workspace and suggest two or three projects hiding in it?"* If yes, scan the
     workspace (recent files, folders, notes, half-started things) and propose 2–3
     concrete candidates, one line each, with a recommendation.
- **The idea is genuinely big and foggy** (they can feel it but can't say it) → offer the
  **`discovery-interview`** skill: *"This sounds like it deserves a proper interview —
  want me to interview you thoroughly first, then set the project up from what we find?"*
  Hand off, then return here with its spec.

Don't rush this step, and don't over-stay either — the moment there's a nameable piece of
work, move on.

## Step 3 — Shape it, lightly (one question at a time)

This is **not** the deep discovery interview. Ask only what's needed to scaffold well —
about three or four questions, **one at a time, never batched.** Batched questions get
mushy answers, and mushy answers make mushy projects.

1. **What's the project — and why does it matter?** Capture a name (suggest a kebab-case
   slug, e.g. `q3-launch`), a one- or two-sentence description, and the reason it's worth
   doing. The "why" usually falls out of the description — don't make it a separate
   interrogation. If they don't volunteer one, infer a light why for `overview.md` rather
   than leaving it blank.
2. **What does "done" look like for this phase?** If the goal is huge, ask what the *first
   phase's* done looks like — keep it shippable.
3. **Any hard constraints?** Time, money, must-uses, must-not-dos.
4. **What's explicitly out of scope for now?** The non-goals — just as useful as the
   goals.

If the answers stay mushy and the person clearly hasn't figured the idea out, offer the
off-ramp again: *interview me properly first* → **`discovery-interview`**, then return
here; or *push on and scaffold what we have*.

## Step 4 — Propose the structure, then wait

Before writing a single file, show the plan and get approval. Frame it negatively —
*"anything wrong with that?"*, not *"look good?"* — because negative framing surfaces real
objections instead of a reflexive yes:

> *"Here's how I'll set this up:*
> *`projects/<slug>/` — `overview.md` (what it is, goal, constraints), `plan.md` (approach
> + steps), `progress.md` (a running log I'll keep current), plus a one-line entry in your
> `<router>` pointing at it.*
> *Anything wrong with that before I write it?"*

## Step 5 — Scaffold the three files

The file shapes live in this skill's **`assets/`** folder — `assets/overview.md`,
`assets/plan.md`, `assets/progress.md`. Read each, **fill in the `<placeholders>` from the
interview**, and write the populated versions into `projects/<slug>/`. Write *filled-in*
files, never the empty templates.

- `progress.md`'s date: get it from the system clock (run `date`) — don't guess.
- **Mirror existing conventions.** If `projects/` already holds projects with a different
  shape (extra files like `brief.md`, frontmatter, a custom layout), match that shape
  rather than rigidly imposing these three. Consistency with the workspace beats the
  template.

## Step 6 — Update the router file

Add a one-line entry to the router under a **Projects** / **My projects** section:

```markdown
- **<Project name>** — `projects/<slug>/` — <one-line description>. <status>
```

- No Projects section yet → add one. Only a placeholder (`- (none yet)`) → replace it.
  Otherwise **append** — don't reorder or rewrite existing entries.
- **If both `CLAUDE.md` and `AGENTS.md` exist**, update the one for the active runtime; if
  the user works across both, update both so the project shows up either way.

## Step 7 — Offer the next step (don't force it)

Close by offering, not doing. Present these as choices (AskUserQuestion if available):

- **Flesh out the plan into milestones and tasks?** → the **`project-planner`** subagent,
  pointed at the new `overview.md` / `plan.md`.
- **Add the fuller project structure?** → the extras in Step 8.
- Otherwise: *"You're set up. Open the folder and start — I'll keep `progress.md` current
  as we work."*

## Step 8 — The fuller structure (only if asked)

For bigger or longer-running work, offer four more files — their shapes live in
**`assets/extras/`** (`decisions.md`, `questions.md`, `sources.md`, `handoff.md`). Copy
only the ones requested; leave them as headers-with-prompts until there's something real
to put in them. Mention they exist; don't pre-create them.

---

## Composition

- **Before** (idea still vague): `discovery-interview` → a spec → scaffold from it.
- **After** (need a real plan): `project-planner` subagent → milestones, tasks, estimates.
- **No workspace yet:** `setup-workspace` → creates the router + `projects/`.

`new-project` is the front door for new work: it helps find the project, then turns it
into a tracked structure — pointing at the thinking tool before it and the planning tool
after it.

## Gotchas

- **Start the interview on invocation.** A bare `/new-project` (or the skill text pasted
  with no instruction) means *begin Step 2 now* — don't list files or wait for more input.
- **Let Step 2 do its job.** Even when the goal seems obvious, the one warm opening
  question costs nothing and often reshapes the project. Don't skip straight to file
  creation.
- **Don't write files before the user approves the structure** (Step 4). Plan first.
- **Find the workspace root; don't scaffold into the current directory by reflex.** A
  project created next to the wrong folder is invisible to the router and the next
  session.
- **Mirror existing project conventions** rather than imposing the 3-file default — match
  the shape already in `projects/`.
- **Don't overwrite an existing project.** If `projects/<slug>/` already exists, stop and
  ask (rename, or resume the existing one) — never clobber it.
- **Don't batch the interview**, and **don't duplicate `discovery-interview`.** If you're
  asking ten questions, you're in the wrong skill — hand off.
- **Don't invent answers.** Missing info gets a `<TODO: ...>` marker or a follow-up
  question, never a confident guess.
- **Don't pre-bloat.** Three populated files beat seven empty ones. The extras are opt-in.
