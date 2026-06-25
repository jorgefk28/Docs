---
name: spec-discussion
description: Use when discussing, analyzing, debating, or reviewing requirements, use cases, data models, workflows, or architecture decisions without writing code. Triggers: "discutir requisitos", "analizar casos de uso", "revisar modelo de datos", "debate de arquitectura", "spec review", "discuss requirements", "use case analysis", "data model review", "/a_discuss".
---

# Spec Discussion Workflow — `/a_discuss`

Use this workflow when the user wants to analyze, discuss, or debate requirements, use cases, data models, workflows, or architecture decisions WITHOUT writing code.

## Workflow Steps

### Paso 1: Research
Delegá a `@deep_diver` para investigar la documentación existente (archivos MD, diagramas, docs) y obtener contexto.

### Paso 2: Proposal
Delegá a `@spec_writer` para producir un documento de especificación estructurado en Markdown.
- Indicá claramente QUÉ debe documentar (ej: "modelo de datos del subsistema de laboratorio", "casos de uso de gestión de turnos").
- Indicá el formato esperado.

### Paso 3: Attack
Delegá a `@spec_attacker` pasándole el documento generado en el Paso 2.
- El agente devolverá una lista numerada de hallazgos con severidad.

### Paso 4: Defend
Delegá a `@spec_defender` pasándole:
- El documento original (Paso 2)
- La lista de ataques (Paso 3)
- El agente devolverá una respuesta por cada ataque.

### Paso 5: Resolve
Delegá a `@spec_tie_breaker` pasándole:
- El documento original (Paso 2)
- Los ataques (Paso 3)
- Las defensas (Paso 4)
- El agente devolverá la versión final resuelta del documento.

### Paso 6: Present
Escribí (vos, el Analyst) el documento final como artifact en `OPENCODE-ARTIFACTS/` y presentale un resumen al usuario con:
- Qué cambió respecto al original
- Cuántos ataques se aceptaron/rechazaron
- Cuáles fueron las decisiones más importantes

## Variantes del flujo

| Variante | Pasos | Cuándo usarla |
|---|---|---|
| **Completo** | 1→2→3→4→5→6 | Discusión profunda de un tema nuevo |
| **Rápido** | 2→3→5→6 | Cuando ya hay contexto/investigación |
| **Solo propuesta** | 1→2→6 | Cuando solo se necesita documentar |
| **Ataque directo** | 3→4→5→6 | Cuando ya existe un documento para revisar |
