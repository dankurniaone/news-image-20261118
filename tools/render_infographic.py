#!/usr/bin/env python3
"""Render the v8 of the 18 Nov 2026 news image — supersampled text.

V8 fixes ONE thing only: Ruu's v7 critique "teks masih pecah" (the text
is still pixelated). Verified with 2x-zoomed crops of the v7 entry.png:
the 52px headline is passable, but the 19px deck and especially the
13px captions/footer are visibly stair-stepped and jagged at the pixel
level — Pillow rendering directly at 680x1024 does not anti-alias
small light-on-dark text well enough.

THE FIX — SUPERSAMPLING: the whole page is rendered at 2x resolution
(1360x2048) — every font size, every coordinate, every photo target
size, every rule and radius scaled by exactly SS=2 — then the finished
image is downscaled to 680x1024 with Image.LANCZOS before saving.
The downscale turns the 2x raster into smooth anti-aliased edges at
1x. If 2x is not visibly smooth enough on the small text, raise SS to
3 (2040x3072) and downscale the same way. SS is the single constant
at the top; nothing else about the render changes.

Also new in v8: fonts are loaded with layout_engine=RAQM (libraqm is
available in this environment — verified via PIL.features.check).
RAQM gives better glyph shaping/kerning; it is a bonus, not the fix
— supersampling is what smooths the edges.

EVERYTHING ELSE IS V7, UNCHANGED: same layout, same 4-size type
scale (nameplate 40, headline 52, secondary 25, body 19, small 13 —
all xSS in the supersampled render), same facts, same Omala hero,
same Kerch strip, same 680x1024 broadsheet output, deterministic.

V7 DIRECTION (unchanged, from reading the actual bounty RULES.txt):
entry.png is AT MOST 1024x1024 px and at most 1 MiB — NOT exactly
1024x1024. So entry.png itself IS the newspaper: a 680x1024
broadsheet (width:height ~0.66, real broadsheet proportions),
full-bleed. No square canvas, no dark backdrop, no small floating
page. Judge criteria (RULES.txt, in order): (1) one day's news,
names that day; (2) most consequential stories across regions/
fields; (3) it reads from the image alone; (4) faithful, no hype;
(5) ONE clear composition, legible at about 300 pixels across,
no smears/artefacts/garbled text. "Detail for its own sake does
not count" — so v7 CUT the clutter: fewer items, bigger type,
more air. References studied in v7 (Guardian 15 Jun 2023, WSJ
4 Jun 2026): 3-4 text sizes total, one dominant headline, body
leading 1.5-1.6x, ONE display face + ONE text face, thin rules
between sections, whitespace between blocks larger than within.

Facts (unchanged, verified 18 Nov): Gulf lead (Reuters 17 Nov
Qeshm strike + 18 Nov Bahrain/Kuwait intercepts; ~20% of world
oil through Hormuz); Kerch strip keeps its real SBU photo (CC BY
4.0); Fed Dec HIKE 96% (Fed held 3.75-4.00% on 28 Oct); Nvidia
Huang angle (resigned 12 Nov, board confirmed 17 Nov it will not
reinstate him, interim CEO Colette Kress); Ebola (WHO 17 Nov:
>11,000 cases, 5,400 deaths); measles in the ticker (US/Mexico/
Bolivia lost elimination status 17 Nov). The September "five
tankers sunk" story stays OUT entirely (8 September 2026, not
18 Nov news). No AP / Reuters / AFP / Getty photo anywhere.

Pure Pillow drawing from news.json and the committed photo assets.
No network, no clock, no randomness. Run from the repo root:
  python3 tools/render_infographic.py
Writes entry.png (the entry) in the repo root. main.ts only
copies entry.png, so the 680x1024 size flows through unchanged
(the grader checks magic bytes, IHDR dimensions and the 1 MiB cap).
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# --- Supersampling: render at SS x, downscale with LANCZOS. ---
SS = 2

BG = (13, 24, 40)          # deep navy (page IS the canvas now)
PANEL_LINE = (52, 84, 116)
WHITE = (244, 246, 248)
SOFT = (196, 208, 220)
MUTED = (140, 155, 172)
RED = (230, 57, 70)
AMBER = (245, 176, 65)
GOLD = (201, 162, 39)      # thin rule under the masthead only

# Final (output) geometry — 1x values, as in v7.
W, H = 680, 1024
MARGIN = 28
COL = W - 2 * MARGIN        # 624
HERO_H = 165

# Working (supersampled) geometry — every coordinate xSS.
W2, H2 = W * SS, H * SS
M2 = MARGIN * SS
COL2 = COL * SS
HERO_H2 = HERO_H * SS


def font(name, size):
    # size is the 1x (final) size; the render uses size*SS with RAQM.
    return ImageFont.truetype(
        os.path.join(FONT_DIR, name), size * SS,
        layout_engine=ImageFont.Layout.RAQM)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, max_w):
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


def para(draw, x, y, text, fnt, color, max_w, leading, max_lines=None):
    """Draw wrapped text; returns the y after the last line.

    leading is given in 1x (final) pixels and scaled by SS here,
    so every call site keeps the v7 numbers.
    """
    leading = leading * SS
    lines = wrap(draw, text, fnt, max_w)
    if max_lines is not None and len(lines) > max_lines:
        raise SystemExit(
            f"layout overflow: {text[:48]!r} wraps to {len(lines)} lines "
            f"(max {max_lines}) at {fnt.size // SS}px in {max_w // SS}px"
        )
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def photo(img, path, crop, size, radius=0, contrast=1.0, color=1.0,
          sharpness=1.0, brightness=1.0, warm=1.0):
    """Crop + resize a committed asset photo. Deterministic.

    crop is in SOURCE-image coordinates — never scaled. size is the
    target size in working (SSx) pixels; callers pass the scaled size.
    The grade (contrast/colour/sharpness/brightness + a subtle warm
    shift) is standard photo grading: it changes tone only — no
    content added or removed.
    """
    from PIL import ImageEnhance
    src = Image.open(os.path.join(HERE, path)).convert("RGB")
    src = src.crop(crop).resize(size, Image.LANCZOS)
    if contrast != 1.0:
        src = ImageEnhance.Contrast(src).enhance(contrast)
    if color != 1.0:
        src = ImageEnhance.Color(src).enhance(color)
    if sharpness != 1.0:
        src = ImageEnhance.Sharpness(src).enhance(sharpness)
    if brightness != 1.0:
        src = ImageEnhance.Brightness(src).enhance(brightness)
    if warm != 1.0:
        r, g, b = src.split()
        r = r.point(lambda v: min(255, int(v * warm)))
        b = b.point(lambda v: int(v * (2 - warm)))
        src = Image.merge("RGB", (r, g, b))
    if radius:
        mask = Image.new("L", size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, size[0], size[1]],
                                               radius=radius, fill=255)
        out = Image.new("RGB", size, BG)
        out.paste(src, (0, 0), mask)
        return out
    return src


def main():
    with open(os.path.join(HERE, "news.json"), encoding="utf-8") as fh:
        news = json.load(fh)
    img = Image.new("RGB", (W2, H2), BG)
    draw = ImageDraw.Draw(img)
    log = []

    # --- Masthead block: eyebrow, nameplate (serif, 40px — must fit
    # 624px; measured 579px at 40px), date, gold hairline. ---
    y = M2
    draw.text((M2, y), "WORLD NEWS  ·  ONE DAY, ONE IMAGE",
              font=SANS_B(13), fill=SOFT)
    y += (13 + 6) * SS
    draw.text((M2, y), "THE WORLD IN ONE DAY", font=SERIF_B(40),
              fill=WHITE)
    y += (40 + 4) * SS
    draw.text((M2, y), "WEDNESDAY, 18 NOVEMBER 2026",
              font=SANS_B(13), fill=SOFT)
    y += (13 + 8) * SS
    draw.line([(M2, y), (W2 - M2, y)], fill=GOLD, width=2 * SS)
    y += (2 + 14) * SS
    log.append(f"masthead ends {y // SS}")

    # --- Hero: the REAL photo — the oil tanker Omala at the Al
    # Basrah Oil Terminal, Persian Gulf (U.S. Navy photo, public
    # domain). Panoramic crop (0,360)-(2464,1052): keeps the full
    # hull, the terminal and the mooring ropes with a strip of sky.
    # Mild grade only (tone, no content change), rounded corners.
    # Captioned in news.json as a FILE PHOTO — it does not depict
    # the 17-18 Nov attacks. ---
    hero = photo(img, "assets/omala.jpg", (0, 390, 2464, 1042),
                 (COL2, HERO_H2), radius=10 * SS, contrast=1.15,
                 color=1.1, sharpness=1.15, brightness=1.02, warm=1.03)
    img.paste(hero, (M2, y))
    y += HERO_H2 + 6 * SS
    y = para(draw, M2, y, news["hero_caption"], SANS(13), MUTED,
             COL2, 17, max_lines=2)
    log.append(f"hero ends {y // SS}")

    # --- Lead: kicker (13px bold red) + 52px serif headline
    # (2 lines at this width — correct for a broadsheet) + 2-line
    # 19px deck, leading 29 (1.53x). ---
    y += 12 * SS
    draw.text((M2, y), news["lead"]["kicker"], font=SANS_B(13),
              fill=RED)
    y += (13 + 6) * SS
    y = para(draw, M2, y, news["lead"]["headline"], SERIF_B(52),
             WHITE, COL2, 56, max_lines=2)
    y += 8 * SS
    y = para(draw, M2, y, news["lead"]["deck"], SANS(19), SOFT,
             COL2, 29, max_lines=2)
    log.append(f"lead ends {y // SS}")

    # --- Thin rule, then Kerch strip: real SBU photo left, text
    # right. Photo 150x80; credit under it. Headline 25px serif
    # (1 line at 458px — measured 431px), deck 19px 2 lines. ---
    y += 12 * SS
    draw.line([(M2, y), (W2 - M2, y)], fill=PANEL_LINE, width=1 * SS)
    y += (1 + 12) * SS
    strip_y = y
    kerch = news["kerch"]
    thumb = photo(img, "assets/kerch-real.jpg", (100, 470, 1900, 1430),
                  (150 * SS, 80 * SS), radius=6 * SS, contrast=1.32,
                  color=1.22, sharpness=1.3, brightness=1.03, warm=1.05)
    img.paste(thumb, (M2, strip_y))
    draw.text((M2, strip_y + 80 * SS + 4 * SS), "PHOTO: SBU, CC BY 4.0",
              font=SANS(13), fill=MUTED)
    tx = M2 + 150 * SS + 16 * SS
    tw = COL2 - 150 * SS - 16 * SS
    ty = strip_y
    draw.text((tx, ty), kerch["kicker"], font=SANS_B(13), fill=AMBER)
    ty += (13 + 6) * SS
    ty = para(draw, tx, ty, kerch["headline"], SERIF_B(25), WHITE,
              tw, 29, max_lines=1)
    ty += 6 * SS
    para(draw, tx, ty, kerch["deck"], SANS(19), SOFT,
         tw, 29, max_lines=2)
    y = strip_y + 112 * SS
    log.append(f"kerch strip {strip_y // SS}..{y // SS}")

    # --- Thin rule, then Ebola + Nvidia side by side: TWO wide
    # columns (~300px each), not three cramped ones. Vertical
    # hairline between them. Headline 25px serif, deck 19px. ---
    y += 12 * SS
    draw.line([(M2, y), (W2 - M2, y)], fill=PANEL_LINE, width=1 * SS)
    y += (1 + 12) * SS
    gap = 24 * SS
    card_w = (COL2 - gap) // 2
    cards_y = y
    sx = M2 + card_w + gap // 2
    draw.line([(sx, cards_y), (sx, cards_y + 112 * SS)],
              fill=PANEL_LINE, width=1 * SS)
    for col, item in enumerate(news["stories"][:2]):
        x0 = M2 + col * (card_w + gap)
        cy = cards_y
        draw.text((x0, cy), item["kicker"], font=SANS_B(13), fill=AMBER)
        cy += (13 + 6) * SS
        cy = para(draw, x0, cy, item["headline"], SERIF_B(25), WHITE,
                  card_w, 29, max_lines=2)
        cy += 6 * SS
        para(draw, x0, cy, item["deck"], SANS(19), SOFT,
             card_w, 29, max_lines=2)
    y = cards_y + 112 * SS
    log.append(f"cards end {y // SS}")

    # --- Manila full-width row: kicker + 1-line headline + 1-line
    # deck, then a thin rule. ---
    y += 12 * SS
    item = news["stories"][2]
    draw.text((M2, y), item["kicker"], font=SANS_B(13), fill=AMBER)
    y += (13 + 6) * SS
    y = para(draw, M2, y, item["headline"], SERIF_B(25), WHITE,
             COL2, 29, max_lines=1)
    y += 6 * SS
    y = para(draw, M2, y, item["deck"], SANS(19), SOFT,
             COL2, 29, max_lines=1)
    y += 12 * SS
    draw.line([(M2, y), (W2 - M2, y)], fill=PANEL_LINE, width=1 * SS)
    y += (1 + 10) * SS
    log.append(f"manila ends {y // SS}")

    # --- Ticker: ONE line in a slim red strip (7 items, trimmed).
    # 13px bold, 1 line — no more 3-line pile-up. ---
    draw.rounded_rectangle([M2, y, W2 - M2, y + 34 * SS],
                           radius=8 * SS, fill=RED)
    para(draw, M2 + 16 * SS, y + 10 * SS, news["ticker"], SANS_B(13),
         WHITE, COL2 - 32 * SS, 19, max_lines=1)
    y += 34 * SS
    log.append(f"ticker ends {y // SS}")

    # --- Footer: sources + photo credits, ONE line, 13px, centred.
    # Ends well above the bottom edge (no frame line to cross — the
    # page IS the canvas — but the safe bottom margin is enforced
    # by the check below). ---
    y += 10 * SS
    draw.text((W2 / 2, y), news["footer"], font=SANS(13), fill=MUTED,
              anchor="ma")
    y += 13 * SS
    log.append(f"footer ends {y // SS}")
    if y > H2 - M2:
        raise SystemExit(f"layout overflow: page ends at y={y // SS} "
                         f"(limit {H - MARGIN})")

    # --- Supersample downscale: the 2x raster becomes the 680x1024
    # entry with smooth anti-aliased text edges. LANCZOS is
    # deterministic, so repeated renders are byte-identical. ---
    img = img.resize((W, H), Image.LANCZOS)

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")
    for line in log:
        print("  layout:", line)


if __name__ == "__main__":
    main()
