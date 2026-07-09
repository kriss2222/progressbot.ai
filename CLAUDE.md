# CLAUDE.md — ProgressBot.AI v2 (github.com/kriss2222/progressbot.ai)

Marketing site for ProgressBot.AI (AI phone agents for home-service contractors).
**Mission:** translate every old progressbot.ai page into the v2 design system until
v2 IS the site — homepage at root, everything else under `/v2/<name>/`.
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
   tokens from `home4.html`; facts from the claims inventory below or
   `docs/context/CONTENT-CAPSULES.md`. If a fact isn't in either, fetch the live
   old page first.
3. **Assert before replace:** count exact occurrences of the target string first;
   abort on surprises. Blind replace has already shipped one regression here.
4. **No invented facts** — no new stats, quotes, testimonials, or capabilities.
   Missing proof = say so on the page or leave it out.
5. Phone numbers are an **unresolved client question** — see below. Don't "fix"
   them without a logged decision in CLIENT-NOTES.

## Repo layout (flat files; canonical tag = truth)

Filenames don't define URLs — each file's `<link rel="canonical">` and its
top-of-file `Deploy as:` comment do. Quirks to know:

- `home4.html` = CURRENT homepage (canonical `/`, deploys to root). Legacy
  `home3.html` + duplicate `progressbot-home2.html` were deleted 2026-07-08
  (recoverable from git history). The live `/v2/home3` URL still serves an old
  deploy and is what v2 nav links point to until root cutover.
- `savings-calculator.html` → `/v2/calculator` (name ≠ path).
- `ula-the-ai-updater.html` = byte-copy of `ula.html` serving the old URL path
  (canonical correctly → `/v2/ula`). Edit Ula ⇒ update both (re-copy one over the
  other), or the alias drifts.
- `scripts/verify.py` = the quality gate. `docs/context/` = brief, client log,
  migration checklist, content capsules.

## Hosting constraints (hard)

- HTML + CSS + vanilla JS, all inline, one file per page.
- Exactly one plain `<style>` and one plain `<script>` per file
  (`<script type="application/ld+json">` allowed as data). No `<script src>`.
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
- Components: `.wrap` 1160px; cards 1px `--line` radius 14–18; buttons radius 9;
  mono eyebrow + 26×2px green rule; sticky header (static ≤860) with pulse
  "on shift"; dark mono-headed footer; sticky mobile CTA ≤860; `.rv` reveals.
- Animated signatures (dispatch board, phone sim, contract check, timeline,
  calculator count-ups) must: render complete static state without JS, pause via
  IntersectionObserver off-screen, go static under `prefers-reduced-motion`.
- Voice: blunt, money-first, trades-aware. **No em dashes anywhere** (client
  rule 2026-07-08, enforced by verify.py): use a plain "-". Only exemption:
  verbatim legal body text on /v2/terms + /v2/privacy.

## Phone numbers — OPEN QUESTION (see CLIENT-NOTES)

README.md (2026-07-03): use ONLY **(863) 354-1635**. But every page built and
deployed since uses **(863) 356-0181**, except the demo landing (354 — tracking
split). Until the client confirms: verify.py defaults to the split
(`PB_PHONE_POLICY=split`); the README directive is one env var away
(`PB_PHONE_POLICY=single_354`). Whatever is decided: log it, set the policy,
convert pages, update this section.

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
| `/` | home4.html | Demo | dispatch board + crew board |
| `/v2/botty-landing2` | botty-landing2.html | 2-step form | phone sim; honeypot+dwell; TCPA |
| `/v2/frank` | frank.html | Tel | contract check (red mismatch) |
| `/v2/ula` | ula.html (+alias) | Tel | project timeline (red-free) |
| `/v2/ava` | ava.html | Tel | call-log timeline (red-free) |
| `/v2/faq2` | faq.html | Demo | accordions + mirrored FAQPage JSON-LD |
| `/v2/calculator` | savings-calculator.html | Demo/Tel | URL-state sliders, copy-link |
| `/v2/roofing` | roofing.html | **Demo** (script match) | roofing dispatch; $520k eq |
| `/v2/solar` | solar.html | **Tel** (mismatch→disclosed) | red 33% burn; Frank mini |
| `/v2/hvac` | hvac.html | **Tel** (disclosed) | emergency lens; $520k eq |

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
8. og:image TODOs (1200×630) sit in every head.
