# Repository Rules

## Sources of truth — hierarchy, not a set

Authority is ordered. A lower level answers to the one above it and may **never** contradict it. If a lower level needs to contradict a higher one, the higher one changes first.

| Order | File | Answers | Loses against |
|---|---|---|---|
| 1 — Requirements | `TF_2026_Requerimientos_KLUKA_JORGE.md` | **what** the business needs | nothing |
| 2 — Conceptual domain | `Diagramas/modelo_dominio_sigemi_unificado.md` | **which concepts** exist and how they relate | 1 |
| 3 — Persistence schema | `Diagramas/modelo_esquema_bd_sigemi.md` | **how** it is stored | 1, 2 |

Everything else in this repository is **derived, outdated, or auxiliary** and must never be used as a basis for answering, implementing, or validating anything.

**Levels are not required to correspond 1:1.** A concept defined at level 2 may be realized flattened at level 3 (for example, `Muestra` has no table of its own and lives as columns of `analisis_micologico`). That is translation between levels, not a contradiction — but the mapping **must be documented** in level 3, under "Correspondencia con el modelo de dominio". An undocumented flattening is a contradiction.

## Screen designs (UI/UX)

Screen designs passed for frontend work — Figma files, views or images, or markdown describing screens — carry **presentation authority** (layout, components, copy, visual order). They are not a requirement.

**They never carry maximum authority.** They are derived artifacts: if a design contradicts a business flow or rule from level 1 (requirements), a concept from level 2, or a datum from level 3, **the higher level wins, not the design's UX**.

On conflict, implement the flow per the higher level and report the divergence to the user; never silently "fix" the design, and never propagate the contradiction into levels 1-3.

## Explicitly not authoritative

Treat all of the following as stale copies, reports, generated summaries, prompts, or scratch material — **not** as requirements:

- `TF_2026_Requerimientos_KLUKA_JORGE_backup.md`
- `TF _2026_Requerimientos_KLUKA_JORGE.docx`
- `RESUMEN_EJECUTIVO_AVANCE.md`
- `Presentación SIGEMI- Trabajo Final (ASC) - Proyecto Software (LSI).docx`
- Everything under `OPENCODE-ARTIFACTS/`
- Everything under `NotasClases/`
- Everything under `Diagramas/_superseded/` — archived and replaced by levels 2 and 3. Do not read, cite, or restore from it.
- `Diagramas/modelo_datos_sigemi.md`, `Diagramas/modelo_conceptual_sigemi.md`, `Diagramas/fichas_medicas_de_micosis.md`, `Diagramas/diagrama_casos_uso_sigemi.drawio`, `Diagramas/).pdf`
- `mapa_areas_trabajo_sigemi.drawio`, `diagrama_flujos_sigemi.drawio`, `docx_raw.xml`

These files may describe the system as it used to be. They do not define current behavior.

Scripts under `Herramientas/` and `gen_mapa_areas.py` are neutral tooling, not requirements sources: use or modify them when the task is about them, but never cite their output as a specification.

## Session startup behavior

- Do **not** scan, index, or glob this repository at session start.
- Do **not** preemptively open derived, generated, or auxiliary documents "to get context". Assume no context beyond this file.
- The three levels above are the exception: reading them for context is expected and allowed when the session is about the requirements, the domain model, the persistence schema, or the system itself.
- Still avoid loading the whole 144 KB requirements file when the request is narrow: search it for the relevant section. The domain and schema files are small enough to read fully.

## Reading policy

Read a file only when one of these is true:

1. The user explicitly names or asks about that file.
2. The user explicitly asks to create, update, or generate a document.
3. The file is one of the three levels above and the current work needs its context.

When a read is required:

- Match the level to the question: **requirements, behaviour, actors, business rules → level 1**; **entities, relationships, attributes, concepts → level 2**; **tables, columns, types, keys, indexes → level 3**.
- Read only the minimal section needed (search for the relevant heading or term first; use bounded offsets), never the whole 144 KB file by default.
- State which file and section you relied on.

Never read `OPENCODE-ARTIFACTS/`, `NotasClases/`, `Diagramas/_superseded/`, backups, or generated reports to "confirm" or "cross-check" a requirement. If the sources of truth are silent on something, say so — do not fill the gap from derived documents.

## Infrastructure decisions

`OPENCODE-ARTIFACTS/MANIFIESTO_INFRAESTRUCTURA_SIGEMI.md` is a technical decision manifest (stack, environment, deployment, legal framework). It is **operational context**, not a requirement source. When a session is about infrastructure, environment, deployment, tooling, or the technical stack, read it to recover and honor the decisions already made. It never overrides levels 1-3, and it never describes *what the system is* — only *how we decided to build and deploy it*.

## Conflict handling

- If a derived document contradicts a source of truth, the source of truth wins, silently. Do not report the discrepancy unless the user asks.
- If level 3 contradicts level 2, or level 2 contradicts level 1, the **higher level wins**. The lower one is a defect: report it only when the user asks, propose the minimal fix, and never patch the lower level by inventing content that the higher level does not support.
- Never propagate content from a derived file into the sources of truth without an explicit instruction from the user.

## Writing policy

- Writes to any of the three levels require an explicit request that names the change.
- Generating new reports, summaries, or analysis artifacts goes to `OPENCODE-ARTIFACTS/` unless the user says otherwise.
- Never regenerate or "sync" a derived document on your own initiative.
- Never archive, rename, or move a source of truth without an explicit instruction.
