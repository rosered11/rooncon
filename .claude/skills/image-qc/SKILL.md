---
name: "image-qc"
description: "Quality-check a batch of AI-generated images before they go into a video — verify count, filenames, unwanted baked-in text, watermarks, metadata, and style consistency. Use when the user has downloaded images from Google Flow, Midjourney, or similar and wants them checked or renamed before editing."
---

# Image QC — ตรวจภาพชุดใหญ่ก่อนเอาไปตัดต่อ

ตรวจ 6 อย่างกับโฟลเดอร์ภาพที่ได้จาก AI แล้วเปลี่ยนชื่อให้ตรงกับ Timecode Map

## กฎเหล็กข้อเดียว

> **OCR เชื่อไม่ได้ ต้องเปิดดูด้วยตาเสมอ**

จากการตรวจจริง 221 ภาพ OCR พลาดครบทั้งสามแบบในรอบเดียว — **แจ้งขาด 3 ใบ** (มีข้อความชัดเจนแต่ไม่จับ เพราะอยู่ในลูกโป่งความคิดขนาดเล็ก) · **แจ้งผิดตัว 1 ใบ** (บอกว่าอยู่ภาพ 157 แต่จริงคือ 158) · **แจ้งเกิน 2 ใบ** (อ่านเส้นหนวดเคราเป็นตัวอักษร)

ใช้ OCR เป็นตัวคัดกรองหยาบ แล้วสร้าง contact sheet ให้คนดูยืนยันเสมอ

## ขั้นที่ 1 — นับและจับคู่เลขช็อต

```python
import os, re
bynum={}; noname=[]
for f in os.listdir(SRC):
    m=re.search(r'_SHOT_(\d{3})_', f)
    if m: bynum[int(m.group(1))]=f
    else: noname.append(f)
missing=[i for i in range(1,N+1) if i not in bynum]
```

**เครื่องมือ AI มักไม่ทำตามคำสั่งเรื่องชื่อไฟล์** — รอบจริงเจอ **32 ใบจาก 221** ที่ Flow ตั้งชื่อเองตามเนื้อภาพ เช่น `Chunky_monkey_sitting_forward.jpeg`

จับคู่ไฟล์เหล่านั้นกลับเข้าเลขช็อตโดยเทียบชื่อกับคำบรรยายใน shot list **แล้วต้องเปิดดูยืนยันทุกใบ** — รอบจริงมีคู่หนึ่งที่ชื่อกำกวมจนสลับกัน (`Stick_figure_chain_illustration` กับ `Stick_figures_on_white_background`)

## ขั้นที่ 2 — สแกน OCR หาข้อความที่ไม่ควรมี

```bash
cd IMAGE_DIR
for f in *.jpeg; do
  t=$(tesseract "$f" - --psm 11 2>/dev/null | tr '\n' ' ' | tr -s ' ')
  echo "$f :: $t"
done > /tmp/ocr.txt
```

ค้นหา `@[A-Za-z]{3,}` · `SHOT \d+` · รูปแบบชื่อไฟล์ `\d\d[_ ]\d\d[_ ]\d\d`

ถ้าไม่มี tesseract: `apt-get install -y tesseract-ocr`

## ขั้นที่ 3 — เปิดดูด้วยตา (ห้ามข้าม)

สร้าง contact sheet พร้อมเลขช็อตติดบนภาพ ครั้งละ 20 ภาพ:

```bash
ffmpeg -y -v error -i IMG \
  -vf "scale=340:-1,drawbox=x=0:y=0:w=64:h=30:color=black@0.8:t=fill,drawtext=fontfile=FONT:text='001':x=6:y=3:fontsize=22:fontcolor=yellow" \
  /tmp/s0.png
# แล้ว hstack ทีละ 5 → vstack 4 แถว
```

ไล่ดูทุกแผ่นแล้วเทียบกับคำบรรยายใน shot list ทีละช็อต ตรวจสามอย่างพร้อมกัน — **เนื้อหาตรงกับที่สั่งไหม** · **มีข้อความหลุดไหม** · **วัตถุหลักอยู่ตรงตำแหน่งที่ตั้งใจไหม**

ข้อสุดท้ายเจอจริงจากคลิป 003: วัตถุ/ตัวละครหลักบางภาพหลุดไปกองอยู่มุมใดมุมหนึ่งของเฟรมแทนที่จะอยู่กลางจอ ทั้งที่ prompt ไม่ได้ตั้งใจให้จัดองค์ประกอบแบบนั้น — เกิดเพราะ prompt ส่วนใหญ่บอกแค่ "มีอะไรในภาพ" ไม่ได้ระบุตำแหน่ง โมเดลเลยตัดสินใจเอง ถ้าไม่ได้ตั้งใจให้ชิดขอบ (เช่นเว้นที่ใส่ป้าย) ให้นับเป็นต้อง gen ใหม่เหมือนปัญหาอื่น

## ขั้นที่ 4 — ลายน้ำ

ครอปมุมล่างขวาที่ความละเอียดเต็มจากภาพต้น กลาง ท้าย แล้วเปิดดู

```bash
ffmpeg -y -v error -i IMG -vf "crop=400:120:960:640" /tmp/corner.png
```

**ถ้าเจอลายน้ำ ห้ามครอปทิ้ง** เพราะผิดเงื่อนไขผู้ให้บริการและทำให้สิทธิ์ใช้งานทั้งชุดมีปัญหา ให้อัปเกรดแพลนแทน

## ขั้นที่ 5 — metadata

```bash
strings -n 4 IMG | grep -iE "c2pa|synthid|google|Created by|pre-GA|experimental" | head -10
```

ดู 2 อย่าง — **ใครเป็นคนเซ็น** (ยืนยันแหล่งที่มา) และ **เป็นโมเดล pre-GA หรือ experimental ไหม** เพราะสิทธิ์เชิงพาณิชย์มักไม่ครอบคลุมโมเดลที่ยังไม่ GA

## ขั้นที่ 6 — ความละเอียด

```bash
for f in *; do ffprobe -v error -show_entries stream=width,height -of csv=p=0 "$f"; done | sort | uniq -c
```

ต่ำกว่า 1920×1080 = ต้องอัปสเกลตอนตัดต่อ บอกผู้ใช้ให้รู้ตัวก่อน

## เปลี่ยนชื่อไฟล์

ใช้ **hard link** ไม่ใช่ copy — ไม่กินพื้นที่เพิ่มและไม่แตะไฟล์ต้นฉบับ ถ้าผลลัพธ์ผิดก็ลบโฟลเดอร์ใหม่ทิ้งได้เลย

```python
os.makedirs(DST, exist_ok=True)
for i in range(1, N+1):
    os.link(os.path.join(SRC, bynum[i]), os.path.join(DST, new_names[i-1]))
```

**สร้างโฟลเดอร์ใหม่เสมอ อย่าเขียนทับของเดิม** — ถ้าเจอว่าจับคู่ผิดทีหลังจะได้ย้อนได้

## รูปแบบรายงาน

แยกเป็น **ผ่าน** / **แก้ให้แล้ว** / **ต้อง gen ใหม่** ให้ชัด และในกลุ่มสุดท้ายต้องระบุ **เลขช็อต · ชื่อไฟล์ · เวลาในคลิป · ข้อความที่หลุด** เพื่อให้ผู้ใช้ gen ซ้ำเฉพาะที่จำเป็น ไม่ต้องทำใหม่ทั้งชุด

## ถ้าเจอสไตล์หลุดกรอบเยอะ

อาการ: ภาพที่มีฉากหลังกลายเป็นภาพวาดระบายสีมีเทกซ์เจอร์ ส่วนภาพพื้นขาวออกมาถูก · ตัวละครเดียวกันหน้าตาไม่เหมือนกันข้ามช็อต

**สาเหตุมักอยู่ใน style bible เอง** คำอย่าง *paper grain*, *tonal shading*, *slight texture* คือใบอนุญาตให้โมเดลไประบายสี พอเจอคำบรรยายฉากอย่าง "savanna" หรือ "highway" มันจะวาดเป็นภาพประกอบเต็มรูปแบบ

แนะนำผู้ใช้ให้แก้ 3 อย่าง:

1. **ลบคำที่เปิดช่อง** — grain, shading, texture ออกจาก style bible
2. **เพิ่มข้อห้ามให้ชัด** — `Painted or illustrated backgrounds FORBIDDEN — backgrounds are FLAT COLOR ONLY` · `Realistic humans FORBIDDEN — every person is a STICK FIGURE with no exceptions`
3. **ย้ำสไตล์ท้ายทุกบรรทัด shot** — `| Style: flat vector, single flat color background, stick figures only` การย้ำทุกช็อตกัน drift ได้ดีกว่าเขียนไว้ครั้งเดียวข้างบน

และแนะนำให้ **gen ทีละ 40–50 ภาพ แล้ววาง style bible ใหม่ทุกครั้ง** อย่ายิงรวดเดียวเป็นร้อยใบ เพราะโมเดลจะลืม style มากขึ้นเรื่อย ๆ ตามความยาว batch

## กฎที่ควรมีใน prompt เสมอ

```
- NEVER render @tags, filenames, or shot numbers as visible text in the image
- The filename is the FIRST token of each shot line. Output it EXACTLY.
- Do NOT invent descriptive filenames. Do NOT rename based on image content.
- If you cannot use the given filename, still keep the SHOT number in the name.
```

ใส่กฎพวกนี้แล้วยังต้อง QC อยู่ดี รอบจริงใส่กฎแล้วยังหลุด 9 ใบจาก 221 แต่ดีขึ้นจาก 28 ใบในรอบที่ไม่มีกฎ

