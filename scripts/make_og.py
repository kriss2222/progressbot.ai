#!/usr/bin/env python3
"""Regenerate the og:image assets in og/ (1200x630 PNG, one per mascot variant).

Usage: python3 scripts/make_og.py   (needs Google Chrome installed; macOS path below)

Fetches the site fonts from Google Fonts, composites the mascot lockup in a
1200x630 HTML page, and screenshots it with headless Chrome. Mascot drawings
mirror the <svg class="bmark"> blocks in the pages (headset: home4.html,
hard hat: roofing.html, sunglasses: solar.html) - if those change, change
BOTS below to match.
"""
import base64, os, re, subprocess, sys, tempfile, urllib.request

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120.0 Safari/537.36'}
FONTS = {
    'BSD800':    'https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&display=swap',
    'BARLOW600': 'https://fonts.googleapis.com/css2?family=Barlow:wght@600&display=swap',
    'MONO500':   'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&display=swap',
}

PRE = '<g fill="none" stroke="#14181D" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">'
HEAD = ('<rect x="22" y="30" width="76" height="62" rx="20" fill="#FFFFFF"/>'
        '<rect x="9" y="48" width="16" height="30" rx="8" fill="#0E7B43"/>'
        '<rect x="95" y="48" width="16" height="30" rx="8" fill="#0E7B43"/>')
FACE = ('<circle cx="76" cy="58" r="9.5" fill="#FFFFFF"/>'
        '<circle cx="76" cy="58" r="4.2" fill="#0E7B43" stroke="none"/>'
        '<circle cx="77.8" cy="56.2" r="1.5" fill="#FFFFFF" stroke="none"/>'
        '<path d="M36 57c3.5 5.5 11.5 5.5 15 0"/>'
        '<path d="M50 76c4 5 16 5 20 0"/>')
GEAR = '<path d="M16 78c-1 13 8 17 16 13"/><rect x="28" y="86" width="13" height="9" rx="4.5" fill="#0E7B43"/>'
BAND = '<path d="M16 52C24 16 96 16 104 52"/>'
HAT = ('<path d="M34 25C36 11 52 7 60 7c8 0 24 4 26 18Z" fill="#0E7B43"/>'
       '<rect x="24" y="24" width="72" height="9" rx="4.5" fill="#0E7B43"/>')
SHADES = ('<rect x="30" y="49" width="24" height="17" rx="6" fill="#14181D"/>'
          '<rect x="66" y="49" width="24" height="17" rx="6" fill="#14181D"/>'
          '<path d="M54 54h12"/><path d="M30 56h-5"/><path d="M90 56h5"/>'
          '<path d="M50 78c4 5 16 5 20 0"/>')
BOTS = {
    'og':         PRE + BAND + HEAD + GEAR + FACE + '</g>',
    'og-hardhat': PRE + HEAD + HAT + FACE + '</g>',
    'og-solar':   PRE + BAND + HEAD + GEAR + SHADES + '</g>',
}
TAGLINE = {
    'og':         'AI phone agents for home-service contractors',
    'og-hardhat': 'AI phone agents for roofing and HVAC contractors',
    'og-solar':   'AI phone agents for solar companies',
}

TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8">
<style>
@font-face{font-family:'Big Shoulders Display';font-weight:800;src:url(data:font/woff2;base64,__BSD800__) format('woff2')}
@font-face{font-family:'Barlow';font-weight:600;src:url(data:font/woff2;base64,__BARLOW600__) format('woff2')}
@font-face{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,__MONO500__) format('woff2')}
*{margin:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden}
body{background:#F3F4F1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;border-top:10px solid #0E7B43}
.lock{display:flex;align-items:center;gap:44px}
.wm{font-family:'Big Shoulders Display';font-weight:800;font-size:120px;line-height:1;letter-spacing:.03em;text-transform:uppercase;color:#14181D;white-space:nowrap}
.wm span{color:#0E7B43}
.tag{font-family:'Barlow';font-weight:600;font-size:30px;color:#454D48}
.mono{font-family:'IBM Plex Mono';font-weight:500;font-size:17px;letter-spacing:.16em;text-transform:uppercase;color:#68716B;display:flex;align-items:center;gap:14px;margin-top:10px}
.mono i{width:12px;height:12px;border-radius:50%;background:#0E7B43}
</style></head>
<body>
  <div class="lock">
    <svg viewBox="0 0 120 120" width="230" height="230">__BOT__</svg>
    <div class="wm">Progressbot<span>.AI</span></div>
  </div>
  <div class="tag">__TAGLINE__</div>
  <div class="mono"><i></i>On shift 24/7 &middot; Answered before the third ring</div>
</body></html>
"""

def latin_woff2_b64(css_url):
    css = urllib.request.urlopen(urllib.request.Request(css_url, headers=UA)).read().decode()
    latin = re.split(r'/\* latin \*/', css)[-1]
    url = re.search(r'url\((https://[^)]+woff2)\)', latin).group(1)
    return base64.b64encode(urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read()).decode()

def main():
    if not os.path.exists(CHROME):
        sys.exit('Chrome not found at ' + CHROME)
    os.makedirs('og', exist_ok=True)
    tpl = TEMPLATE
    for key, url in FONTS.items():
        tpl = tpl.replace('__' + key + '__', latin_woff2_b64(url))
    with tempfile.TemporaryDirectory() as tmp:
        for name, bot in BOTS.items():
            page = os.path.join(tmp, name + '.html')
            open(page, 'w').write(tpl.replace('__BOT__', bot).replace('__TAGLINE__', TAGLINE[name]))
            out = os.path.abspath(os.path.join('og', name + '.png'))
            subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                            '--force-device-scale-factor=1', '--window-size=1200,630',
                            '--virtual-time-budget=4000', '--screenshot=' + out,
                            'file://' + page], check=True, capture_output=True)
            print('wrote', out)

if __name__ == '__main__':
    main()
