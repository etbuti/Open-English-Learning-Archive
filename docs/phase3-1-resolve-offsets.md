# Phase 3.1: resolve offsets

Tool:

```bash
python3 extractor/tools/resolve_offsets.py embeddb out_realfiles out_offsets
```

Inputs:

```text
out_realfiles/realfiles_integer_candidates.tsv
out_realfiles/realfiles_lesson1.tsv
```

Outputs:

```text
out_offsets/offset_scores.tsv
out_offsets/lesson1_offset_probe.tsv
out_offsets/signature_hits.tsv
out_offsets/resolve_report.md
out_offsets/resolve.json
```

Purpose:

- rank integer candidates as possible payload offsets
- compare candidate offsets against known binary signatures
- provide evidence before payload extraction

This step does not extract files.
