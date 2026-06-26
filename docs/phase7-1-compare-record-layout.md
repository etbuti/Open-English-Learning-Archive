# Phase 7.1: compare record layout

Run:

```bash
python3 extractor/tools/compare_record_layout.py     embeddb out_resource_table out_record_compare
```

Outputs:

```text
out_record_compare/record_compare.tsv
out_record_compare/lesson1_compare.tsv
out_record_compare/byte_columns.tsv
out_record_compare/lesson1_dwords.tsv
out_record_compare/compare_report.md
```

Purpose:

Compare neighbouring resource records horizontally to infer the actual record fields.
