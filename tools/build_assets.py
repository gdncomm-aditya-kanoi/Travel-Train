#!/usr/bin/env python3
"""Make the city banner (SVG) and the cheat-sheet PDF for a trip.

    python3 tools/build_assets.py hampi          # one trip
    python3 tools/build_assets.py                # every trip that has stops filled in

Reads _trips/<slug>.md and writes
    assets/images/<slug>/cover.svg
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
    W, H = 1260, 540
    name = t["title"].upper()
    lines = "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0, H, 7))

    def hill(pts, op):
        d = "M" + " L".join(f"{x},{y}" for x, y in pts) + f" L{W},{H} L0,{H} Z"
        return f'<path d="{d}" fill="url(#h)" opacity="{op}"/>'

    hills = (
        hill([(0, 400), (180, 330), (330, 380), (520, 300), (700, 370), (900, 310), (1080, 370), (1260, 320)], 0.35)
        + hill([(0, 450), (220, 395), (430, 440), (640, 385), (860, 445), (1060, 400), (1260, 440)], 0.6)
        + hill([(0, 500), (300, 470), (600, 505), (900, 468), (1260, 500)], 0.9)
    )
    sun = "".join(f'<line x1="{1010 - r}" y1="{y}" x2="{1010 + r}" y2="{y}"/>'
                  for y in range(95, 215, 6)
                  for r in [math.sqrt(max(0, 60 ** 2 - (y - 155) ** 2))])
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{t["title"]}, {t["state"]}">
<defs><pattern id="h" width="8" height="7" patternUnits="userSpaceOnUse"><rect width="8" height="3" y="2" fill="{INK}"/></pattern></defs>
<rect width="{W}" height="{H}" fill="{GROUND}"/>
<g stroke="{INK}" stroke-width="2.2" opacity=".9">{sun}</g>
{hills}
<text x="70" y="250" font-family="Newsreader, Georgia, 'Times New Roman', serif" font-size="150" letter-spacing="6" fill="{NAVY}">{name}</text>
<text x="76" y="305" font-family="'Instrument Sans', Helvetica, Arial, sans-serif" font-size="26" letter-spacing="6" fill="{INK}">{t["state"].upper()}  ·  TRAVEL TRAIN</text>
</svg>
'''
    out = os.path.join(ROOT, "assets", "images", slug)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "cover.svg"), "w", encoding="utf-8").write(svg)


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
    bh = 190
    c.setFillColor(HexColor(PAPER)); c.rect(0, H - bh, W, bh, stroke=0, fill=1)
    c.setStrokeColor(HexColor(INK)); c.setLineWidth(1)
    for layer, (base, amp, op) in enumerate([(H - bh + 44, 22, .35), (H - bh + 26, 18, .6), (H - bh + 8, 14, .9)]):
        c.saveState(); c.setStrokeAlpha(op)
        for yy in range(int(H - bh), int(base + amp), 4):
            for x in range(0, int(W), 6):
                prof = base + amp * math.sin((x + layer * 70) / 55.0 + layer) * 0.5 + amp * 0.5
                if yy < prof:
                    c.line(x, yy, x + 4, yy)
        c.restoreState()
    c.setFillColor(HexColor(NAVY)); c.setFont("Times-Roman", 52)
    c.drawString(M, H - 78, t["title"])
    c.setFont(sans, 10); c.setFillColor(HexColor(INK))
    c.drawString(M + 2, H - 100, f'{t["state"].upper()}  ·  {t["days_count"]} DAYS  ·  CHEAT SHEET')

    y = H - bh - 34
    c.setFillColor(HexColor(TEXT)); c.setFont(sans, 11)
    c.drawString(M, y, t["summary"])

    # stats
    total = sum(e["amount"] for e in t["expenses"])
    y -= 44
    stats = [("PER PERSON", rupee(total, rup)), ("DAYS", str(t["days_count"])), ("BEST SEASON", t["best_season"]), ("STAY", "Kadirampura")]
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
        c.setFillColor(HexColor(TEXT)); c.setFont(sans, 8.5); c.drawString(M + 120, y, e["note"][:62])
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

    y -= 40
    half = (W - 2 * M - 24) / 2
    y_end_l = block("Where to eat", t["eat"], M, y, half, "•")
    y_end_r = block("Skip these", t["things_to_skip"], M + half + 24, y, half, "×")
    y2 = min(y_end_l, y_end_r) - 28
    block("Good to know", [f'{d["label"]}: {d["value"]}' for d in t["details"]], M, y2, W - 2 * M, "•")
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
