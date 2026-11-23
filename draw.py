#!/usr/bin/env python3
"""Draw the front page for Sunday 22 November 2026 as entry.png.

A 1024x1024 newspaper front page, drawn entirely in code with Pillow:
no external images, no network, no randomness, no clock. Running this
script twice writes byte-identical files.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (246, 241, 231)
INK = (27, 42, 74)
RED = (179, 38, 30)
SKY = (14, 27, 48)
SKY2 = (24, 46, 78)
MERCURY = (201, 122, 59)
MERCURY_DARK = (150, 84, 36)
MERCURY_LIGHT = (226, 158, 96)
GOLD = (212, 164, 74)
WHITE = (250, 248, 243)
GREY = (90, 92, 96)
RULE = (180, 172, 152)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except (OSError, IOError):
        return ImageFont.load_default()


SERIF_B = load_font("DejaVuSerif-Bold.ttf", 66)
SERIF_B_SMALL = load_font("DejaVuSerif-Bold.ttf", 30)
SANS_B = load_font("DejaVuSans-Bold.ttf", 20)
SANS_B_SM = load_font("DejaVuSans-Bold.ttf", 14)
SANS = load_font("DejaVuSans.ttf", 15)
SANS14 = load_font("DejaVuSans.ttf", 14)
SANS_SM = load_font("DejaVuSans.ttf", 13)
SANS_XS = load_font("DejaVuSans.ttf", 12)


def wrap(draw, text, font, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centred(draw, y, text, font, fill, cx=W // 2):
    draw.text((cx, y), text, font=font, fill=fill, anchor="ma")


def draw_masthead(draw):
    draw.text((28, 26), "THE WORLD TODAY", font=SERIF_B, fill=INK)
    draw.line([(28, 108), (996, 108)], fill=RED, width=4)
    draw.line([(28, 116), (996, 116)], fill=INK, width=2)
    draw.text((28, 126), "No. 326", font=SANS_SM, fill=GREY)
    centred(draw, 126, "SUNDAY 22 NOVEMBER 2026", SANS_B_SM, INK)
    right = "ONE DAY \u00b7 ONE PAGE"
    draw.text((996, 126), right, font=SANS_SM, fill=GREY, anchor="ra")


def draw_hero(draw):
    x0, y0, x1, y1 = 28, 166, 996, 392
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=SKY)
    # stars: fixed positions from modular arithmetic, no randomness
    for i in range(46):
        sx = x0 + 14 + (i * 173) % 940
        sy = y0 + 12 + (i * 97) % 150
        r = 1 if i % 3 else 2
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(200, 210, 235))
    # small sun, top left
    draw.ellipse([62, 186, 104, 228], fill=(244, 196, 90))
    for k in range(8):
        import math
        ang = math.pi * k / 4
        x2 = 83 + int(34 * math.cos(ang))
        y2 = 207 + int(34 * math.sin(ang))
        x3 = 83 + int(26 * math.cos(ang))
        y3 = 207 + int(26 * math.sin(ang))
        draw.line([(x3, y3), (x2, y2)], fill=(244, 196, 90), width=3)
    # orbit ellipse around Mercury
    draw.ellipse([640, 176, 990, 330], outline=(120, 140, 175), width=2)
    # Mercury: cratered disc, right side
    cx, cy, r = 815, 268, 62
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=MERCURY)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=MERCURY_DARK, width=2)
    for (ox, oy, cr) in [(-28, -18, 12), (18, -30, 9), (30, 12, 14),
                         (-8, 22, 10), (2, -6, 7), (-38, 14, 6), (40, -8, 6)]:
        draw.ellipse([cx + ox - cr, cy + oy - cr, cx + ox + cr, cy + oy + cr],
                     fill=MERCURY_DARK)
    draw.ellipse([cx - r + 8, cy - r + 6, cx - r + 44, cy - r + 34],
                 fill=MERCURY_LIGHT)
    # BepiColombo on its orbit: bus, panels, dish
    bx, by = 700, 196
    draw.polygon([(bx, by - 4), (bx + 26, by - 4), (bx + 26, by + 8),
                  (bx, by + 8)], fill=(226, 226, 220))
    draw.polygon([(bx + 26, by - 4), (bx + 34, by), (bx + 26, by + 8)],
                 fill=GOLD)
    draw.rectangle([bx - 34, by - 2, bx - 2, by + 6], fill=(58, 96, 150))
    draw.rectangle([bx + 36, by - 2, bx + 68, by + 6], fill=(58, 96, 150))
    draw.line([(bx - 34, by + 2), (bx - 2, by + 2)], fill=(200, 220, 240), width=1)
    draw.line([(bx + 36, by + 2), (bx + 68, by + 2)], fill=(200, 220, 240), width=1)
    draw.line([(bx + 13, by + 8), (bx + 13, by + 16)], fill=(200, 200, 190), width=2)
    draw.ellipse([bx + 8, by + 15, bx + 18, by + 23], outline=(200, 200, 190), width=2)
    # headline over the sky, left
    draw.text((128, 190), "AFTER EIGHT YEARS,", font=SERIF_B_SMALL, fill=WHITE)
    draw.text((128, 226), "A NEW WORLD", font=SERIF_B_SMALL, fill=WHITE)
    draw.text((128, 268), "BepiColombo slips into orbit around Mercury.",
              font=SANS, fill=(205, 214, 230))
    draw.text((128, 290), "A thruster glitch on arrival \u2014 but the",
              font=SANS, fill=(205, 214, 230))
    draw.text((128, 312), "spacecraft is safe, ESA says.",
              font=SANS, fill=(205, 214, 230))
    # caption strip at the foot of the panel
    draw.rectangle([x0, 352, x1, y1], fill=(10, 20, 38))
    draw.text((48, 362), "SPACE \u00b7 ESA\u2013JAXA probe reaches the solar system\u2019s smallest planet",
              font=SANS_B_SM, fill=(244, 196, 90))


def icon_crack(draw, x, y, s, colour):
    """Cracked earth: a disc split by jagged lines."""
    draw.ellipse([x, y, x + s, y + s], outline=colour, width=3)
    draw.line([(x + s * 0.5, y + 3), (x + s * 0.42, y + s * 0.4),
               (x + s * 0.58, y + s * 0.6), (x + s * 0.5, y + s - 3)],
              fill=colour, width=3)
    draw.line([(x + s * 0.42, y + s * 0.4), (x + s * 0.2, y + s * 0.55)],
              fill=colour, width=2)
    draw.line([(x + s * 0.58, y + s * 0.6), (x + s * 0.8, y + s * 0.72)],
              fill=colour, width=2)


def icon_rocket(draw, x, y, s, colour):
    """A rocket climbing, with flame."""
    draw.polygon([(x + s * 0.5, y + 2), (x + s * 0.72, y + s * 0.5),
                  (x + s * 0.5, y + s * 0.42), (x + s * 0.28, y + s * 0.5)],
                 fill=colour)
    draw.polygon([(x + s * 0.5, y + s * 0.42), (x + s * 0.62, y + s * 0.62),
                  (x + s * 0.5, y + s * 0.8), (x + s * 0.38, y + s * 0.62)],
                 fill=(244, 196, 90))
    draw.line([(x + s * 0.28, y + s * 0.5), (x + s * 0.14, y + s * 0.62)],
              fill=colour, width=3)
    draw.line([(x + s * 0.72, y + s * 0.5), (x + s * 0.86, y + s * 0.62)],
              fill=colour, width=3)


def icon_flats(draw, x, y, s, colour):
    """An apartment block with a broken corner and smoke."""
    draw.rectangle([x + s * 0.14, y + s * 0.16, x + s * 0.86, y + s * 0.92],
                   outline=colour, width=3)
    for row in range(3):
        for col in range(3):
            wx = x + s * (0.24 + col * 0.24)
            wy = y + s * (0.26 + row * 0.24)
            draw.rectangle([wx, wy, wx + s * 0.12, wy + s * 0.12],
                           fill=colour)
    draw.polygon([(x + s * 0.62, y + s * 0.16), (x + s * 0.86, y + s * 0.16),
                  (x + s * 0.86, y + s * 0.4), (x + s * 0.7, y + s * 0.3)],
                 fill=PAPER)
    draw.line([(x + s * 0.7, y + s * 0.1), (x + s * 0.78, y - 2),
               (x + s * 0.86, y + s * 0.08)], fill=GREY, width=2)


def icon_ship(draw, x, y, s, colour):
    """A warship on waves, with a drone dot above."""
    draw.polygon([(x + s * 0.12, y + s * 0.5), (x + s * 0.88, y + s * 0.5),
                  (x + s * 0.76, y + s * 0.72), (x + s * 0.24, y + s * 0.72)],
                 fill=colour)
    draw.rectangle([x + s * 0.38, y + s * 0.3, x + s * 0.58, y + s * 0.5],
                   fill=colour)
    draw.line([(x + s * 0.48, y + s * 0.3), (x + s * 0.48, y + s * 0.14)],
              fill=colour, width=2)
    draw.arc([x + s * 0.08, y + s * 0.74, x + s * 0.42, y + s * 0.94],
             0, 180, fill=colour, width=2)
    draw.arc([x + s * 0.55, y + s * 0.74, x + s * 0.9, y + s * 0.94],
             0, 180, fill=colour, width=2)
    draw.ellipse([x + s * 0.74, y + s * 0.08, x + s * 0.82, y + s * 0.16],
                 fill=RED)


def icon_orbit(draw, x, y, s, colour):
    """A ringed planet on its orbit."""
    draw.ellipse([x + s * 0.12, y + s * 0.12, x + s * 0.88, y + s * 0.88],
                 outline=colour, width=2)
    draw.ellipse([x + s * 0.32, y + s * 0.32, x + s * 0.68, y + s * 0.68],
                 fill=colour)
    draw.ellipse([x + s * 0.4, y + s * 0.38, x + s * 0.52, y + s * 0.5],
                 fill=PAPER)
    draw.ellipse([x + s * 0.7, y + s * 0.14, x + s * 0.78, y + s * 0.22],
                 fill=GOLD)


def icon_flame(draw, x, y, s, colour):
    """Flame over a factory roofline."""
    draw.polygon([(x + s * 0.14, y + s * 0.92), (x + s * 0.14, y + s * 0.6),
                  (x + s * 0.3, y + s * 0.6), (x + s * 0.3, y + s * 0.48),
                  (x + s * 0.46, y + s * 0.48), (x + s * 0.46, y + s * 0.6),
                  (x + s * 0.86, y + s * 0.6), (x + s * 0.86, y + s * 0.92)],
                 outline=colour, width=3)
    draw.polygon([(x + s * 0.5, y + s * 0.06), (x + s * 0.68, y + s * 0.34),
                  (x + s * 0.62, y + s * 0.5), (x + s * 0.38, y + s * 0.5),
                  (x + s * 0.32, y + s * 0.34)], fill=(244, 140, 40))
    draw.polygon([(x + s * 0.5, y + s * 0.22), (x + s * 0.6, y + s * 0.4),
                  (x + s * 0.4, y + s * 0.4)], fill=(244, 196, 90))


ICONS = {
    "crack": icon_crack,
    "rocket": icon_rocket,
    "flats": icon_flats,
    "ship": icon_ship,
    "orbit": icon_orbit,
    "flame": icon_flame,
}

STORIES = [
    ("CLIMATE", (46, 125, 91), "crack",
     "COP31 ends with no deal",
     "The UN climate summit in Antalya, Turkey, collapsed on Sunday "
     "after nearly 200 nations failed to agree. The EU, Britain, Panama "
     "and climate-vulnerable states rejected a final draft that never "
     "mentioned fossil fuels."),
    ("GULF", (179, 38, 30), "rocket",
     "Iran strikes Bahrain site",
     "Iranian projectiles hit a civilian industrial facility in Sitra, "
     "Bahrain, starting a fire and injuring two people. Iran also struck "
     "three tankers near the Strait of Hormuz, raising fears of a wider war."),
    ("UKRAINE", (31, 78, 121), "flats",
     "Drone flattens flats near Kyiv",
     "A Russian drone destroyed part of a five-storey apartment block in "
     "Dymer, north of Kyiv, overnight into Sunday. Two people were killed, "
     "four wounded and 14 are missing under the rubble."),
    ("LIBYA", (122, 90, 18), "ship",
     "Sea drones hit Russian warship",
     "Suspected Ukrainian sea drones struck the Russian corvette Merkury "
     "at Benghazi naval base in Libya, causing an explosion and a brief "
     "fire. The war in Ukraine reaches the Mediterranean."),
    ("SPACE", (91, 45, 142), "orbit",
     "BepiColombo reaches Mercury",
     "After an eight-year journey, the ESA\u2013JAXA probe slipped into "
     "orbit around Mercury, only the third spacecraft ever to visit the "
     "planet. A thruster burn ran short, but the spacecraft is safe."),
    ("DISASTER", (194, 87, 27), "flame",
     "Factory fire in Indonesia",
     "A fire tore through a candy factory in Cikande, Banten, killing "
     "three workers. Rescuers are searching the ruins for 37 people "
     "still unaccounted for."),
]


def draw_stories(draw):
    col_x = [28, 520]
    col_w = 476
    row_y = [408, 592, 776]
    row_h = 170
    for i, (tag, colour, icon, headline, deck) in enumerate(STORIES):
        x = col_x[i % 2]
        y = row_y[i // 2]
        # kicker chip
        tw = draw.textlength(tag, font=SANS_B_SM)
        draw.rectangle([x, y, x + tw + 18, y + 24], fill=colour)
        draw.text((x + 9, y + 4), tag, font=SANS_B_SM, fill=WHITE)
        ICONS[icon](draw, x + col_w - 46, y, 42, colour)
        # headline, up to two lines
        lines = wrap(draw, headline, SANS_B, col_w - 56)
        hy = y + 34
        for line in lines[:2]:
            draw.text((x, hy), line, font=SANS_B, fill=INK)
            hy += 24
        # deck, up to four lines
        dlines = wrap(draw, deck, SANS14, col_w)
        dy = hy + 6
        for line in dlines[:4]:
            draw.text((x, dy), line, font=SANS14, fill=(52, 54, 60))
            dy += 18
        draw.line([(x, y + row_h - 8), (x + col_w, y + row_h - 8)],
                  fill=RULE, width=1)


def draw_also(draw):
    y0, y1 = 958, 1002
    draw.rectangle([28, y0, 996, y1], fill=INK)
    draw.text((44, y0 + 12), "ALSO TODAY", font=SANS_B_SM, fill=(244, 196, 90))
    text = ("Fire at a power station near Basra, Iraq, kills at least 4 and "
            "injures 35.   \u25c6   Settlers torch 12 vehicles in four West "
            "Bank villages; Israel opens an inquiry.")
    lines = wrap(draw, text, SANS_SM, 996 - 44 - 150)
    ly = y0 + 3
    for line in lines[:2]:
        draw.text((200, ly), line, font=SANS_SM, fill=WHITE)
        ly += 17


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
    draw_masthead(draw)
    draw_hero(draw)
    draw_stories(draw)
    draw_also(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)


if __name__ == "__main__":
    main()
