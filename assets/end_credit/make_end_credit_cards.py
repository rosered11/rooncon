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

    def wrap(text, max_w=W - 120):
        # ตัดบรรทัดที่ช่องว่างเมื่อข้อความกว้างเกินการ์ด (ชื่อเปเปอร์ยาว ๆ เคยล้นขอบ — คลิป 010)
        lines, cur = [], ""
        for word in text.split(" "):
            test = f"{cur} {word}".strip()
            if cur and d.textbbox((0, 0), test, font=item_font)[2] > max_w:
                lines.append(cur); cur = word
            else:
                cur = test
        return lines + [cur]

    y = 240
    for c in citations:
        for line in wrap(c["authors"]) + (wrap(c["title"]) if c.get("title") else []):
            center_text(d, line, item_font, y, fill=DARK)
            y += 44
        y += 16  # ช่องว่างระหว่างรายการ

    img.save(out_path, quality=95)
    print(f"บันทึกการ์ด SOURCES ที่ {out_path}")


def make_thanks_card(out_path, handle="@ROONCON"):
    """การ์ด THANK YOU — เลย์เอาต์ปรับ 2026-09-23 ให้รองรับ YouTube end screen

    ครึ่งบนของเฟรม (y < 590) และขอบซ้าย/ขวา (x < 690 / x > 1230) ถูกเว้นว่างไว้
    โดยตั้งใจ สำหรับวางการ์ดวิดีโอของ end screen 2 ใบโดยไม่บังข้อความหรือตัวละคร
    เนื้อหาทั้งหมดถูกบีบมาอยู่ในคอลัมน์กลาง-ล่าง
    """
    img, d, horizon_y = base_card(WHITE, TEAL, horizon_frac=0.52)
    thank_font = ImageFont.truetype(FONT_BOLD, 60)
    sub_font = ImageFont.truetype(FONT_BOLD, 44)
    handle_font = ImageFont.truetype(FONT_REG, 36)

    center_text(d, "THANK YOU FOR WATCHING", thank_font, 600, fill=DARK)

    S = 0.68                      # ย่อตัวละคร/กระดิ่งให้พอดีแถบล่าง
    w = lambda n: max(3, round(n * S))
    def box(cx, cy, x0, y0, x1, y1):
        return [cx + x0 * S, cy + y0 * S, cx + x1 * S, cy + y1 * S]
    def seg(cx, cy, x0, y0, x1, y1):
        return [(cx + x0 * S, cy + y0 * S), (cx + x1 * S, cy + y1 * S)]

    # @you สติ๊กฟิกเกอร์โบกมือ ตาม Character Bible (เสื้อเขียวหม่น ผมน้ำตาลหม่น)
    cx, cy = W // 2 - 140, 815
    d.ellipse(box(cx, cy, -35, -160, 35, -90), outline=DARK, width=w(6))
    d.ellipse(box(cx, cy, -18, -135, -6, -123), outline=DARK, width=w(4))
    d.ellipse(box(cx, cy, 6, -135, 18, -123), outline=DARK, width=w(4))
    d.line(seg(cx, cy, -18, -142, -6, -140), fill=DARK, width=w(4))
    d.line(seg(cx, cy, 6, -140, 18, -142), fill=DARK, width=w(4))
    d.line(seg(cx, cy, 0, -90, 0, 40), fill=DARK, width=w(6))
    d.polygon([(cx - 30 * S, cy - 60 * S), (cx + 30 * S, cy - 60 * S),
               (cx + 22 * S, cy + 10 * S), (cx - 22 * S, cy + 10 * S)],
              fill=TEAL, outline=DARK)
    d.line(seg(cx, cy, 0, -70, -55, -130), fill=DARK, width=w(6))
    d.line(seg(cx, cy, 0, -50, 45, -10), fill=DARK, width=w(6))
    d.line(seg(cx, cy, 0, 40, -25, 130), fill=DARK, width=w(6))
    d.line(seg(cx, cy, 0, 40, 25, 130), fill=DARK, width=w(6))
    d.pieslice(box(cx, cy, -38, -165, 38, -110), 180, 360, fill=BROWN)

    # ไอคอนกระดิ่ง subscribe
    bx, by = W // 2 + 140, 790
    d.polygon([(bx - 45 * S, by + 50 * S), (bx + 45 * S, by + 50 * S),
               (bx + 30 * S, by - 30 * S), (bx - 30 * S, by - 30 * S)],
              outline=DARK, width=w(6))
    d.ellipse(box(bx, by, -12, -55, 12, -30), outline=DARK, width=w(6))
    d.ellipse(box(bx, by, -8, 50, 8, 68), fill=DARK)

    center_text(d, "SUBSCRIBE", sub_font, 935, fill=DARK)
    center_text(d, handle, handle_font, 1000, fill=DARK)

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
