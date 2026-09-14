#!/usr/bin/env python3
"""Full DOCX extraction: ALL tables (including nested in sdt), ALL text."""
import zipfile, xml.etree.ElementTree as ET

docx_path = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF _2026_Requerimientos_KLUKA_JORGE.docx"
out_path = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF_2026_Requerimientos_KLUKA_JORGE.md"

with zipfile.ZipFile(docx_path) as z:
    with z.open("word/document.xml") as f:
        tree = ET.parse(f)
        root = tree.getroot()

ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def get_run_text(run):
    rpr = run.find("w:rPr", ns)
    is_bold = False
    if rpr is not None:
        b = rpr.find("w:b", ns)
        if b is not None:
            val = b.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")
            if val is None or val in ("true", "1"):
                is_bold = True
    t = run.find("w:t", ns)
    if t is not None and t.text:
        text = t.text
        if is_bold:
            text = "**" + text + "**"
        return text
    return ""

def get_para_text(p):
    parts = []
    for r in p.findall(".//w:r", ns):
        t = get_run_text(r)
        if t:
            parts.append(t)
    txt = "".join(parts)
    txt = txt.replace("****", "")
    return txt

def get_cell_text(cell):
    paras = cell.findall(".//w:p", ns)
    texts = []
    for p in paras:
        t = get_para_text(p)
        if t.strip():
            texts.append(t)
    return "<br>".join(texts) if texts else ""

def process_element(elem, depth=0):
    """Process an XML element, extracting paragraphs and tables in order."""
    tag = elem.tag.split("}")[1] if "}" in elem.tag else elem.tag
    lines = []
    
    if tag == "p":
        txt = get_para_text(elem)
        if txt.strip():
            lines.append(("text", txt))
    
    elif tag == "tbl":
        mcols = 0
        rows_data = []
        for tr in elem.findall(".//w:tr", ns):
            cells = tr.findall(".//w:tc", ns)
            mcols = max(mcols, len(cells))
        
        for tr in elem.findall(".//w:tr", ns):
            cells = tr.findall(".//w:tc", ns)
            cell_texts = [get_cell_text(c) for c in cells]
            while len(cell_texts) < mcols:
                cell_texts.append("")
            rows_data.append(cell_texts)
        
        lines.append(("table", mcols, rows_data))
    
    else:
        # Recurse into children, preserving order
        for child in elem:
            lines.extend(process_element(child, depth + 1))
    
    return lines

body = root.find(".//w:body", ns)
elements = process_element(body)

# Build output
result = []
for item in elements:
    if item[0] == "text":
        result.append(item[1])
    elif item[0] == "table":
        mcols = item[1]
        rows_data = item[2]
        for ri, cells in enumerate(rows_data):
            result.append("| " + " | ".join(cells) + " |")
            if ri == 0:
                result.append("|" + "|".join(["---" for _ in range(mcols)]) + "|")
        result.append("")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(result))

# Count tables
tbl_count = sum(1 for i in elements if i[0] == "table")
print(f"Done. Lines: {len(result)}, Tables: {tbl_count}")
