# ภาพ

## ⚠️ บทเรียน: images.md เคยเพี้ยนไปจาก Blueprint V4 — ห้ามพลาดซ้ำ

พบ 2026-08-08 ตอนทำคลิปที่สอง: ไฟล์นี้เคยเขียนไว้ว่า "พื้นหลังสีเรียบสีเดียว" ซึ่ง**ผิด** — Blueprint V4 (`Cartoon_Storytelling_Blueprint_V4.md` ที่ root ของ repo) กำหนดพื้นหลังเป็น 45% ขาว + 55% สีหม่นแบ่งด้วยเส้นขอบฟ้า ไม่ใช่สีเดียวล้วน ผลคือ Flow gen ภาพผิดสไตล์ไปหลาย batch ก่อนจับได้

**และไม่เคยมี Character Bible ในโปรเจกต์เลยตั้งแต่ต้น** มีแต่ชื่อแท็ก `@you @ancestor` ไม่มีคำบรรยายรูปลักษณ์ผูกไว้ — โมเดลเลยตีความหน้าตาใหม่ทุกครั้งที่เจอแท็ก ทำให้ตัวละคร "ไม่ล็อก"

**กฎจากนี้ไป:** ก่อนเริ่ม batch ภาพทุกครั้ง **ต้องเปิด `Cartoon_Storytelling_Blueprint_V4.md` เทียบกับ Style Bible/Character Bible ด้านล่างนี้ก่อนเสมอ** ถ้าสองไฟล์ขัดกัน ให้ blueprint ชนะ แล้วแก้ไฟล์นี้ให้ตรง อย่าเชื่อ session ก่อนหน้าเฉย ๆ

## Style Bible — หัวใจ (ตรงกับ Blueprint V4 STAGE 6)

flat vector stick-figure illustration
- เส้น: บาง–กลาง น้ำหนักคงที่ แบบปากกาหมึก (ห้ามเส้นหนาแบบมาร์กเกอร์)
- พื้นหลัง: **45% ขาว/สว่าง + 55% สีหม่นเต็มเฟรม แบ่งด้วยเส้นขอบฟ้า** — ไม่ใช่สีเรียบสีเดียวทั้งภาพ
- พาเลตต์หม่นเอิร์ธโทนเท่านั้น: `#FCFCFC #B4E4CC #E4CC9C #B4E4E4 #9CCCE4 #549C54 #B46C54 #E46C24 #846CCC #9C6C3C #CCCCCC #9C9C9C #6C6C6C` · แดง `#D94040` สำหรับตัวเลขบนภาพเท่านั้น
- ดวงตาตัวละคร: วงกลมมีขอบ + รูม่านตา + คิ้วเส้นเดียว / ดวงตาสัตว์: วงกลมมีขอบ + รูม่านตา (ไม่มีคิ้ว)
- สัตว์มีหู/หนวด/หาง/สีหน้า แต่ยังเป็นทรงเรียบ ไม่มีเทกซ์เจอร์ขน/ขนนก
- สิ่งปลูกสร้างใช้มุม isometric ได้ ตัวละครกับสัตว์ต้องแบน/หน้าตรงเสมอ
- ข้อความบนภาพ: ALL CAPS ภาษาอังกฤษเท่านั้น สีดำเป็นหลัก แดงเฉพาะตัวเลข ห้ามมีข้อความไทยบนภาพเด็ดขาด

## Character Bible — ล็อกรูปลักษณ์ (ใช้ทุกคลิปที่มีตัวละครเหล่านี้)

**@you** (ตัวเอก "คุณ" — ตัวละครหลักของช่อง ควรใช้ดีไซน์เดียวกันทุกคลิป)
สติ๊กฟิกเกอร์ เส้นหมึกบาง เพศไม่ระบุชัด · เสื้อสีเรียบเขียวหม่น `#B4E4CC` ไม่มีรอยพับ · ผมทรงเรียบสีน้ำตาลหม่น `#9C6C3C` ไม่มีเส้นผม · ตา: วงกลมมีขอบ+รูม่านตา+คิ้วเส้นเดียว (จุดเดียวที่มีรายละเอียดหน้า)

**@ancestor** (บรรพบุรุษยุคหิน — callback วิวัฒนาการ ใช้ซ้ำได้หลายคลิป)
โครงร่าง/เส้นแบบเดียวกับ @you · ห่มหนังสัตว์สีน้ำตาลหม่น `#9C6C3C` ทรงเรียบไม่มีรอยพับ · ผมรุงรังกว่า @you (ก้อนสีเข้มทึบ ไม่มีเส้นผม) กันสับสนตอนเห็นในเฟรมเดียวกัน · ตาแบบเดียวกับ @you

**@dolphin** (โลมาปากขวด — สัญลักษณ์ unihemispheric sleep เฉพาะคลิปนี้)
ทรงตอร์ปิโดเรียบ สีฟ้าอมเขียวหม่น `#9CCCE4` เส้นขอบบาง · ตาวงกลมมีขอบ+รูม่านตา (ไม่มีคิ้ว) · ครีบหลัง+หางแบนเรียบ · **เฉพาะช็อตที่อธิบายการหลับครึ่งสมองเท่านั้น** ให้ลำตัวครึ่งหนึ่งเป็นโทนเข้มกว่าเล็กน้อยแทน "ซีกที่หลับ" นอกนั้นสีเดียวสม่ำเสมอ

**@duck** (เป็ดแมลลาร์ด — สัญลักษณ์ risk-based half-sleep เฉพาะคลิปนี้)
ทรงกลมเรียบ ลำตัวสีน้ำตาลอ่อนหม่น `#E4CC9C` ปากส้มหม่น `#E46C24` แถบหัวเขียวหม่น `#549C54` (สัญลักษณ์เป็ดตัวผู้) ไม่มีลายขนนก · ตาวงกลมมีขอบ+รูม่านตา · หางทรงสามเหลี่ยมแบน

## บทเรียน: คำที่เปิดช่องให้โมเดลไประบายสี

สองบรรทัดนี้ทำให้ **1 ใน 3 ของภาพหลุดกรอบ** กลายเป็นภาพวาดมีเทกซ์เจอร์:

```
- Slight paper grain over flat color areas
- Occasional light tonal shading inside objects
```

คำว่า *grain* *shading* *texture* คือใบอนุญาต พอเจอคำบรรยายฉากอย่าง savanna หรือ highway มันจะวาดเต็มรูปแบบ **ลบทิ้ง** — บทเรียนนี้ยังใช้ได้แม้พื้นหลังจะมีสองโซนตาม V4 ก็ตาม เพราะแต่ละโซนยังต้องเป็นสีเรียบ ไม่ใช่ภาพวาดมีพื้นผิว

**วันที่:** 2026-08-06

## FORBIDDEN ที่ต้องมี

```
- Painted or illustrated backgrounds within each flat-color zone
- Grass texture, cloud shading, ground detail, atmospheric perspective
- Realistic humans — every person is a STICK FIGURE with no exceptions
- Muscles, clothing folds, hair strands, teeth, nose shading
- Gradients, drop shadows, glows, textures of any kind
- Thai text rendered anywhere in the image
- NEVER render @tags, filenames, or shot numbers as visible text in the image
```

## [RULES] ที่ต้องมีทุก batch (นอกเหนือจาก FORBIDDEN ด้านบน)

```
- Keep character appearance IDENTICAL across all shots — follow CHARACTER BIBLE exactly
- On-screen text allowed ONLY where written in the shot line, ALL CAPS English
- Aspect ratio 16:9 for ALL images, highest resolution available
- Muted palette only — no saturated primaries, no thick marker lines
```

## ย้ำสไตล์ท้ายทุกบรรทัด shot

```
| Style: flat vector stick-figure, thin consistent ink line, muted earth palette, background split by horizon line (NOT single solid color) | Characters per CHARACTER BIBLE
```

ย้ำทุกช็อตกัน drift ได้ดีกว่าเขียนไว้ครั้งเดียวข้างบน

## gen ทีละ 40–50 ใบ

วาง Style Bible ใหม่ทุก batch อย่ายิง 221 ใบรวดเดียว ยิ่งยาวยิ่งลืม

## บทเรียน: OCR เชื่อไม่ได้

ตรวจ 221 ใบ OCR พลาดครบสามแบบในรอบเดียว:

- **แจ้งขาด 3 ใบ** — SHOT 065, 066, 134 มีข้อความชัดแต่ไม่จับ
- **แจ้งผิดตัว 1 ใบ** — บอก 157 จริงคือ 158
- **แจ้งเกิน 2 ใบ** — SHOT 200, 201 อ่านหนวดเคราเป็นตัวอักษร

**ต้องเปิดดู contact sheet ด้วยตาทุกใบ**

**วันที่:** 2026-08-06

## Google Flow ตั้งชื่อไฟล์เองบ่อย

รอบล่าสุด 32 ใบจาก 221 ได้ชื่อแบบ `Chunky_monkey_sitting_forward.jpeg`
ต้องจับคู่กลับเข้าเลข SHOT ด้วยมือ **และเปิดดูยืนยันทุกใบ** — เคยมีคู่ที่ชื่อกำกวมจนสลับกัน (SHOT 046 ↔ 047)

## กฎเรื่อง @tag ช่วยได้แต่ไม่หมด

ก่อนใส่กฎ หลุด 28/221 · หลังใส่กฎ หลุด 9/221 — ยังต้อง QC อยู่ดี

## ลิขสิทธิ์

ภาพจาก Google Flow มี C2PA ลงนามโดย Google LLC · ไม่ใช่โมเดล pre-GA · ไม่มีลายน้ำ = ใช้เชิงพาณิชย์ได้
**ถ้าเจอลายน้ำ ห้ามครอปทิ้ง** ให้อัปเกรดแพลนแทน
