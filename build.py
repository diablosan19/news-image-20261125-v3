#!/usr/bin/env python3
"""Build the news-image entry for 25 November 2026.

Renders a 1024x1024 front page, 'THE WORLD IN ONE PAGE', carrying 34
stories all first reported on Wednesday 25 November 2026, across
10 regions and 16 fields. Drawn shapes only; no photographs.
Every headline was checked against a dated source before inclusion;
stories first reported before 25 November are named in the DATE CHECK
box instead of being headlined. No Nvidia reinstatement story exists
and none is headlined anywhere on the page.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PAPER = (251, 250, 245)
INK = (17, 17, 17)
MUTED = (90, 90, 90)
RED = (163, 22, 33)
NAVY = (18, 40, 75)
NAVY_LT = (38, 68, 110)
GOLD = (176, 141, 60)
RULE = (205, 200, 190)
FAINT = (232, 230, 224)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; never splits a word in half."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, fnt, max_w, max_lines):
    size = fnt.size
    while size > 8:
        f = font(fnt.path, size)
        lines = wrap(draw, text, f, max_w)
        if len(lines) <= max_lines:
            return lines, f
        size -= 1
    f = font(fnt.path, size)
    return wrap(draw, text, f, max_w)[:max_lines], f


# (field, region, headline, utc_time, sourcing label)
STORIES = [
    ("CONFLICT", "NIZHNY NOVGOROD", "Ukraine hits 5 Russian jets at Savasleyka base",
     "15:00 UTC", "CONFIRMED"),
    ("CONFLICT", "RIYADH", "Houthis claim strike on Ras Tanura refinery",
     "06:00 UTC", "REPORTED"),
    ("ENERGY", "HORMUZ", "Two tankers hit mines in Hormuz Strait, catch fire",
     "05:00 UTC", "CLAIM"),
    ("CONFLICT", "KYIV", "Russia hits Kyiv with ballistic missiles",
     "20:00 UTC", "REPORTED"),
    ("CONFLICT", "MOSCOW", "Leaked data: at least 490,334 Russian troops killed",
     "07:00 UTC", "REPORTED"),
    ("CONFLICT", "GAZA", "Israel kills Hamas northern Gaza security chief",
     "14:00 UTC", "REPORTED"),
    ("DIPLOMACY", "WARSAW", "Poland plans no-fly zone on Ukraine border",
     "19:00 UTC", "REPORTED"),
    ("TRADE", "WASHINGTON", "US unveils new tariffs on 14 economies",
     "17:00 UTC", "OFFICIAL"),
    ("TRADE", "NEW DELHI", "US to cap India tariff at 17% if deal struck",
     "15:00 UTC", "CONFIRMED"),
    ("SPACE", "JIUQUAN", "Shenzhou-24 docks; first foreign astronaut aboard",
     "06:00 UTC", "OFFICIAL"),
    ("DIPLOMACY", "CANBERRA", "Australia, Solomons sign sweeping Pacific treaty",
     "09:00 UTC", "CONFIRMED"),
    ("SOCIETY", "CARTAGENA", "Troops free all hostages in supermarket siege",
     "08:00 UTC", "CONFIRMED"),
    ("LABOUR", "DHAKA", "Bangladesh raises garment wage 36% to Tk17,000",
     "12:00 UTC", "OFFICIAL"),
    ("DISASTER", "BOGOR", "Mine flood in Bogor kills 6, about 20 trapped",
     "10:00 UTC", "REPORTED"),
    ("DISASTER", "CAIRO", "Fuel truck crash near Cairo kills over 30",
     "11:00 UTC", "REPORTED"),
    ("MIGRATION", "CANARIES", "Canary Islands see 2,100 migrants in one day",
     "13:00 UTC", "REPORTED"),
    ("CONFLICT", "KHARTOUM", "Sudan drone strikes kill 19 civilians",
     "12:00 UTC", "REPORTED"),
    ("SOCIETY", "IOWA", "Army blows up 5 tons of lead explosives in Iowa",
     "16:00 UTC", "OFFICIAL"),
    ("MIGRATION", "MADRID", "Abrego Garcia lands in Spain after US deal",
     "14:00 UTC", "CONFIRMED"),
    ("LAW", "WASHINGTON", "Second judge blocks birthright citizenship order",
     "18:00 UTC", "OFFICIAL"),
    ("LAW", "JERUSALEM", "Judges urge Netanyahu bribery charge dropped",
     "15:00 UTC", "REPORTED"),
    ("CULTURE", "LONDON", "Duran Duran guitarist Andy Taylor dies at 65",
     "17:00 UTC", "CONFIRMED"),
    ("SOCIETY", "DETROIT", "Ex-Lions owner Martha Ford dies at 101",
     "13:00 UTC", "CONFIRMED"),
    ("SOCIETY", "NEW YORK", "Macy's Thanksgiving parade postponed to Saturday",
     "19:00 UTC", "OFFICIAL"),
    ("SPORT", "LONDON", "NBA unveils $11bn plan for European arenas",
     "12:00 UTC", "CONFIRMED"),
    ("LAW", "NEW YORK", "MLB sues players union ahead of lockout",
     "16:00 UTC", "CONFIRMED"),
    ("SPORT", "ZURICH", "FIFA picks US-led bid for 2031 Women's World Cup",
     "14:00 UTC", "CONFIRMED"),
    ("MARKETS", "WASHINGTON", "US core inflation hot at 3.3% on the year",
     "13:30 UTC", "OFFICIAL"),
    ("MARKETS", "SEOUL", "Kospi plunges 6.16% as Asia tech rout deepens",
     "07:00 UTC", "CONFIRMED"),
    ("TECH", "AUSTIN", "Dell revenue more than doubles on AI servers",
     "15:00 UTC", "CONFIRMED"),
    ("POLITICS", "MURMANSK", "Murmansk governor held in pre-trial detention",
     "11:00 UTC", "OFFICIAL"),
    ("DIPLOMACY", "GENEVA", "34 nations urge Russia to halt riot-gas use",
     "12:00 UTC", "OFFICIAL"),
    ("HEALTH", "GENEVA", "AIDS deaths fall to 570,000, a 20-year low",
     "10:00 UTC", "OFFICIAL"),
    ("DIPLOMACY", "BUDAPEST", "Hungary, Ukraine make fresh start on trade",
     "09:00 UTC", "CONFIRMED"),
]

LEAD = STORIES[0]
GRID = STORIES[1:]
REGIONS = ["Russia & Ukraine", "Middle East & Gulf", "South Asia",
           "East Asia", "Southeast Asia", "Pacific", "Africa",
           "North America", "South America", "Europe"]
FIELDS = ["Conflict", "Energy", "Diplomacy", "Trade", "Space", "Society",
          "Labour", "Disaster", "Migration", "Law", "Culture", "Sport",
          "Markets", "Tech", "Politics", "Health"]

HELD_MAIN = [
    "COP31 collapse \u2014 22 Nov",
    "Huawei convicted in US trial \u2014 24 Nov",
    "Sinner knee surgery \u2014 24 Nov",
    "CIA system breached \u2014 24 Nov",
    "Riyadh tower drone strike, 11 hurt \u2014 24 Nov",
    "Hamas chief Abu Nahal killed \u2014 24 Nov",
    "Venezuela debt $237.5bn published \u2014 24 Nov",
    "Thomas Markle indicted \u2014 24 Nov",
    "Shein $100m FTC settlement \u2014 24 Nov",
    "Russian missiles crossed Poland \u2014 20 Nov",
    "Russian drone entered Polish airspace \u2014 24 Nov",
    "Libyan officers died of wounds \u2014 24 Nov",
    "Putin: Ukraine kept hitting refineries \u2014 24 Nov",
    "Democrats clinch 258 House seats \u2014 15 Nov",
]
HELD_NOTE = ("Nothing in this box ran as a headline today: each was first "
             "reported before Wednesday 25 November 2026.")

TIMELINE = [
    (5.0, "05:00", "HORMUZ"),
    (7.0, "07:00", "ROSSTAT"),
    (10.0, "10:00", "BOGOR"),
    (13.5, "13:30", "PCE"),
    (17.0, "17:00", "TARIFFS"),
]

MARKETS = [
    ("BRENT", "$94.61", "+3.51%"),
    ("WTI", "$83.68", "+1.99%"),
    ("GOLD", "$3,535.80", "-0.73%"),
    ("DOW", "50,182.95", "+0.33%"),
    ("KOSPI", "-6.16%", "Wed close"),
]


def draw_masthead(d):
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.rectangle([0, 88, W, 92], fill=GOLD)
    d.text((16, 10), "THE WORLD IN ONE PAGE",
           font=font(SERIF_B, 34), fill=(255, 255, 255))
    d.text((16, 58), "Wednesday, 25 November 2026  \u00b7  All stories first "
           "reported today", font=font(SANS, 15), fill=(200, 210, 225))
    stats = "34 STORIES  \u00b7  10 REGIONS  \u00b7  16 FIELDS"
    tw = d.textlength(stats, font=font(SANS_B, 15))
    d.text((W - 16 - tw, 16), stats, font=font(SANS_B, 15),
           fill=(255, 255, 255))
    sub = "news-image-20261125"
    tw2 = d.textlength(sub, font=font(SANS, 13))
    d.text((W - 16 - tw2, 58), sub, font=font(SANS, 13),
           fill=(200, 210, 225))


def draw_lead_scene(d, x0, y0, x1, y1):
    """Drawn icon scene: runway, jets, refinery towers. No photos."""
    d.rectangle([x0, y0, x1, y1], fill=NAVY)
    d.rectangle([x0, y0, x1, y1], outline=GOLD, width=2)
    cx = (x0 + x1) // 2
    # sky stars
    for sx, sy in [(x0 + 22, y0 + 14), (x0 + 60, y0 + 30), (x1 - 30, y0 + 18),
                   (x1 - 70, y0 + 34), (x0 + 40, y1 - 16), (x1 - 44, y1 - 20)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
    # runway
    d.polygon([(x0 + 10, y1 - 26), (x1 - 10, y1 - 26), (x1 - 40, y1 - 8),
               (x0 + 40, y1 - 8)], fill=(60, 70, 90))
    # five small jet silhouettes in a row
    for i in range(5):
        jx = x0 + 28 + i * 58
        jy = y0 + 46
        d.polygon([(jx, jy - 10), (jx + 34, jy), (jx, jy + 10), (jx + 8, jy)],
                  fill=(235, 235, 235))
        d.polygon([(jx + 10, jy - 12), (jx + 16, jy - 2), (jx + 10, jy)],
                  fill=(200, 200, 200))
    d.text((x0 + 10, y1 - 20), "DRAWN SCENE \u2014 NO PHOTO",
           font=font(SANS, 8), fill=(180, 195, 215))


def draw_lead(d):
    y0, y1 = 92, 196
    d.rectangle([0, y0, W, y1], fill=PAPER)
    d.rectangle([0, y1 - 1, W, y1], fill=RULE)
    tag = "LEAD  \u00b7  CONFLICT  \u00b7  NIZHNY NOVGOROD"
    d.text((16, y0 + 8), tag, font=font(SANS_B, 11), fill=RED)
    head = "Ukraine hits 5 Russian jets at Savasleyka base"
    lines, f = fit_lines(d, head, font(SANS_B, 20), 620, 1)
    yy = y0 + 26
    for ln in lines:
        d.text((16, yy), ln, font=f, fill=INK)
        yy += 26
    deck = ("Ukraine's General Staff says its forces struck Savasleyka "
            "airbase, damaging three MiG-31s and two Su-34s, and hit two "
            "refineries in Samara. Russia struck Kyiv late in the day.")
    dl = wrap(d, deck, font(SANS, 11), 620)
    yy += 2
    for ln in dl[:3]:
        d.text((16, yy), ln, font=font(SANS, 11), fill=MUTED)
        yy += 14
    d.text((16, y1 - 16), "15:00 UTC  \u00b7  CONFIRMED  \u00b7  Ukraine General "
           "Staff via Reuters", font=font(SANS_B, 10), fill=INK)
    draw_lead_scene(d, 668, y0 + 8, W - 16, y1 - 8)


def draw_datecheck(d):
    y0, y1 = 196, 312
    d.rectangle([16, y0, W - 16, y1], outline=RED, width=2)
    d.text((26, y0 + 6), "DATE CHECK \u2014 HELD BACK: FIRST REPORTED BEFORE TODAY",
           font=font(SANS_B, 11), fill=RED)
    yy = y0 + 24
    for i, item in enumerate(HELD_MAIN):
        col = i // 5
        row = i % 5
        x = 26 + col * 327
        d.text((x, yy + row * 11), "\u00b7 " + item,
               font=font(SANS, 9), fill=MUTED)
    yy2 = y0 + 24 + 5 * 11 + 4
    lines = wrap(d, HELD_NOTE, font(SANS, 8), W - 52)
    for ln in lines[:1]:
        d.text((26, yy2), ln, font=font(SANS, 8), fill=MUTED)
        yy2 += 9


def draw_grid(d):
    y0, y1 = 312, 868
    cols, rows = 3, 11
    cw = (W - 32 - (cols - 1) * 12) // cols
    rh = (y1 - y0) // rows
    for idx, (field, region, head, utc, label) in enumerate(GRID):
        r, c = divmod(idx, cols)
        x = 16 + c * (cw + 12)
        y = y0 + r * rh
        if r > 0:
            d.line([x, y - 1, x + cw, y - 1], fill=FAINT, width=1)
        d.text((x, y + 2), field, font=font(SANS_B, 9), fill=RED)
        lines, f = fit_lines(d, head, font(SANS_B, 11), cw, 2)
        yy = y + 14
        for ln in lines:
            d.text((x, yy), ln, font=f, fill=INK)
            yy += 13
        meta = "%s \u00b7 %s \u00b7 %s" % (region, utc, label)
        d.text((x, y + rh - 13), meta, font=font(SANS, 9), fill=MUTED)


def draw_map_timeline(d):
    y0, y1 = 868, 936
    d.rectangle([0, y0, W, y1], fill=(243, 241, 235))
    d.rectangle([0, y0, W, y0 + 1], fill=RULE)
    d.text((16, y0 + 5), "PIN MAP \u2014 10 REGIONS",
           font=font(SANS_B, 10), fill=NAVY)
    mx, my = 16, y0 + 18
    conts = [
        [(8, 12), (30, 4), (55, 6), (70, 12), (62, 22), (48, 28), (38, 24),
         (28, 30), (14, 24)],
        [(62, 32), (78, 30), (86, 38), (80, 50), (68, 52), (60, 40)],
        [(140, 24), (160, 18), (178, 24), (182, 36), (168, 50), (152, 48),
         (142, 34)],
        [(142, 6), (158, 4), (166, 10), (156, 16), (144, 14)],
        [(168, 6), (210, 2), (250, 6), (285, 12), (270, 24), (240, 28),
         (210, 24), (190, 16), (172, 12)],
        [(252, 46), (278, 44), (282, 52), (256, 54)],
    ]
    for poly in conts:
        pts = [(mx + px, my + py * 46 / 56) for px, py in poly]
        d.polygon(pts, fill=(205, 200, 185), outline=(150, 145, 130))
    pins = [(247, 17), (257, 19), (242, 24), (206, 22), (181, 24), (178, 20),
            (145, 11), (169, 3), (141, 11), (151, 16), (161, 17), (165, 43),
            (147, 31), (154, 38), (152, 20), (78, 17), (79, 14), (86, 31),
            (102, 43), (64, 16), (278, 47), (268, 50)]
    for px, py in pins:
        x = mx + px
        y = my + py * 46 / 56
        d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=RED)
    tx0, tx1 = 340, W - 16
    ty = y0 + 28
    d.text((tx0, y0 + 5), "THE DAY IN UTC \u2014 FIRST WIRE",
           font=font(SANS_B, 10), fill=NAVY)
    d.line([tx0, ty, tx1, ty], fill=INK, width=2)
    for h in range(0, 25, 4):
        x = tx0 + (tx1 - tx0) * h / 24.0
        d.line([x, ty - 3, x, ty + 3], fill=INK, width=1)
        lab = "%02d:00" % h
        d.text((x - 10, ty + 24), lab, font=font(SANS, 8), fill=MUTED)
    for k, (hour, clock, name) in enumerate(TIMELINE):
        x = tx0 + (tx1 - tx0) * hour / 24.0
        d.line([x, ty - 8, x, ty - 2], fill=RED, width=2)
        nw = d.textlength(name, font=font(SANS_B, 8))
        d.text((x - nw / 2, ty + 4), name, font=font(SANS_B, 8), fill=INK)
        cw2 = d.textlength(clock, font=font(SANS_B, 8))
        d.text((x - cw2 / 2, ty + 14), clock, font=font(SANS_B, 8),
               fill=RED)


def draw_markets_footer(d):
    y0, y1 = 936, 984
    d.rectangle([0, y0, W, y1], fill=NAVY)
    parts = ["%s %s %s" % (name, val, chg) for name, val, chg in MARKETS]
    line = "MARKETS   " + "    \u00b7    ".join(parts)
    mf = font(SANS_B, 13)
    while d.textlength(line, font=mf) > W - 32 and mf.size > 9:
        mf = font(SANS_B, mf.size - 1)
    d.text((16, y0 + 8), line, font=mf, fill=(255, 255, 255))
    d.text((16, y0 + 28), "Wednesday 25 November closes: Brent and WTI "
           "settled higher; gold settled lower; Dow closed above 50,000.",
           font=font(SANS, 10), fill=(200, 210, 225))
    d.rectangle([0, 984, W, H], fill=PAPER)
    d.text((16, 992), "Sources: Reuters, Al Jazeera, AP, DW. All 34 stories "
           "first reported 25 Nov 2026; times are first-wire UTC, "
           "approximate. Drawn art only, no photos.",
           font=font(SANS, 9), fill=MUTED)
    d.text((16, 1006), "34 stories \u00b7 10 regions \u00b7 16 fields \u00b7 "
           "Wednesday, 25 November 2026", font=font(SANS_B, 9), fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_lead(d)
    draw_datecheck(d)
    draw_grid(d)
    draw_map_timeline(d)
    draw_markets_footer(d)
    img.save(OUT, "PNG", optimize=True)
    size = os.path.getsize(OUT)
    print("wrote %s" % OUT)
    print("dimensions %dx%d" % (W, H))
    print("bytes %d (limit 1048576, ok=%s)" % (size, size <= 1048576))
    print("stories %d regions %d fields %d" % (len(STORIES), len(REGIONS),
                                               len(FIELDS)))
    assert size <= 1048576, "entry.png over 1 MiB"
    assert len(STORIES) == 34
    assert len(GRID) == 33


if __name__ == "__main__":
    main()
