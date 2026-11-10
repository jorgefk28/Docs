# Artifact: Cambios Aplicados — Completitud UCE 2.8.2 (Laboratorio Bioquímico)

**Fecha:** 04/10/2026
**Documento destino:** `TF_2026_Requerimientos_KLUKA_JORGE.md`
**Origen:** `OPENCODE-ARTIFACTS/propuesta_uce_diag_2_8_2.md` (revisada y aprobada por el autor)

---

## 1. Decisiones del autor

| Decisión | Resultado |
|---|---|
| UCE de Cobertura Actual (DIAG-03 a DIAG-10) | **Aprobados** e insertados en 2.8.2. |
| Reabrir Análisis (DIAG-11 propuesto) | **Descartado.** |
| Observaciones de Cultivo (DIAG-13 propuesto) | **Descartado.** |
| Asignar Análisis a Bioquímico (DIAG-14 propuesto) | **Descartado.** |
| Derivar Muestra a Laboratorio Externo (DIAG-15 propuesto) | **Descartado.** |
| Reenviar Notificación de Resultados | **Retenido**, pero **NO como caso de uso**: el reenvío al expirar el TTL es **automático** y se especifica como **postcondición** de UC-DIAG-04. El reenvío manual queda como **excepción de respaldo** ("por las dudas"). |

## 2. Cambios aplicados

### 2.1 Sección 2.8.2 — Inserción de 8 UCE nuevos

Insertadas las tablas `UCE–DIAG-03` a `UCE–DIAG-10` tras UCE–DIAG-02:

| UCE | Nombre |
|---|---|
| UCE–DIAG-03 | Actualizar Estado de Análisis |
| UCE–DIAG-04 | Validar Análisis (incluye reenvío automático de OTP) |
| UCE–DIAG-05 | Descargar Informe |
| UCE–DIAG-06 | Consultar Historial de Paciente |
| UCE–DIAG-07 | Modificar Ficha Clínica |
| UCE–DIAG-08 | Cancelar Análisis |
| UCE–DIAG-09 | Consultar Panel de Análisis |
| UCE–DIAG-10 | Gestionar Tipos de Análisis y Muestra |

Resultado: 2.8.2 queda con **10/10 UCE** (DIAG-01 a DIAG-10).

### 2.2 Reenvío automático de OTP (especificación)

- **UC–DIAG-04 (2.7.3.2) — Postcondiciones ampliadas:** el sistema programa automáticamente el reenvío de un nuevo Token OTP al expirar el TTL del vigente (7 días, RNF-02) mientras el Informe no sea descargado, invalidando el anterior en cada ciclo. El reenvío automático es postcondición del caso de uso; el manual queda como respaldo.
- **UCE–DIAG-04 (2.8.2):**
  - Paso 10 (nuevo): programación del proceso automático de reenvío de OTP.
  - Paso 11: registro en auditoría.
  - Excepción (paso 9): fallo del envío inicial → reintento automático en cola.
  - Excepción (paso 10): reenvío manual de respaldo ante falla reiterada o solicitud del paciente.
  - Comentarios: aclara que el reenvío automático es postcondición y NO constituye un caso de uso independiente.
- **RF-07 (2.5) — Descripción ampliada:** reenvío automático de un nuevo OTP al expirar el TTL (invalidando el anterior) hasta la descarga del informe; reenvío manual como respaldo.
- **UCE–DIAG-05:** excepción de OTP vencido referida al reenvío automático (UC–DIAG-04) y al respaldo manual.

### 2.3 Correcciones de consistencia

| # | Ubicación | Detalle | Aplicado |
|---|---|---|---|
| C1 | 2.7.3.2 · UC–DIAG-01 (Comentarios) | `<<extend>>` a **UC–DIAG-08 (Modificar Ficha)** → **UC–DIAG-07** | ✅ |
| C2 | 2.7.3.2 · UC–DIAG-09 (Comentarios) | "Diferente de **DIAG-07**" → **DIAG-06** | ✅ |
| C3 | 2.4 · IRQ-05 (Comentarios) | "Soporta **UC–DIAG-11**" → **UC–DIAG-10** | ✅ |
| C4 | 2.8.2 · UCE–DIAG-02 paso 1 | "UC-DIAG-01" → "UC–DIAG-01" (en-dash) | ✅ |
| C5 | 2.8.2 · UCE–DIAG-02 pasos 5, 6 | "Backend" → "El sistema" | ✅ |
| C6 | 2.8.2 · UCE–DIAG-01 (Comentarios) | "Backend" → "El sistema" | ✅ |

### 2.4 Lista de Cambios

- Agregada entrada Nro 8 (04/10/2026): completitud de UCE-DIAG-03 a UCE-DIAG-10 y especificación del reenvío automático de OTP como postcondición.

## 3. No aplicado (por decisión del autor)

- UC/UCE–DIAG-11 (Reabrir Análisis), DIAG-13 (Observaciones de Cultivo), DIAG-14 (Asignar), DIAG-15 (Derivar).
- RF-22 a RF-26 propuestos, ampliación de IRQ-02 (estado "Derivado", bioquímico asignado, bitácora) y ajustes de actores.
- Referencias residuales a estos flujos **no quedaron** en 2.8.2 (verificadas).

---

*Fin del artifact.*