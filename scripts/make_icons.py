import os, sys
from playwright.sync_api import sync_playwright
OUT = sys.argv[1]

DEFS = '''
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4f46e5"/><stop offset=".55" stop-color="#6d6cf5"/><stop offset="1" stop-color="#22b8f0"/>
  </linearGradient>
  <radialGradient id="glow" cx=".8" cy=".15" r=".6">
    <stop offset="0" stop-color="#f0abfc" stop-opacity=".75"/><stop offset="1" stop-color="#f0abfc" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glow2" cx=".1" cy=".95" r=".55">
    <stop offset="0" stop-color="#67e8f9" stop-opacity=".55"/><stop offset="1" stop-color="#67e8f9" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity=".12"/>
  </linearGradient>
  <linearGradient id="arc" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#fde68a"/><stop offset="1" stop-color="#fb923c"/>
  </linearGradient>
</defs>'''

# 스톱워치 그림 (1024 좌표계, 중심 512,560)
def watch():
    import math
    cx, cy, r = 512, 568, 300
    # 남은 시간 호: 12시에서 시계방향 270도
    a0, a1 = -90, 180
    x0, y0 = cx + 250*math.cos(math.radians(a0)), cy + 250*math.sin(math.radians(a0))
    x1, y1 = cx + 250*math.cos(math.radians(a1)), cy + 250*math.sin(math.radians(a1))
    ticks = ''.join(
        f'<line x1="{cx+222*math.cos(math.radians(a))}" y1="{cy+222*math.sin(math.radians(a))}" '
        f'x2="{cx+196*math.cos(math.radians(a))}" y2="{cy+196*math.sin(math.radians(a))}" '
        f'stroke="#fff" stroke-opacity=".85" stroke-width="16" stroke-linecap="round"/>'
        for a in range(-90, 270, 90))
    return f'''
  <rect x="452" y="170" width="120" height="70" rx="26" fill="#fff" fill-opacity=".92"/>
  <rect x="490" y="228" width="44" height="60" rx="14" fill="#fff" fill-opacity=".92"/>
  <rect x="742" y="262" width="80" height="48" rx="22" fill="#fff" fill-opacity=".8" transform="rotate(45 782 286)"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glass)" stroke="#fff" stroke-opacity=".75" stroke-width="14"/>
  <circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="34"/>
  <path d="M{x0:.1f} {y0:.1f} A250 250 0 1 1 {x1:.1f} {y1:.1f}" fill="none" stroke="url(#arc)" stroke-width="34" stroke-linecap="round"/>
  {ticks}
  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-170}" stroke="#fff" stroke-width="30" stroke-linecap="round"/>
  <line x1="{cx}" y1="{cy}" x2="{cx+110}" y2="{cy+64}" stroke="#fff" stroke-width="30" stroke-linecap="round"/>
  <circle cx="{cx}" cy="{cy}" r="34" fill="#fff"/>
  <circle cx="{cx}" cy="{cy}" r="14" fill="#5b5bf0"/>'''

def bg(shape):
    if shape == 'square':  clip = '<rect width="1024" height="1024" rx="230"/>'
    elif shape == 'circle': clip = '<circle cx="512" cy="512" r="512"/>'
    else: clip = '<rect width="1024" height="1024"/>'
    return f'''<clipPath id="c">{clip}</clipPath>
  <g clip-path="url(#c)">
    <rect width="1024" height="1024" fill="url(#bg)"/>
    <rect width="1024" height="1024" fill="url(#glow)"/>
    <rect width="1024" height="1024" fill="url(#glow2)"/>
  </g>'''

def svg(kind):
    if kind == 'fg':      # 적응형 아이콘 전경: 안전영역(66%) 안에 들어가게 축소
        body = f'<g transform="translate(512 512) scale(.62) translate(-512 -540)">{watch()}</g>'
    elif kind == 'bgonly':
        body = bg('full')
    else:
        body = bg(kind) + f'<g transform="translate(512 512) scale(.92) translate(-512 -540)">{watch()}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">{DEFS}{body}</svg>'

def render(page, kind, size, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s = svg(kind).replace('width="1024" height="1024">', f'width="{size}" height="{size}">', 1)
    tmp = '/tmp/_icon.svg'
    open(tmp, 'w').write(s)
    page.set_viewport_size({'width': size, 'height': size})
    page.goto('file://' + tmp)
    page.screenshot(path=path, omit_background=True)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page()
    open(f'{OUT}/icon.svg', 'w').write(svg('square'))
    render(pg, 'square', 1024, f'{OUT}/build/icon.png')          # electron-builder (exe)
    render(pg, 'square', 512, f'{OUT}/icon-512.png')               # 웹/창 아이콘
    dens = {'mdpi':1, 'hdpi':1.5, 'xhdpi':2, 'xxhdpi':3, 'xxxhdpi':4}
    for d, s in dens.items():
        base = f'{OUT}/android-res/mipmap-{d}'
        render(pg, 'square', int(48*s), f'{base}/ic_launcher.png')
        render(pg, 'circle', int(48*s), f'{base}/ic_launcher_round.png')
        render(pg, 'fg', int(108*s), f'{base}/ic_launcher_foreground.png')
        render(pg, 'bgonly', int(108*s), f'{base}/ic_launcher_background.png')
    b.close()
