# ProgressBot.AI v2 — Project Brief

Read this at the start of any non-trivial session. The rules live in `/CLAUDE.md`;
this file is the *why* and the *state*.

## Mission

Translate **every page of the old progressbot.ai site** into the v2 design system —
one self-contained HTML file per page, same verified facts, new skin and structure —
until v2 IS the site. The homepage ships to the **root** (`public_html/index.html`);
everything else lives under `/v2/<name>/index.html`. `docs/context/MIGRATION-MAP.md`
is the checklist; a page is *done* when it passes `scripts/verify.py`, is deployed,
and everything that linked to the old page links to the new one.

## Who's who

- **Builder:** Enrique — works from this repo (terminal + Claude Code), deploys to
  hosting.com shared hosting by uploading files.
- **Client:** owns progressbot.ai and the business facts. Client decisions arrive
  over WhatsApp and MUST be logged in `docs/context/CLIENT-NOTES.md` — that file is
  the only client-instruction memory future sessions have.

## How the repo maps to the live site

Flat `.html` files at repo root. Each file's `<link rel="canonical">` and its
top-of-file `Deploy as:` comment define its live path — filenames don't. Known quirks:

- `home4.html` = the CURRENT homepage (canonical `/`). `home3.html` is legacy and
  fails verification on purpose; `progressbot-home2.html` is a byte-identical
  duplicate of home4. **Recommended cleanup: delete home3 + progressbot-home2.**
- `savings-calculator.html` deploys to `/v2/calculator` (name ≠ path; canonical rules).
- `ula-the-ai-updater.html` is a byte-identical copy of `ula.html`, kept so the OLD
  WordPress URL can serve the new page (its canonical correctly points to `/v2/ula`).
  When editing Ula, update BOTH or re-copy one over the other.

## Current state (2026-07-08)

- Built & verified: home (root-ready), botty-landing2, frank, ula, faq2, calculator,
  roofing, solar, hvac. Live under `/v2/...`; the live `/v2/home3` deployment predates
  the latest integrations — redeploy pending; root cutover pending client go-ahead.
- The Botty demo page keeps its own tracking number and its form protections
  (honeypot, dwell-time, TCPA line) — load-bearing, see CLAUDE.md.

## Open questions (resolve before related work)

1. **PHONE NUMBERS.** README.md (2026-07-03) says use ONLY (863) 354-1635. Every
   page built and deployed since uses (863) 356-0181 except the demo landing. One
   WhatsApp to the client settles it. Then: set the policy in `scripts/verify.py`
   (env `PB_PHONE_POLICY`), convert pages if needed, update CLAUDE.md + this file,
   log the decision in CLIENT-NOTES.
2. **Root cutover.** When does home4 actually replace the WordPress homepage at `/`?
3. **Analytics.** No snippet has been confirmed on any page — all UTM work is
   unmeasured until this is checked/added.
4. **og:images.** Every head carries a TODO for a 1200×630 image.

## Suggested first terminal session

1. `git pull`, read this file + CLIENT-NOTES, run `python3 scripts/verify.py`.
2. Fetch `https://progressbot.ai/sitemap.xml` (or crawl the old nav) and complete
   MIGRATION-MAP.md so the mission has a full checklist.
3. Resolve open question 1 with the client; execute the outcome.
4. Delete legacy home files; commit.
