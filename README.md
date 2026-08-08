# rooncon

ช่อง YouTube สารคดีสั้นภาษาไทย — การ์ตูนสติ๊กฟิกเกอร์ 8–10 นาที เรื่องประวัติศาสตร์มนุษย์ วิวัฒนาการ และจิตวิทยา

## เริ่มใช้งาน

```bash
git clone git@github.com:rosered11/rooncon.git
cd rooncon
brew install ffmpeg tesseract
claude
```

Claude Code จะโหลด `CLAUDE.md` · skill · agent · และความจำใน `.claude/memory/` ให้เองทั้งหมด ไม่ต้องตั้งค่าอะไรเพิ่ม

## โครงสร้าง

```
CLAUDE.md                  กฎระดับโปรเจกต์ + กฎ memory
.claude/
  skills/                  วิธีทำงานแต่ละขั้น Claude หยิบเองอัตโนมัติ
    audio-master/          มาสเตอร์เสียงให้ได้ -14 LUFS
    timecode-builder/      จับคู่ภาพกับเสียง + ซับ + จุด mid-roll
    image-qc/              ตรวจภาพก่อนเข้าไทม์ไลน์
  agents/                  subagent ที่มี context แยก
    video-audio.md
    video-timecode.md
    video-imageqc.md
  memory/                  ความจำร่วมของทีม ← commit ทุกครั้ง
  settings.json            สิทธิ์ + กันเขียน memory ผิดที่
```

## กฎที่สำคัญที่สุด

**ความจำทั้งหมดอยู่ใน `.claude/memory/` ของ repo นี้เท่านั้น** ห้ามเขียนลง `~/.claude/` เพราะทีมจะไม่เห็นและหายเมื่อเปลี่ยนเครื่อง

รายละเอียดอยู่ใน `CLAUDE.md` และ `.claude/memory/README.md`

## Pipeline

```
หัวข้อ → บท → เสียง (ElevenLabs) → มาสเตอร์เสียง [audio-master]
→ ถอด SRT (SayToWords) → Timecode Map + ซับ [timecode-builder]
→ gen ภาพ (Google Flow) → QC ภาพ [image-qc]
→ ตัดต่อ (CapCut) → metadata → อัปโหลด
```
