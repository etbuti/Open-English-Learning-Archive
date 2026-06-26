# Phase 4.3: classify binfiles sections

The MP3 extent probe showed that MP3-looking candidates are not continuous streams.
We now classify each `binfiles` section separately.

Tool:

```bash
python3 extractor/tools/classify_bin_sections.py embeddb out_binfiles out_section_classify
```

Outputs:

```text
out_section_classify/section_summary.tsv
out_section_classify/section_gaps.tsv
out_section_classify/section_samples.tsv
out_section_classify/section_classify.json
out_section_classify/section_classify_report.md
out_section_classify/samples/
```

Purpose:

- classify the three `binfiles` sections
- count resources/signatures per section
- dump local evidence samples
- decide which section to reverse next
