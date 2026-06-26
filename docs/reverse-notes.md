# Reverse engineering notes

## Rule

Do not guess final extraction. Every parser step must produce evidence.

## Phase 1 tools

`embeddb_info.py` is intentionally conservative. It does not claim to extract final files. It produces:

- byte-level metadata
- discovered ASCII / GBK strings
- likely resource names
- offsets of known markers
- JSON evidence for future parsers

## Next milestones

- M1: locate resource name table
- M2: locate table row boundaries
- M3: parse `realfiles` rows
- M4: parse `binfiles` rows
- M5: export first HTML/JPG/MP3
- M6: generate Lesson 1 static page
