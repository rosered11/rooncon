#!/usr/bin/env python3
"""
สร้างการ์ด end credit ประจำช่อง rooncon — ใช้ซ้ำได้ทุกคลิป

การ์ด 1 "SOURCES"     — เปลี่ยนรายการอ้างอิงตามคลิป (แก้ที่ CITATIONS ด้านล่าง หรือส่งเข้ามาทาง --citations)
การ์ด 2 "THANK YOU"   — คงที่ทุกคลิป ไม่ต้องแก้ (สติ๊กฟิกเกอร์ @you โบกมือ + กระดิ่ง subscribe)

ทั้งสองการ์ดยาวใบละ 6 วินาที (รวม 12 วิ) ต่อท้ายวิดีโอ — ดู .claude/memory/decisions.md
หัวข้อ "End credit ประจำช่อง" สำหรับสเปกเต็ม (BGM ต้องดังขึ้นเป็น 40% ช่วงนี้ ต่างจาก 10% ช่วงคลิปหลัก)

วิธีใช้:
    python3 make_end_credit_cards.py \\
        --citations citations.json \\
        --out-sources /path/to/work/00X-clip-name/final_upscaled/HH_MM_SS.jpeg \\
        --out-thanks  /path/to/work/00X-clip-name/final_upscaled/HH_MM_SS.jpeg

citations.json ตัวอย่าง:
    [
      {"authors": "TAMAKI, BANG, WATANABE & SASAKI (2016) — CURRENT BIOLOGY",
       "title": "\\"NIGHT WATCH IN ONE BRAIN HEMISPHERE DURING SLEEP\\""},
      {"authors": "RATTENBORG, LIMA & AMLANER (1999) — NATURE", "title": ""}
    ]

ถ้าไม่ส่ง --citations จะใช้รายการของคลิป 002 (first-night-sleep) เป็นตัวอย่าง default
"""
import argparse
import json
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080

# พาเลตต์หม่นเอิร์ธโทน — ต้องตรงกับ Style Bible ใน .claude/memory/images.md เสมอ
TAN = (228, 204, 156)      # #E4CC9C
TEAL = (180, 228, 204)     # #B4E4CC
WHITE = (252, 252, 252)    # #FCFCFC
DARK = (60, 60, 60)        # muted dark ink
BROWN = (156, 108, 60)     # #9C6C3C

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

DEFAULT_CITATIONS = [
    {"authors": "TAMAKI, BANG, WATANABE & SASAKI (2016) — CURRENT BIOLOGY",
     "title": '"NIGHT WATCH IN ONE BRAIN HEMISPHERE DURING SLEEP"'},
    {"authors": "RATTENBORG, LIMA & AMLANER (1999) — NATURE",
     "title": '"HALF-AWAKE TO THE RISK OF PREDATION"'},
    {"authors": "LYAMIN, PRYASLOVA, KOSENKO & SIEGEL (2007) — PHYSIOLOGY & BEHAVIOR",
     "title": '"BEHAVIORAL ASPECTS OF SLEEP IN BOTTLENOSE DOLPHIN MOTHERS AND CALVES"'},
    {"authors": "AGNEW, WEBB & WILLIAMS (1966) — PSYCHOPHYSIOLOGY", "title": ""},
    {"authors": "TAMAKI & SASAKI (2019) — SURVEILLANCE DURING REM SLEEP", "title": ""},
    {"authors": "MANOACH & STICKGOLD (2016) — CURRENT BIOLOGY", "title": ""},
]


def base_card(top_color, bottom_color, horizon_frac):
    """พื้นหลังมาตรฐานของช่อง: บนสว่าง/ล่างสีหม่น แบ่งด้วยเส้นขอบฟ้า (ห้ามใช้สีเรียบสีเดียวทั้งภาพ)"""
    img = Image.new('RGB', (W, H), top_color)
    d = ImageDraw.Draw(img)
    horizon_y = int(H * horizon_frac)
    d.rectangle([0, horizon_y, W, H], fill=bottom_color)
    return img, d, horizon_y


def center_text(d, text, font, y, fill=DARK):
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    d.text(((W - w) // 2, y), text, font=font, fill=fill)


def make_sources_card(citations, out_path):
    img, d, _ = base_card(WHITE, TAN, horizon_frac=0.22)
    title_font = ImageFont.truetype(FONT_BOLD, 64)
    item_font = ImageFont.truetype(FONT_REG, 34)

    center_text(d, "SOURCES", title_font, 90, fill=DARK)

    y = 240
    for c in citations:
        center_text(d, c["authors"], item_font, y, fill=DARK)
        y += 44
        if c.get("title"):
            center_text(d, c["title"], item_font, y, fill=DARK)
            y += 44
        y += 16  # ช่องว่างระหว่างรายการ

    img.save(out_path, quality=95)
    print(f"บันทึกการ์ด SOURCES ที่ {out_path}")


def make_thanks_card(out_path, handle="@ROONCON"):
    img, d, horizon_y = base_card(WHITE, TEAL, horizon_frac=0.55)
    thank_font = ImageFont.truetype(FONT_BOLD, 72)
    sub_font = ImageFont.truetype(FONT_BOLD, 48)
    handle_font = ImageFont.truetype(FONT_REG, 40)

    center_text(d, "THANK YOU FOR WATCHING", thank_font, 110, fill=DARK)

    # @you สติ๊กฟิกเกอร์โบกมือ ตาม Character Bible (เสื้อเขียวหม่น ผมน้ำตาลหม่น)
    cx, cy = W // 2 - 220, horizon_y - 40
    d.ellipse([cx - 35, cy - 160, cx + 35, cy - 90], outline=DARK, width=6)
    d.ellipse([cx - 18, cy - 135, cx - 6, cy - 123], outline=DARK, width=4)
    d.ellipse([cx + 6, cy - 135, cx + 18, cy - 123], outline=DARK, width=4)
    d.line([cx - 18, cy - 142, cx - 6, cy - 140], fill=DARK, width=4)
    d.line([cx + 6, cy - 140, cx + 18, cy - 142], fill=DARK, width=4)
    d.line([cx, cy - 90, cx, cy + 40], fill=DARK, width=6)
    d.polygon([(cx - 30, cy - 60), (cx + 30, cy - 60), (cx + 22, cy + 10), (cx - 22, cy + 10)],
               fill=TEAL, outline=DARK)
    d.line([cx, cy - 70, cx - 55, cy - 130], fill=DARK, width=6)
    d.line([cx, cy - 50, cx + 45, cy - 10], fill=DARK, width=6)
    d.line([cx, cy + 40, cx - 25, cy + 130], fill=DARK, width=6)
    d.line([cx, cy + 40, cx + 25, cy + 130], fill=DARK, width=6)
    d.pieslice([cx - 38, cy - 165, cx + 38, cy - 110], 180, 360, fill=BROWN)

    # ไอคอนกระดิ่ง subscribe
    bx, by = W // 2 + 180, horizon_y - 90
    d.polygon([(bx - 45, by + 50), (bx + 45, by + 50), (bx + 30, by - 30), (bx - 30, by - 30)],
               outline=DARK, width=6)
    d.ellipse([bx - 12, by - 55, bx + 12, by - 30], outline=DARK, width=6)
    d.ellipse([bx - 8, by + 50, bx + 8, by + 68], fill=DARK)

    center_text(d, "SUBSCRIBE", sub_font, horizon_y + 130, fill=DARK)
    center_text(d, handle, handle_font, horizon_y + 195, fill=DARK)

    img.save(out_path, quality=95)
    print(f"บันทึกการ์ด THANK YOU ที่ {out_path}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--citations", help="path ไปยัง citations.json ของคลิปนี้ (ไม่ใส่ = ใช้ default ของคลิป 002)")
    p.add_argument("--out-sources", required=True, help="path ไฟล์ output การ์ด SOURCES เช่น work/00X/final_upscaled/HH_MM_SS.jpeg")
    p.add_argument("--out-thanks", required=True, help="path ไฟล์ output การ์ด THANK YOU")
    p.add_argument("--handle", default="@ROONCON")
    args = p.parse_args()

    citations = DEFAULT_CITATIONS
    if args.citations:
        with open(args.citations, encoding="utf-8") as f:
            citations = json.load(f)

    make_sources_card(citations, args.out_sources)
    make_thanks_card(args.out_thanks, handle=args.handle)
