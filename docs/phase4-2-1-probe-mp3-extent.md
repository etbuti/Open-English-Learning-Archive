# Phase 4.2.1: probe MP3 extent

Tool:

```bash
python3 extractor/tools/probe_mp3_extent.py embeddb out_bindata out_mp3_extent
```

Purpose:

- test whether MP3-looking chunks are continuous streams
- calculate valid MPEG frame chains
- identify true start and end positions
- dump candidate playable streams

Outputs:

```text
out_mp3_extent/mp3_extent_report.tsv
out_mp3_extent/mp3_extent_manifest.json
out_mp3_extent/mp3_extent_report.md
out_mp3_extent/candidates/
```
