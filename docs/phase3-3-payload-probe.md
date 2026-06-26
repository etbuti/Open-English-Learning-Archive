# Phase 3.3: payload probe

`broad_offset_scan.py` found one strong direct offset:

```text
0x21810 -> mp3_frame_f3
```

This may be:

- a real raw MP3 payload start,
- a false positive inside protected data,
- or part of an encoded/compressed stream.

Tool:

```bash
python3 extractor/tools/payload_probe.py embeddb out_broad_offsets out_payload_probe
```

Outputs:

```text
out_payload_probe/probe_manifest.json
out_payload_probe/probe_offsets.tsv
out_payload_probe/chunks/
```

The probe dumps small chunks from candidate offsets and checks whether MP3 frame headers look plausible.
It still does not claim final extraction.
