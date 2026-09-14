#!/usr/bin/env python3
"""Extract DOCX to Markdown preserving bold formatting."""
import zipfile
import xml.etree.ElementTree as ET

docx_path = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF _2026_Requerimientos_KLUKA_JORGE.docx"
out_path = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF_2026_Requerimientos_KLUKA_JORGE.md"

with zipfile.ZipFile(docx_path) as z:
    with z.open("word/document.xml") as f:
        tree = ET.parse(f)
        root = tree.getroot()

ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def get_text_with_bold(elem):
    parts = []
    for r in elem.findall(".//w:r", ns):
        rpr = r.find("w:rPr", ns)
        is_bold = False
        if rpr is not None:
            b = rpr.find("w:b", ns)
            if b is not None:
                val = b.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")
                if val is None or val in ("true", "1"):
                    is_bold = True
        t = r.find("w:t", ns)
        if t is not None and t.text:
            text = t.text
            if is_bold:
                text = "**" + text + "**"
            # Merge consecutive bold runs
            parts.append(text)
    
    # Merge adjacent bold markers: **text1****text2** -> **text1text2**
    merged = "".join(parts)
    merged = merged.replace("****", "")
    return merged

def get_cell_texts(cell):
    paragraphs = cell.findall(".//w:p", ns)
    texts = []
    for p in paragraphs:
        txt = get_text_with_bold(p)
        if txt.strip():
            texts.append(txt)
    return " ".join(texts) if texts else ""

body = root.find(".//w:body", ns)
result = []
prev_was_para = False

for child in body:
    tag = child.tag.split("}")[1] if "}" in child.tag else child.tag
    
    if tag == "p":
        txt = get_text_with_bold(child)
        result.append(txt)
        prev_was_para = True
    
    elif tag == "tbl":
        # Detect heading level from previous paragraph
        rows = child.findall(".//w:tr", ns)
        for ri, row in enumerate(rows):
            cells = row.findall(".//w:tc", ns)
            cell_texts = [get_cell_texts(c) for c in cells]
            result.append("| " + " | ".join(cell_texts) + " |")
            if ri == 0:
                ncols = len(cells)
                result.append("|" + "|".join(["---" for _ in range(ncols)]) + "|")
        result.append("")
        prev_was_para = False

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(result))

print(f"Done. Lines: {len(result)}")
