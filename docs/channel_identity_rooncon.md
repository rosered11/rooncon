# ROONCON — Channel Identity Kit

**Channel name (display):** ROONCON
**Handle:** `@rooncon`
**อ่านว่า:** รูน-คอน
**Niche:** ประวัติศาสตร์มนุษย์ · วิวัฒนาการ · จิตวิทยา · เรื่องที่คนดูหยุดดูไม่ได้

> **หลักออกแบบข้อเดียวที่ต้องจำ:** ชื่อ Rooncon ไม่ได้ออกเสียงว่า raccoon
> ฉะนั้น **โลโก้ต้องแบกมุกทั้งหมด** แรคคูนต้องชัดจนไม่มีใครเดาผิด และต้องปรากฏคู่ wordmark เสมอ
> ห้ามใช้ wordmark เดี่ยวๆ โดยไม่มีแรคคูน จนกว่าช่องจะดังพอที่คนจำได้เอง

---

## 1. Mascot — `@roon`

เพิ่มลง Character Bible ได้เลย ใช้เป็นตัวละครในคลิปได้ด้วย ไม่ใช่แค่โลโก้

```
@roon = แรคคูนมาสคอตประจำช่อง
  - Chunky cartoon raccoon, large round head, short stubby body
  - Body & head: brown #8B5E3C flat fill, thick black outline
  - Face patch: white #FFFFFF muzzle and brow area
  - Mask: solid black band across both eyes, edge slightly jagged
  - Eyes: two white dots inside the black mask
  - Nose: small solid black triangle
  - Ears: two rounded brown triangles with white inner
  - Tail: thick, tan #C4965A with 3 solid black rings
  - Hands: small black mitten shapes, always visible

USAGE RULES:
- @roon ปรากฏเฉพาะ cold open (3 วิแรก) และ outro เท่านั้น
- ห้ามให้ @roon อยู่ในช็อตเล่าเนื้อหา จะแย่ง attention จาก @you
- ห้ามเปลี่ยนสี ห้ามเพิ่มเสื้อผ้า ห้ามเอาหน้ากากออก
```

**ทำไมต้องจำกัดการปรากฏ:** มาสคอตที่โผล่ทุกฉากจะกลายเป็นตัวเอก แต่ตัวเอกของช่องนี้คือ `@you` — คนดูต้องรู้สึกว่าเรื่องนี้เกี่ยวกับตัวเอง ไม่ใช่เกี่ยวกับแรคคูน

---

## 2. Profile Picture — 800×800 PNG

YouTube crop เป็นวงกลม และแสดงเล็กสุดที่ **24px** ในคอมเมนต์ ฉะนั้นทดสอบด้วยการย่อรูปเหลือ 24px ถ้ายังบอกได้ว่าเป็นแรคคูน = ผ่าน

### แบบ A — Head Only ⭐ แนะนำ

```
Flat 2D doodle cartoon raccoon head, front facing, centered.
Brown #8B5E3C head with white #FFFFFF muzzle, solid black bandit mask
band across the eyes, two white dot eyes inside the mask, small black
triangle nose, two rounded ears. Bold black marker outline, flat colors.
Solid orange #F5820D background filling the entire square.
No text, no gradients, no shadows, no textures. Square 1:1.
```

หัวอย่างเดียว เต็มเฟรม อ่านออกที่ 24px แน่นอน พื้นส้มทำให้เด้งออกจากพื้นขาวของ YouTube

### แบบ B — Peeking

```
Same raccoon head but only the top half visible, peeking up from the
bottom edge of the frame, both hands gripping the edge. Wide curious eyes.
Solid cobalt blue #2D5FBF background. Square 1:1, no text.
```

ตรงคอนเซปต์ช่องมาก (ความอยากรู้ที่ห้ามไม่ได้) แต่เสี่ยงอ่านยากตอนย่อเล็ก ใช้เป็นภาพโปรโมทหรือ end screen ดีกว่า

### แบบ C — Magnifier

```
Same raccoon head holding a black magnifying glass over one eye,
that eye enlarged through the lens. Solid golden yellow #F5C518
background. Square 1:1, no text.
```

สื่อ "ขุดคุ้ยหาความจริง" ชัด แต่รายละเอียดเยอะเกินสำหรับขนาดเล็ก

---

## 3. Banner — 2560×1440 PNG (ไม่เกิน 6MB)

**สำคัญ:** ข้อความและโลโก้ทั้งหมดต้องอยู่ใน safe area กลางภาพขนาด **1546×423** เท่านั้น นอกกรอบนี้จะโดนตัดบนมือถือ

```
Flat 2D doodle cartoon banner, 16:9, wide horizontal composition.
Background: solid white #FFFFFF with a grass green #3A9E3A horizontal
strip along the bottom edge as ground.
Left of center: a chunky cartoon raccoon standing upright, brown #8B5E3C
body, white muzzle, solid black bandit mask, tan #C4965A ringed tail,
one hand raised pointing right.
Center: bold ALL CAPS hand-lettered marker text "ROONCON" in solid black,
very large, slightly uneven letterforms.
Below the wordmark: smaller ALL CAPS marker text in red #D94040.
Bold black outlines everywhere, flat colors only.
ZERO gradients, ZERO shadows, ZERO textures.
```

### Tagline (ใส่ใต้ wordmark เป็นภาษาไทยตอนตัดต่อ ไม่ต้อง bake ใน AI)

เลือกหนึ่ง:

1. **เรื่องที่คุณหยุดดูไม่ได้** ← แนะนำ กว้างพอรองรับคลิปที่ไม่ใช่วิทยาศาสตร์ และ echo คลิปแรกพอดี
2. ทุกอย่างที่คุณทำ มีที่มาเสมอ
3. ความอยากรู้ที่ห้ามตัวเองไม่ได้

> กฎ 7 ของ Blueprint ห้าม bake ข้อความไทยลงภาพ AI — ให้ gen แบนเนอร์เป็นภาพเปล่ากับ wordmark อังกฤษ แล้วพิมพ์ไทยทับใน Canva/Figma ตอนท้าย

---

## 4. Watermark — 96×96 PNG พื้นโปร่งใส

หัว `@roon` อย่างเดียว ตัดพื้นออก ไม่มีตัวอักษร ตั้งให้โผล่ **ตลอดทั้งคลิป** ในการตั้งค่า Branding เพราะเป็นปุ่ม subscribe ในตัว

---

## 5. About / คำอธิบายช่อง

วาง 2 บรรทัดแรกให้ดี เพราะโชว์ในผลค้นหา:

```
คุณทำสิ่งต่างๆ ทุกวันโดยไม่เคยถามว่าทำไม

ROONCON เล่าเรื่องเบื้องหลังพฤติกรรมมนุษย์ ตั้งแต่ทุ่งหญ้าแอฟริกาเมื่อสองล้านปีก่อน
จนถึงหน้าจอที่คุณถืออยู่ตอนนี้ — ประวัติศาสตร์ วิวัฒนาการ จิตวิทยา และงานวิจัยจริง
เล่าด้วยภาษาที่ไม่ต้องมีพื้นฐานก็เข้าใจได้

คลิปใหม่ทุกสัปดาห์

ติดต่องาน: [อีเมล]
```

**Keywords ใส่ใน Settings → Channel → Keywords:**
`ประวัติศาสตร์มนุษย์, วิวัฒนาการ, จิตวิทยา, สารคดี, ความรู้, มนุษย์ยุคหิน, สมอง, พฤติกรรมมนุษย์, อธิบายง่ายๆ, human evolution, psychology`

---

## 6. เช็คลิสต์ตั้งค่าช่อง

**Customization → Branding**

- [ ] Profile picture 800×800 (ทดสอบย่อ 24px แล้วยังอ่านออก)
- [ ] Banner 2560×1440 (ข้อความอยู่ในกรอบ 1546×423)
- [ ] Watermark 96×96 พื้นโปร่งใส · ตั้งเป็น "Entire video"

**Customization → Basic info**

- [ ] Name: `ROONCON`
- [ ] Handle: `@rooncon`
- [ ] Description + keywords ตามข้อ 5
- [ ] Links: ใส่อย่างน้อย 1 (อีเมลติดต่องาน)

**Customization → Layout**

- [ ] Channel trailer สำหรับคนที่ยังไม่ subscribe → ใส่คลิปแรกไปก่อน
- [ ] Featured sections: Videos → Popular uploads

**Settings → Channel → Advanced**

- [ ] "ช่องนี้ไม่ได้ทำเพื่อเด็ก" (ระดับช่อง)
- [ ] Country: Thailand

---

## 7. ลำดับงานถัดไป

1. จอง `@rooncon` ก่อนใครทันที
2. gen เสียงสคริปต์ 9 นาที ตอน Starter active แล้ว
3. ส่ง timestamp มา → ผมทำ Timecode Map + Shot List ชุดใหม่ (~215 ช็อต)
4. gen โลโก้ + แบนเนอร์จาก prompt ข้างบน
5. OUTPUT 4 — title / description / tags / thumbnail
