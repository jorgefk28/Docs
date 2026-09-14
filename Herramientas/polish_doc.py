#!/usr/bin/env python3
"""More precise doc post-processing: removes TOC, adds headings, cleans bold."""
import re

INPUT = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF_2026_Requerimientos_KLUKA_JORGE.md"

with open(INPUT, encoding="utf-8") as f:
    lines = f.readlines()

lines = [l.rstrip() for l in lines]

# 1. Find the real content start: after "No se encontraron entradas de tabla de contenido."
# or after the last Índice/TOC entry (which is line 78 in 0-indexed = 79 in 1-indexed)
toc_end = 0
for i, line in enumerate(lines):
    if "No se encontraron entradas de tabla de contenido" in line:
        toc_end = i + 1  # line after this
        break

if toc_end == 0:
    # Fallback: find first "1. Presentación General" that's NOT in Índice/TOC
    # The TOC has Índice at lines 27-78, so just find "1. Presentación General" after Índice
    toc_end = 0  # skip nothing if we can't detect

# Remove TOC lines
lines = lines[:27] + lines[toc_end:]
# (lines 0-26 = title + Lista de Cambios; lines 27+ = rest)

########################################################################
# 2. Convert section numbers to markdown headings
########################################################################
def section_to_heading(line):
    s = line.strip()
    # Remove bold markers first if present
    m = re.match(r'^\*\*(\d+(?:\.\d+){0,3})\s+(.+?)\*\*$', s)
    if m:
        nums = m.group(1)
        text = m.group(2).strip()
        depth = nums.count(".") + 1 if nums else 1
        return "#" * depth + " " + nums + " " + text

    # Numbered sections: "1. Presentación General" or "2.1 Objetivos del sistema"
    m = re.match(r'^(\d+(?:\.\d+){0,3})\s+(.+)$', s)
    if m:
        nums = m.group(1)
        text = m.group(2).strip()
        depth = nums.count(".") + 1 if nums else 1
        return "#" * depth + " " + nums + " " + text

    # Bold standalone lines like "**Lista de Cambios**"
    m = re.match(r'^\*\*(.+?)\*\*$', s)
    if m:
        return "# " + m.group(1)

    return line

for i, line in enumerate(lines):
    lines[i] = section_to_heading(line)

########################################################################
# 3. Clean bold spacing
########################################################################
text = "\n".join(lines)
text = re.sub(r"\*\*(\s+)", "**", text)   # "** texto" -> "**texto"
text = re.sub(r"(\s+)\*\*", "**", text)   # "texto **" -> "texto**"
# Fix double asterisks that shouldn't be there
text = text.replace("****", "")

########################################################################
# 4. Clean up blank lines
########################################################################
while "\n\n\n" in text:
    text = text.replace("\n\n\n", "\n\n")

with open(INPUT, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Done. Lines: {len(text.split(chr(10)))}")
