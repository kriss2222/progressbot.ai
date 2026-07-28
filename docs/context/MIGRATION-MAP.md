# Migration map — old progressbot.ai → v2

Mission checklist. A row is DONE when the v2 page passes verify.py, is deployed,
and inbound links are retargeted.

**Inventory note (2026-07-08):** no sitemap exists — `/sitemap.xml`,
`/sitemap_index.xml`, `/wp-sitemap.xml`, and `/robots.txt` all 404. Inventory
below comes from crawling the live homepage nav/footer links instead. Homepage
links `/faq` (not `/faq.html`) — both presumably serve the same page.

**2026-07-27: root cutover complete.** Every v2 target below moved off `/v2/<name>`
to root `/<name>` — the table is updated to the current (root) paths. Deploy
folders on hosting.com are now `public_html/<name>/`, not `public_html/v2/<name>/`.

| Old URL | v2 target | Repo file | Status |
|---|---|---|---|
| `/` (WordPress home) | `/` (root) | index.html | DONE — root cutover live in repo |
| `/v2/demo2` (old demo) | `/botty-landing2` | botty-landing2.html | DONE (live) |
| `/frank-confirmation-voice-bot/` | `/frank` | frank.html | BUILT — deploy latest |
| `/ula-the-ai-updater/` | `/ula` | ula-the-ai-updater.html | BUILT — deploy |
| `/faq.html` | `/faq` | faq.html | BUILT — deploy latest |
| `/franks-welcome-call-faq` | `/frank-faq` | frank-faq.html | BUILT 2026-07-08 (20 Q&As from live page, verbatim copy in CONTENT-CAPSULES) — deploy pending; footers retargeted |
| `/terms-and-conditions/` | `/terms` (restyle only) | terms.html | BUILT 2026-07-08 — legal text verbatim from live page (text-node integrity asserted); deploy pending. NOTE: live legal text cites (863) 654-1635 + kristen@progressbot.ai — third number, resolved as a typo, converted to 354-1635 2026-07-23 |
| `/privacy.html` | `/privacy` (restyle only) | privacy.html | BUILT 2026-07-08 — legal text verbatim from live page (text-node integrity asserted); deploy pending |
| — (new) | `/calculator` | savings-calculator.html | DONE concept — deploy latest |
| — (new) | `/roofing` `/solar` `/hvac` | roofing/solar/hvac.html | BUILT — deploy |
| `/ava-the-assistant` | `/ava` | ava.html | BUILT 2026-07-08 (live copy captured in CONTENT-CAPSULES; Ava added to claims inventory; red-free, Tel CTA) — deploy pending; every footer links to it, incl. botty-landing2 (Product list) |
| `/solar-ai-team/` | TBD — overlaps `/solar` | — | **NOT BUILT** — found via nav crawl 2026-07-08. Agent-roster page for solar (Botty/Banx/Frank/Ava/Ula), headline "In 5 Years, there won't be any human solar sales reps." Decide: rebuild vs. redirect to `/solar`. |
| — (new) | `/banx` `/zoe` `/brenda` | banx/zoe/brenda.html | BUILT 2026-07-08 from homepage crew-board copy + claims inventory only (no old pages existed). Banx carries the real Natalie cold-call recording; Zoe carries the $10k missed-call redline; Brenda red-free. Deploy pending. Crew boards on home + roofing/solar/hvac now show all seven agents (Ava card added, counts updated, cards link to agent pages) |
| — (new, backlog) | Spanish versions, post-demo page | — | NOT BUILT |
