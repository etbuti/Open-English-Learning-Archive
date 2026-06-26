# Phase 2: realfiles / binfiles table analysis

Goal: export the first batch of HTML / JPG / MP3 from `embeddb`.

## Milestones

- [ ] 2.1 Scan markers and resource hits
- [ ] 2.2 Locate `realfiles[filename:S,offset:I,size:I]`
- [ ] 2.3 Locate `binfiles[filename:S,bindata:B]`
- [ ] 2.4 Parse table row boundaries
- [ ] 2.5 Export first JPG
- [ ] 2.6 Export first HTML
- [ ] 2.7 Export first MP3
- [ ] 2.8 Generate Lesson 1 manifest and static page

## Current tool

```bash
python3 extractor/tools/embeddb_scan.py embeddb out_scan
```

Outputs:

```text
out_scan/markers.tsv
out_scan/table_windows.tsv
out_scan/resource_hits.tsv
out_scan/payload_candidates.tsv
out_scan/scan.json
```

## Rule

The scanner is evidence-only. Extraction begins only after the table layout is supported by scan evidence.
