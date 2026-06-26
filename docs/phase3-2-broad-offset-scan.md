# Phase 3.2: broad offset scan

Phase 3.1 only scored 22 integers near the visible filename block. The best result was weak, so the offset/size table is probably elsewhere or encoded differently.

Tool:

```bash
python3 extractor/tools/broad_offset_scan.py embeddb out_broad_offsets
```

Outputs:

```text
out_broad_offsets/broad_offset_scores.tsv
out_broad_offsets/signature_hits.tsv
out_broad_offsets/cluster_summary.tsv
out_broad_offsets/schema_hits.tsv
out_broad_offsets/broad_resolve.json
out_broad_offsets/broad_resolve_report.md
```

Purpose:

- scan all int32 values across `embeddb`
- rank those that point directly to JPEG/HTML/XML/MP3 signatures
- cluster repeated references to the same payload start
- provide evidence for first extraction

This step still does not extract files.
