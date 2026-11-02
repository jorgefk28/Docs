# Repository Rules

## Source of truth

Only these two files are authoritative:

1. `TF_2026_Requerimientos_KLUKA_JORGE.md` — requirements specification.
2. `Diagramas/diagrama_clases_sigemi.mmd` — class diagram / data model.

Everything else in this repository is **derived, outdated, or auxiliary** and must never be used as a basis for answering, implementing, or validating anything.

## Explicitly not authoritative

Treat all of the following as stale copies, reports, generated summaries, prompts, or scratch material — **not** as requirements:

- `TF_2026_Requerimientos_KLUKA_JORGE_backup.md`
- `TF _2026_Requerimientos_KLUKA_JORGE.docx`
- `RESUMEN_EJECUTIVO_AVANCE.md`
- `Presentación SIGEMI- Trabajo Final (ASC) - Proyecto Software (LSI).docx`
- Everything under `OPENCODE-ARTIFACTS/`
- Everything under `NotasClases/`
- `Diagramas/modelo_datos_sigemi.md`, `Diagramas/modelo_conceptual_sigemi.md`, `Diagramas/fichas_medicas_de_micosis.md`, `Diagramas/diagrama_casos_uso_sigemi.drawio`, `Diagramas/).pdf`
- `mapa_areas_trabajo_sigemi.drawio`, `diagrama_flujos_sigemi.drawio`, `docx_raw.xml`

These files may describe the system as it used to be. They do not define current behavior.

Scripts under `Herramientas/` and `gen_mapa_areas.py` are neutral tooling, not requirements sources: use or modify them when the task is about them, but never cite their output as a specification.

## Session startup behavior

- Do **not** scan, index, or glob this repository at session start.
- Do **not** preemptively open derived, generated, or auxiliary documents "to get context". Assume no context beyond this file.
- The two sources of truth are the exception: reading them for context is expected and allowed when the session is about the requirements, the domain model, or the system itself.
- Still avoid loading the whole 144 KB specification when the request is narrow: read the `.mmd` fully (it is small), and search the `.md` for the relevant sections.

## Reading policy

Read a file only when one of these is true:

1. The user explicitly names or asks about that file.
2. The user explicitly asks to create, update, or generate a document.
3. The file is one of the two sources of truth and the current work needs requirements or domain-model context.

When a read is required:

- Read only the minimal section needed (search for the relevant heading or term first; use bounded offsets), never the whole 144 KB file by default.
- Read the `.mmd` diagram before the `.md` when the question is about entities, relationships, attributes, or types.
- State which file and section you relied on.

Never read `OPENCODE-ARTIFACTS/`, `NotasClases/`, backups, or generated reports to "confirm" or "cross-check" a requirement. If the sources of truth are silent on something, say so — do not fill the gap from derived documents.

## Conflict handling

If a derived document contradicts a source of truth, the source of truth wins, silently. Do not report the discrepancy unless the user asks. Never propagate content from a derived file into the sources of truth without an explicit instruction from the user.

## Writing policy

- Writes to the two authoritative files require an explicit request that names the change.
- Generating new reports, summaries, or analysis artifacts goes to `OPENCODE-ARTIFACTS/` unless the user says otherwise.
- Never regenerate or "sync" a derived document on your own initiative.
