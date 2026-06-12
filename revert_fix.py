#!/usr/bin/env python3
"""
Revierte el dano causado por fix_tables.py.
- Divide filas que fueron incorrectamente fusionadas
- Restaura la estructura de tabla correcta
"""
import re

INPUT = r"C:\Users\Jorge Kluka\Documents\Facultad\TF 2026\Docs\TF_2026_Requerimientos_KLUKA_JORGE.md"

with open(INPUT, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

def is_sep(s):
    return s.startswith("|") and all(c in "| -:" for c in s.strip())

def is_data(s):
    return s.startswith("|") and not is_sep(s)

def cells_of(s):
    c = [x.strip() for x in s.split("|")]
    if c and c[0] == "":
        c = c[1:]
    if c and c[-1] == "":
        c = c[:-1]
    return c

def get_ncols(s):
    return len([c for c in s.split("|") if c.strip()])

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
        
        # Determinar ncols real del separador
        seps = [l for l in block if is_sep(l.strip())]
        if seps:
            target_ncols = max(get_ncols(s) for s in seps)
        else:
            target_ncols = max(get_ncols(l) for l in block if is_data(l.strip()))
        
        if target_ncols >= 2:
            # Procesar el bloque: dividir filas fusionadas
            new_block = []
            for line in block:
                s = line.strip()
                if is_data(s):
                    c = cells_of(s)
                    # Si la fila tiene MAS celdas que el target, dividir
                    if len(c) > target_ncols:
                        # Dividir en grupos de target_ncols
                        parts = []
                        for j in range(0, len(c), target_ncols):
                            group = c[j:j+target_ncols]
                            while len(group) < target_ncols:
                                group.append("")
                            parts.append(group)
                        for group in parts:
                            new_block.append("| " + " | ".join(group) + " |")
                    else:
                        while len(c) < target_ncols:
                            c.append("")
                        new_block.append("| " + " | ".join(c[:target_ncols]) + " |")
                elif is_sep(s):
                    new_block.append(f"|{'|'.join(['---' for _ in range(target_ncols)])}|")
                else:
                    new_block.append(line)
            
            # Post-procesamiento: unir continuaciones correctamente
            # Caso A: primera celda vacia en fila siguiente -> fusionar con ultima celda anterior
            # Caso B: primera celda completa bold partido -> fusionar con primera celda anterior
            merged = []
            skip = False
            for j, row in enumerate(new_block):
                if skip:
                    skip = False
                    continue
                if not is_data(row.strip()):
                    merged.append(row)
                    continue
                    
                if j + 1 < len(new_block):
                    nxt = new_block[j+1]
                    if is_data(nxt.strip()):
                        cur_c = cells_of(row)
                        nxt_c = cells_of(nxt)
                        
                        # Caso A: nxt_c[0] vacio -> continuacion de ultima celda
                        if nxt_c and not nxt_c[0] and any(nxt_c[1:]):
                            content = " ".join(c for c in nxt_c[1:] if c)
                            if cur_c:
                                cur_c[-1] = (cur_c[-1] + " " + content).strip()
                                row = "| " + " | ".join(cur_c) + " |"
                            # No saltar siguiente, permitir mas continuaciones
                        
                        # Caso B: bold partido en primera celda
                        elif (cur_c and nxt_c and 
                              cur_c[0].startswith("**") and not cur_c[0].endswith("**") and
                              nxt_c[0] and not nxt_c[0].startswith("**") and nxt_c[0].endswith("**")):
                            for k in range(max(len(cur_c), len(nxt_c))):
                                a = cur_c[k] if k < len(cur_c) else ""
                                b = nxt_c[k] if k < len(nxt_c) else ""
                                if k == 0:
                                    cur_c[k] = a + " " + b
                                elif k < len(cur_c) and b:
                                    cur_c[k] = a + " " + b
                                elif k >= len(cur_c):
                                    cur_c.append(b)
                            row = "| " + " | ".join(cur_c) + " |"
                            skip = True  # Saltar la fila siguiente
                
                merged.append(row)
            
            # Agregar separador si no hay ninguno
            has_sep = any(is_sep(l.strip()) for l in merged)
            if has_sep:
                output.extend(merged)
            else:
                output.extend(merged)
        else:
            output.extend(block)
    else:
        output.append(line)
        i += 1

# Post-procesamiento global: limpiar bold markers partidos
text2 = "\n".join(output)
text2 = re.sub(r"\*\*\s+\*\*", " ", text2)

with open(INPUT, "w", encoding="utf-8") as f:
    f.write(text2)

print(f"Reversion completada. Lineas: {len(text2.split(chr(10)))}")
