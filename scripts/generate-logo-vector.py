#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fig Jam Theme — vector logo candidates (SVG rendered by headless Chromium).

Every mark carries a gradient fill, a soft drop shadow and highlights so it reads
as a designed icon rather than flat clip-art.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "01"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


WINE = hx(_C["frame"])                             # #7C0E44
TOOLBAR = hx(_C["toolbar"])                        # #8E1249
PEACH = hx(_C["ntp_background"])                   # #F2DACE
ROSE = hx(_C["ntp_header"])                        # #D49A9A
MAUVE = hx(_C["button_background_secondary"])      # #AA5E7A
LINK = hx(_C["ntp_link"])                          # #7C0E44
INK = hx(_C["ntp_text"])                           # #4A0A28

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".20"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def seeds(cx, cy, rx, ry, color, n=7, seed_r=3.2):
    """Ring of fig seeds around (cx, cy)."""
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        for k in (0.62, 0.34):
            x, y = cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)
            out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" fill-opacity=".55"/>'
                       % (x, y, seed_r, color))
    return "".join(out)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="fg1" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <radialGradient id="in1" cx="42%%" cy="38%%" r="70%%">
    <stop offset="0" stop-color="#E8A0A0"/>
    <stop offset="1" stop-color="%s"/>
  </radialGradient>
  %s
</defs>
<g filter="url(#ds)">
  <path d="M128 34 C176 60 204 108 200 156 C196 198 166 224 128 224 C90 224 60 198 56 156
           C52 108 80 60 128 34 Z" fill="url(#fg1)"/>
  <ellipse cx="128" cy="146" rx="62" ry="58" fill="url(#in1)"/>
  %s
</g>
<ellipse cx="96" cy="96" rx="14" ry="22" fill="#FFFFFF" opacity=".18" transform="rotate(-24 96 96)"/>
""" % (MAUVE, WINE, MAUVE, SHADOW, seeds(128, 146, 52, 48, INK)))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="gl2" x1="0" y1="0" x2="0.4" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="jm2" x1="0" y1="0" x2="0.5" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)">
  <path d="M76 96 h104 l-8 108 q-1 14 -16 14 h-56 q-15 0 -16 -14 z" fill="url(#gl2)"
        fill-opacity=".55" stroke="%s" stroke-opacity=".4" stroke-width="4"/>
  <path d="M82 122 h92 l-8 82 q-1 12 -14 12 h-48 q-13 0 -14 -12 z" fill="url(#jm2)"/>
  <rect x="68" y="60" width="120" height="34" rx="14" fill="%s"/>
  <rect x="68" y="60" width="120" height="14" rx="7" fill="#FFFFFF" fill-opacity=".18"/>
</g>
<path d="M96 138 q-2 30 0 56" stroke="#FFFFFF" stroke-opacity=".40" stroke-width="6"
      stroke-linecap="round" fill="none"/>
<circle cx="146" cy="176" r="5" fill="%s" fill-opacity=".45"/>
""" % (PEACH, ROSE, MAUVE, WINE, SHADOW, WINE, ROSE, INK))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="lf3" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)">
  <path d="M128 42 C160 58 176 84 172 108 C188 116 196 134 190 152 C182 174 158 184 138 176
           C132 196 112 208 92 202 C68 194 58 168 68 148 C50 140 44 118 54 102 C64 84 88 80 104 88
           C108 62 116 48 128 42 Z" fill="url(#lf3)"/>
  <path d="M128 60 V206" stroke="%s" stroke-opacity=".40" stroke-width="5" stroke-linecap="round"/>
  <g stroke="%s" stroke-opacity=".30" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M128 96 C112 92 100 80 96 68"/>
    <path d="M128 96 C144 92 156 80 160 68"/>
    <path d="M128 140 C108 136 92 124 86 110"/>
    <path d="M128 140 C148 136 164 124 170 110"/>
  </g>
</g>
""" % (ROSE, WINE, SHADOW, WINE, WINE))

SVG_04 = svg_open("""
<defs>
  <linearGradient id="jm4" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="sp4" x1="0" y1="0" x2="0.4" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)">
  <!-- handle: one continuous stroke from the bowl up to the right -->
  <path d="M104 176 C136 154 168 122 190 84" stroke="url(#sp4)" stroke-width="17"
        stroke-linecap="round" fill="none"/>
  <!-- bowl -->
  <ellipse cx="100" cy="180" rx="44" ry="30" fill="url(#sp4)" transform="rotate(-22 100 180)"/>
  <!-- jam sitting in the bowl -->
  <ellipse cx="98" cy="170" rx="33" ry="21" fill="url(#jm4)" transform="rotate(-22 98 170)"/>
  <!-- drips over the rim -->
  <path d="M74 186 q4 14 12 20 q6 4 8 -6 q2 -12 -4 -20 z" fill="url(#jm4)"/>
</g>
<ellipse cx="92" cy="160" rx="12" ry="7" fill="#FFFFFF" opacity=".38" transform="rotate(-22 92 160)"/>
""" % (MAUVE, WINE, ROSE, PEACH, SHADOW))

SVG_05 = svg_open("""
<defs>
  <linearGradient id="bd5" x1="0" y1="0" x2="0.8" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<circle cx="128" cy="128" r="102" fill="url(#bd5)" filter="url(#ds)"/>
<circle cx="128" cy="128" r="102" fill="none" stroke="%s" stroke-opacity=".22" stroke-width="4"/>
<g transform="translate(128 132) scale(0.70) translate(-128 -130)">
  <path d="M128 34 C176 60 204 108 200 156 C196 198 166 224 128 224 C90 224 60 198 56 156
           C52 108 80 60 128 34 Z" fill="%s"/>
  <ellipse cx="128" cy="146" rx="58" ry="54" fill="%s" fill-opacity=".55"/>
  %s
</g>
""" % (TOOLBAR, WINE, SHADOW, PEACH, PEACH, WINE, seeds(128, 146, 48, 44, PEACH, n=6, seed_r=3)))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="dp6" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 40 C170 84 198 122 198 154 C198 192 168 220 128 220 C88 220 58 192 58 154
         C58 122 86 84 128 40 Z" fill="url(#dp6)" filter="url(#ds)"/>
<ellipse cx="104" cy="146" rx="18" ry="26" fill="#FFFFFF" opacity=".22" transform="rotate(-18 104 146)"/>
<circle cx="146" cy="128" r="6" fill="%s" fill-opacity=".45"/>
<circle cx="158" cy="160" r="4.6" fill="%s" fill-opacity=".40"/>
<circle cx="132" cy="182" r="4" fill="%s" fill-opacity=".35"/>
""" % (MAUVE, ROSE, WINE, SHADOW, INK, INK, INK))

CANDIDATES = [
    ("01", "fig-cut", "Fig cut in half with seeds — most literal", SVG_01),
    ("02", "jam-jar", "Jam jar with a rose lid — most product-like", SVG_02),
    ("03", "fig-leaf", "Lobed fig leaf with veins — botanical", SVG_03),
    ("04", "jam-spoon", "Spoon with a dollop of jam — warm and homely", SVG_04),
    ("05", "fig-badge", "Pale fig in a wine badge — strongest at 32px", SVG_05),
    ("06", "jam-drop", "Jam drop with seeds — softest abstract mark", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (250, 238, 234))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(74, 10, 40))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (250, 238, 234), (74, 10, 40), (140, 108, 120),
                  CAND_DIR / "contact-light.png", "Fig Jam — vector logo candidates (light)")
    contact_sheet(rendered, (48, 8, 28), (242, 218, 206), (196, 152, 160),
                  CAND_DIR / "contact-dark.png", "Fig Jam — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
