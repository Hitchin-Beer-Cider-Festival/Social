#!/usr/bin/env python3
"""
Generate free-entry-6pm.png for HBCF Saturday announcement.
Pink hedgehog style card: FREE ENTRY / FROM 6PM / hedgehog / festival footer.
"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont

REPO = '/home/runner/work/Social/Social'
BRAND_PINK = (236, 0, 140)   # #EC008C

# ── 1. Font ────────────────────────────────────────────────────────────────
def find_or_download_bebas(size):
    candidates = [
        '/usr/share/fonts/truetype/bebas-neue/BebasNeue-Regular.ttf',
        '/usr/share/fonts/truetype/BebasNeue-Regular.ttf',
        '/home/runner/.local/share/fonts/BebasNeue-Regular.ttf',
        '/tmp/BebasNeue-Regular.ttf',
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    # fc-list search
    try:
        r = subprocess.run(['fc-list', ':family=Bebas Neue', '--format=%{file}\n'],
                           capture_output=True, text=True, timeout=5)
        for line in r.stdout.splitlines():
            line = line.strip()
            if line and os.path.exists(line):
                return ImageFont.truetype(line, size)
    except Exception:
        pass
    # Download from Google Fonts
    dest = '/tmp/BebasNeue-Regular.ttf'
    if not os.path.exists(dest):
        print('Downloading Bebas Neue...', file=sys.stderr)
        subprocess.run([
            'curl', '-L', '-o', dest,
            'https://github.com/google/fonts/raw/main/ofl/bebasneue/BebasNeue-Regular.ttf'
        ], check=True, timeout=30)
    return ImageFont.truetype(dest, size)

# ── 2. Extract hedgehog from a countdown PNG ───────────────────────────────
def get_hedgehog(target_size):
    src_path = f'{REPO}/countdown/countdown-1.png'
    src = Image.open(src_path).convert('RGBA')
    w, h = src.size
    # Hedgehog sits in the centre ~520x520; crop middle 640x640 to capture it
    pad = 220
    crop = src.crop((pad, pad, w - pad, h - pad))
    # Make near-white pixels transparent
    pixels = [
        (255, 255, 255, 0) if (r > 240 and g > 240 and b > 240) else (r, g, b, a)
        for r, g, b, a in crop.getdata()
    ]
    crop.putdata(pixels)
    # Trim to content bounding box
    bbox = crop.getbbox()
    if bbox:
        crop = crop.crop(bbox)
    return crop.resize((target_size, target_size), Image.LANCZOS)

# ── 3. Build the announcement card ────────────────────────────────────────
def make_card():
    W, H = 1080, 1080
    canvas = Image.new('RGBA', (W, H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    top_margin = 35

    f_top = find_or_download_bebas(155)
    f_sub = find_or_download_bebas(95)
    f_bot = find_or_download_bebas(76)

    # "FREE ENTRY"
    t1 = 'FREE ENTRY'
    bb1 = draw.textbbox((0, 0), t1, font=f_top)
    tw1 = bb1[2] - bb1[0]; th1 = bb1[3] - bb1[1]
    x1 = (W - tw1) // 2 - bb1[0]
    y1 = top_margin - bb1[1]
    draw.text((x1, y1), t1, fill=BRAND_PINK, font=f_top)

    # "FROM 6PM TONIGHT"
    t2 = 'FROM 6PM TONIGHT'
    bb2 = draw.textbbox((0, 0), t2, font=f_sub)
    tw2 = bb2[2] - bb2[0]; th2 = bb2[3] - bb2[1]
    x2 = (W - tw2) // 2 - bb2[0]
    y2 = y1 + th1 + 8 - bb2[1]
    draw.text((x2, y2), t2, fill=BRAND_PINK, font=f_sub)

    top_end = y2 + th2 + 10

    # BOTTOM TEXT
    t3 = 'HITCHIN BEER & CIDER'
    t4 = 'FESTIVAL 2026'
    bb3 = draw.textbbox((0, 0), t3, font=f_bot)
    bb4 = draw.textbbox((0, 0), t4, font=f_bot)
    th3 = bb3[3] - bb3[1]; th4 = bb4[3] - bb4[1]
    bot_block_h = th3 + 8 + th4
    bot_margin = 25
    bot_start = H - bot_margin - bot_block_h

    # Hedgehog
    available = bot_start - top_end
    hedge_size = min(480, available - 30)
    hedgehog = get_hedgehog(hedge_size)
    hedge_x = (W - hedge_size) // 2
    hedge_y = top_end + (available - hedge_size) // 2
    canvas.paste(hedgehog, (hedge_x, hedge_y), hedgehog)

    # Draw bottom text
    x3 = (W - (bb3[2] - bb3[0])) // 2 - bb3[0]
    y3 = bot_start - bb3[1]
    draw.text((x3, y3), t3, fill=BRAND_PINK, font=f_bot)

    x4 = (W - (bb4[2] - bb4[0])) // 2 - bb4[0]
    y4 = y3 + th3 + 8 - bb4[1]
    draw.text((x4, y4), t4, fill=BRAND_PINK, font=f_bot)

    return canvas.convert('RGB')


if __name__ == '__main__':
    card = make_card()
    out = f'{REPO}/community/free-entry-6pm.png'
    card.save(out, 'PNG', optimize=True)
    print(f'Saved: {out}')
