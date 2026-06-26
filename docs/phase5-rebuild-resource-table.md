# Phase 5: rebuild resource table

Goal:

Rebuild a high-level resource table from the evidence gathered so far.

Tool:

```bash
python3 extractor/tools/rebuild_resource_table.py embeddb out_realfiles out_binfiles out_resource_table
```

Outputs:

```text
out_resource_table/resource_table.json
out_resource_table/resource_table.tsv
out_resource_table/lesson1_resource_table.tsv
out_resource_table/section1_neighbors.tsv
out_resource_table/rebuild_report.md
```

Purpose:

- correlate resource names from realfiles and binfiles
- focus on section 1, which looks like the resource/index table
- map each resource to nearby names and nearby blob candidates
- prepare for `extract_resource.py`

This step does not yet extract final files.
