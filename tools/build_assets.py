#!/usr/bin/env python3
"""Make the city banner (SVG) and the cheat-sheet PDF for a trip.

    python3 tools/build_assets.py hampi          # one trip
    python3 tools/build_assets.py                # every trip that has stops filled in

Reads _trips/<slug>.md and writes
    assets/images/<slug>/banner.svg
    assets/maps/<slug>-guide.pdf
Needs: pip install reportlab pyyaml
"""
import math
import os
import sys

import yaml
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUND, PAPER, INK, NAVY, TEXT, RULE = "#F2EAD8", "#F7F1E4", "#1D3A9C", "#14204F", "#4A5368", "#C9B98F"


def load(slug):
    raw = open(os.path.join(ROOT, "_trips", slug + ".md"), encoding="utf-8").read()
    _, fm, _ = raw.split("---", 2)
    return yaml.safe_load(fm)


# ───────────────────────── banner ─────────────────────────
def banner(slug, t):
    if t.get("art") == "coast":
        return banner_coast(slug, t)
    """Text-free line-art strip in the site's engraved style: boulders, a gopuram, the stone chariot, a coracle."""
    W, H, GY = 1260, 420, 352     # width, height, ground line
    out = []

    def hump(cx, w, h, base=GY, fill="url(#h1)"):
        out.append(f'<path d="M{cx - w / 2:.0f},{base} C{cx - w / 2:.0f},{base - h * 1.35:.0f} {cx + w / 2:.0f},{base - h * 1.35:.0f} {cx + w / 2:.0f},{base} Z" fill="{fill}" stroke="{GROUND}" stroke-width="3"/>')

    # sun
    sun = "".join(f'<line x1="{1075 - r:.0f}" y1="{y}" x2="{1075 + r:.0f}" y2="{y}"/>'
                  for y in range(48, 138, 6) for r in [math.sqrt(max(0, 45 ** 2 - (y - 93) ** 2))])
    out.append(f'<g stroke="{INK}" stroke-width="2.2">{sun}</g>')
    # far ridge
    out.append(f'<path d="M0,{GY} L0,300 L110,262 L230,296 L360,248 L500,294 L760,284 L900,240 L1040,290 L1160,262 L{W},290 L{W},{GY} Z" fill="url(#h0)" stroke="{GROUND}" stroke-width="3"/>')
    # boulder piles, back to front
    for cx, w, h in [(70, 150, 90), (200, 190, 110), (330, 150, 80), (150, 130, 70), (270, 120, 60)]:
        hump(cx, w, h, fill="url(#h1)" if h > 70 else "url(#h2)")
    for cx, w, h in [(1000, 170, 100), (1130, 200, 120), (1230, 130, 70), (1060, 120, 62), (1180, 110, 54)]:
        hump(cx, w, h, fill="url(#h1)" if h > 70 else "url(#h2)")
    # gopuram (Virupaksha style): stacked tiers
    cx = 600
    tiers = [(190, 40), (162, 36), (136, 34), (112, 32), (90, 30), (70, 28), (52, 26)]
    y = GY
    for i, (w, hh) in enumerate(tiers):
        y -= hh
        out.append(f'<rect x="{cx - w / 2:.0f}" y="{y}" width="{w}" height="{hh}" fill="url(#h{1 if i % 2 == 0 else 2})" stroke="{INK}" stroke-width="1.6"/>')
        out.append(f'<rect x="{cx - w / 2 - 4:.0f}" y="{y - 4}" width="{w + 8}" height="6" fill="{GROUND}" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<path d="M{cx - 20},{y - 4} A20,20 0 0 1 {cx + 20},{y - 4} Z" fill="url(#h1)" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<g stroke="{INK}" stroke-width="2"><line x1="{cx - 10}" y1="{y - 22}" x2="{cx - 10}" y2="{y - 34}"/><line x1="{cx}" y1="{y - 24}" x2="{cx}" y2="{y - 40}"/><line x1="{cx + 10}" y1="{y - 22}" x2="{cx + 10}" y2="{y - 34}"/></g>')
    out.append(f'<rect x="{cx - 24}" y="{GY - 64}" width="48" height="64" fill="{INK}"/>')                      # doorway
    out.append(f'<path d="M{cx - 24},{GY - 64} A24,24 0 0 1 {cx + 24},{GY - 64}" fill="{INK}"/>')
    # temple wall either side
    out.append(f'<rect x="{cx - 330}" y="{GY - 34}" width="{330 - 96}" height="34" fill="url(#h2)" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<rect x="{cx + 96}" y="{GY - 34}" width="{330 - 96}" height="34" fill="url(#h2)" stroke="{INK}" stroke-width="1.6"/>')
    # stone chariot (Vittala)
    sx = 860
    out.append(f'<rect x="{sx - 62}" y="{GY - 16}" width="124" height="16" fill="url(#h1)" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<rect x="{sx - 50}" y="{GY - 52}" width="100" height="36" fill="url(#h2)" stroke="{INK}" stroke-width="1.6"/>')
    for k, (w, hh) in enumerate([(78, 12), (60, 12), (44, 12), (28, 12)]):
        yy = GY - 52 - 12 * (k + 1)
        out.append(f'<rect x="{sx - w / 2:.0f}" y="{yy}" width="{w}" height="{hh}" fill="url(#h1)" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<line x1="{sx}" y1="{GY - 100}" x2="{sx}" y2="{GY - 112}" stroke="{INK}" stroke-width="2"/>')
    for wx in (sx - 34, sx + 34):
        out.append(f'<circle cx="{wx}" cy="{GY - 8}" r="15" fill="{GROUND}" stroke="{INK}" stroke-width="2"/><circle cx="{wx}" cy="{GY - 8}" r="4" fill="{INK}"/>'
                   + "".join(f'<line x1="{wx}" y1="{GY - 8}" x2="{wx + 15 * math.cos(a):.1f}" y2="{GY - 8 + 15 * math.sin(a):.1f}" stroke="{INK}" stroke-width="1.2"/>' for a in [i * math.pi / 4 for i in range(8)]))
    # river with waves and a coracle
    out.append(f'<rect x="0" y="{GY}" width="{W}" height="{H - GY}" fill="{GROUND}"/>')
    for i, yy in enumerate(range(GY + 12, H - 4, 11)):
        d = f"M0,{yy}"
        for x in range(0, W, 60):
            d += f" q15,{-5 if i % 2 else 5} 30,0 t30,0"
        out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8" opacity="{0.9 - i * 0.12:.2f}"/>')
    out.append(f'<path d="M430,{GY + 22} q60,40 120,0 Z" fill="url(#h1)" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<line x1="470" y1="{GY + 14}" x2="508" y2="{GY - 14}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Line drawing of Hampi: boulders, a gopuram, the stone chariot and a coracle on the river">
<defs>
<pattern id="h0" width="8" height="6" patternUnits="userSpaceOnUse"><rect width="8" height="1.3" y="2" fill="{INK}" opacity=".45"/></pattern>
<pattern id="h1" width="8" height="5" patternUnits="userSpaceOnUse"><rect width="8" height="2.2" y="1.4" fill="{INK}"/></pattern>
<pattern id="h2" width="8" height="5" patternUnits="userSpaceOnUse"><rect width="8" height="1.2" y="2" fill="{INK}" opacity=".7"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="{GROUND}"/>
{chr(10).join(out)}
</svg>
'''
    d = os.path.join(ROOT, "assets", "images", slug)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "banner.svg"), "w", encoding="utf-8").write(svg)


def banner_coast(slug, t):
    """Text-free line art for a coastal trip: Shiva statue, gopuram, palms, a headland and a sailing boat."""
    W, H, GY = 1260, 420, 330
    out = []
    ID = f'stroke="{INK}" stroke-width="1.6"'

    def hump(cx, w, h, base=GY, fill="url(#h1)"):
        out.append(f'<path d="M{cx - w / 2:.0f},{base} C{cx - w / 2:.0f},{base - h * 1.35:.0f} {cx + w / 2:.0f},{base - h * 1.35:.0f} {cx + w / 2:.0f},{base} Z" fill="{fill}" stroke="{GROUND}" stroke-width="3"/>')

    def palm(x, h, lean):
        tx, ty = x + lean, GY - h
        out.append(f'<path d="M{x},{GY} Q{x + lean * 0.2:.0f},{GY - h * 0.55:.0f} {tx},{ty}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
        for a in (-160, -125, -90, -55, -20, 15):
            r = math.radians(a)
            ex, ey = tx + 52 * math.cos(r), ty + 40 * math.sin(r) + 14
            out.append(f'<path d="M{tx},{ty} Q{(tx + ex) / 2:.0f},{ty + 4 * math.sin(r) - 22:.0f} {ex:.0f},{ey:.0f}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')

    # sun
    sun = "".join(f'<line x1="{1060 - r:.0f}" y1="{y}" x2="{1060 + r:.0f}" y2="{y}"/>'
                  for y in range(52, 140, 6) for r in [math.sqrt(max(0, 44 ** 2 - (y - 96) ** 2))])
    out.append(f'<g stroke="{INK}" stroke-width="2.2">{sun}</g>')
    # far headlands
    out.append(f'<path d="M0,{GY} L0,300 L120,270 L260,298 L420,262 L600,296 L820,280 L980,252 L1120,284 L{W},262 L{W},{GY} Z" fill="url(#h0)" stroke="{GROUND}" stroke-width="3"/>')
    # hill under the statue
    hump(250, 330, 90, fill="url(#h2)")
    hump(120, 200, 60, fill="url(#h1)")
    # Shiva statue (Murudeshwar): plinth, folded legs, torso, head, crown, raised hand
    sx, sy = 250, GY - 70
    out.append(f'<path d="M{sx - 70},{sy} L{sx + 70},{sy} L{sx + 56},{sy - 26} L{sx - 56},{sy - 26} Z" fill="url(#h1)" {ID}/>')
    out.append(f'<path d="M{sx - 52},{sy - 26} Q{sx},{sy - 58} {sx + 52},{sy - 26} Z" fill="url(#h2)" {ID}/>')                 # legs
    out.append(f'<path d="M{sx - 26},{sy - 44} L{sx - 20},{sy - 118} Q{sx},{sy - 128} {sx + 20},{sy - 118} L{sx + 26},{sy - 44} Z" fill="url(#h1)" {ID}/>')  # torso
    out.append(f'<path d="M{sx - 22},{sy - 100} Q{sx - 54},{sy - 84} {sx - 44},{sy - 54}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<path d="M{sx + 22},{sy - 100} Q{sx + 52},{sy - 118} {sx + 50},{sy - 150}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<circle cx="{sx}" cy="{sy - 136}" r="15" fill="{GROUND}" {ID}/>')
    out.append(f'<path d="M{sx - 14},{sy - 146} L{sx - 8},{sy - 170} L{sx},{sy - 154} L{sx + 8},{sy - 170} L{sx + 14},{sy - 146} Z" fill="{INK}"/>')
    # gopuram (Murudeshwar: tall, many tiers)
    cx = 560
    y = GY
    for i, (w, hh) in enumerate([(150, 30), (136, 28), (122, 27), (108, 26), (94, 25), (80, 24), (68, 23), (56, 22), (44, 21)]):
        y -= hh
        out.append(f'<rect x="{cx - w / 2:.0f}" y="{y}" width="{w}" height="{hh}" fill="url(#h{1 if i % 2 == 0 else 2})" {ID}/>')
        out.append(f'<rect x="{cx - w / 2 - 4:.0f}" y="{y - 4}" width="{w + 8}" height="5" fill="{GROUND}" {ID}/>')
    out.append(f'<path d="M{cx - 14},{y - 4} A14,14 0 0 1 {cx + 14},{y - 4} Z" fill="url(#h1)" {ID}/>')
    out.append(f'<line x1="{cx}" y1="{y - 16}" x2="{cx}" y2="{y - 36}" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<rect x="{cx - 20}" y="{GY - 56}" width="40" height="56" fill="{INK}"/><path d="M{cx - 20},{GY - 56} A20,20 0 0 1 {cx + 20},{GY - 56}" fill="{INK}"/>')
    # palms and rocks
    palm(760, 120, 26); palm(820, 150, -18); palm(1160, 130, 20); palm(1215, 100, -14)
    hump(960, 120, 44, fill="url(#h1)"); hump(1010, 80, 30, fill="url(#h2)")
    # sea: waves, and a sailing boat
    out.append(f'<rect x="0" y="{GY}" width="{W}" height="{H - GY}" fill="{GROUND}"/>')
    for i, yy in enumerate(range(GY + 12, H - 4, 11)):
        d = f"M0,{yy}"
        for x in range(0, W, 60):
            d += f" q15,{-5 if i % 2 else 5} 30,0 t30,0"
        out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8" opacity="{0.9 - i * 0.12:.2f}"/>')
    bx = 430
    out.append(f'<path d="M{bx - 40},{GY + 20} L{bx + 44},{GY + 20} L{bx + 32},{GY + 36} L{bx - 28},{GY + 36} Z" fill="url(#h1)" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<line x1="{bx}" y1="{GY + 20}" x2="{bx}" y2="{GY - 36}" stroke="{INK}" stroke-width="2.4"/>')
    out.append(f'<path d="M{bx + 4},{GY - 32} L{bx + 36},{GY + 14} L{bx + 4},{GY + 14} Z" fill="url(#h2)" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<path d="M{bx - 4},{GY - 24} L{bx - 26},{GY + 14} L{bx - 4},{GY + 14} Z" fill="url(#h1)" stroke="{INK}" stroke-width="1.6"/>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Line drawing of the Karnataka coast: a Shiva statue, a temple tower, palms and a sailing boat">
<defs>
<pattern id="h0" width="8" height="6" patternUnits="userSpaceOnUse"><rect width="8" height="1.3" y="2" fill="{INK}" opacity=".45"/></pattern>
<pattern id="h1" width="8" height="5" patternUnits="userSpaceOnUse"><rect width="8" height="2.2" y="1.4" fill="{INK}"/></pattern>
<pattern id="h2" width="8" height="5" patternUnits="userSpaceOnUse"><rect width="8" height="1.2" y="2" fill="{INK}" opacity=".7"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="{GROUND}"/>
{chr(10).join(out)}
</svg>
"""
    d = os.path.join(ROOT, "assets", "images", slug)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "banner.svg"), "w", encoding="utf-8").write(svg)



# ───────────────────────── pdf ─────────────────────────
def pick_fonts():
    """A serif and sans that have the ₹ sign; fall back to 'Rs'."""
    for reg, bold in [("/System/Library/Fonts/Supplemental/Georgia.ttf", "/System/Library/Fonts/Supplemental/Georgia Bold.ttf")]:
        pass
    sans_candidates = ["/System/Library/Fonts/Supplemental/Arial Unicode.ttf", "/Library/Fonts/Arial Unicode.ttf",
                       "/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for f in sans_candidates:
        if os.path.exists(f):
            try:
                pdfmetrics.registerFont(TTFont("TT-Sans", f))
                if 0x20B9 in pdfmetrics.getFont("TT-Sans").face.charToGlyph:
                    return "TT-Sans", True
            except Exception:
                continue
    return "Helvetica", False


def rupee(n, ok):
    return "Rs " + f"{int(n):,}"


def fit(text, width, font, size):
    if pdfmetrics.stringWidth(text, font, size) <= width:
        return text
    while text and pdfmetrics.stringWidth(text + "…", font, size) > width:
        text = text[:-1]
    return text.rstrip(" ,.:;") + "…"


def project(stops, x, y, w, h, pad=34):
    lat0 = sum(s["lat"] for s in stops) / len(stops)
    kx, ky = math.cos(math.radians(lat0)) * 111.32, 110.57
    lngs, lats = [s["lng"] for s in stops], [s["lat"] for s in stops]
    sx = max((max(lngs) - min(lngs)) * kx, 3)
    sy = max((max(lats) - min(lats)) * ky, 3)
    sc = min((w - 2 * pad) / sx, (h - 2 * pad) / sy)
    ox, oy = x + (w - sx * sc) / 2, y + (h - sy * sc) / 2
    pts = [(ox + (s["lng"] - min(lngs)) * kx * sc, oy + (s["lat"] - min(lats)) * ky * sc) for s in stops]
    return relax(pts, 17), sc


def relax(pts, gap):
    """Push markers apart when stops are too close to tell apart (exact repeats are left alone)."""
    out = []
    for i, (x, y) in enumerate(pts):
        for _ in range(6):
            moved = False
            for qx, qy in out:
                d = math.hypot(x - qx, y - qy)
                if 4 <= d < gap:
                    x, y = qx + (x - qx) / d * gap, qy + (y - qy) / d * gap; moved = True
            if not moved:
                break
        out.append((x, y))
    return out


def pdf(slug, t):
    sans, rup = pick_fonts()
    t = yaml.safe_load(yaml.safe_dump(t, allow_unicode=True).replace("₹", "Rs ").replace("Rs  ", "Rs "))  # built-in fonts have no ₹ sign
    W, H = A4
    c = canvas.Canvas(os.path.join(ROOT, "assets", "maps", f"{slug}-guide.pdf"), pagesize=A4)
    c.setTitle(f'{t["title"]} cheat sheet — Travel Train')
    c.setAuthor("Aditya Kanoi")
    M = 42

    def page_bg():
        c.setFillColor(HexColor(GROUND)); c.rect(0, 0, W, H, stroke=0, fill=1)

    def footer(n):
        c.setFont(sans, 8); c.setFillColor(HexColor(TEXT))
        c.drawString(M, 24, "Travel Train · by Aditya Kanoi")
        c.drawRightString(W - M, 24, f"{n} / 2")

    # ── page 1 ──
    page_bg()
    # banner: engraved hills
    bh = 165
    c.setFillColor(HexColor(PAPER)); c.rect(0, H - bh, W, bh, stroke=0, fill=1)
    c.setStrokeColor(HexColor(INK)); c.setLineWidth(1)
    for layer, (base, amp, op) in enumerate([(H - bh + 36, 18, .35), (H - bh + 22, 15, .6), (H - bh + 8, 12, .9)]):
        c.saveState(); c.setStrokeAlpha(op)
        for yy in range(int(H - bh), int(base + amp), 4):
            for x in range(0, int(W), 6):
                prof = base + amp * math.sin((x + layer * 70) / 55.0 + layer) * 0.5 + amp * 0.5
                if yy < prof:
                    c.line(x, yy, x + 4, yy)
        c.restoreState()
    tsize = 52
    while pdfmetrics.stringWidth(t["title"], "Times-Roman", tsize) > W - 2 * M and tsize > 24:
        tsize -= 2
    c.setFillColor(HexColor(NAVY)); c.setFont("Times-Roman", tsize)
    c.drawString(M, H - 78, t["title"])
    c.setFont(sans, 10); c.setFillColor(HexColor(INK))
    c.drawString(M + 2, H - 100, f'{t["state"].upper()}  ·  {t["days_count"]} DAYS  ·  CHEAT SHEET')

    y = H - bh - 34
    c.setFillColor(HexColor(TEXT)); c.setFont(sans, 11)
    c.drawString(M, y, t["summary"])

    # stats
    total = sum(e["amount"] for e in t["expenses"])
    y -= 44
    stats = [("PER PERSON", rupee(total, rup)), ("DAYS", str(t["days_count"])), ("BEST SEASON", t["best_season"]), ("STAY", t.get("stay_short", ""))]
    colw = (W - 2 * M) / len(stats)
    c.setStrokeColor(HexColor(RULE)); c.line(M, y + 28, W - M, y + 28); c.line(M, y - 14, W - M, y - 14)
    for i, (k, v) in enumerate(stats):
        c.setFont(sans, 7.5); c.setFillColor(HexColor(TEXT)); c.drawString(M + i * colw, y + 16, k)
        c.setFont("Times-Roman", 15); c.setFillColor(HexColor(NAVY)); c.drawString(M + i * colw, y - 4, v)

    # costs
    y -= 52
    c.setFont("Times-Roman", 18); c.setFillColor(HexColor(NAVY)); c.drawString(M, y, "What it cost, per person")
    y -= 10
    for e in t["expenses"]:
        y -= 20
        c.setFont(sans, 10); c.setFillColor(HexColor(NAVY)); c.drawString(M, y, e["category"])
        c.setFillColor(HexColor(TEXT)); c.setFont(sans, 8.5); c.drawString(M + 120, y, fit(e["note"], W - 2 * M - 120 - 70, sans, 8.5))
        c.setFont(sans, 10); c.setFillColor(HexColor(NAVY)); c.drawRightString(W - M, y, rupee(e["amount"], rup))
        c.setStrokeColor(HexColor("#D9CCB0")); c.line(M, y - 6, W - M, y - 6)
    y -= 24
    c.setFont("Times-Roman", 14); c.setFillColor(HexColor(INK)); c.drawString(M, y, "Total")
    c.drawRightString(W - M, y, rupee(total, rup))

    # eat / do / skip in two columns
    def block(title, items, x, y0, width, bullet):
        c.setFont("Times-Roman", 16); c.setFillColor(HexColor(NAVY)); c.drawString(x, y0, title)
        yy = y0 - 8
        for it in items:
            txt = it if isinstance(it, str) else f'{it["name"]} — {it["note"]}'
            for ln, line in enumerate(wrap(txt, width - 14, sans, 9)):
                yy -= 13
                if ln == 0:
                    c.setFillColor(HexColor(INK)); c.setFont(sans, 9); c.drawString(x, yy, bullet)
                c.setFillColor(HexColor(TEXT)); c.setFont(sans, 9); c.drawString(x + 12, yy, line)
            yy -= 3
        return yy

    def wrap(text, width, font, size):
        words, line, out = text.split(), "", []
        for wd in words:
            trial = (line + " " + wd).strip()
            if pdfmetrics.stringWidth(trial, font, size) <= width:
                line = trial
            else:
                out.append(line); line = wd
        out.append(line)
        return out

    y -= 30
    half = (W - 2 * M - 24) / 2
    y_end_l = block("Where to eat", t["eat"], M, y, half, "•")
    y_end_r = block("Skip these", t["things_to_skip"], M + half + 24, y, half, "×")
    y2 = min(y_end_l, y_end_r) - 20
    facts = [f'{d["label"]}: {d["value"]}' for d in t["details"]]
    mid = (len(facts) + 1) // 2
    c.setFont("Times-Roman", 16); c.setFillColor(HexColor(NAVY)); c.drawString(M, y2, "Good to know")
    block("", facts[:mid], M, y2 - 6, half, "•")
    block("", facts[mid:], M + half + 24, y2 - 6, half, "•")
    footer(1); c.showPage()

    # ── page 2: the day maps ──
    page_bg()
    c.setFont("Times-Roman", 26); c.setFillColor(HexColor(NAVY)); c.drawString(M, H - 60, "The route, day by day")
    top = H - 90
    ph = (top - 60) / len(t["days"])
    for i, d in enumerate(t["days"]):
        y0 = top - i * ph
        mx, mw, mh = M, 320, ph - 18
        c.setFillColor(HexColor(PAPER)); c.setStrokeColor(HexColor("#D9CCB0"))
        c.roundRect(mx, y0 - mh, mw, mh, 6, stroke=1, fill=1)
        stops = d["stops"]
        c.setFillColor(HexColor(INK)); c.saveState(); c.setFillAlpha(.25)
        for gx in range(int(mx) + 10, int(mx + mw) - 6, 14):
            for gy in range(int(y0 - mh) + 10, int(y0) - 6, 11):
                c.circle(gx + (gy % 2) * 5, gy, .6, stroke=0, fill=1)
        c.restoreState()
        pts, sc = project(stops, mx, y0 - mh, mw, mh)
        for a, b, s in zip(pts, pts[1:], stops[1:]):
            c.setStrokeColor(HexColor(INK)); c.setLineWidth(1.6)
            c.setDash(1, 4) if s.get("return") else c.setDash(6, 4)
            c.line(a[0], a[1], b[0], b[1])
        c.setDash()
        for n, ((px, py), s) in enumerate(zip(pts, stops), 1):
            if any(math.hypot(px - qx, py - qy) < 4 for qx, qy in pts[: n - 1]):
                c.setStrokeColor(HexColor(INK)); c.setLineWidth(1.4); c.circle(px, py, 10, stroke=1, fill=0); continue
            hollow = s.get("return")
            c.setFillColor(HexColor(PAPER) if hollow else HexColor(INK)); c.setStrokeColor(HexColor(INK)); c.setLineWidth(1.6)
            c.circle(px, py, 7, stroke=1, fill=1)
            c.setFillColor(HexColor(INK) if hollow else HexColor(PAPER)); c.setFont(sans, 7.5)
            c.drawCentredString(px, py - 2.6, str(n))
        # scale bar and north arrow
        nice = [1, 2, 5, 10, 20, 50]
        km = max([k for k in nice if k * sc <= 80] or [1])
        bx, by = mx + mw - 18 - km * sc, y0 - mh + 18
        c.setStrokeColor(HexColor(INK)); c.setLineWidth(1.4); c.setDash()
        c.line(bx, by, bx + km * sc, by); c.line(bx, by - 3, bx, by + 3); c.line(bx + km * sc, by - 3, bx + km * sc, by + 3)
        c.setFont(sans, 7.5); c.setFillColor(HexColor(INK)); c.drawCentredString(bx + km * sc / 2, by + 6, f"{km} km")
        c.drawCentredString(mx + mw - 20, y0 - 22, "N"); c.line(mx + mw - 20, y0 - 30, mx + mw - 20, y0 - 44)
        # list
        lx = mx + mw + 22
        c.setFont("Times-Roman", 18); c.setFillColor(HexColor(NAVY)); c.drawString(lx, y0 - 20, f"Day {i + 1}")
        c.setFont(sans, 9); c.setFillColor(HexColor(TEXT)); c.drawString(lx, y0 - 35, d["title"])
        yy = y0 - 55
        for n, s in enumerate(stops, 1):
            c.setFillColor(HexColor(INK)); c.setFont(sans, 9); c.drawString(lx, yy, f"{n}.")
            c.setFillColor(HexColor(NAVY)); c.drawString(lx + 16, yy, s["name"])
            if s.get("note"):
                yy -= 11; c.setFillColor(HexColor(TEXT)); c.setFont(sans, 8); c.drawString(lx + 16, yy, s["note"][:46])
            yy -= 15
        c.setFont(sans, 8); c.setFillColor(HexColor(INK))
        c.linkURL(d["route"], (lx, y0 - mh, W - M, y0 - mh + 16), relative=0)
        c.drawString(lx, y0 - mh + 4, "Open this day in Google Maps  →")
    c.setFont(sans, 8); c.setFillColor(HexColor(TEXT))
    c.drawString(M, 44, "Dashed line = route · dotted line = way back · ring = where you started")
    footer(2)
    c.save()


def main():
    slugs = sys.argv[1:] or [f[:-3] for f in sorted(os.listdir(os.path.join(ROOT, "_trips"))) if f.endswith(".md")]
    os.makedirs(os.path.join(ROOT, "assets", "maps"), exist_ok=True)
    for slug in slugs:
        t = load(slug)
        if not t.get("days") or not any(d.get("stops") for d in t["days"]) or not any(e["amount"] for e in t["expenses"]):
            print(f"skip {slug}: no stops or costs yet"); continue
        banner(slug, t); pdf(slug, t)
        print(f"made assets for {slug}")


if __name__ == "__main__":
    main()
