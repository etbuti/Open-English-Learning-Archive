#!/usr/bin/env python3
"""
embeddb_info.py

Phase-1 inspection tool for Open English Learning Archive.

Usage:
    python3 extractor/tools/embeddb_info.py embeddb out

This tool is conservative:
- it does not pretend to fully decode protected payloads;
- it records evidence needed for the next parser.
"""

from __future__ import annotations

import argparse
import json
import re
import hashlib
from pathlib import Path
from typing import Iterable


KNOWN_MARKERS = [
    b"ebookmm",
    b"ebook mm file",
    b"shinesoft",
    b"binfiles",
    b"realfiles",
    b"system.config",
    b"filelist.xml",
    b".htm",
    b".html",
    b".jpg",
    b".jpeg",
    b".gif",
    b".png",
    b".mp3",
    b"JFIF",
    b"\xff\xd8\xff",
    b"ID3",
    b"RIFF",
    b"<html",
]


RESOURCE_RE = re.compile(
    rb"(?i)(?:[A-Za-z0-9_\-./\x80-\xff]+?\.(?:htm|html|jpg|jpeg|gif|png|xml|mp3|wav|wma|css|js))"
)


def find_all(data: bytes, needle: bytes) -> list[int]:
    out: list[int] = []
    start = 0
    while True:
        i = data.find(needle, start)
        if i < 0:
            break
        out.append(i)
        start = i + 1
    return out


def decode_name(raw: bytes) -> str:
    raw = raw.strip(b"\x00\r\n\t ")
    for enc in ("utf-8", "gbk", "gb18030", "latin1"):
        try:
            s = raw.decode(enc)
            # Keep mostly printable strings.
            if any(ch.isprintable() for ch in s):
                return s
        except UnicodeDecodeError:
            pass
    return repr(raw)


def extract_ascii_strings(data: bytes, min_len: int = 4) -> list[dict]:
    # Include high-bit bytes because paths contain Chinese GBK nearby.
    pattern = re.compile(rb"[\x20-\x7e\x80-\xff]{" + str(min_len).encode() + rb",}")
    rows = []
    for m in pattern.finditer(data):
        raw = m.group(0)
        text = decode_name(raw)
        if text:
            rows.append({"offset": m.start(), "text": text})
    return rows


def extract_resource_names(data: bytes) -> list[dict]:
    seen = set()
    rows = []
    for m in RESOURCE_RE.finditer(data):
        raw = m.group(0).strip(b"\x00")
        text = decode_name(raw)
        key = (m.start(), text)
        if key in seen:
            continue
        seen.add(key)
        rows.append({
            "offset": m.start(),
            "raw_hex": raw[:80].hex(),
            "name": text,
        })
    return rows


def write_tsv(path: Path, rows: Iterable[dict], columns: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write("\t".join(columns) + "\n")
        for row in rows:
            f.write("\t".join(str(row.get(c, "")) for c in columns) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("embeddb", type=Path)
    ap.add_argument("outdir", type=Path)
    args = ap.parse_args()

    data = args.embeddb.read_bytes()
    out = args.outdir
    out.mkdir(parents=True, exist_ok=True)

    sha256 = hashlib.sha256(data).hexdigest()

    marker_hits = {}
    for marker in KNOWN_MARKERS:
        marker_hits[marker.hex()] = {
            "marker_repr": repr(marker),
            "count": len(find_all(data, marker)),
            "offsets": find_all(data, marker)[:50],
        }

    strings = extract_ascii_strings(data)
    resource_names = extract_resource_names(data)

    info = {
        "source": str(args.embeddb),
        "size_bytes": len(data),
        "sha256": sha256,
        "head_hex": data[:128].hex(),
        "tail_hex": data[-128:].hex(),
        "marker_hits": marker_hits,
        "string_count": len(strings),
        "resource_name_count": len(resource_names),
        "notes": [
            "This is an evidence file, not a final extraction manifest.",
            "Next step: parse realfiles/binfiles table boundaries and row structures.",
        ],
    }

    (out / "embeddb-info.json").write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    write_tsv(out / "strings.txt", strings, ["offset", "text"])
    write_tsv(out / "resource-names.txt", resource_names, ["offset", "name", "raw_hex"])

    path_hits = []
    for row in resource_names:
        name = row["name"]
        if "/" in name or "\\" in name or name.lower().endswith((".htm", ".html", ".jpg", ".xml", ".mp3")):
            path_hits.append(row)
    write_tsv(out / "path-hits.tsv", path_hits, ["offset", "name", "raw_hex"])

    print(f"OK: {args.embeddb}")
    print(f"size: {len(data)} bytes")
    print(f"sha256: {sha256}")
    print(f"strings: {len(strings)}")
    print(f"resource-like names: {len(resource_names)}")
    print(f"output: {out}")


if __name__ == "__main__":
    main()
