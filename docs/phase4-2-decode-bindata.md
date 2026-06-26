# Phase 4.2: decode bindata candidates

Tool:

```bash
python3 extractor/tools/decode_bindata.py embeddb out_binfiles out_bindata
```

Input:

```text
out_binfiles/binfiles_blob_candidates.tsv
```

Outputs:

```text
out_bindata/decode_candidates.tsv
out_bindata/decode_manifest.json
out_bindata/decode_report.md
out_bindata/decoded/
```

Purpose:

- dump length-prefixed blob candidates
- try raw, zlib, gzip, and raw-deflate decoding
- identify recovered file types
- preserve evidence before final extraction

This step may recover files, but does not yet assign original filenames.
