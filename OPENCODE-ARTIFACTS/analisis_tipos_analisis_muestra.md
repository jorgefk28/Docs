# Análisis — Tipos de Análisis vs. Tipos de Muestra en el Modelo Conceptual

**Fecha:** 14/09/2026
**Contexto:** Revisión de las entidades involucradas en la consulta al rellenar una ficha clínica (subsistema DIAG / Laboratorio Bioquímico).
**Pregunta original:** ¿Los tipos de análisis y los tipos de muestras deberían ser entidades o atributos?

---

## 1. Cómo lo maneja el modelo actualmente

| Concepto | Representación | Dónde |
|---|---|---|
| **Tipo de análisis** | **ENTIDAD** catálogo `TipoAnalisis` (`nombre`, `descripcion`, `estado`) | `modelo_conceptual_sigemi.md:22`, `modelo_datos_sigemi.md:25` |
| | Referenciado por FK desde `AnalisisMicologico.tipo_analisis_id`, `Turno.tipo_analisis_id`, `IndicacionMedica.tipo_analisis_id` | `modelo_datos_sigemi.md:86,108,150` |
| | Con UC de gestión (DIAG-13 / RF-16 / IRQ-05) | `COMPLETITUD_DIAG_LAB.md:104`, `TF_2026_Requerimientos_KLUKA_JORGE.md:149` |
| **Tipo de muestra** | **ATRIBUTO** libre: `AnalisisMicologico.tipo_muestra` (string, sin catálogo ni FK) | `modelo_datos_sigemi.md:152` |
| | Sin UC de gestión propia, sin IRQ propio | — |

**Problema central:** `TipoAnalisis` declara ser "catálogo de análisis y tipos de muestra" (un solo catálogo que nominalmente contiene las dos dimensiones), pero `tipo_muestra` no es FK a ese catálogo: es un string libre. Conviven dos representaciones contradictorias de lo mismo.

---

## 2. Inconsistencias identificadas

1. **INC-1 — Tipo de muestra modelado dos veces y sin conexión:** el catálogo `TipoAnalisis` "incluye tipos de muestra", pero `AnalisisMicologico.tipo_muestra` es texto libre desconectado de todo catálogo. No hay validación de valores (tipos/typos), no se puede desactivar uno, ni filtrar/reportar de forma confiable.

2. **INC-2 — Dos dimensiones ortogonales colapsadas en un catálogo sin discriminador:** una fila "Micosis ungueal" (tipo de análisis) y una fila "Uñas" (tipo de muestra) coexistirían en la misma tabla con idéntica estructura (`nombre`, `descripcion`, `estado`), sin columna que distinga qué representa cada una. El CRUD de DIAG-13 se vuelve ambiguo.

3. **INC-3 — La UI pide dos catálogos que el modelo no tiene:** el brief muestra **dos selectores separados** — "tipo de muestra (uñas/piel/cabello)" y "tipo de análisis" — en Ingreso de Muestra, Panel y Nueva Consulta (`BRIEF_DISENO_UX_UI_SIGEMI.md:147,186,250`). El modelo solo tiene un catálogo y un texto libre para la muestra.

4. **INC-4 — Los requisitos nombran los conceptos de forma cruzada:** UC-DIAG-02 dice "indicando el **tipo de análisis** a realizar" (`requerimientos:567`) pero UCE-DIAG-02 paso 3 dice "selecciona el **Tipo de Muestra**" (`requerimientos:1382`). IRQ-02 lista "Tipo de muestra" y no "tipo de análisis". Los requisitos tratan cada uno como lista cerrada, pero el modelo solo tiene catálogo para uno.

5. **INC-5 — No hay restricción de combinaciones válidas (análisis × muestra):** en el mundo real "Micosis ungueal" admite uñas, "Superficial/cutánea" admite piel/cabello. Al no modelarse la relación, cualquier análisis puede tener cualquier muestra (o un texto libre arbitrario). Esto también rompe la UX: al elegir tipo de análisis, la UI no sabe qué muestras ofrecer.

6. **INC-6 — El "tipo de ficha/micosis" no está modelado:** las fichas físicas son 3 plantillas por tipo de micosis — ungueales / superficiales-cutáneas / profundas — con campos clínicos distintos (`fichas_medicas_de_micosis.md`). Eso es lo que hoy define qué `DatoClinico` se carga, pero `FichaClinica` no tiene ninguna relación con `TipoAnalisis`. El tipo de ficha que se renderiza al crear la consulta no es derivable del modelo.

---

## 3. Decisión: ¿entidad o atributo?

- **TipoAnalisis → entidad:** ya lo es y está justificado (lo referencian 3 entidades, tiene ciclo de vida y gestión de catálogo).
- **TipoMuestra → hoy atributo, la evidencia apunta a entidad:** es un conjunto cerrado gestionable (uñas/piel/cabello/suero…), se filtra en el panel, se valida, y `COMPLETITUD_DIAG_LAB.md` F6 ya detecta la necesidad de catálogo.
- El verdadero defecto no es "entidad vs atributo" sino **la fusión de dos conceptos en un solo catálogo híbrido**.

---

## 4. Decisiones tomadas

1. **Dos catálogos separados:** crear `TipoMuestra` como entidad catálogo; `tipo_muestra` pasa a FK; tabla N:N `TipoAnalisisTipoMuestra` para restringir combinaciones válidas. Alinea UI, requisitos y modelo.
2. **`TipoAnalisis` es el tipo de ficha:** la categoría de micosis (ungueal/superficial/profunda) es el mismo concepto que el tipo de ficha; define la plantilla de campos clínicos de la ficha.

---

## 5. Plan de modificación

### 5.1 Cambios al modelo conceptual

1. **`TipoAnalisis` — redefinir alcance:** de "catálogo de análisis y tipos de muestra" a *categoría de micosis / tipo de ficha clínica* (ungueal, superficial-cutánea, profunda). Define la plantilla de campos clínicos que la ficha renderiza en `DatoClinico`. Sin cambios de atributos.

2. **Nueva entidad `TipoMuestra`** (catálogo funcional):
   - Atributos: `nombre`, `descripcion`, `estado` (uñas, piel, cabello, suero…).

3. **`AnalisisMicologico` — convertir atributo en FK:**
   - `tipo_muestra` (string) → `tipo_muestra_id` (FK → `TipoMuestra`).
   - Mantiene `tipo_analisis_id` (FK → `TipoAnalisis`).

4. **Nueva relación N:N `TipoAnalisisTipoMuestra`** (tabla asociativa):
   - "Un tipo de análisis admite 0..N tipos de muestra; un tipo de muestra es válido para 0..N tipos de análisis."
   - Resuelve INC-5 (combinaciones válidas) y alimenta la UI: al elegir tipo de análisis, solo se ofrecen muestras válidas.

5. **`FichaClinica` — nueva relación a `TipoAnalisis`:**
   - `FichaClinica → TipoAnalisis` (N←1): la ficha es de una categoría de micosis.
   - Resuelve INC-6: el tipo de ficha (y su plantilla de `DatoClinico`) ahora es derivable del modelo. La ficha y los análisis que origina comparten el mismo tipo.

### 5.2 Cambios derivados en la documentación

| Documento | Cambio |
|---|---|
| `modelo_datos_sigemi.md` | Nueva clase `TipoMuestra`, tabla asociativa `TipoAnalisisTipoMuestra`, `tipo_muestra_id` FK en `AnalisisMicologico`, `tipo_analisis_id` FK en `FichaClinica`; actualizar matriz de relaciones + mermaid |
| `TF_2026_Requerimientos_KLUKA_JORGE.md` | IRQ-05 se divide: "Catálogo de Tipos de Análisis" + nuevo "Catálogo de Tipos de Muestra"; IRQ-02 referencia ambos; UC-DIAG-13/RF-16 se separan en gestión de cada catálogo (o un UC con dos sub-flujos); UCE-DIAG-02 paso 3 aclara los dos selectores |
| `BRIEF_DISENO_UX_UI_SIGEMI.md` | Catálogo de entidades: agregar `TipoMuestra`; Nueva Consulta / Ingreso de Muestra / Panel reflejan los dos catálogos y el filtrado por combinaciones válidas |
| `fichas_medicas_de_micosis.md` | Documentar la correspondencia: plantilla de ficha ↔ `TipoAnalisis` |

### 5.3 Punto abierto (decisión menor)

El vínculo `TipoAnalisis` → plantilla de `DatoClinico` se puede modelar de dos formas:

- **(a) Mínima (recomendada):** documentarlo como regla — `TipoAnalisis` define qué `campo`/`tipo_dato` admite la ficha, sin tablas nuevas.
- **(b) Rigurosa:** nuevo catálogo `DatoClinicoDefinicion` (campos por `TipoAnalisis`) que la ficha instancia en `DatoClinico`.

---

## 6. Referencias de archivos

- `Diagramas/modelo_conceptual_sigemi.md`
- `Diagramas/modelo_datos_sigemi.md`
- `Diagramas/fichas_medicas_de_micosis.md`
- `TF_2026_Requerimientos_KLUKA_JORGE.md`
- `BRIEF_DISENO_UX_UI_SIGEMI.md`
- `OPENCODE-ARTIFACTS/COMPLETITUD_DIAG_LAB.md`
