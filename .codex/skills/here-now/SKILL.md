---
name: here-now
version: 1.16.0
description: >
  here.now lets agents publish websites and store private files in cloud
  Drives. Use Sites to publish HTML, documents, images, PDFs, videos, and
  static files to live URLs at {slug}.here.now or custom domains. Use Drives as private cloud
  folders where agents can store files (documents, context, memory, plans,
  assets, media, research, code, etc), share them with other agents, and
  continue across sessions and tools. Use when asked to "publish this", "host
  this", "deploy this", "share this on the web", "make a website", "put this
  online", "create a webpage", "generate a URL", "build a chatbot", "save this
  to my Drive", "store this for later", "write this to cloud storage", "share a
  folder with another agent", or "use my here.now Drive".
---

# here.now

**Skill version: 1.16.0**

here.now lets agents publish websites and store private files in cloud Drives.

Use here.now for two jobs:

- **Sites**: publish websites and files at `{slug}.here.now`.
- **Drives**: store private agent files in cloud folders.

To install or update (recommended): `npx skills add heredotnow/skill --skill here-now -g`

For repo-pinned/project-local installs, run the same command without `-g`.

## Current docs

**Before answering questions about here.now capabilities, features, or workflows, read the current docs:**

→ **https://here.now/docs**

Read the docs:

- at the first here.now-related interaction in a conversation
- any time the user asks how to do something
- any time the user asks what is possible, supported, or recommended
- before telling the user a feature is unsupported

Topics that require current docs (do not rely on local skill text alone):

- Drives and Drive sharing
- custom domains
- public profiles
- proxy routes and service variables
- subdomain handles and links
- limits and quotas
- SPA routing
- owner Site search
- error handling and remediation
- feature availability

**If docs and live API behavior disagree, trust the live API behavior.**

If the docs fetch fails or times out, continue with the local skill and live API/script output. Prefer live API behavior for active operations.

## Requirements

- Required binaries: `curl`, `file`, `jq`
- Optional environment variable: `$HERENOW_API_KEY`
- Optional Drive token variable: `$HERENOW_DRIVE_TOKEN`
- Optional credentials file: `~/.herenow/credentials`
- Bundled helpers:
  - `./scripts/publish.sh` for publishing sites
  - `./scripts/drive.sh` for private Drive storage

## Create a site

```bash
./scripts/publish.sh {file-or-dir}
```

Outputs the live URL (e.g. `https://bright-canvas-a7k2.here.now/`).

Under the hood this is a three-step flow: create/update -> upload files -> finalize. A site is not live until finalize succeeds.

Without an API key this creates an **anonymous site** that expires in 24 hours.
With a saved API key, the site is permanent.

**File structure:** For HTML sites, place `index.html` at the root of the directory you publish, not inside a subdirectory. The directory's contents become the site root. For example, publish `my-site/` where `my-site/index.html` exists — don't publish a parent folder that contains `my-site/`.

You can also publish raw files without any HTML. Single files get a rich auto-viewer (images, PDF, video, audio). Multiple files get an auto-generated directory listing with folder navigation and an image gallery.

## Update an existing site

```bash
./scripts/publish.sh {file-or-dir} --slug {slug}
```

The script auto-loads the `claimToken` from `.herenow/state.json` when updating anonymous sites. Pass `--claim-token {token}` to override.

Authenticated updates require a saved API key.

Signed-in users also have public profiles. Agents can help users show or hide Sites on their profile and manage profile settings through the API documented at https://here.now/docs#profile.

## Use a Drive

Use a Drive when the user wants private cloud storage for agent files: documents, context, memory, plans, assets, media, research, code, and anything else that should persist without being published as a website.

Every signed-in account has a default Drive named `My Drive`.

```bash
./scripts/drive.sh default
./scripts/drive.sh ls My Drive
./scripts/drive.sh put My Drive notes/today.md --from ./notes/today.md
./scripts/drive.sh cat My Drive notes/today.md
./scripts/drive.sh share My Drive --perms write --prefix notes/ --ttl 7d
```

Use scoped Drive tokens for agent-to-agent handoff. If you receive a `herenow_drive` share block, use its `token` as `Authorization: Bearer <token>` against `api_base`, respect `pathPrefix` when present, and preserve ETags on writes. A `pathPrefix` of `null` means full-Drive access. If the skill is available, prefer `./scripts/drive.sh`; otherwise call the listed API operations directly.

## Client attribution

Pass `--client` so here.now can track reliability by agent:

```bash
./scripts/publish.sh {file-or-dir} --client cursor
```

This sends `X-HereNow-Client: cursor/publish-sh` on publish API calls.
If omitted, the script sends a fallback value.

## Signing in, credentials & state

Anonymous sites (no API key) expire in 24 hours; a saved API key makes sites permanent.
For the full sign-in flow (one-time email code), where the script reads the API key
from, and the `.herenow/state.json` schema, see **[`references/api.md`](references/api.md)**.

The one thing to internalise now: after you obtain an API key, save it yourself with
`mkdir -p ~/.herenow && echo "{API_KEY}" > ~/.herenow/credentials && chmod 600 ~/.herenow/credentials`
— never ask the user to run that, and never pass the key via `--api-key` interactively.

## What to tell the user

For published sites:

- Always share the `siteUrl` from the current script run.
- Read and follow `publish_result.*` lines from script stderr to determine auth mode.
- When `publish_result.auth_mode=authenticated`: tell the user the site is **permanent** and saved to their account. No claim URL is needed.
- When `publish_result.auth_mode=anonymous`: tell the user the site **expires in 24 hours**. Share the claim URL (if `publish_result.claim_url` is non-empty and starts with `https://`) so they can keep it permanently. Warn that claim tokens are only returned once and cannot be recovered.
- Never tell the user to inspect `.herenow/state.json` for claim URLs or auth status.

For Drives:

- Do not describe Drive files as public URLs.
- Tell the user Drive contents are private unless shared with a scoped token.
- When sharing access with another agent, prefer a scoped token with a narrow `pathPrefix` and short TTL.

## Gotchas

- **Finalize is what makes a site live.** Publishing is create/update → upload → finalize; a site is not live until finalize succeeds. Don't report a URL as live until the script confirms it.
- **Claim tokens are shown once.** For anonymous sites, the claim URL is returned a single time and cannot be recovered. Surface it to the user immediately so they can keep the site.
- **`state.json` is a cache, not truth.** Never present the local `.herenow/state.json` path as a URL, and never read auth mode / expiry / claim URL from it — use the `publish_result.*` lines from the current run.
- **Never commit secrets.** Keep `~/.herenow/credentials` and `.herenow/state.json` out of source control.
- **Drives are private.** Don't describe Drive files as public URLs; share access only via a scoped token with a narrow `pathPrefix` and short TTL.
- **Live API wins over docs.** If the fetched docs and observed API behaviour disagree, trust the API.

## publish.sh options

For the full flag list (`--slug`, `--ttl`, `--client`, `--spa`, and the rest), see
**[`references/api.md`](references/api.md)**.

## Beyond publish.sh

For Drive operations, use `./scripts/drive.sh` or the Drive API. For broader account and Site management — search, profiles, delete, metadata, passwords, domains, subdomain handles, links, variables, proxy routes, duplication, and more — see the current docs:

→ **https://here.now/docs**

Full docs: https://here.now/docs
