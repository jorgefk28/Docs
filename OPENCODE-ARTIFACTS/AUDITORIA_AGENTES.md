# Auditoría de Agentes — Distribución de Responsabilidades y Permisos

**Versión:** 1.0 | **Autor:** Analyst | **Fecha:** 2026-07-29

---

## 1. Resumen Ejecutivo

Se detectaron **8 problemas**, clasificados por severidad:

| # | Severidad | Problema |
|---|---|---|
| 1 | 🔴 CRÍTICO | `writeArtifact` mal indentado (dentro de `bash`) en analyst local y global |
| 2 | 🟠 ALTO | Analyst local no puede delegar a `developer`, `review_attacker`, `review_defender`, `review_tie_breaker` |
| 3 | 🟠 ALTO | `spec_writer` y `spec_tie_breaker` tienen `edit: allow` innecesario |
| 4 | 🟡 MEDIO | `spec_writer` y `spec_defender` usan el mismo modelo (qwen3.6-plus) — riesgo de cámara de eco |
| 5 | 🟡 MEDIO | `spec_attacker` usa modelo débil (deepseek-v4-flash) para tarea adversarial |
| 6 | 🟡 MEDIO | Analyst local no tiene `todowrite`/`todoread` explícitos |
| 7 | 🟢 BAJO | `deep_diver` local no tiene `pnpm run knip` (el global sí) |
| 8 | 🟢 BAJO | Analyst local no tiene skills específicas listadas (solo `"*": allow`) |

---

## 2. Análisis Detallado por Agente

### 2.1 Agent Matrix

| Agente | Ubicación | Mode | Modelo | Variant | Edit | Task (subagentes) |
|---|---|---|---|---|---|---|
| **analyst** | local | `all` | deepseek-v4-pro | conservative | ❌ deny | deep_diver, spec_attacker, spec_defender, spec_tie_breaker, spec_writer |
| **analyst** | global | `all` | deepseek-v4-flash | conservative | ❌ deny | deep_diver, developer(ask), review_attacker, review_defender, review_tie_breaker |
| **deep_diver** | local | `subagent` | qwen3.6-flash | creative | ❌ deny | (puede task a otros) |
| **deep_diver** | global | `subagent` | qwen3.6-flash | creative | ❌ deny | (puede task a otros) |
| **spec_writer** | local | `subagent` | qwen3.6-plus | conservative | ✅ allow | — |
| **spec_attacker** | local | `subagent` | deepseek-v4-flash | creative | ❌ deny | — |
| **spec_defender** | local | `subagent` | qwen3.6-plus | conservative | ❌ deny | — |
| **spec_tie_breaker** | local | `subagent` | deepseek-v4-pro | conservative | ✅ allow | — |
| **developer** | global | `subagent` | qwen3.6-plus | conservative | ✅ allow | deep_diver |
| **review_attacker** | global | `subagent` | deepseek-v4-pro | creative | ✅ allow | deep_diver |
| **review_defender** | global | `subagent` | qwen3.6-plus | conservative | ✅ allow | deep_diver |
| **review_tie_breaker** | global | `subagent` | deepseek-v4-pro | conservative | ✅ allow | deep_diver |
| **solo_dev** | global | `primary` | deepseek-v4-pro | — | ✅ allow | deep_diver |

---

## 3. Hallazgos — Detalle

### 🔴 H-01: `writeArtifact` mal indentado (CRÍTICO)

**Archivos afectados:**
- `.opencode/agents/analyst.md` (local) — línea 33
- `~/.config/opencode/agents/analyst.md` (global) — línea 37

**Problema:** `writeArtifact: allow` está indentado dentro del bloque `bash:`, lo que significa que se interpreta como un comando bash llamado `writeArtifact`, no como el permiso de herramienta de alto nivel.

**Configuración actual (incorrecta):**
```yaml
  bash:
    "*": deny
    ls: allow
    ...
    "git log *": allow
    writeArtifact: allow    # ← MAL: está dentro de bash
```

**Configuración correcta:**
```yaml
  bash:
    "*": deny
    ls: allow
    ...
    "git log *": allow
  writeArtifact: allow      # ← BIEN: al mismo nivel que read, edit, grep, etc.
```

**Impacto:** El analyst no puede escribir artifacts. Como el analyst es el orquestador y su única salida son los artifacts, esto rompe el flujo completo de trabajo.

---

### 🟠 H-02: Analyst local no puede delegar a agentes de desarrollo/review (ALTO)

**Archivo:** `.opencode/agents/analyst.md` (local)

**Problema:** El analyst local solo permite `task` a:
- `deep_diver`
- `spec_attacker`
- `spec_defender`
- `spec_tie_breaker`
- `spec_writer`

Pero **no** permite:
- `developer`
- `review_attacker`
- `review_defender`
- `review_tie_breaker`

El analyst global sí los tiene (con `developer: ask`).

**Impacto:** El analyst local solo puede ejecutar los workflows `/a_create_specs` y `/a_discuss`. No puede ejecutar `/a_develop` ni `/a_review`. Esto limita al proyecto a ser solo de especificación, sin capacidad de implementación.

**Decisión necesaria:** ¿Es intencional? Si el proyecto solo necesita specs, está bien. Si necesita desarrollo, hay que agregar los permisos.

---

### 🟠 H-03: `spec_writer` y `spec_tie_breaker` tienen `edit: allow` innecesario (ALTO)

**Archivos:**
- `.opencode/agents/spec_writer.md` — línea 8: `edit: allow`
- `.opencode/agents/spec_tie_breaker.md` — línea 8: `edit: allow`

**Problema:** Ambos agentes tienen reglas explícitas de "NO escribo código". Sin embargo, tienen `edit: allow`, lo que les da permiso para modificar archivos del proyecto. Esto contradice su propósito.

**Comparación:** `spec_attacker` y `spec_defender` correctamente tienen `edit: deny`.

**Riesgo:** Un spec_writer o spec_tie_breaker podría accidentalmente modificar archivos de código fuente.

**Corrección sugerida:** Cambiar a `edit: deny`. Solo necesitan `writeArtifact: allow` para generar documentos.

---

### 🟡 H-04: `spec_writer` y `spec_defender` usan el mismo modelo (MEDIO)

**Archivos:**
- `.opencode/agents/spec_writer.md` — `model: openrouter/qwen3.6-plus`
- `.opencode/agents/spec_defender.md` — `model: openrouter/qwen3.6-plus`

**Problema:** El spec_writer produce el documento y el spec_defender lo defiende. Si ambos usan el mismo modelo con la misma variante (`conservative`), hay riesgo de "cámara de eco": el defensor tenderá a coincidir con el escritor porque razonan de forma similar.

**Sugerencia:** Cambiar uno de los dos a un modelo diferente. Opciones:
- spec_defender → `deepseek-v4-flash` (creative) para una perspectiva diferente
- spec_writer → `deepseek-v4-pro` (conservative) para mayor calidad de documento base

---

### 🟡 H-05: `spec_attacker` usa modelo débil para tarea adversarial (MEDIO)

**Archivo:** `.opencode/agents/spec_attacker.md` — `model: openrouter/deepseek-v4-flash`

**Problema:** El spec_attacker es el encargado de encontrar fallas en especificaciones. Usa `deepseek-v4-flash`, que es un modelo rápido pero menos potente. Para una tarea que requiere pensamiento crítico y detección de sutilezas (ambigüedades, inconsistencias, gaps de arquitectura), un modelo más débil puede pasar por alto problemas importantes.

**Comparación:** El `review_attacker` global (que hace un trabajo similar pero sobre código) usa `deepseek-v4-pro`.

**Sugerencia:** Evaluar subir a `deepseek-v4-pro` o al menos a `qwen3.6-plus`.

---

### 🟡 H-06: Analyst local no tiene `todowrite`/`todoread` explícitos (MEDIO)

**Archivo:** `.opencode/agents/analyst.md` (local)

**Problema:** El system prompt del analyst dice "Track progress with todos. Mark items done only when verified." y el tool `todowrite` está disponible en el sistema, pero los permisos no mencionan `todowrite` ni `todoread` explícitamente.

El `deep_diver` sí los tiene explícitos:
```yaml
  todoread: allow
  todowrite: allow
```

**Riesgo:** Si el sistema interpreta la ausencia como `deny` por defecto, el analyst no podría crear ni actualizar todos. En la práctica parece funcionar (los creé en esta sesión), pero es frágil.

**Corrección sugerida:** Agregar explícitamente:
```yaml
  todoread: allow
  todowrite: allow
```

---

### 🟢 H-07: `deep_diver` local no tiene `pnpm run knip` (BAJO)

**Archivos:**
- `.opencode/agents/deep_diver.md` (local) — sin `pnpm run knip`
- `~/.config/opencode/agents/deep_diver.md` (global) — líneas 27-28: `pnpm run knip: allow`

**Problema:** El deep_diver global puede ejecutar `pnpm run knip` para análisis de código muerto, pero el local no. Si el proyecto usa knip, el deep_diver local no podrá aprovecharlo.

**Impacto:** Bajo. Solo afecta si el proyecto tiene knip configurado.

---

### 🟢 H-08: Analyst local no lista skills específicas (BAJO)

**Archivo:** `.opencode/agents/analyst.md` (local) — línea 7-8: `skill: { "*": allow }`

**Comparación con global:**
```yaml
  skill: 
    "*": allow
    "supabase": allow
    "supabase-postgres-best-practices": allow
    "writing-tests": allow
```

**Problema:** El analyst local usa `"*": allow` que ya cubre todo. Listar skills específicas es redundante pero sirve como documentación de qué skills se espera usar.

**Impacto:** Nulo en funcionalidad. Solo es una cuestión de claridad/documentación.

---

## 4. Flujo de Responsabilidades — ¿Está bien distribuido?

### 4.1 Spec Workflow (`/a_discuss` y `/a_create_specs`)

```
analyst → deep_diver (investigación)
        → spec_writer (documento base)
        → spec_attacker (hallazgos)
        → spec_defender (defensa)
        → spec_tie_breaker (resolución final)
        → analyst escribe artifact final
```

**Veredicto:** ✅ Bien diseñado. Separación clara de responsabilidades. Cada agente tiene un rol único y bien definido.

**Problemas:** Los hallazgos H-03, H-04, H-05 afectan la calidad de este flujo.

### 4.2 Development Workflow (`/a_develop`)

```
analyst → developer → código + tests
```

**Veredicto:** ❌ Roto en el proyecto local. El analyst local no puede invocar al `developer` (H-02).

### 4.3 Review Workflow (`/a_review`)

```
analyst → review_attacker → review_defender → review_tie_breaker → developer (fixes)
```

**Veredicto:** ❌ Roto en el proyecto local. El analyst local no puede invocar a los agentes de review (H-02).

---

## 5. Recomendaciones

### Acciones inmediatas (CRÍTICO + ALTO):

1. **Corregir indentación de `writeArtifact`** en ambos `analyst.md` (local y global). Sin esto, el analyst no puede persistir nada.

2. **Decidir alcance del proyecto local:**
   - Si es solo specs → el task list actual está bien.
   - Si necesita desarrollo → agregar `developer`, `review_attacker`, `review_defender`, `review_tie_breaker` al `task:` del analyst local.

3. **Quitar `edit: allow`** de `spec_writer` y `spec_tie_breaker`. Cambiar a `edit: deny`.

### Mejoras recomendadas (MEDIO):

4. **Diversificar modelos** en el flujo spec: cambiar spec_defender a otro modelo para evitar cámara de eco.

5. **Evaluar subir el modelo de spec_attacker** a `deepseek-v4-pro` para mejorar la calidad del análisis adversarial.

6. **Agregar `todowrite`/`todoread` explícitos** al analyst local.

### Opcionales (BAJO):

7. Sincronizar `pnpm run knip` en deep_diver local si el proyecto lo usa.

8. Listar skills específicas en analyst local para documentación.

---

## 6. Tabla de Decisión

| Hallazgo | ¿Arreglar? | Responsable |
|---|---|---|
| H-01: writeArtifact indentado | ✅ SÍ — crítico | Usuario |
| H-02: Sin acceso a dev/review | ❓ Decidir según alcance | Usuario |
| H-03: edit: allow en spec agents | ✅ SÍ — riesgo real | Usuario |
| H-04: Mismo modelo writer/defender | ⚠️ Recomendado | Usuario |
| H-05: Modelo débil en attacker | ⚠️ Recomendado | Usuario |
| H-06: todowrite explícito | ⚠️ Recomendado | Usuario |
| H-07: knip en deep_diver | 🔽 Opcional | Usuario |
| H-08: Skills explícitas | 🔽 Opcional | Usuario |