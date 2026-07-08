#!/usr/bin/env python3
"""ProgressBot.AI v2 page verifier. Run before every commit/deploy.

Usage:  python3 scripts/verify.py [file.html ...]     (no args = all *.html in repo root)
Exit 0 = shippable. Any FAIL = exit 1. See CLAUDE.md for the rules encoded here.
Phone policy: env PB_PHONE_POLICY = 'split' (default: 354 on demo landing, 356 elsewhere)
or 'single_354' (README directive). OPEN QUESTION - see docs/context/CLIENT-NOTES.md.
"""
import sys, os, re, json, glob
from html.parser import HTMLParser

POLICY = os.environ.get('PB_PHONE_POLICY', 'split')
P356, P354 = '(863) 356-0181', '(863) 354-1635'
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF]')
# page-link forms only (trailing quote) - asset subpaths like .../voice-bot/file.mp3 are legit
STALE = ['progressbot.ai/frank-confirmation-voice-bot/"', 'progressbot.ai/ula-the-ai-updater/"',
         'progressbot.ai/faq.html"', 'progressbot.ai/v2/botty-landing?', 'progressbot.ai/v2/botty-landing"']
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

# keyed by canonical path
CFG = {
 '/':                  dict(utm='homepage',        must=['startDispatch', 'Built for roofing']),
 '/v2/botty-landing2': dict(utm=None, phone=P354,  must=['id="website"', 'isHuman', 'By submitting, you agree to receive a phone call']),
 '/v2/frank':          dict(utm='frank_page',      must=['runCheck']),
 '/v2/ula':            dict(utm='ula_page',        must=['runTimeline'], red_free=True),
 '/v2/faq2':           dict(utm='faq_page',        must=[]),
 '/v2/frank-faq':       dict(utm='frank_faq_page',  must=[]),
 '/v2/calculator':     dict(utm='calculator_page', must=['URLSearchParams', '$468,000']),
 '/v2/roofing':        dict(utm='roofing_page',    must=[], industry=True),
 '/v2/solar':          dict(utm='solar_page',      must=['NREL', 'tab=cancel'], industry=True),
 '/v2/hvac':           dict(utm='hvac_page',       must=[], industry=True, forbid=['NREL', '33%']),
}
RED_CLASSES = ['class="leak-n"', 'class="mr-flag"', '<p class="eq', 'class="redline']

def balance(s):
    class C(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True); self.st=[]; self.err=[]
        def handle_starttag(self, t, a):
            if t not in VOID: self.st.append(t)
        def handle_endtag(self, t):
            if self.st and self.st[-1]==t: self.st.pop()
            else: self.err.append(t)
    c=C(); c.feed(s); return not c.err and not c.st

def tokens(s):
    m = re.search(r':root\{(.*?)\}', s, re.S)
    return sorted(re.sub(r'/\*.*?\*/', '', m.group(1)).replace(' ', '').split(';')) if m else None

def check(path, ref_tokens):
    s = open(path, encoding='utf-8').read()
    fails, warns = [], []
    m = re.search(r'rel="canonical" href="https://progressbot\.ai(/[^"]*?)/?"', s)
    canon = m.group(1) if m else None
    if canon and canon != '/': canon = canon.rstrip('/')
    cfg = CFG.get(canon or '', {})
    if canon is None: fails.append('no canonical tag')
    elif not cfg: warns.append('unknown canonical %s - generic checks only' % canon)

    if not balance(s): fails.append('unbalanced tags')
    if ref_tokens and tokens(s) != ref_tokens: fails.append('design tokens differ from reference')
    if s.count('<script>') != 1: fails.append('expected exactly one plain <script>')
    if '<script src' in s: fails.append('external <script src> forbidden')
    if '`' in s: fails.append('backtick found')
    if '${' in s: fails.append('${ found (template literal)')
    if EMOJI.search(s): fails.append('emoji found')
    if s.count('<h1') != 1: fails.append('expected exactly one <h1>')
    for u in STALE:
        if u in s: fails.append('stale URL: ' + u)

    phone = cfg.get('phone', P356)
    if POLICY == 'single_354': phone = P354
    other = P354 if phone == P356 else P356
    if phone not in s: fails.append('expected phone %s missing' % phone)
    if other in s: fails.append('forbidden phone %s present' % other)

    tags = re.findall(r'utm_content=([a-z_]+)', s)
    if len(set(tags)) != len(tags): fails.append('duplicate utm_content placements')
    if cfg.get('utm') and 'utm_source=' + cfg['utm'] not in s:
        fails.append('expected utm_source=%s' % cfg['utm'])

    for needle in cfg.get('must', []):
        if needle not in s: fails.append('missing required content: %r' % needle)
    for needle in cfg.get('forbid', []):
        if needle in s: fails.append('forbidden content present: %r' % needle)

    main = re.search(r'<main.*</main>', s, re.S)
    main = main.group(0) if main else s
    if cfg.get('red_free'):
        hits = [c for c in RED_CLASSES if c in main]
        if hits: fails.append('red-free page has red-styled elements: %s' % hits)
    if cfg.get('industry') and s.count('[industry capsule]') != 9:
        fails.append('industry template needs exactly 9 capsule markers, found %d' % s.count('[industry capsule]'))

    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: data = json.loads(ld)
        except Exception as e: fails.append('JSON-LD parse error: %s' % e); continue
        graph = data.get('@graph', [data])
        for g in graph:
            if g.get('@type') == 'FAQPage':
                n, d = len(g.get('mainEntity', [])), s.count('<details class="qa"')
                if n != d: fails.append('FAQPage JSON-LD (%d) != visible accordions (%d)' % (n, d))
    return canon, fails, warns

def main():
    files = sys.argv[1:] or sorted(glob.glob('*.html'))
    if not files: print('no html files found'); return 1
    ref = None
    for f in files:  # reference tokens = first root-canonical file, else first file
        s = open(f, encoding='utf-8').read()
        if 'rel="canonical" href="https://progressbot.ai/"' in s: ref = tokens(s); break
    if ref is None: ref = tokens(open(files[0], encoding='utf-8').read())
    bad = 0
    if POLICY == 'split':
        print('NOTE: phone policy = split (356 default / 354 on demo landing).')
        print('      README.md says only 354-1635 - unresolved, see docs/context/CLIENT-NOTES.md.')
        print('      To enforce README: PB_PHONE_POLICY=single_354 python3 scripts/verify.py')
    for f in files:
        canon, fails, warns = check(f, ref)
        tag = 'OK  ' if not fails else 'FAIL'
        print('%s %-26s %s' % (tag, os.path.basename(f), canon or '?'))
        for w in warns: print('        warn: ' + w)
        for x in fails: print('        - ' + x)
        bad += bool(fails)
    print('\n%d file(s), %d failing' % (len(files), bad))
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
