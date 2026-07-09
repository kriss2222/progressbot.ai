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
| `/terms-and-conditions/` | `/v2/terms` (restyle only) | — | NOT BUILT — never rewrite legal text |
| `/privacy.html` | `/v2/privacy` (restyle only) | — | NOT BUILT — never rewrite legal text |
| — (new) | `/v2/calculator` | savings-calculator.html | DONE concept — deploy latest |
| — (new) | `/v2/roofing` `/v2/solar` `/v2/hvac` | roofing/solar/hvac.html | BUILT — deploy |
| `/ava-the-assistant` | `/v2/ava` | ava.html | BUILT 2026-07-08 (live copy captured in CONTENT-CAPSULES; Ava added to claims inventory; red-free, Tel CTA) — deploy pending; all v2 footers link to it (botty-landing2 excluded by design) |
| `/solar-ai-team/` | TBD — overlaps `/v2/solar` | — | **NOT BUILT** — found via nav crawl 2026-07-08. Agent-roster page for solar (Botty/Banx/Frank/Ava/Ula), headline "In 5 Years, there won't be any human solar sales reps." Decide: rebuild vs. redirect to `/v2/solar`. |
| — (new, backlog) | Banx / Zoe / Brenda agent pages | — | NOT BUILT (frank/ula pattern) |
| — (new, backlog) | Spanish versions, post-demo page | — | NOT BUILT |
