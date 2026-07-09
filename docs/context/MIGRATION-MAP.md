# Migration map — old progressbot.ai → v2

Mission checklist. A row is DONE when the v2 page passes verify.py, is deployed,
and inbound links are retargeted.

**Inventory note (2026-07-08):** no sitemap exists — `/sitemap.xml`,
`/sitemap_index.xml`, `/wp-sitemap.xml`, and `/robots.txt` all 404. Inventory
below comes from crawling the live homepage nav/footer links instead. Homepage
links `/faq` (not `/faq.html`) — both presumably serve the same page.

| Old URL | v2 target | Repo file | Status |
|---|---|---|---|
| `/` (WordPress home) | `/` (root) | home4.html | BUILT — root cutover pending (open Q2) |
| `/v2/demo2` (old demo) | `/v2/botty-landing2` | botty-landing2.html | DONE (live) |
| `/frank-confirmation-voice-bot/` | `/v2/frank` | frank.html | BUILT — deploy latest |
| `/ula-the-ai-updater/` | `/v2/ula` | ula.html (+ alias file) | BUILT — deploy both paths |
| `/faq.html` | `/v2/faq2` | faq.html | BUILT — deploy latest |
| `/franks-welcome-call-faq` | `/v2/frank-faq` | frank-faq.html | BUILT 2026-07-08 (20 Q&As from live page, verbatim copy in CONTENT-CAPSULES) — deploy pending; v2 footers retargeted |
| `/terms-and-conditions/` | `/v2/terms` (restyle only) | terms.html | BUILT 2026-07-08 — legal text verbatim from live page (text-node integrity asserted); deploy pending. NOTE: live legal text cites (863) 654-1635 + kristen@progressbot.ai — third number, kept verbatim, flagged as open question |
| `/privacy.html` | `/v2/privacy` (restyle only) | privacy.html | BUILT 2026-07-08 — legal text verbatim from live page (text-node integrity asserted); deploy pending |
| — (new) | `/v2/calculator` | savings-calculator.html | DONE concept — deploy latest |
| — (new) | `/v2/roofing` `/v2/solar` `/v2/hvac` | roofing/solar/hvac.html | BUILT — deploy |
| `/ava-the-assistant` | `/v2/ava` | ava.html | BUILT 2026-07-08 (live copy captured in CONTENT-CAPSULES; Ava added to claims inventory; red-free, Tel CTA) — deploy pending; every v2 footer links to it, incl. botty-landing2 (Product list) |
| `/solar-ai-team/` | TBD — overlaps `/v2/solar` | — | **NOT BUILT** — found via nav crawl 2026-07-08. Agent-roster page for solar (Botty/Banx/Frank/Ava/Ula), headline "In 5 Years, there won't be any human solar sales reps." Decide: rebuild vs. redirect to `/v2/solar`. |
| — (new) | `/v2/banx` `/v2/zoe` `/v2/brenda` | banx/zoe/brenda.html | BUILT 2026-07-08 from home4 crew-board copy + claims inventory only (no old pages existed). Banx carries the real Natalie cold-call recording; Zoe carries the $10k missed-call redline; Brenda red-free. Deploy pending. Crew boards on home4 + roofing/solar/hvac now show all seven agents (Ava card added, counts updated, cards link to agent pages) |
| — (new, backlog) | Spanish versions, post-demo page | — | NOT BUILT |
