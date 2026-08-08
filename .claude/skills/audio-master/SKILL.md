---
name: "audio-master"
description: "Master a narration/voiceover audio file to YouTube loudness standard (-14 LUFS, LRA 2-3, no clipping). Use when the user has a TTS or recorded voiceover WAV/MP3 and wants it ready for video, or asks to fix audio that sounds quiet, flat, uneven, or distorted."
---

# Audio Master — เสียงพากย์ให้ได้มาตรฐาน YouTube

มาสเตอร์ไฟล์เสียงพากย์ให้ได้ค่าเป้าหมายที่ YouTube ใช้ ทำงานด้วย ffmpeg ทั้งหมด ไม่ต้องเปิดโปรแกรมตัดต่อ

## ค่าเป้าหมาย (ต้องผ่านทุกข้อ)

| ตัวชี้วัด | เป้าหมาย | ทำไม |
|---|---|---|
| Integrated loudness | **-14 ถึง -16 LUFS** | YouTube หรี่คลิปที่ดังเกินลงมาที่ ~-14 แต่**ไม่ดันคลิปที่เบาให้ดังขึ้น** ส่งไปเบา = เสียเปรียบตลอดไป |
| Loudness range (LRA) | **2–3 LU** | คลิปสารคดีระดับมืออาชีพวัดได้ 1.9–2.0 · ไฟล์ดิบจาก TTS มักอยู่ที่ 3.5–5.5 |
| True peak | **ไม่เกิน -1.0 dBFS** | กันเสียงแตกหลังบีบอัดเป็นวิดีโอ |
| แซมเปิลชนเพดาน | **0** | ถ้ามีแปลว่าเสียงแตกจริงและแก้ไม่ได้แล้ว |

## ขั้นตอน

### 1. วัดค่าไฟล์ต้นทางก่อนเสมอ

```bash
ffmpeg -hide_banner -i INPUT -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I:|LRA:|Peak"
```

จด **LRA** ไว้ เพราะเป็นตัวเลือกว่าจะบีบอัดกี่ชั้น

### 2. เลือกความแรงของ compressor ตาม LRA ที่วัดได้

**LRA > 4.5 → บีบสองชั้น**
```
acompressor=threshold=-28dB:ratio=5:attack=20:release=250,acompressor=threshold=-16dB:ratio=3:attack=5:release=120
```

**LRA 3–4.5 → บีบชั้นเดียว**
```
acompressor=threshold=-22dB:ratio=4:attack=20:release=250
```

**LRA < 3 → ข้าม compressor ไปเลย**

> แยกสองชั้นเบา ๆ ได้ผลดีกว่าชั้นเดียวแรง ๆ — ทดสอบแล้วชั้นเดียวได้ LRA 4.2 แต่สองชั้นได้ 2.7 และฟังเป็นธรรมชาติกว่า

### 3. รันทั้งเชน

```bash
CHAIN="<compressor ที่เลือกจากข้อ 2>"
ffmpeg -y -v error -i INPUT -af "$CHAIN" -ar 44100 -ac 1 /tmp/_comp.wav

ffmpeg -y -v error -i /tmp/_comp.wav \
  -af "loudnorm=I=-13.2:TP=-1.2:LRA=3,alimiter=limit=0.891:attack=5:release=50:level=disabled" \
  -ar 44100 -ac 1 -c:a pcm_s16le OUTPUT.wav
```

**สองจุดที่ห้ามพลาด**

- `level=disabled` ใน alimiter — ถ้าไม่ใส่ ตัวลิมิตจะดันความดังกลับขึ้นมาจน peak ทะลุอีก
- ตั้ง loudnorm ที่ **-13.2 ไม่ใช่ -14** เพราะลิมิตเตอร์จะดึงลงอีกราว 1 dB ผลสุดท้ายจะลงที่ -14.x พอดี

### 4. ตรวจผล — ต้องผ่านทั้งสองคำสั่ง

```bash
ffmpeg -hide_banner -i OUTPUT.wav -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I:|LRA:|Peak"

python3 -c "
import numpy as np, wave, sys
w=wave.open('OUTPUT.wav'); a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16)
clip=int(((a>=32767)|(a<=-32768)).sum())
print('แซมเปิลชนเพดาน:', clip, '<- ต้องเป็น 0')
"
```

ถ้า **แซมเปิลชนเพดาน > 0** หรือ **peak เกิน -1.0** ให้ลด `I=` ลง 0.5 แล้วรันข้อ 3 ใหม่ อย่าแก้ด้วยการลดเสียงทั้งไฟล์

## ตัดช่วงเงียบให้กระชับ (ทำเมื่อฟังแล้วรู้สึกอืด)

TTS บางตัวโดยเฉพาะโหมด long-form ใส่ช่วงหยุดยาวเกินจริง วัดก่อน:

```bash
ffmpeg -y -v error -i INPUT -ac 1 -ar 16000 /tmp/_s.wav
ffmpeg -hide_banner -i /tmp/_s.wav -af "silencedetect=noise=-40dB:d=0.15" -f null - 2>&1 \
  | grep -o "silence_start: [0-9.]*\|silence_end: [0-9.]*" | sed 's/silence_//' > /tmp/_sil.txt
```

**เกณฑ์:** ช่วงหยุดเฉลี่ยควรอยู่ราว **0.33–0.40 วินาที** และยาวสุดไม่เกิน **0.95 วินาที** ถ้าเกินมากให้ตัด

```python
import re, numpy as np, wave
SR=44100; CAP_NORMAL=0.35; CAP_LONG=0.90; LONG=1.00; EDGE=0.06; RAMP=int(0.004*SR)
# อ่าน /tmp/_sil.txt เป็นคู่ start/end แล้วสำหรับแต่ละช่วงเงียบ
#   ถ้ายาว >= LONG  ให้เหลือ CAP_LONG   (รอยต่อบท ต้องเก็บไว้)
#   ถ้าสั้นกว่านั้น ให้เหลือ CAP_NORMAL
# ตัดออกจาก "กลาง" ช่วงเงียบ เว้นขอบข้างละ EDGE วินาที
# ใส่ fade in/out RAMP แซมเปิลทุกรอยต่อ กันเสียงป๊อก
```

**หลักการที่ห้ามลืม** — อย่าตัดช่วงหยุดทุกจุดให้เท่ากันหมด ช่วงที่ยาวเกิน 1 วินาทีคือลมหายใจที่แบ่งบทของเรื่อง ถ้าตัดเท่ากันหมดจะฟังเหมือนอ่านรวดเดียวไม่มีวรรคตอน

## กฎที่ต้องบอกผู้ใช้เสมอ

**Export เป็น WAV 16-bit ไม่ใช่ MP3** — ถ้าต้นทางเป็น MP3 อยู่แล้ว การ export เป็น MP3 อีกครั้งคือบีบอัดสองรอบ

**ห้ามกด Normalize Loudness ในโปรแกรมตัดต่อทับไฟล์นี้** — CapCut เล็งที่ประมาณ -23 LUFS จะดึงงานที่ทำมาทิ้งทั้งหมด

**ปิด Noise reduction และ Voice enhance** — เสียง TTS ไม่มี noise อยู่แล้ว เปิดแล้วเสียงบางลงเปล่า ๆ

## สิ่งที่เครื่องมือ TTS ทำให้ไม่ได้

ElevenLabs และ TTS อื่น ๆ **ไม่มี compressor ไม่มี limiter ไม่มีที่ตั้ง LUFS** ทุกแพลน ค่าที่ส่งออกมาคงที่ราว -23.5 LUFS เสมอ ขั้นตอนนี้จึงต้องทำนอกเครื่องมือ TTS เสมอ ไม่มีทางลัด

