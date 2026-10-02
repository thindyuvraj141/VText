import os, glob
from PIL import Image, ImageDraw

RES = 'android/app/src/main/res'
LEGACY = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
FORE = {'mdpi': 108, 'hdpi': 162, 'xhdpi': 216, 'xxhdpi': 324, 'xxxhdpi': 432}
PURPLE = (124, 58, 237)


def gradient(n):
    g = Image.new('RGB', (n, n))
    px = g.load()
    for y in range(n):
        for x in range(n):
            t = (x + y) / (2 * n - 2)
            px[x, y] = (int(124 - 118 * t), int(58 + 124 * t), int(237 - 25 * t))
    return g


def bubble(img, k):
    n = img.size[0]
    d = ImageDraw.Draw(img)
    f = n / 512 * k
    c = n / 2
    P = lambda x, y: (c + (x - 256) * f, c + (y - 256) * f)
    d.ellipse([*P(96, 96), *P(416, 352)], fill='white')
    d.polygon([P(150, 330), P(136, 420), P(230, 372)], fill='white')
    w = max(2, int(34 * f))
    pts = [P(194, 192), P(256, 308), P(318, 192)]
    d.line(pts, fill=PURPLE, width=w, joint='curve')
    for q in pts:
        d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=PURPLE)


def legacy(n, round_):
    big = n * 4
    im = gradient(big).convert('RGBA')
    bubble(im, 1.0)
    mask = Image.new('L', (big, big), 0)
    md = ImageDraw.Draw(mask)
    if round_:
        md.ellipse([0, 0, big - 1, big - 1], fill=255)
    else:
        md.rounded_rectangle([0, 0, big - 1, big - 1], radius=int(big * 0.22), fill=255)
    im.putalpha(mask)
    return im.resize((n, n), Image.LANCZOS)


def foreground(n):
    im = Image.new('RGBA', (n * 2, n * 2), (0, 0, 0, 0))
    bubble(im, 0.9)
    return im.resize((n, n), Image.LANCZOS)


for d, n in LEGACY.items():
    folder = os.path.join(RES, 'mipmap-' + d)
    os.makedirs(folder, exist_ok=True)
    for f in glob.glob(os.path.join(folder, 'ic_launcher*.webp')):
        os.remove(f)
    legacy(n, False).save(os.path.join(folder, 'ic_launcher.png'))
    legacy(n, True).save(os.path.join(folder, 'ic_launcher_round.png'))
    foreground(FORE[d]).save(os.path.join(folder, 'ic_launcher_foreground.png'))

os.makedirs(os.path.join(RES, 'values'), exist_ok=True)
open(os.path.join(RES, 'values', 'ic_launcher_background.xml'), 'w').write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#7C3AED</color>\n</resources>\n')
print('launcher icons written')

import wave, math
os.makedirs(os.path.join(RES, 'raw'), exist_ok=True)
SR = 22050
buf = [0.0] * int(SR * 0.7)
for f, start in ((880, 0.0), (1318, 0.14)):
    for i in range(int(SR * 0.45)):
        t = i / SR
        env = min(1.0, t / 0.015) * math.exp(-7 * t)
        j = int((start + t) * SR)
        if j < len(buf):
            buf[j] += 0.45 * env * math.sin(2 * math.pi * f * t)
with wave.open(os.path.join(RES, 'raw', 'vtext_msg.wav'), 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(int(max(-1, min(1, x)) * 32000).to_bytes(2, 'little', signed=True) for x in buf))
print('notification sound written')
