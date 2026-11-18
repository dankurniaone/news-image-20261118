#!/usr/bin/env python3
"""Render the 18 November 2026 news front page to entry.png.

Pure Pillow drawing from news.json: no network, no clock, no randomness,
so the same input always renders the same bytes. Run from the repo root:
    python3 tools/render.py
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

INK = (22, 21, 19)
PAPER = (248, 244, 232)
MUTED = (92, 86, 76)
RED = (163, 22, 33)
NAVY = (31, 58, 95)
SEA = (207, 221, 230)
LAND = (231, 220, 192)
RULE = (22, 21, 19)

W, H = 1024, 1024
MARGIN = 36
COL = W - 2 * MARGIN


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels, word by word."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    """Draw a wrapped paragraph, return the y just below it."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def centre(draw, y, text, fnt, color):
    draw.text((W / 2, y), text, font=fnt, fill=color, anchor="ma")
    return y + fnt.size


def rule(draw, y, weight=2, color=RULE, x0=MARGIN, x1=W - MARGIN):
    draw.line([(x0, y), (x1, y)], fill=color, width=weight)
    return y + weight


def masthead(draw, news):
    y = 24
    draw.text((MARGIN, y), news["masthead"], font=SERIF_B(88), fill=INK)
    tag = news["masthead_tag"]
    tw = draw.textlength(tag, font=SANS_B(28))
    draw.rectangle([W - MARGIN - tw - 26, y + 16, W - MARGIN, y + 16 + 44], fill=RED)
    draw.text((W - MARGIN - tw - 13, y + 24), tag, font=SANS_B(28), fill=PAPER)
    y = 128
    draw.text((MARGIN, y), "WEDNESDAY, 18 NOVEMBER 2026", font=SANS_B(20), fill=RED)
    draw.text((W - MARGIN, y), "ONE DAY  ·  ONE IMAGE", font=SANS_B(20), fill=INK, anchor="ra")
    y = rule(draw, 150, 3)
    centre(draw, y + 8, news["strapline"], SERIF(20), MUTED)
    return 184


def lead(draw, news):
    y = 198
    draw.text((MARGIN, y), news["lead"]["kicker"], font=SANS_B(18), fill=RED)
    y += 28
    y = para(draw, MARGIN, y, news["lead"]["headline"], SERIF_B(48), INK, COL, 56)
    y += 6
    y = para(draw, MARGIN, y, news["lead"]["deck"], SANS(20), INK, COL, 27)
    return y + 6


def gulf_map(draw, y0, news):
    """Schematic of the Gulf overnight: sea, two coasts, five tanker marks."""
    x0, x1 = MARGIN, W - MARGIN
    h = 118
    y1 = y0 + h
    draw.rectangle([x0, y0, x1, y1], fill=SEA, outline=INK, width=2)
    draw.polygon(
        [(x0, y0), (x1, y0), (x1, y0 + 30), (740, y0 + 44), (520, y0 + 26), (340, y0 + 48), (x0, y0 + 56)],
        fill=LAND,
    )
    draw.polygon(
        [(x0, y1), (x1, y1), (x1, y1 - 30), (760, y1 - 48), (560, y1 - 28), (360, y1 - 50), (x0, y1 - 34)],
        fill=LAND,
    )
    draw.text((x0 + 12, y0 + 6), "IRAN", font=SANS_B(15), fill=MUTED)
    draw.text((x0 + 12, y1 - 24), "ARABIAN PENINSULA", font=SANS_B(15), fill=MUTED)
    draw.text((x0 + 150, y0 + 62), "GULF OF OMAN", font=SANS_B(14), fill=NAVY)
    marks = [
        (420, "DERYA", "above"),
        (560, "KAVIZ", "below"),
        (690, "CHARMINAR", "above"),
        (800, "HORIZON 1", "below"),
        (905, "RIESCO", "above"),
    ]
    my = y0 + 66
    for mx, name, side in marks:
        draw.ellipse([mx - 6, my - 6, mx + 6, my + 6], fill=RED, outline=PAPER, width=2)
        if name == "RIESCO":
            draw.text((x1 - 10, my - 22), name, font=SANS_B(13), fill=INK, anchor="ra")
        elif side == "above":
            draw.text((mx + 10, my - 22), name, font=SANS_B(13), fill=INK)
        else:
            draw.text((mx + 10, my + 10), name, font=SANS_B(13), fill=INK)
    centre(draw, y1 + 5, news["lead"]["map_caption"], SANS_B(13), INK)
    return y1 + 24


def bridge_art(draw, x, y, w):
    """Kerch Strait: a broken road deck over the water, compact strip."""
    h = 30
    draw.rectangle([x, y, x + w, y + h], fill=(233, 228, 210), outline=INK, width=1)
    draw.rectangle([x, y + 22, x + w, y + h], fill=SEA)
    for wx in range(x + 8, x + w - 8, 24):
        draw.arc([wx, y + 23, wx + 16, y + 29], 0, 180, fill=NAVY, width=2)
    draw.rectangle([x, y + 12, x + 40, y + 22], fill=INK)
    draw.rectangle([x + w - 40, y + 12, x + w, y + 22], fill=INK)
    mid = x + w // 2
    draw.line([(x + 40, y + 12), (mid - 28, y + 12)], fill=INK, width=4)
    draw.line([(mid + 32, y + 12), (x + w - 40, y + 12)], fill=INK, width=4)
    draw.line([(mid - 28, y + 12), (mid + 2, y + 22)], fill=RED, width=4)
    draw.text((x + w - 6, y + 1), "ROAD SPAN DOWN", font=SANS_B(11), fill=RED, anchor="ra")
    return y + h


def story(draw, x, y, w, item, headline_size=26, deck_size=17):
    draw.text((x, y), item["kicker"], font=SANS_B(15), fill=RED)
    y += 22
    y = para(draw, x, y, item["headline"], SERIF_B(headline_size), INK, w, headline_size + 7)
    y += 4
    y = para(draw, x, y, item["deck"], SANS(deck_size), INK, w, deck_size + 7)
    return y


def main():
    with open(os.path.join(HERE, "news.json"), encoding="utf-8") as fh:
        news = json.load(fh)
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    y = masthead(draw, news)
    y = lead(draw, news)
    y = rule(draw, y + 6, 1, MUTED)
    y = gulf_map(draw, y + 6, news)
    y = rule(draw, y + 8, 1, MUTED)

    y += 8
    row1 = y
    col_w = (COL - 24) // 2
    x2 = MARGIN + col_w + 24
    by = bridge_art(draw, MARGIN, row1, col_w)
    end1 = story(draw, MARGIN, by + 8, col_w, news["stories"][0])
    end2 = story(draw, x2, row1, col_w, news["stories"][1])
    y = max(end1, end2)
    print("row1 ends at", y)
    y = rule(draw, y + 8, 1, MUTED)

    y += 8
    ends = []
    for i, item in enumerate(news["stories"][2:]):
        ends.append(story(draw, MARGIN if i == 0 else x2, y, col_w, item, headline_size=24, deck_size=17))
    y = max(ends)
    print("row2 ends at", y)
    y = rule(draw, y + 8, 2)

    y += 6
    draw.rectangle([MARGIN, y, W - MARGIN, y + 44], fill=NAVY)
    para(draw, MARGIN + 14, y + 4, news["ticker"], SANS_B(15), PAPER, COL - 28, 19)
    y = y + 44
    centre(draw, y + 6, news["footer"], SANS(13), MUTED)
    print("footer at", y + 8)

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
