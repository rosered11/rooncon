# rooncon — ช่อง YouTube สารคดีสั้นภาษาไทย

คลิปการ์ตูนสติ๊กฟิกเกอร์ความยาว 8–10 นาที เรื่องประวัติศาสตร์มนุษย์ วิวัฒนาการ และจิตวิทยา
เล่าด้วยบุรุษที่ 2 ("คุณ") ตลอดทั้งเรื่อง ห้ามใช้ "เรา" หรือ "ผม" ในบทบรรยาย

---

## 🔒 กฎเรื่อง Memory — สำคัญที่สุด อ่านก่อนทำอะไร

**agent และ skill ทุกตัวในโปรเจกต์นี้ ต้องเขียนความจำลงใน `.claude/memory/` ของโปรเจกต์นี้เท่านั้น**

| ที่อยู่ | เขียนได้ไหม | เหตุผล |
|---|---|---|
| `.claude/memory/*.md` (ในโปรเจกต์) | ✅ **ที่เดียวที่อนุญาต** | commit ขึ้น git ทีมเห็นเหมือนกันหมด |
| `CLAUDE.md` (ไฟล์นี้) | ✅ เฉพาะกฎถาวรระดับโปรเจกต์ | commit ขึ้น git |
| `~/.claude/CLAUDE.md` | ❌ **ห้าม** | อยู่แค่ในเครื่องคนเดียว ทีมไม่เห็น |
| `~/.claude/memory/` หรือ `~/.claude/*` | ❌ **ห้าม** | เหตุผลเดียวกัน |
| `CLAUDE.local.md` | ❌ **ห้าม** | ถูก gitignore ทีมไม่เห็น |

**ห้ามใช้ `/memory` หรือคำสั่งบันทึกความจำใด ๆ ที่ปลายทางเป็น user scope** ถ้าเครื่องมือถามว่าจะบันทึกที่ไหน ให้เลือก **Project** เสมอ ถ้าเลือกไม่ได้ ให้เขียนไฟล์ลง `.claude/memory/` ตรง ๆ ด้วย Write แทน

**เวลาจะบันทึกอะไร** ให้เขียนต่อท้ายไฟล์ที่ตรงหัวข้อที่สุดใน `.claude/memory/` แล้วบอกผู้ใช้ว่าเขียนไฟล์ไหนไป เพื่อให้เขา commit ได้ ไม่ต้องสร้างไฟล์ใหม่ถ้ามีไฟล์ที่ตรงอยู่แล้ว

---

## ความจำที่โหลดอัตโนมัติ

@.claude/memory/channel.md
@.claude/memory/audio.md
@.claude/memory/timecode.md
@.claude/memory/images.md
@.claude/memory/decisions.md

---

## Pipeline

```
1 หาหัวข้อ [content-research] → 2 บท → 3 เสียง (ElevenLabs) → 4 มาสเตอร์เสียง [audio-master]
→ 5 ถอด SRT (SayToWords) → 6 Timecode Map + ซับ [timecode-builder]
→ 7 gen ภาพ (Google Flow) → 8 QC ภาพ [image-qc]
→ 9 ตัดต่อ (CapCut) → 10 metadata + อัปโหลด
```

## Skill ในโปรเจกต์นี้

| Skill | ใช้ตอน | ไฟล์ |
|---|---|---|
| `content-research` | ขั้น 1 | `.claude/skills/content-research/SKILL.md` |
| `audio-master` | ขั้น 4 | `.claude/skills/audio-master/SKILL.md` |
| `timecode-builder` | ขั้น 6 | `.claude/skills/timecode-builder/SKILL.md` |
| `image-qc` | ขั้น 8 | `.claude/skills/image-qc/SKILL.md` |

## Subagent

| Agent | คู่กับ skill |
|---|---|
| `video-content` | content-research |
| `video-audio` | audio-master |
| `video-timecode` | timecode-builder |
| `video-imageqc` | image-qc |

agent มี context แยกจากบทสนทนาหลัก ต้องบอกพาธไฟล์ให้ครบทุกครั้ง

## เครื่องมือที่ต้องมีในเครื่อง

`ffmpeg` · `ffprobe` · `python3` · `tesseract` (เฉพาะ image-qc)

```bash
brew install ffmpeg tesseract
```

## กฎที่ใช้ทั้งโปรเจกต์

- ไฟล์เสียงส่งออกเป็น **WAV 16-bit 44.1kHz** เท่านั้น ไม่ใช่ MP3
- ห้ามกด Normalize Loudness ใน CapCut ทับไฟล์ที่มาสเตอร์แล้ว
- ซับและ Timecode Map ใช้ **ข้อความจากสคริปต์ต้นฉบับ** ไม่ใช่จาก ASR
- ตรวจภาพต้องเปิดดูด้วยตา OCR อย่างเดียวไม่พอ
- คลิปต้องยาวเกิน 8 นาที เพื่อให้ใส่ mid-roll ได้
