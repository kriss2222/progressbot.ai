# CLAUDE.md — ProgressBot.AI v2 (github.com/kriss2222/progressbot.ai)

Marketing site for ProgressBot.AI (AI phone agents for home-service contractors).
**Mission:** translate every old progressbot.ai page into the v2 design system until
v2 IS the site — every page deploys at site root (`/<name>/`). **Root cutover
complete 2026-07-27:** the `/v2/` prefix is retired sitewide; every page's
canonical, `Deploy as:` path, and every internal link now point at root. See
`docs/context/CLIENT-NOTES.md`.
Every page = one self-contained HTML file for hosting.com shared hosting. No build
step, no framework — ever.

## Session start ritual

1. `git pull`
2. Read `docs/context/PROJECT-BRIEF.md` and `docs/context/CLIENT-NOTES.md`
   (client decisions live ONLY in that log — summaries only; never paste
   private message text into this public repo).
3. `python3 scripts/verify.py` — know the baseline before touching anything.
4. Work (rules below) → `python3 scripts/verify.py <changed files>` → commit only
   on green. Commit style: `page: what changed` (e.g. `solar: fix calc prefill`).
5. Deploying = uploading the file to its `Deploy as:` path on hosting.com.

## Golden rules

1. **verify.py green before every commit/deploy.** No exceptions.
2. **Never retype tokens, phone numbers, stats, or claims from memory** — copy
   tokens from `index.html`; facts from the claims inventory below or
   `docs/context/CONTENT-CAPSULES.md`. If a fact isn't in either, fetch the live
   old page first.
3. **Assert before replace:** count exact occurrences of the target string first;
   abort on surprises. Blind replace has already shipped one regression here.
4. **No invented facts** — no new stats, quotes, testimonials, or capabilities.
   Missing proof = say so on the page or leave it out.
5. Phone numbers: **resolved** — (863) 354-1635 everywhere, see below. Don't
   change without a new logged decision in CLIENT-NOTES.

## Repo layout (flat files; canonical tag = truth)

Filenames don't define URLs — each file's `<link rel="canonical">` and its
top-of-file `Deploy as:` comment do. Quirks to know:

- `index.html` = CURRENT homepage (canonical `/`, deploys to root; cut over from
  `home4.html` 2026-07-23). Legacy `home3.html` + duplicate
  `progressbot-home2.html` were deleted 2026-07-08 (recoverable from git history).
- `savings-calculator.html` → `/calculator` (name ≠ path).
- `ula-the-ai-updater.html` is the only Ula file in the repo (canonical → `/ula`);
  despite the filename there is no separate `ula.html` to keep in sync.
- `scripts/verify.py` = the quality gate. `docs/context/` = brief, client log,
  migration checklist, content capsules.
- `robots.txt`, `sitemap.xml`, `llms.txt` deploy verbatim to `public_html/`
  root (domain-root files, not per-page folders). See SEO section below.

## Hosting constraints (hard)

- HTML + CSS + vanilla JS, all inline, one file per page.
- Exactly one plain `<style>` and one plain `<script>` per file
  (`<script type="application/ld+json">` allowed as data; the Google Tag
  Manager loader snippet in `<head>` is also exempt - install it verbatim as
  Google recommends, don't merge it into the page script). No `<script src>`.
- Only external request: the Google Fonts URL (+ own-domain audio where used).
- **No backticks or `${}` in JS** (heredoc-generation safety + codebase
  convention) — string concatenation only. **No emoji. No raster images** —
  inline SVG feather-style icons only.
- Every file starts with a deployment comment; keep it accurate.

## Design system contract

Tokens live in `:root` and must be byte-identical across pages (verify.py checks
against the root-canonical file). Copy the block — never retype. Palette roles:
paper `#F3F4F1` / card white / ink `#14181D` / `--green #0E7B43` = **action** /
`--red #C6392B`+`--red-b` = **cost-of-inaction ONLY** / `--gold` stars only /
`--phone #0D1116` dark UI surfaces.

- Fonts: Big Shoulders Display 800 UPPERCASE (display) · Barlow 17px (body) ·
  IBM Plex Mono (uppercase letterspaced "dispatch log" labels). One fonts URL.
- Red discipline: one–two red beats per page max, measured on **styled elements**
  (`.leak-n`, `.eq b`, `.redline`, `.mr-flag`), never text mentions. `ula.html`
  is deliberately red-free (no published stat → no red).
- Logo (client decisions 2026-07-09): header `.brand` = inline SVG mascot
  (class `bmark`) + the wordmark text. Per-page variants: **headset** bot =
  default (canonical copy: `index.html`) · **hard-hat** bot on roofing + hvac
  (copy: `roofing.html`) · **sunglasses** bot on solar (copy: `solar.html`).
  Copy the `<svg class="bmark">` block, never redraw. New industry pages: pick
  the trade-appropriate variant, default to headset. Footer brand uses the
  raster PNG lockup (`ProgressBot.AI-green-v2-logo.png`), header does not.
  Favicon = simplified fat-stroke headset bot as data-URI SVG
  `<link rel="icon">`, identical on every page (copy from `index.html`).
  og:image = mascot lockup PNGs in `og/` (deploy the folder to site root as
  `/og/`): `og.png` default · `og-hardhat.png` roofing+hvac · `og-solar.png`
  solar. Every head points at its variant; twitter:card = summary_large_image.
  Regenerate via headless Chrome from the compositor in the og assets, keep
  1200x630.
- Components: `.wrap` 1160px; cards 1px `--line` radius 14–18; buttons radius 9;
  mono eyebrow + 26×2px green rule; sticky header (static ≤860) with pulse
  "on shift"; dark mono-headed footer; sticky mobile CTA ≤860; `.rv` reveals.
- Animated signatures (dispatch board, phone sim, contract check, timeline,
  calculator count-ups) must: render complete static state without JS, pause via
  IntersectionObserver off-screen, go static under `prefers-reduced-motion`.
- Voice: blunt, money-first, trades-aware. **No em dashes anywhere** (client
  rule 2026-07-08, enforced by verify.py): use a plain "-". Only exemption:
  verbatim legal body text on /terms + /privacy.

## SEO + AI discoverability (added 2026-07-27)

- `robots.txt` (repo root) allows every crawler, search and AI alike
  (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, etc. listed by name),
  and points at `sitemap.xml`. Client decision: maximize AI-answer-engine
  visibility over blocking training crawlers - see CLIENT-NOTES.
- `sitemap.xml` (repo root) lists every canonical URL. **New page = new
  `<url>` entry here**, or `scripts/verify.py`'s site-level check fails
  (it diffs every page's canonical tag against the sitemap both ways).
- `llms.txt` (repo root) is the AI-crawler-facing summary (llmstxt.org
  convention): company one-liner, the verified claims inventory below, and a
  link per agent/page. Keep it in sync with the claims inventory and site
  map - same "no invented facts" rule applies, it's public copy.
- Every page carries exactly one `<script type="application/ld+json">`
  block (`verify.py` now fails on a missing one). Pattern: `Service` +
  `provider: Organization` (+ `FAQPage` mirroring any on-page mini-FAQ,
  count-checked against `<details class="qa">`) for agent/industry pages;
  `Organization` + `WebSite` + `ItemList` of the seven agents on the
  homepage; plain `WebPage` for terms/privacy. Copy the pattern from the
  nearest matching page - don't invent new schema types without a reason.

## Phone numbers — RESOLVED (see CLIENT-NOTES 2026-07-23)

Client confirmed: use **(863) 354-1635** everywhere, no split. `verify.py`
defaults to `PB_PHONE_POLICY=single_354`; pass `PB_PHONE_POLICY=split` only to
check the pre-resolution legacy state intentionally.

## Claims inventory (the ONLY permitted facts)

- Answers 24/7 within 3 rings; no voicemail; routes & triages; books onto
  calendar; human handoff; recaps texted; CRM auto-updates.
- One missed call = $10,000 job → 52 × 1 × $10,000 = **$520k+/yr** frame.
- Live in 1–2 weeks · 70–90% less than human reps · ROI 30–60 days · 3–5× calls ·
  20–40% conversion ("typical results" framing).
- TCPA · GDPR · CCPA; encrypted; audit trails; multilingual (incl. Spanish).
- **NREL 2022: 33% of residential solar sales cancel — SOLAR-ONLY.**
- Blake Ambrester (CEO, Solar Bear): welcome calls → ~20% fewer cancellations.
  Verbatim quote lives on frank.html; elsewhere only as "reported ~20%", labeled
  "reported by one customer, not a promise".
- Agents: Banx (cold caller, aged/dormant leads) · Zoe (24/7 receptionist) ·
  Brenda (web bot) · Botty (AI sales rep — LIVE DEMO) · Frank (welcome call
  minutes after signing; catches rep promises; voicemail retry; setup fee +
  per-call) · Ula (weekly + milestone update calls; flags at-risk customers;
  CRM/quoting/calendar/dialers/financing integrations) · Ava (answers your
  personal phone line 24/7, friendly natural voice; accurate info about you or
  your business; books into Google Calendar; texts owner a summary post-call;
  texts caller a confirmation/thank-you — NO published stats, page is red-free).
- **The public demo runs the DEFAULT ROOFING FLOW.** Non-roofing pages promoting
  it must disclose ("your build gets trained on X"). Roofing pages may lean in.
- Quotes stay anonymized (trade + region). **No HVAC testimonial exists** — that
  page runs on the trust claim only.
- Longer source copy per old page: `docs/context/CONTENT-CAPSULES.md`.

## UTM + calculator conventions

`utm_source=<page>_page` (homepage: `homepage`) · `utm_medium=internal` ·
`utm_campaign=botty_demo|calculator` · `utm_content=<placement>` unique per page.
Calculator deep links carry state (`?tab=&mc=&cr=&jv=&dm=&cv=&xr=&rd=`); industry
prefiller MUST match that trade's calculator chip: Roofing `tab=calls&cr=35&jv=12000`
· Solar `tab=cancel&cv=28000&xr=33&rd=20` · HVAC `tab=calls&cr=40&jv=8000`.

## Site map (canonical → repo file · primary CTA · signature)

| Canonical | File | CTA | Signature |
|---|---|---|---|
| `/` | index.html | Demo | dispatch board + crew board |
| `/botty-landing2` | botty-landing2.html | 2-step form | phone sim; honeypot+dwell; TCPA |
| `/frank` | frank.html | Tel | contract check (red mismatch) |
| `/ula` | ula-the-ai-updater.html | Tel | project timeline (red-free) |
| `/ava` | ava.html | Tel | call-log timeline (red-free) |
| `/banx` | banx.html | Tel | outbound-run timeline + real cold-call player (red-free) |
| `/zoe` | zoe.html | Tel | 11:52 PM inbound timeline; one $10k redline |
| `/brenda` | brenda.html | Tel | web-chat timeline (red-free) |
| `/terms` | terms.html | - | legal restyle, text verbatim |
| `/privacy` | privacy.html | - | legal restyle, text verbatim |
| `/faq2` | faq.html | Demo | accordions + mirrored FAQPage JSON-LD |
| `/calculator` | savings-calculator.html | Demo/Tel | URL-state sliders, copy-link |
| `/roofing` | roofing.html | **Demo** (script match) | roofing dispatch; $520k eq |
| `/solar` | solar.html | **Tel** (mismatch→disclosed) | red 33% burn; Frank mini |
| `/hvac` | hvac.html | **Tel** (disclosed) | emergency lens; $520k eq |

Old pages still live (linkable): `/franks-welcome-call-faq` (rebuild pending),
`/terms-and-conditions/`, `/privacy.html` — **never rewrite legal text**.
Full checklist: `docs/context/MIGRATION-MAP.md`.

## Industry template (capsule system)

`roofing.html` is canonical. Exactly **9 `[industry capsule]` markers** per
industry page: 6 HTML zones (hero copy, static feed rows, calc prefill, agent
one-liners, moments, mini-FAQ) + 2 JS (`EVENTS`, `STATS`) + 1 header note.
New industry = copy roofing, swap only capsules, then head/canonical/OG, global
`utm_source`, JSON-LD (`Service`+`FAQPage` mirroring the mini-FAQ), calc prefill
per chip table, Demo-vs-Tel by script match, and check trade proof exists.
Agent pages follow the frank/ula pattern.

## Editing workflow (each rule traces to a real incident)

1. Read the whole file first — CSS/HTML/JS interlock in ~50KB single files.
2. Assert occurrence counts before every replace.
3. **JS block-order trap:** blocks were assembled incrementally; when removing a
   block between comment markers, confirm what's actually between them — a lazy
   span-regex once deleted the dispatch engine with an unused player. After any
   script surgery confirm engines exist (`startDispatch`/`runSim`/`runCheck`/
   `runTimeline`/calculator `render`).
4. Gate every copy/deploy/commit on verify exit 0 (an ungated `cp` once shipped a
   stale file).
5. Round before comparing numbers (float precision caused a false FAIL).
6. Live may drift from repo: raw HTML can't be fetched reliably — get the file,
   diff before wholesale edits.
7. Landing form protections (honeypot `website`, 3s dwell, `isHuman`, TCPA line)
   are load-bearing; server must still re-verify (rate-limit, SMS-confirm).
8. og:image is wired in every head (see design contract); new pages copy the
   five-tag block and pick the right `/og/` variant.
