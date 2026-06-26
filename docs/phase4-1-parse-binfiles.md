# Phase 4.1: parse binfiles

Tool:

```bash
python3 extractor/tools/parse_binfiles.py embeddb out_binfiles
```

Outputs:

```text
out_binfiles/binfiles_sections.json
out_binfiles/binfiles_resource_hits.tsv
out_binfiles/binfiles_blob_candidates.tsv
out_binfiles/binfiles_signature_hits.tsv
out_binfiles/binfiles_hex_windows.tsv
out_binfiles/binfiles_report.md
```

Purpose:

- locate `binfiles[filename:S,bindata:B]` sections
- scan resource names inside binfiles spans
- scan binary signatures inside binfiles spans
- look for length-prefixed blob candidates

This step does not extract final files.
