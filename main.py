#!/usr/bin/env python3
"""Draw "The World in One Page" — a busy newspaper front page summing up
Monday 23 November 2026's world news, as a single 1024x1024 PNG.

Text and layout are drawn in code (Pillow); the six story illustrations
are original AI-generated artwork stored in assets/ (no photographs, no
network, no random numbers, no timestamps) — running this twice writes
byte-identical PNGs.

Usage:  python3 main.py
Writes: /output/entry.png (or $OUTPUT_PATH; falls back to ./output/entry.png)
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1024, 1024
PAPER = (247, 243, 234)   # newsprint
INK = (17, 17, 17)
NAVY = (15, 36, 64)
GOLD = (217, 164, 65)
RED = (185, 28, 28)
TEAL = (13, 116, 128)
MUTED = (96, 92, 84)
WHITE = (255, 255, 255)

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "DejaVuSans.ttf")
FONT_B = os.path.join(HERE, "fonts", "DejaVuSans-Bold.ttf")
ASSETS = os.path.join(HERE, "assets")


def f(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, font, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def tag(draw, x, y, label, bg, size=16):
    """Category chip; returns its width."""
    tf = f(FONT_B, size)
    tw = draw.textlength(label, font=tf)
    pad_x, pad_y = 10, 5
    draw.rounded_rectangle(
        [x, y, x + tw + pad_x * 2, y + tf.size + pad_y * 2],
        radius=4, fill=bg)
    draw.text((x + pad_x, y + pad_y), label, font=tf, fill=WHITE)
    return tw + pad_x * 2


def load_thumb(name, size):
    """Load an illustration from assets/ and center-crop it to size."""
    im = Image.open(os.path.join(ASSETS, name)).convert("RGB")
    return ImageOps.fit(im, size, Image.LANCZOS)


def frame(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)


# --- the stories (verified from multiple outlets, 23 Nov 2026) -----------

LEAD = {
    "tag": "CLIMATE", "color": RED, "thumb": "thumb-climate.jpg",
    "headline": "COP31 climate deal collapses as draft drops fossil fuels",
    "sub": "Antalya pact omits fossil-fuel phase-out",
    "deck": "EU and island states rejected the Antalya pact after fossil fuels "
            "were stripped from every draft, though 100+ nations backed keeping "
            "them. The longest COP ever ended with no deal — the first collapse "
            "since 2009.",
}

GRID = [
    {"tag": "MIDDLE EAST", "color": (146, 64, 14), "thumb": "thumb-gulf.jpg",
     "headline": "Iran strikes US bases in Bahrain",
     "sub": "Gulf war widens to Saudi Arabia",
     "deck": "Tehran claims it hit two US Patriot radars at Al-Riffa and Awali. "
            "Bahrain says two were hurt and a factory burned; the US reports no "
            "damage."},
    {"tag": "UKRAINE WAR", "color": (30, 64, 175), "thumb": "thumb-ship.jpg",
     "headline": "Russian cargo ship ablaze off Finland",
     "sub": "14 missing after drone strike",
     "deck": "Two drones hit the 121m Sparta II, bound for Kaliningrad; all 16 "
            "crew were evacuated, one hurt. Finnish, Estonian and Russian crews "
            "fought the fire together."},
    {"tag": "AMERICAS", "color": (153, 27, 27), "thumb": "thumb-mexico.jpg",
     "headline": "Mexico captures cartel boss \u2018El Chapo Isidro\u2019",
     "sub": "11 killed in the raid to capture him",
     "deck": "Four soldiers and seven gunmen died in Guasave as troops seized "
            "the FBI’s most-wanted fugitive with US help. Eight were arrested; "
            "he was flown to Mexico City."},
    {"tag": "ASIA", "color": (5, 122, 85), "thumb": "thumb-seoul.jpg",
     "headline": "Seoul minister quits in AI exam scandal",
     "sub": "Cheating rocks national exams",
     "deck": "Choi Kyo-jin quit after last-minute anti-cheating rules sowed chaos "
            "before the Suneung. A top scorer cheated with a mini camera and AI; "
            "111 cases were caught."},
]

STRIP = {
    "tag": "CYBER", "color": TEAL, "thumb": "thumb-cyber.jpg",
    "headline": "FBI crime database hacked, Trump confirms",
    "deck": "The NCIC holds warrants, fingerprints and missing-persons files; it is "
            "unclear what was taken. It is the FBI’s second breach in months — "
            "ShinyHunters hit its jobs site in September — and the USDA was hit the "
            "same day.",
}

BRIEFS = [
    ("LISBON", "Thousands march over living costs."),
    ("INDONESIA", "50 missing after factory fire."),
    ("DELHI", "Nepal PM meets Modi."),
    ("CRICKET", "India posts record 720/9d at Wellington."),
]

NUMBERS = ("11 killed in the Guasave raid \u00b7 16 crew evacuated from the Sparta II "
           "\u00b7 111 cheating cases at the Suneung \u00b7 194 delegations at COP31 "
           "\u00b7 50 missing in the Indonesia fire \u00b7 720/9d \u2014 India\u2019s "
           "record Test total")

SOURCES = ("Sources: CNN \u00b7 Reuters \u00b7 AP \u00b7 Le Monde \u00b7 WSJ \u00b7 Korea "
           "JoongAng Daily \u00b7 SecurityWeek \u00b7 IANS \u2014 23 Nov 2026")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 112], fill=NAVY)
    title = "THE WORLD IN ONE PAGE"
    tf = f(FONT_B, 48)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 14), title, font=tf, fill=WHITE)
    sub = "MONDAY, 23 NOVEMBER 2026   \u00b7   SIX STORIES THAT DEFINED THE DAY"
    sf = f(FONT, 18)
    sw = d.textlength(sub, font=sf)
    d.text(((W - sw) / 2, 78), sub, font=sf, fill=GOLD)
    d.rectangle([0, 112, W, 116], fill=GOLD)

    x0, x1 = 36, 988

    # ---- lead story (thumbnail right, headline + sub-headline + deck) ---
    y = 128
    tag(d, x0, y, LEAD["tag"], LEAD["color"], size=17)
    th = load_thumb(LEAD["thumb"], (180, 135))
    img.paste(th, (772, 146))
    frame(d, 772, 146, 180, 135)
    hf = f(FONT_B, 32)
    lines = wrap(d, LEAD["headline"], hf, 700)[:3]
    y = draw_lines(d, lines, x0, 164, hf, INK, 39)
    sf = f(FONT_B, 19)
    lines = wrap(d, LEAD["sub"], sf, 700)[:1]
    y = draw_lines(d, lines, x0, y + 6, sf, LEAD["color"], 24)
    df = f(FONT, 17)
    lines = wrap(d, LEAD["deck"], df, 700)[:3]
    y = draw_lines(d, lines, x0, y + 6, df, MUTED, 22)
    y = max(y, 146 + 135) + 12
    d.line([x0, y, x1, y], fill=INK, width=2)
    print("after lead:", y)

    # ---- 2x2 grid (thumbnail left, headline + sub + deck right) --------
    def grid_cell(s, x, y):
        tag(d, x, y, s["tag"], s["color"], size=15)
        th = load_thumb(s["thumb"], (140, 88))
        img.paste(th, (x, y + 32))
        frame(d, x, y + 32, 140, 88)
        tx = x + 152
        hf = f(FONT_B, 19)
        lines = wrap(d, s["headline"], hf, 318)[:2]
        yy = draw_lines(d, lines, tx, y + 32, hf, INK, 23)
        sf = f(FONT_B, 14)
        lines = wrap(d, s["sub"], sf, 318)[:1]
        yy = draw_lines(d, lines, tx, yy + 4, sf, s["color"], 18)
        df = f(FONT, 13)
        lines = wrap(d, s["deck"], df, 318)[:4]
        yy = draw_lines(d, lines, tx, yy + 4, df, MUTED, 15)
        return max(y + 32 + 88, yy)

    y += 12
    row1 = max(grid_cell(GRID[0], 36, y), grid_cell(GRID[1], 518, y))
    y = row1 + 8
    row2 = max(grid_cell(GRID[2], 36, y), grid_cell(GRID[3], 518, y))
    y = row2 + 8
    d.line([x0, y, x1, y], fill=INK, width=2)
    print("after grid:", y)

    # ---- strip story (tag + headline inline, thumbnail left) -----------
    y += 8
    tw = tag(d, x0, y, STRIP["tag"], STRIP["color"], size=15)
    hf = f(FONT_B, 24)
    d.text((x0 + tw + 12, y + 2), STRIP["headline"], font=hf, fill=INK)
    th = load_thumb(STRIP["thumb"], (100, 64))
    img.paste(th, (x0, y + 32))
    frame(d, x0, y + 32, 100, 64)
    df = f(FONT, 15)
    lines = wrap(d, STRIP["deck"], df, 800)[:3]
    yy = draw_lines(d, lines, x0 + 112, y + 34, df, MUTED, 20)
    y = max(y + 32 + 64, yy) + 8
    print("after strip:", y)

    # ---- briefs: four more one-line headlines --------------------------
    bf = f(FONT_B, 14)
    d.text((x0, y), "MORE FROM AROUND THE WORLD", font=bf, fill=INK)
    hw = d.textlength("MORE FROM AROUND THE WORLD", font=bf)
    d.line([x0 + hw + 10, y + 8, x1, y + 8], fill=MUTED, width=1)
    y += 20
    bf2 = f(FONT_B, 15)
    rf = f(FONT, 15)
    for i in range(0, 4, 2):
        for j, bx in enumerate((36, 518)):
            lead, rest = BRIEFS[i + j]
            lx = d.textlength(lead + " ", font=bf2)
            d.text((bx, y), lead + " ", font=bf2, fill=INK)
            d.text((bx + lx, y), rest, font=rf, fill=MUTED)
        y += 18
    print("after briefs:", y)

    # ---- by the numbers ------------------------------------------------
    y += 6
    d.rectangle([0, y, W, y + 64], fill=NAVY)
    tf = f(FONT_B, 16)
    d.text((36, y + 9), "BY THE NUMBERS", font=tf, fill=GOLD)
    tf2 = f(FONT, 14)
    lines = wrap(d, NUMBERS, tf2, 916)[:2]
    draw_lines(d, lines, 36, y + 30, tf2, WHITE, 18)
    y = y + 64
    print("after numbers:", y)

    # ---- footer --------------------------------------------------------
    y += 8
    ff = f(FONT, 13)
    lines = wrap(d, SOURCES, ff, 952)[:2]
    y = draw_lines(d, lines, 36, y, ff, MUTED, 16)
    d.text((36, y + 4), "Text and layout drawn in code \u00b7 Illustrations are original AI-generated artwork, no photographs \u00b7 Entry for make.fun news-image-20261123",
           font=ff, fill=MUTED)
    print("bottom:", y + 4 + 13)

    # ---- write out -----------------------------------------------------
    out = os.environ.get("OUTPUT_PATH", "/output/entry.png")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        img.save(out, format="PNG")
    except OSError:
        out = os.path.join(os.getcwd(), "output", "entry.png")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        img.save(out, format="PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
