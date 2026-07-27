# ProgressBot.AI v2 — Project Brief

Read this at the start of any non-trivial session. The rules live in `/CLAUDE.md`;
this file is the *why* and the *state*.

## Mission

Translate **every page of the old progressbot.ai site** into the v2 design system —
one self-contained HTML file per page, same verified facts, new skin and structure —
until v2 IS the site. Every page ships to **site root** on hosting.com
(`public_html/<name>/index.html`; homepage is `public_html/index.html`).
**Root cutover for every page completed 2026-07-27** — the `/v2/` prefix is fully
retired, repo-wide. `docs/context/MIGRATION-MAP.md` is the checklist; a page is
*done* when it passes `scripts/verify.py`, is deployed, and everything that linked
to the old page links to the new one.

## Who's who

- **Builder:** Enrique — works from this repo (terminal + Claude Code), deploys to
  hosting.com shared hosting by uploading files.
- **Client:** owns progressbot.ai and the business facts. Client decisions MUST be
  summarized in `docs/context/CLIENT-NOTES.md` — that file is the only
  client-instruction memory future sessions have. Summaries only: this repo is
  public, so never paste private message text into it.

## How the repo maps to the live site

Flat `.html` files at repo root. Each file's `<link rel="canonical">` and its
top-of-file `Deploy as:` comment define its live path — filenames don't. Known quirks:

- `index.html` = the CURRENT homepage (canonical `/`; cut over from `home4.html`
  2026-07-23). Legacy `home3.html` and byte-duplicate `progressbot-home2.html`
  were deleted 2026-07-08 (git history has them).
- `savings-calculator.html` deploys to `/calculator` (name ≠ path; canonical rules).
- `ula-the-ai-updater.html` is the only Ula file in the repo (canonical `/ula`);
  there is no separate `ula.html` to keep in sync despite the filename.

## Current state (2026-07-27)

- Built & verified: home, botty-landing2, frank, ula, ava, banx, zoe, brenda,
  faq2, calculator, roofing, solar, hvac, terms, privacy.
- **Root cutover complete for every page.** All canonical tags, `Deploy as:`
  comments, and internal links repo-wide point at site root
  (`public_html/<name>/`) — the `/v2/` prefix no longer appears anywhere in the
  repo. Deploy step: Enrique uploads each page to its root-level folder on
  hosting.com cPanel (not `public_html/v2/<name>/` anymore).
- The Botty demo page keeps its own tracking number and its form protections
  (honeypot, dwell-time, TCPA line) — load-bearing, see CLAUDE.md.

## Open questions (resolve before related work)

1. **Analytics.** GTM (GTM-5FQDM29P) is installed on every page, but it adds a
   second bare `<script>` tag which currently fails `scripts/verify.py`'s
   "exactly one plain `<script>`" hosting rule sitewide (pre-existing, not
   caused by the root cutover) — needs a decision: merge into the main script
   block, or special-case GTM in verify.py.
2. **og:images.** Every head carries a TODO for a 1200×630 image.

## Suggested first terminal session

1. `git pull`, read this file + CLIENT-NOTES, run `python3 scripts/verify.py`.
2. Fetch `https://progressbot.ai/sitemap.xml` (or crawl the old nav) and complete
   MIGRATION-MAP.md so the mission has a full checklist.
3. ~~Delete legacy home files~~ — done 2026-07-08. ~~Resolve phone number
   policy~~ — done 2026-07-23. ~~Root cutover~~ — done 2026-07-27.
