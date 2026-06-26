# Phase 2.2: parse realfiles

Tool:

```bash
python3 extractor/tools/parse_realfiles.py embeddb out_realfiles
```

Outputs:

```text
out_realfiles/realfiles_sections.json
out_realfiles/realfiles_names.tsv
out_realfiles/realfiles_lesson1.tsv
out_realfiles/realfiles_integer_candidates.tsv
out_realfiles/realfiles_report.md
```

Purpose:

- locate every `realfiles[filename:S,offset:I,size:I]` declaration
- enumerate the visible filename table
- identify Lesson 1 related rows
- collect nearby integer evidence for the next offset/size parser

This step still does not extract payloads.
