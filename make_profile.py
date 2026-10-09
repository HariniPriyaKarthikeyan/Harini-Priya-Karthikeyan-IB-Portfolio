"""Generate a branded placeholder profile photo (assets/profile.jpg).

Creates a 600x600 gradient avatar with an 'HP' monogram and a
'Replace with your photo' hint so the student can swap it easily.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W = H = 600
img = Image.new("RGB", (W, H), "#2F80ED")
draw = ImageDraw.Draw(img)

# --- Diagonal tri-gradient background (blue -> purple -> pink) ---
stops = [(47, 128, 237), (139, 92, 246), (236, 72, 153)]
for y in range(H):
    for x in range(0, W, 1):
        t = (x + y) / (W + H)  # 0..1 diagonal position
        if t < 0.5:
            f = t / 0.5
            c = tuple(int(stops[0][i] + (stops[1][i] - stops[0][i]) * f) for i in range(3))
        else:
            f = (t - 0.5) / 0.5
            c = tuple(int(stops[1][i] + (stops[2][i] - stops[1][i]) * f) for i in range(3))
        draw.point((x, y), fill=c)

# --- Soft radial highlight ---
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for r in range(260, 0, -6):
    a = int(30 * (1 - r / 260))
    od.ellipse([150 - r, 120 - r, 150 + r, 120 + r], fill=(255, 255, 255, a))
img = Image.alpha_composite(img.convert("RGBA"), overlay)

# --- Monogram ---
draw = ImageDraw.Draw(img)


def load_font(size):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


mono = load_font(240)
text = "HP"
bbox = draw.textbbox((0, 0), text, font=mono)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((W - tw) / 2 - bbox[0], (H - th) / 2 - bbox[1] - 40), text, font=mono, fill=(255, 255, 255, 255))

# --- Hint text ---
hint = load_font(30)
htext = "Replace with your photo"
hb = draw.textbbox((0, 0), htext, font=hint)
hw = hb[2] - hb[0]
draw.text(((W - hw) / 2, H - 120), htext, font=hint, fill=(255, 255, 255, 220))

Path("assets").mkdir(exist_ok=True)
img.convert("RGB").save("assets/profile.jpg", "JPEG", quality=90)
print("Saved assets/profile.jpg", img.size)
