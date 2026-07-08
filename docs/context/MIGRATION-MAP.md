# Migration map — old progressbot.ai → v2

Mission checklist. A row is DONE when the v2 page passes verify.py, is deployed,
and inbound links are retargeted. **TODO first session: fetch
https://progressbot.ai/sitemap.xml and add every page missing from this table.**

| Old URL | v2 target | Repo file | Status |
|---|---|---|---|
| `/` (WordPress home) | `/` (root) | home4.html | BUILT — root cutover pending (open Q2) |
| `/v2/demo2` (old demo) | `/v2/botty-landing2` | botty-landing2.html | DONE (live) |
| `/frank-confirmation-voice-bot/` | `/v2/frank` | frank.html | BUILT — deploy latest |
| `/ula-the-ai-updater/` | `/v2/ula` | ula.html (+ alias file) | BUILT — deploy both paths |
| `/faq.html` | `/v2/faq2` | faq.html | BUILT — deploy latest |
| `/franks-welcome-call-faq` | `/v2/frank-faq` (proposed) | — | **NOT BUILT** (20 Q&As; re-fetch live page for content) |
| `/terms-and-conditions/` | `/v2/terms` (restyle only) | — | NOT BUILT — never rewrite legal text |
| `/privacy.html` | `/v2/privacy` (restyle only) | — | NOT BUILT — never rewrite legal text |
| — (new) | `/v2/calculator` | savings-calculator.html | DONE concept — deploy latest |
| — (new) | `/v2/roofing` `/v2/solar` `/v2/hvac` | roofing/solar/hvac.html | BUILT — deploy |
| — (new, backlog) | Banx / Zoe / Brenda agent pages | — | NOT BUILT (frank/ula pattern) |
| — (new, backlog) | Spanish versions, post-demo page | — | NOT BUILT |
