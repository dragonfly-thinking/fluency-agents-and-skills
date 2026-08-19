#!/usr/bin/env python3
"""Convert Word / PowerPoint / Excel files to Markdown using only the Python
standard library — no pip install, no network, nothing to set up.

This is the no-Node fallback for the convert-docs skill. It is fast enough for
batches (parsing, not reading), so 50 documents is seconds rather than minutes.

    python3 office2md.py report.docx                 -> report.md beside it
    python3 office2md.py deck.pptx -o out/deck.md    -> explicit output path
    python3 office2md.py *.docx --outdir converted/  -> batch

Handles .docx, .pptx, .xlsx (and .docm/.pptm/.xlsm). It does NOT handle PDF —
PDFs need anydoc, or the agent reading the file itself. Exit codes: 0 all good,
1 nothing converted, 2 some converted and some failed (details on stderr).
"""

import argparse
import os
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


def _text(node, ns):
    """All text under a node, in document order."""
    return "".join(t.text or "" for t in node.iter("{%s}t" % ns))


def _cell(value):
    """Make a value safe for a Markdown table cell.

    A cell containing a line break would otherwise split the row and corrupt the
    whole table, so newlines become <br> rather than being dropped.
    """
    return (value.replace("|", "\\|")
                 .replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>"))


def docx_to_md(z):
    root = ET.fromstring(z.read("word/document.xml"))
    out, in_list = [], False
    for p in root.iter("{%s}p" % W):
        txt = _text(p, W).strip()
        style_el = p.find(".//{%s}pStyle" % W)
        style = style_el.get("{%s}val" % W) if style_el is not None else ""
        is_list = p.find(".//{%s}numPr" % W) is not None
        if not txt:
            continue
        if style.startswith("Heading"):
            digits = "".join(c for c in style if c.isdigit())
            level = min(int(digits) if digits else 1, 6)
            out.append("#" * level + " " + txt)
            in_list = False
        elif is_list:
            if not in_list and out:
                out.append("")
            out.append("- " + txt)
            in_list = True
        else:
            out.append(txt)
            in_list = False
    return "\n\n".join(out)


def pptx_to_md(z):
    slides = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
    slides.sort(key=lambda n: int(re.search(r"(\d+)\.xml$", n).group(1)))
    out = []
    for i, name in enumerate(slides, 1):
        root = ET.fromstring(z.read(name))
        lines = []
        for p in root.iter("{%s}p" % A):
            t = _text(p, A).strip()
            if t:
                lines.append(t)
        if not lines:
            continue
        # First line of a slide is nearly always its title.
        out.append("## Slide %d — %s" % (i, lines[0]))
        for line in lines[1:]:
            out.append("- " + line)
    return "\n\n".join(out)


def xlsx_to_md(z):
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        shared = [_text(si, S) for si in root.iter("{%s}si" % S)]

    names = {}
    if "xl/workbook.xml" in z.namelist():
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        for i, sh in enumerate(wb.iter("{%s}sheet" % S), 1):
            names[i] = sh.get("name", "Sheet %d" % i)

    sheets = [n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", n)]
    sheets.sort(key=lambda n: int(re.search(r"(\d+)\.xml$", n).group(1)))

    out = []
    for idx, name in enumerate(sheets, 1):
        root = ET.fromstring(z.read(name))
        rows = []
        for row in root.iter("{%s}row" % S):
            cells = []
            for c in row.iter("{%s}c" % S):
                v = c.find("{%s}v" % S)
                raw = v.text if v is not None else ""
                if c.get("t") == "s" and raw not in (None, ""):
                    try:
                        raw = shared[int(raw)]
                    except (ValueError, IndexError):
                        pass
                elif c.get("t") == "inlineStr":
                    raw = _text(c, S)
                cells.append((raw or "").strip())
            while cells and not cells[-1]:
                cells.pop()
            if any(cells):
                rows.append(cells)
        if not rows:
            continue
        out.append("## " + names.get(idx, "Sheet %d" % idx))
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header, body = rows[0], rows[1:]
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join([" --- "] * width) + "|")
        for r in body:
            out.append("| " + " | ".join(_cell(x) for x in r) + " |")
        out.append("")
    if out:
        out.append(
            "\n> Converted from a spreadsheet: values only. Formulas, formatting and "
            "charts are not preserved — open the original if those matter."
        )
    return "\n".join(out)


HANDLERS = {
    ".docx": docx_to_md, ".docm": docx_to_md,
    ".pptx": pptx_to_md, ".pptm": pptx_to_md,
    ".xlsx": xlsx_to_md, ".xlsm": xlsx_to_md,
}


def convert(path, out_path):
    ext = os.path.splitext(path)[1].lower()
    handler = HANDLERS.get(ext)
    if handler is None:
        raise ValueError(
            "unsupported file type '%s' (this script does Word/PowerPoint/Excel; "
            "PDFs need anydoc or reading the file directly)" % (ext or "none")
        )
    if not zipfile.is_zipfile(path):
        raise ValueError(
            "not a valid Office file — old .doc/.ppt/.xls are a different, binary "
            "format; re-save as .docx/.pptx/.xlsx first"
        )
    with zipfile.ZipFile(path) as z:
        md = handler(z)
    if not md.strip():
        raise ValueError("no text found — the file may be empty or image-only")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(md.rstrip() + "\n")
    return len(md)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("-o", "--output", help="output path (single input only)")
    ap.add_argument("--outdir", help="write .md files into this directory")
    args = ap.parse_args()

    if args.output and len(args.files) > 1:
        ap.error("-o takes a single input file; use --outdir for batches")
    if args.outdir:
        os.makedirs(args.outdir, exist_ok=True)

    ok, failed = 0, 0
    for path in args.files:
        if args.output:
            dest = args.output
        else:
            base = os.path.splitext(os.path.basename(path))[0] + ".md"
            dest = os.path.join(args.outdir or os.path.dirname(path) or ".", base)
        try:
            n = convert(path, dest)
            print("%s -> %s (%d chars)" % (path, dest, n))
            ok += 1
        except Exception as exc:                       # noqa: BLE001 - report, continue
            print("FAILED %s: %s" % (path, exc), file=sys.stderr)
            failed += 1

    if ok and failed:
        return 2
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
