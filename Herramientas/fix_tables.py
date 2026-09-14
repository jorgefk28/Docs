#!/usr/bin/env python3
"""
Fija problemas de tablas en TF_2026_Requerimientos_KLUKA_JORGE.md:
- Bold markers partidos (ej: **Datos + especificos**)
- Columnas faltantes en tablas 3-columnas
- Continuaciones mal fusionadas
"""
import re

INPUT = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF_2026_Requerimientos_KLUKA_JORGE.md"

with open(INPUT, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

def is_sep(s):
    return s.startswith("|") and all(c in "| -:" for c in s.strip())

def is_data(s):
    return s.startswith("|") and not is_sep(s) and "|" in s[1:]

def cells_of(s):
    c = [x.strip() for x in s.split("|")]
    if c and c[0] == "":
        c = c[1:]
    if c and c[-1] == "":
        c = c[:-1]
    return c

########################################################################
# PASO 1: Unir filas con bold partido 
########################################################################
def fix_bold_continuations(rows):
    """
    Detecta patrones como:
      | **Objetivos | - algo |
      | asociados** | resto  |
    Y los fusiona en una sola fila.
    """
    result = []
    skip_next = False
    for idx, row in enumerate(rows):
        if skip_next:
            skip_next = False
            continue
        
        if idx + 1 < len(rows):
            cur = cells_of(row)
            nxt = cells_of(rows[idx + 1])
            
            # Verificar si cur_cell0 comienza con ** pero no termina con **
            # Y nxt_cell0 NO comienza con ** pero termina con **
            if (len(cur) >= 1 and len(nxt) >= 1 and
                cur[0].startswith("**") and not cur[0].endswith("**") and
                not nxt[0].startswith("**") and nxt[0].endswith("**")):
                
                # Fusionar celdas
                merged = []
                max_cells = max(len(cur), len(nxt))
                for i in range(max_cells):
                    a = cur[i] if i < len(cur) else ""
                    b = nxt[i] if i < len(nxt) else ""
                    if b and (i == 0 or not a):
                        merged.append(a + " " + b)
                    elif a and b:
                        merged.append(a + " " + b)
                    elif a:
                        merged.append(a)
                    else:
                        merged.append(b)
                
                row2 = "| " + " | ".join(merged) + " |"
                result.append(row2)
                skip_next = True
                continue
        
        result.append(row)
    return result

########################################################################
# PASO 2: Asegurar columnas correctas
########################################################################
def normalize_columns(block):
    """Asegura que todas las filas tengan el mismo nro de columnas que el separador."""
    rows = []
    seps = []
    for line in block:
        s = line.strip()
        if is_sep(s):
            seps.append(line)
        elif is_data(s):
            rows.append(line)
    
    if not seps or not rows:
        return block
    
    ncols = max(get_ncols(s) for s in seps)
    if ncols < 2:
        return block
    
    output = []
    for line in block:
        s = line.strip()
        if is_sep(s):
            output.append(f"|{'|'.join(['---' for _ in range(ncols)])}|")
            continue
        if is_data(s):
            c = cells_of(s)
            while len(c) < ncols:
                c.append("")
            output.append("| " + " | ".join(c[:ncols]) + " |")
            continue
        output.append(line)
    return output

def get_ncols(s):
    return len([c for c in s.split("|") if c.strip()])

########################################################################
# MAIN
########################################################################
output = []
i = 0
while i < len(lines):
    line = lines[i]
    
    if is_sep(line) or is_data(line):
        block = []
        while i < len(lines):
            c = lines[i].strip()
            if c.startswith("|") or c == "":
                block.append(lines[i])
                i += 1
            else:
                break
        
        # Extraer solo filas de datos
        data_rows = [l for l in block if is_data(l.strip())]
        
        # Paso 1: unir bold partidos
        fixed = fix_bold_continuations(data_rows) if data_rows else data_rows
        
        # Reconstruir bloque con lineas fijadas
        new_block = []
        di = 0
        for line in block:
            s = line.strip()
            if is_data(s) and di < len(fixed):
                new_block.append(fixed[di])
                di += 1
            else:
                new_block.append(line)
        
        # Paso 2: normalizar columnas
        new_block = normalize_columns(new_block)
        output.extend(new_block)
    else:
        output.append(line)
        i += 1

# Post-procesamiento: limpiar lineas que quedaron con doble pipe vacio y bold markers
text2 = "\n".join(output)

# Fix: "**texto texto**" patterns that lost their bold
text2 = re.sub(r"\*\*\s+\*\*", " ", text2)  # ** ** -> empty
text2 = re.sub(r"\*\*(.+?)\s+(.+?)\*\*", r"**\1 \2**", text2)

with open(INPUT, "w", encoding="utf-8") as f:
    f.write(text2)

print(f"Fijado: {INPUT}")
print(f"Lineas: {len(text2.split(chr(10)))}")
