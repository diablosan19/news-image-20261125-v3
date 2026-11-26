#!/usr/bin/env python3
"""Render the front page for Wednesday 25 November 2026.

One 1024x1024 PNG: masthead, lead story with a drawn scene, a red
DATE CHECK box, a 4-column story grid, a schematic pin map, a UTC
timeline, a markets strip and a sources footer. All art is drawn with
PIL shapes; there are no photos. Every story below was first reported
on 25 November 2026 (any time zone) and cross-checked against at
least two sources. Times are first-wire UTC, approximate.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 230)
NAVY = (22, 38, 76)
INK = (26, 26, 26)
GREY = (90, 90, 82)
LINE = (216, 210, 194)
RED = (179, 32, 44)
GOLD = (200, 162, 74)
WHITE = (255, 253, 248)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

SRC_COLOR = {
    "OFFICIAL": (30, 107, 74),
    "CONFIRMED": (31, 92, 139),
    "REPORTED": (138, 109, 0),
    "CLAIM": (179, 32, 44),
}

FIELD_COLOR = {
    "War & Conflict": (179, 32, 44),
    "Defence": (122, 59, 18),
    "Diplomacy": (31, 92, 139),
    "Energy": (178, 106, 0),
    "Economy": (30, 107, 74),
    "Business & Markets": (91, 74, 138),
    "Technology": (14, 107, 122),
    "Cybersecurity": (107, 30, 91),
    "Space & Science": (43, 58, 103),
    "Health": (163, 22, 75),
    "Law & Justice": (61, 61, 61),
    "Humanitarian": (138, 109, 0),
    "Culture & Society": (74, 122, 30),
    "Politics": (138, 47, 47),
}

# (headline, one-line label, dateline, utc, sourcing, field, region)
LEAD = (
    "Houthi missiles hit Riyadh tower and refinery",
    "Saudi civil defence counts 11 wounded, two of them Indian; Delhi condemns the strike.",
    "RIYADH", "04:41", "CONFIRMED", "War & Conflict", "Middle East",
)

STORIES = [
    ("Iran claims it downed two US drones over Hormuz",
     "Tehran says defences hit an MQ-9.", "HORMUZ", "05:11",
     "CLAIM", "War & Conflict", "Middle East"),
    ("Trump: Iran war funding secured through January",
     "President warns Democrats over a win.", "WASHINGTON", "06:41",
     "REPORTED", "Defence", "North America"),
    ("Zelensky: Ukraine needs \u20ac115bn in foreign aid for 2027",
     "Kyiv prices next year as donors argue.", "KYIV", "08:15",
     "REPORTED", "Diplomacy", "Europe"),
    ("US defence chief pauses Patriot supplies to Kyiv",
     "Halt lands amid Europe's aid debate.", "WASHINGTON", "08:20",
     "REPORTED", "Defence", "North America"),
    ("Ukraine drones sink Russian warship in Libyan port",
     "Two Libyan officers die in the attack.", "BENGHAZI", "09:05",
     "REPORTED", "War & Conflict", "Africa"),
    ("Ukrainian drones hit two refineries in Samara",
     "Strikes press Russian energy sites.", "SAMARA", "09:30",
     "REPORTED", "Energy", "Europe"),
    ("Huawei convicted in US trial over trade secrets",
     "Theft guilty; racketeering cleared.", "NEW YORK", "02:58",
     "CONFIRMED", "Law & Justice", "North America"),
    ("CIA and ODNI hit by cyber breach, source says",
     "Unclassified systems hit, source says.", "WASHINGTON", "02:39",
     "REPORTED", "Cybersecurity", "North America"),
    ("Shenzhou-24 docks; Pakistani flies to space station",
     "First foreign astronaut on Tiangong.", "BEIJING", "09:47",
     "CONFIRMED", "Space & Science", "East Asia"),
    ("Australia, Solomons sign sweeping Pacific treaty",
     "Principal partner; no foreign bases.", "CANBERRA", "07:00",
     "CONFIRMED", "Diplomacy", "Pacific"),
    ("Eurozone inflation rises to 4.0%, Eurostat says",
     "Prices climb as growth, jobs land.", "BRUSSELS", "10:00",
     "OFFICIAL", "Economy", "Europe"),
    ("Bangladesh raises garment wage 36% to Tk17,000",
     "Minimum about $139 a month, from Dec.", "DHAKA", "09:47",
     "CONFIRMED", "Economy", "South Asia"),
    ("Abrego Garcia leaves US for Spain after 20 months",
     "Ends his fight by flying out.", "WASHINGTON", "11:30",
     "CONFIRMED", "Law & Justice", "North America"),
    ("Troops free all hostages in supermarket siege",
     "Siege ends; one attacker killed.", "CARTAGENA", "12:00",
     "CONFIRMED", "War & Conflict", "Latin America"),
    ("Court restores Senegal's Africa Cup title",
     "Senegal wins; Morocco vows challenge.", "LAUSANNE", "13:00",
     "CONFIRMED", "Culture & Society", "Africa"),
    ("Roche breast-cancer pill wins second FDA approval",
     "Swiss hopeful clears another bar.", "BASEL", "14:00",
     "CONFIRMED", "Health", "Europe"),
    ("Homo erectus lived in rainforest beside Denisovans",
     "Ancient relative lived in wet forest.", "GLOBAL", "15:00",
     "REPORTED", "Space & Science", "Global"),
    ("EasyJet profit falls 89% after \u00a3244m fuel hit",
     "Airline retires older aircraft faster.", "LUTON", "07:30",
     "CONFIRMED", "Business & Markets", "Europe"),
    ("Amazon buys Decart to sharpen its AI chips",
     "Deal bets on software to close chip gap.", "SEATTLE", "16:00",
     "REPORTED", "Technology", "North America"),
    ("Anthropic shares fall below IPO price first time",
     "Stock slides under debut price.", "NEW YORK", "16:30",
     "REPORTED", "Business & Markets", "North America"),
    ("Tidal bans AI-made music, deletes 27m tracks",
     "Streamer purges fully synthetic songs.", "OSLO", "17:00",
     "CONFIRMED", "Technology", "Global"),
    ("US charges 800 in 400 cases in scam crackdown",
     "Justice Dept. acts on global fraud.", "WASHINGTON", "05:11",
     "OFFICIAL", "Law & Justice", "North America"),
    ("Gaza meningitis spreads as ceasefire frays",
     "Health officials warn of disease.", "GAZA", "06:00",
     "REPORTED", "Health", "Middle East"),
    ("WFP: wars imperil food aid for millions",
     "Conflicts strain relief pipelines.", "ROME", "06:05",
     "REPORTED", "Humanitarian", "Global"),
    ("Far right leads polls before Spain's snap vote",
     "Housing tops Sunday vote campaign.", "MADRID", "07:30",
     "REPORTED", "Politics", "Europe"),
    ("China orders 50 Boeing jets in $7.4bn deal",
     "Order signals trade despite tensions.", "BEIJING", "11:00",
     "REPORTED", "Economy", "East Asia"),
    ("Venezuela discloses $237.5bn debt pile",
     "Caracas weighs restructuring talks.", "CARACAS", "12:30",
     "REPORTED", "Economy", "Latin America"),
    ("Rescue hunt in flooded Indonesia gold mine",
     "Teams search for trapped workers.", "JAKARTA", "08:00",
     "REPORTED", "Humanitarian", "Southeast Asia"),
    ("North Korea orders Swiss office to shut",
     "Envoy expelled after sanctions row.", "PYONGYANG", "09:00",
     "REPORTED", "Diplomacy", "East Asia"),
    ("Hong Kong marks year since deadly tower fire",
     "Survivors return; accountability sought.", "HONG KONG", "07:14",
     "REPORTED", "Culture & Society", "East Asia"),
    ("Stars rally for Panahi as petition nears 2,000",
     "Actors back director; term dates to Oct.", "TEHRAN", "10:30",
     "REPORTED", "Culture & Society", "Middle East"),
    ("Rights group: Modi has weakened India's democracy",
     "Report cites a decade of erosion.", "NEW DELHI", "06:10",
     "REPORTED", "Law & Justice", "South Asia"),
    ("Sudan fighting deepens; Blue Nile hit",
     "Attacks threaten displaced families.", "KHARTOUM", "08:45",
     "REPORTED", "Humanitarian", "Africa"),
]

DATE_CHECK = [
    "COP31 Antalya collapse \u2014 first reported Sun 22 Nov \u2014 excluded",
    "Sinner knee surgery \u2014 first reported Tue 24 Nov \u2014 excluded",
    "Panahi 5-year sentence \u2014 ruled Mon 26 Oct \u2014 excluded",
    "Hong Kong tower-block fire \u2014 the fire, Nov 2025 \u2014 excluded",
]

TIMELINE = [
    ("02:39", "CIA BREACH"),
    ("04:41", "RIYADH STRIKE"),
    ("09:47", "SHENZHOU DOCKS"),
    ("13:00", "SENEGAL TITLE"),
    ("16:30", "ANTHROPIC SLIDES"),
]

# (lon, lat, label or None) for the schematic pin map
PINS = [
    (46.7, 24.7, "RIYADH"), (56.5, 26.6, None), (30.5, 50.4, "KYIV"),
    (4.4, 50.8, None), (20.1, 32.1, None), (-77.0, 38.9, None),
    (-74.0, 4.7, "BOGOTA"), (-17.4, 14.7, "DAKAR"), (116.4, 39.9, "BEIJING"),
    (90.4, 23.8, None), (149.1, -35.3, "CANBERRA"), (160.0, -9.6, None),
    (106.8, -6.2, "JAKARTA"), (-0.1, 51.5, None), (114.2, 22.3, None),
    (77.2, 28.6, None), (-75.5, 10.4, None), (-66.9, 10.5, None),
    (6.6, 46.5, None), (34.5, 31.5, None), (-3.7, 40.4, None),
    (125.8, 39.0, None), (32.5, 15.5, None),
]

MARKETS = ("EUROZONE 4.0%  \u00b7  AUSTRALIA 4.9%  \u00b7  "
           "BANGLADESH WAGE +36%  \u00b7  EASYJET \u201389%  \u00b7  "
           "BOEING $7.4BN  \u00b7  VENEZUELA $237.5BN")


def wrap(draw, text, fnt, max_w):
    """Word-wrap; never splits a word. Returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
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


def draw_glyph(d, field, x, y, s=16):
    """Tiny drawn icon for a field, made of plain shapes."""
    c = FIELD_COLOR[field]
    if field == "War & Conflict":
        d.polygon([(x + s / 2, y), (x + s * 0.62, y + s * 0.38),
                   (x + s, y + s / 2), (x + s * 0.62, y + s * 0.62),
                   (x + s / 2, y + s), (x + s * 0.38, y + s * 0.62),
                   (x, y + s / 2), (x + s * 0.38, y + s * 0.38)], fill=c)
    elif field == "Defence":
        d.polygon([(x, y + 2), (x + s, y + 2), (x + s, y + s * 0.55),
                   (x + s / 2, y + s), (x, y + s * 0.55)], outline=c, width=2)
        d.line([(x + s / 2, y + 3), (x + s / 2, y + s - 3)], fill=c, width=2)
    elif field == "Diplomacy":
        d.ellipse([x, y + 2, x + s * 0.55, y + s * 0.62], outline=c, width=2)
        d.ellipse([x + s * 0.45, y + s * 0.38, x + s, y + s - 2],
                  outline=c, width=2)
    elif field == "Energy":
        d.polygon([(x + s * 0.6, y), (x + s * 0.25, y + s * 0.55),
                   (x + s * 0.5, y + s * 0.55), (x + s * 0.4, y + s),
                   (x + s * 0.75, y + s * 0.45), (x + s * 0.5, y + s * 0.45)],
                  fill=c)
    elif field == "Economy":
        d.ellipse([x + 1, y + 1, x + s - 1, y + s - 1], outline=c, width=2)
        d.line([(x + s / 2, y + 2), (x + s / 2, y + s - 2)], fill=c, width=2)
        d.line([(x + s * 0.28, y + s * 0.42), (x + s * 0.72, y + s * 0.42)],
               fill=c, width=2)
    elif field == "Business & Markets":
        d.rectangle([x + 1, y + s * 0.55, x + s * 0.28, y + s - 1], fill=c)
        d.rectangle([x + s * 0.38, y + s * 0.35, x + s * 0.62, y + s - 1], fill=c)
        d.rectangle([x + s * 0.72, y + s * 0.15, x + s - 1, y + s - 1], fill=c)
    elif field == "Technology":
        d.rectangle([x + 3, y + 3, x + s - 3, y + s - 3], outline=c, width=2)
        d.rectangle([x + 6, y + 6, x + s - 6, y + s - 6], fill=c)
        for t in (0.25, 0.5, 0.75):
            d.line([(x + s * t, y), (x + s * t, y + 3)], fill=c, width=1)
            d.line([(x + s * t, y + s - 3), (x + s * t, y + s)], fill=c, width=1)
    elif field == "Cybersecurity":
        d.rectangle([x + 2, y + s * 0.45, x + s - 2, y + s - 1], outline=c, width=2)
        d.arc([x + s * 0.22, y, x + s * 0.78, y + s * 0.6], 180, 360,
              fill=c, width=2)
    elif field == "Space & Science":
        d.polygon([(x + s / 2, y), (x + s * 0.8, y + s * 0.6),
                   (x + s / 2, y + s * 0.45), (x + s * 0.2, y + s * 0.6)],
                  fill=c)
        d.ellipse([x + s * 0.32, y + s * 0.68, x + s * 0.68, y + s], fill=c)
    elif field == "Health":
        d.rectangle([x + s * 0.38, y + 1, x + s * 0.62, y + s - 1], fill=c)
        d.rectangle([x + 1, y + s * 0.38, x + s - 1, y + s * 0.62], fill=c)
    elif field == "Law & Justice":
        d.rectangle([x + 1, y + 1, x + s - 1, y + 4], fill=c)
        d.rectangle([x + s * 0.44, y + 4, x + s * 0.56, y + s - 4], fill=c)
        d.rectangle([x + 1, y + s - 4, x + s - 1, y + s - 1], fill=c)
    elif field == "Humanitarian":
        d.polygon([(x + s / 2, y), (x + s - 1, y + s * 0.4),
                   (x + s * 0.78, y + s - 1), (x + s * 0.22, y + s - 1),
                   (x + 1, y + s * 0.4)], outline=c, width=2)
    elif field == "Culture & Society":
        d.ellipse([x + 1, y + 1, x + s - 1, y + s - 1], outline=c, width=2)
        d.line([(x + 2, y + s / 2), (x + s - 2, y + s / 2)], fill=c, width=1)
        d.arc([x + 2, y + 2, x + s - 2, y + s - 2], 300, 60, fill=c, width=1)
    elif field == "Politics":
        d.rectangle([x + 1, y + s * 0.3, x + s - 1, y + s - 1], outline=c, width=2)
        d.line([(x + s * 0.3, y + s * 0.3), (x + s * 0.7, y + s * 0.3)],
               fill=c, width=2)
        d.line([(x + s * 0.42, y + 1), (x + s * 0.58, y + s * 0.28)],
               fill=c, width=2)


def draw_lead_scene(d, x0, y0, x1, y1):
    """Drawn skyline under attack: tower, arcs, smoke. No photo."""
    d.rectangle([x0, y0, x1, y1], fill=NAVY)
    d.rectangle([x0, y0, x1, y0 + 2], fill=GOLD)
    for sx, sy in [(x0 + 30, y0 + 18), (x0 + 90, y0 + 30), (x0 + 180, y0 + 14),
                   (x0 + 260, y0 + 26), (x0 + 320, y0 + 18)]:
        d.ellipse([sx, sy, sx + 3, sy + 3], fill=WHITE)
    base = y1 - 34
    # skyline blocks
    for bx, bw, bh in [(0, 42, 52), (48, 30, 70), (84, 46, 44),
                       (136, 34, 62), (300, 52, 48)]:
        d.rectangle([x0 + bx, base - bh, x0 + bx + bw, base], fill=(38, 54, 96))
    # the tower: tall block, spire, red tip
    d.rectangle([x0 + 176, base - 84, x0 + 210, base], fill=(58, 76, 122))
    d.polygon([(x0 + 193, base - 102), (x0 + 186, base - 84),
               (x0 + 200, base - 84)], fill=(58, 76, 122))
    d.ellipse([x0 + 190, base - 108, x0 + 196, base - 102], fill=RED)
    # windows
    for wy in range(base - 76, base - 8, 12):
        for wx in (182, 192, 202):
            d.rectangle([x0 + wx, wy, x0 + wx + 4, wy + 5], fill=(232, 200, 106))
    # incoming arcs
    d.arc([x0 + 220, y0 + 8, x0 + 330, y0 + 88], 200, 330, fill=WHITE, width=2)
    d.arc([x0 + 236, y0 + 26, x0 + 316, y0 + 96], 200, 330, fill=(232, 200, 106),
          width=2)
    d.polygon([(x0 + 322, y0 + 66), (x0 + 332, y0 + 74), (x0 + 320, y0 + 78)],
              fill=WHITE)
    # smoke puffs over the tower
    for sx, sy, sr in [(196, base - 94, 9), (210, base - 88, 7),
                       (186, base - 86, 6)]:
        d.ellipse([x0 + sx - sr, sy - sr, x0 + sx + sr, sy + sr],
                  fill=(150, 150, 148))
    d.rectangle([x0, base, x1, y1 - 16], fill=(16, 28, 56))
    d.text((x0 + 8, y1 - 15), "DRAWN SCENE \u2014 NO PHOTO",
           font=SANS_B(9), fill=(200, 200, 190))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 84], fill=NAVY)
    d.text((16, 8), "THE WORLD IN ONE PAGE", font=SERIF_B(40), fill=WHITE)
    d.text((W - 16, 16), "34 STORIES \u00b7 10 REGIONS \u00b7 14 FIELDS",
           font=SANS_B(15), fill=GOLD, anchor="ra")
    d.text((16, 58), "Wednesday 25 November 2026  \u00b7  All stories first reported today",
           font=SANS(16), fill=WHITE)
    d.text((W - 16, 60), "news-image-20261125", font=SANS(12),
           fill=(170, 175, 195), anchor="ra")
    d.rectangle([0, 84, W, 87], fill=GOLD)

    # ---- lead ----
    hx, hy, hw = 16, 94, 624
    head, label, date, utc, src, field, region = LEAD
    d.text((hx, hy), "LEAD \u00b7 WAR & CONFLICT \u00b7 RIYADH",
           font=SANS_B(13), fill=RED)
    hl = wrap(d, head, SERIF_B(24), hw)
    assert len(hl) == 1, f"lead headline wraps to {len(hl)} lines: {hl}"
    yy = hy + 20
    for line in hl:
        d.text((hx, yy), line, font=SERIF_B(24), fill=INK)
        yy += 29
    ll = wrap(d, label, SANS(14), hw)
    assert len(ll) <= 2, f"lead label wraps to {len(ll)} lines"
    for line in ll:
        d.text((hx, yy + 4), line, font=SANS(14), fill=(52, 52, 48))
        yy += 18
    yy += 8
    d.text((hx, yy), f"{utc} UTC \u00b7 {src} \u00b7 SAUDI CIVIL DEFENCE VIA REUTERS",
           font=SANS_B(11), fill=GREY)
    yy += 22
    chips = ["11 WOUNDED", "2 INDIANS HURT", "TOWER + REFINERY HIT"]
    cx = hx
    for chip in chips:
        cw = d.textlength(chip, font=SANS_B(12)) + 18
        d.rectangle([cx, yy, cx + cw, yy + 24], outline=RED, width=2)
        d.text((cx + 9, yy + 5), chip, font=SANS_B(12), fill=RED)
        cx += cw + 10
    draw_lead_scene(d, 656, 90, 1008, 240)

    # ---- date check ----
    d.rectangle([16, 246, 1008, 330], outline=RED, width=2, fill=WHITE)
    d.text((28, 252), "DATE CHECK \u2014 HELD BACK: FIRST REPORTED BEFORE TODAY",
           font=SANS_B(13), fill=RED)
    item_f = SANS(12)
    for i, item in enumerate(DATE_CHECK):
        col_x = 28 if i % 2 == 0 else 516
        row_y = 276 + (i // 2) * 20
        assert d.textlength("\u00b7 " + item, font=item_f) <= 470, item
        d.text((col_x, row_y), "\u00b7 " + item, font=item_f, fill=INK)
    d.text((28, 312),
           "Nothing in this box is a headline today; each item was first reported "
           "before Wednesday 25 November 2026.",
           font=SANS(10), fill=GREY)

    # ---- story grid: 4 columns x 9 rows ----
    gx, gy, cw_, ch_, gap = 16, 336, 239, 60, 12
    assert len(STORIES) == 33, f"grid stories: {len(STORIES)}"
    for idx, st in enumerate(STORIES):
        head, label, date, utc, src, field, region = st
        col, row = idx % 4, idx // 4
        x = gx + col * (cw_ + gap)
        y = gy + row * ch_
        draw_glyph(d, field, x, y + 1, 16)
        assert d.textlength(label, font=SANS(10)) <= cw_ - 22, label
        d.text((x + 20, y + 2), label, font=SANS(10), fill=(74, 74, 68))
        hl = wrap(d, head, SANS_B(13), cw_)
        assert len(hl) <= 2, f"{head!r} wraps to {len(hl)} lines"
        yy = y + 16
        for line in hl:
            d.text((x, yy), line, font=SANS_B(13), fill=INK)
            yy += 16
        meta = f"{date} \u00b7 {utc} UTC \u00b7 {src}"
        d.text((x, y + 48), meta, font=SANS_B(10), fill=SRC_COLOR[src])
        if row < 8:
            d.line([(gx, y + ch_ - 1), (1008, y + ch_ - 1)], fill=LINE, width=1)

    # ---- bottom band: pin map + UTC timeline ----
    d.line([(508, 882), (508, 972)], fill=LINE, width=1)
    d.text((16, 884), "PIN MAP \u2014 10 REGIONS \u00b7 SCHEMATIC, NOT TO SCALE",
           font=SANS_B(11), fill=NAVY)
    mx0, my0, mx1, my1 = 16, 900, 500, 970
    # continent blobs, equirectangular lon -170..190, lat -60..85
    def px(lon, lat):
        return (mx0 + (lon + 170) / 360 * (mx1 - mx0),
                my0 + (85 - lat) / 145 * (my1 - my0))
    blobs = [(-170, 15, -55, 72), (-80, -55, -35, 12), (-12, 36, 45, 71),
             (-18, -35, 52, 37), (45, 5, 180, 77), (110, -50, 180, 0)]
    for lo0, la0, lo1, la1 in blobs:
        x0b, y0b = px(lo0, la1)
        x1b, y1b = px(lo1, la0)
        d.ellipse([x0b, y0b, x1b, y1b], fill=(201, 194, 176))
    for lon, lat, lab in PINS:
        px_, py_ = px(lon, lat)
        d.ellipse([px_ - 3, py_ - 3, px_ + 3, py_ + 3], fill=RED,
                  outline=WHITE, width=1)
        if lab:
            d.text((px_ + 5, py_ - 5), lab, font=SANS_B(9), fill=INK)

    d.text((516, 884), "THE DAY IN UTC \u2014 FIRST WIRE",
           font=SANS_B(11), fill=NAVY)
    tx0, tx1, ty = 524, 1000, 944
    d.line([(tx0, ty), (tx1, ty)], fill=INK, width=2)
    for hr in (0, 4, 8, 12, 16, 20, 24):
        tx = tx0 + hr / 24 * (tx1 - tx0)
        d.line([(tx, ty - 3), (tx, ty + 3)], fill=INK, width=1)
        anch = "la" if hr == 0 else ("ra" if hr == 24 else "ma")
        d.text((tx, ty + 6), f"{hr:02d}:00", font=SANS(9), fill=GREY,
               anchor=anch)
    for i, (utc, tag) in enumerate(TIMELINE):
        hh, mm = int(utc[:2]), int(utc[3:])
        tx = tx0 + (hh + mm / 60) / 24 * (tx1 - tx0)
        d.ellipse([tx - 3, ty - 3, tx + 3, ty + 3], fill=RED)
        up = (i % 2 == 0)
        lab = f"{utc} {tag}"
        if up:
            d.text((tx, ty - 24), lab, font=SANS_B(9), fill=INK, anchor="ma")
            d.line([(tx, ty - 12), (tx, ty - 4)], fill=RED, width=1)
        else:
            d.text((tx, ty + 16), lab, font=SANS_B(9), fill=INK, anchor="ma")
            d.line([(tx, ty + 4), (tx, ty + 14)], fill=RED, width=1)

    # ---- markets strip ----
    d.rectangle([0, 978, W, 1002], fill=NAVY)
    d.text((16, 984), "MARKETS", font=SANS_B(12), fill=GOLD)
    d.text((108, 984), MARKETS, font=SANS_B(12), fill=WHITE)

    # ---- footer ----
    d.text((W / 2, 1008),
           "Sources: Reuters \u00b7 AP \u00b7 Eurostat \u00b7 Principia \u00b7 Open "
           "Chronicle \u00b7 RadioFree \u00b7 WebIndia123 \u00b7 HRANA. All stories "
           "first reported 25 Nov 2026. Times first-wire UTC. Drawn art only.",
           font=SANS(10), fill=GREY, anchor="ma")

    # ---- consistency checks ----
    regions = {LEAD[6]} | {s[6] for s in STORIES}
    fields = {LEAD[5]} | {s[5] for s in STORIES}
    assert len(STORIES) + 1 == 34, "story count"
    assert len(regions) == 10, f"regions: {sorted(regions)}"
    assert len(fields) == 14, f"fields: {sorted(fields)}"
    assert all(s[0] not in [dc.split(" \u2014 ")[0] for dc in DATE_CHECK]
               for s in [LEAD] + STORIES), "headline in date-check box"

    img.save("entry.png", optimize=True)
    size = os.path.getsize("entry.png")
    print(f"entry.png: {img.size[0]}x{img.size[1]}, {size} bytes, "
          f"{len(STORIES) + 1} stories, {len(regions)} regions, "
          f"{len(fields)} fields")
    assert size < 1048576, "over 1 MiB"


if __name__ == "__main__":
    main()
