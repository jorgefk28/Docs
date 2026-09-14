# -*- coding: utf-8 -*-
"""Genera mapa_areas_trabajo_sigemi.drawio : mapa de areas de trabajo del TF.

Layout: arbol jerarquico (mindmap) con raiz a la izquierda y ramas hacia la
derecha. Las posiciones se calculan automaticamente para que no haya
superposiciones. Colores por area: azul (Desarrollo), naranja (Documentacion),
verde (Diagramas), siguiendo la paleta de los diagramas del repo.
"""

from xml.sax.saxutils import escape

OUT = "mapa_areas_trabajo_sigemi.drawio"
DIAGRAM_NAME = "Areas de Trabajo SIGEMI"
DIAGRAM_ID = "mapa-areas"

ROOT_ID = "mapa_root"

LEAF_H = 40.0
NODE_H = 48.0
GAP = 16.0

X_BY_DEPTH = {0: 40.0, 1: 330.0, 2: 620.0, 3: 890.0}
W_BY_DEPTH = {0: 250.0, 1: 240.0, 2: 240.0, 3: 240.0}
MAX_DEPTH = 3

PALETTE = {
    1: {"area": "#dae8fc", "area_stroke": "#6c8ebf", "sub": "#eef4fc", "edge": "#6c8ebf"},
    2: {"area": "#fce4d6", "area_stroke": "#b85450", "sub": "#fdeee0", "edge": "#b85450"},
    3: {"area": "#d5e8d4", "area_stroke": "#82b366", "sub": "#eef4ea", "edge": "#82b366"},
}

ROOT_FILL = "#fff2cc"
ROOT_STROKE = "#d6b656"
LEAF_FILL = "#ffffff"
LEAF_STROKE = "#a6a6a6"


def tree():
    """Devuelve el arbol de areas como dict {label, children}."""
    return {
        "label": "Trabajo Final SIGEMI",
        "children": [
            {
                "area": 1,
                "label": "1. Desarrollo",
                "children": [
                    {
                        "label": "Frontend",
                        "children": [
                            "Módulos (Pacientes, Turnos, Stock, Residuos, Reportes)",
                            "Pantallas y CRUDs",
                            "Validaciones de formularios",
                            "Roles y permisos en UI",
                            "Alertas y notificaciones (stock / vencimientos)",
                            "Consumo de API y sesión JWT",
                            "Responsive y accesibilidad",
                        ],
                    },
                    {
                        "label": "Backend",
                        "children": [
                            "API REST y autenticación JWT",
                            "Reglas de negocio (FIFO/FEFO, vencimientos, edad calculada)",
                            "Autenticación y autorización (RBAC)",
                            "Base de datos y consultas",
                            "Reportes (CSV/XLSX) y anonimización",
                            "Seguridad y auditoría",
                            "Despliegue",
                        ],
                    },
                    {
                        "label": "Testing",
                        "children": [
                            "Pruebas unitarias",
                            "Pruebas de integracion",
                            "Pruebas E2E",
                            "Pruebas de interfaz (UI)",
                            "Trazabilidad con casos de uso",
                            "CI/CD",
                        ],
                    },
                ],
            },
            {
                "area": 2,
                "label": "2. Documentacion",
                "children": [
                    {
                        "label": "Requerimientos",
                        "children": [
                            "Funcionales (RF)",
                            "No funcionales (RNF)",
                            "Casos de uso",
                            "Reglas de negocio",
                            "Alcance / modulos",
                        ],
                    },
                    {
                        "label": "Diseño",
                        "children": [
                            "Arquitectura",
                            "Modelos (conceptual, datos, dominio)",
                            "Prototipos y mockups",
                            "Decisiones técnicas (ADR)",
                        ],
                    },
                    {
                        "label": "Gestión",
                        "children": [
                            "Cronograma / plan de trabajo",
                            "Informe de avance",
                            "Memoria final / defensa",
                        ],
                    },
                ],
            },
            {
                "area": 3,
                "label": "3. Diagramas",
                "children": [
                    {
                        "label": "Para documentacion",
                        "children": [
                            "DCU (casos de uso)",
                            "Diagramas de flujo",
                            "Diagramas de secuencia",
                            "Diagramas de estados",
                            "Modelo de clases / dominio",
                            "Modelo de datos (DER)",
                            "Componentes / despliegue",
                        ],
                    },
                    {
                        "label": "Para stakeholders",
                        "children": [
                            "Mapa conceptual de alto nivel",
                            "Roadmap / hitos",
                            "Cronograma gráfico (Gantt)",
                            "Presentación / demo",
                            "Video demostrativo",
                        ],
                    },
                ],
            },
        ],
    }


def normalize(root):
    """Convierte el arbol en nodos {id, label, depth, area, children, is_leaf}."""
    counter = {"n": 0}

    def build(node, depth, area):
        counter["n"] += 1
        node_area = node.get("area") if isinstance(node, dict) else None
        resolved = node_area if node_area is not None else area
        n = {
            "id": "n%d" % counter["n"],
            "label": node if isinstance(node, str) else node["label"],
            "depth": depth,
            "area": resolved,
            "is_leaf": isinstance(node, str) or not node.get("children"),
            "children": [],
        }
        if isinstance(node, dict) and node.get("children"):
            child_area = node_area if (depth == 1 and node_area is not None) else resolved
            for child in node["children"]:
                n["children"].append(build(child, depth + 1, child_area if depth >= 1 else resolved))
        return n

    return build(root, 0, None)


def compute_h(n):
    if n["is_leaf"]:
        n["h"] = LEAF_H
    else:
        total = sum(compute_h(c) + GAP for c in n["children"]) - GAP
        n["h"] = max(total, NODE_H)
    return n["h"]


def assign_y(n):
    if n["is_leaf"]:
        return
    cur = n["y"] - n["h"] / 2.0
    for c in n["children"]:
        c["y"] = cur + c["h"] / 2.0
        cur += c["h"] + GAP
        assign_y(c)


def assign_x(n, depth):
    n["depth"] = depth
    n["x"] = X_BY_DEPTH[depth]
    n["w"] = W_BY_DEPTH[depth]
    for c in n["children"]:
        assign_x(c, depth + 1)


def style_for(n):
    if n["depth"] == 0:
        return (
            "shape=cloud;whiteSpace=wrap;html=1;fillColor=%s;"
            "strokeColor=%s;fontStyle=1;" % (ROOT_FILL, ROOT_STROKE)
        )
    p = PALETTE[n["area"]]
    if n["depth"] == 1:
        return (
            "rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=%s;"
            "strokeColor=%s;fontStyle=1;" % (p["area"], p["area_stroke"])
        )
    if n["depth"] == 2:
        return (
            "rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=%s;"
            "strokeColor=%s;fontStyle=1;" % (p["sub"], p["area_stroke"])
        )
    return "whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;" % (LEAF_FILL, LEAF_STROKE)


def edge_style(n):
    if n["depth"] == 1:
        color = PALETTE[n["area"]]["edge"]
    elif n["area"]:
        color = PALETTE[n["area"]]["edge"]
    else:
        color = "#666666"
    return (
        "edgeStyle=mindmapEdgeStyle;html=1;exitX=1;exitY=0.5;"
        "entryX=0;entryY=0.5;rounded=0;startArrow=none;endArrow=none;"
        "strokeColor=%s;" % color
    )


def draw_h(n):
    return n["h"] if n["is_leaf"] else NODE_H


def build_xml(root):
    root["y"] = 0.0
    compute_h(root)
    assign_y(root)
    assign_x(root, 0)

    min_y = {"v": 0.0}
    max_y = {"v": 0.0}
    max_x = {"v": 0.0}

    def extent(n):
        min_y["v"] = min(min_y["v"], n["y"])
        max_y["v"] = max(max_y["v"], n["y"] + draw_h(n))
        max_x["v"] = max(max_x["v"], n["x"] + n["w"])
        for c in n["children"]:
            extent(c)

    extent(root)

    margin_y = 60.0
    shift_y = margin_y - min_y["v"]

    def shift(n):
        n["y"] += shift_y
        for c in n["children"]:
            shift(c)

    shift(root)

    page_w = int(max_x["v"] + 120)
    page_h = int(max_y["v"] + margin_y * 2)

    out = []
    out.append('<mxfile host="app.diagrams.net" agent="opencode">')
    out.append('  <diagram name="%s" id="%s">' % (escape(DIAGRAM_NAME), DIAGRAM_ID))
    out.append(
        '    <mxGraphModel dx="681" dy="279" grid="1" gridSize="10" guides="1" '
        'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
        'pageWidth="%d" pageHeight="%d" math="0" shadow="0">' % (page_w, page_h)
    )
    out.append("      <root>")
    out.append('        <mxCell id="0" />')
    out.append('        <mxCell id="1" parent="0" />')

    edges = []

    def emit(n):
        value = escape(n["label"])
        style = style_for(n)
        out.append(
            '        <mxCell id="%s" parent="1" style="%s" '
            'value="%s" vertex="1">' % (n["id"], style, value)
        )
        out.append(
            '          <mxGeometry height="%g" width="%g" x="%g" y="%g" '
            'as="geometry" />' % (draw_h(n), n["w"], n["x"], n["y"])
        )
        out.append("        </mxCell>")
        for c in n["children"]:
            edges.append((n, c))
            emit(c)

    emit(root)

    counter = {"e": 0}
    for src, dst in edges:
        counter["e"] += 1
        eid = "e%d" % counter["e"]
        out.append(
            '        <mxCell id="%s" parent="1" source="%s" style="%s" '
            'target="%s" edge="1">' % (eid, src["id"], edge_style(dst), dst["id"])
        )
        out.append(
            '          <mxGeometry relative="1" as="geometry" />'
        )
        out.append("        </mxCell>")

    out.append("      </root>")
    out.append("    </mxGraphModel>")
    out.append("  </diagram>")
    out.append("</mxfile>")
    return "\n".join(out) + "\n", page_w, page_h


def main():
    root = normalize(tree())
    xml, page_w, page_h = build_xml(root)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(xml)

    import xml.etree.ElementTree as ET
    ET.fromstring(xml)

    total = 0

    def count(n):
        nonlocal total
        total += 1
        for c in n["children"]:
            count(c)

    count(root)
    print("OK -> %s (%d nodos, lienzo %dx%d)" % (OUT, total, page_w, page_h))


if __name__ == "__main__":
    main()