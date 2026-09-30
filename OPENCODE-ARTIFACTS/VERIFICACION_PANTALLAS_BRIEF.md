# Verificación de Pantallas y Flujos en el BRIEF de Diseño SIGEMI

**Objeto revisado:** `BRIEF_DISENO_UX_UI_SIGEMI.md` (§3 Arquitectura, §4 Flujos críticos, §5 Pantallas necesarias, §6 Estados)
**Fuentes cruzadas:** `TF_2026_Requerimientos_KLUKA_JORGE.md` (RF/RNF/UC/UCE), `Diagramas/modelo_datos_sigemi.md`, `mapeo_flujos_uc.md`
**Propósito:** Determinar si el BRIEF deja bien definidas (1) las pantallas que deben existir y (2) el flujo de trabajo de cada pantalla, como guía para que la IA construya el sitio.

---

## 1. Veredicto general

**Parcialmente adecuado.** El BRIEF inventaría correctamente ~30 pantallas con un formato consistente (objetivo · usuario principal · datos · acciones · estados), y define con detalle los 5 flujos clínicos críticos en §4. Sin embargo, **no cumple del todo el requisito de "flujo de trabajo para cada pantalla"**: los flujos paso a paso solo existen para el núcleo clínico, no para la mayoría de pantallas. Además hay **1 pantalla ausente**, varias **ambigüedades de rol** y **discrepancias de ubicación en el árbol de navegación** que la IA resolvería de forma inconsistente.

Conclusión accionable: el BRIEF está cerca de ser una guía de construcción, pero necesita cerrar los puntos de la sección 3 antes de usarse como contrato de build.

---

## 2. Auditoría de completitud: pantalla ↔ caso de uso

Matriz cruzada. "UC" = casos de uso que debe cubrir la pantalla. "Flujo §4" = si tiene flujo paso a paso definido en el BRIEF.

| # | Pantalla (BRIEF §5) | UC que cubre | Flujo paso a paso (§4) | ¿Completa? |
|---|---|---|---|---|
| 1 | Login | SEG-01, SEG-03 | ❌ No (solo acciones/estados) | ⚠️ Falta flujo de login/bloqueo/recuperación |
| 2 | Panel de Control (Dashboard) | RF-09, LAB-08 | ❌ No | ⚠️ Contenido **FALTA DEFINIR** (reconocido) |
| 3 | Auditoría | RF-14 | ❌ No (sí en §4 flujo 5) | ⚠️ Flujo en §4, falta por-pantalla |
| 4 | Agenda (día/semana/mes) | REC-06, REC-15, REC-20..22 | ❌ No (flujo complementario en §4) | ✅ |
| 5 | Nuevo Turno | REC-20 | ❌ No | ✅ |
| 6 | Detalle/Acciones de Turno | REC-15, REC-21, REC-22 | ❌ No | ⚠️ Falta formulario de completar demográficos (UCE-REC-15 paso 6) |
| 7 | Configuración de Agenda | REC-07 | ❌ No | ✅ |
| 8 | Bloqueos de Agenda | REC-08 | ❌ No | ✅ |
| 9 | Indicaciones Médicas | REC-10..13 | ❌ No | ✅ |
| 10 | Listado de Pacientes | REC-18, REC-S-01 | ❌ No | ✅ |
| 11 | Perfil de Paciente | DIAG-06, REC-18 | ❌ No | ✅ |
| 12 | Registro/Edición de Paciente | REC-16, REC-17, REC-19 | ❌ No | ✅ |
| 13 | Nueva Consulta (Ficha Clínica) | DIAG-01 | ✅ Flujo 1 | ✅ |
| 14 | Historial de Versiones de Ficha | DIAG-07 | ❌ No | ✅ |
| 15 | Panel de Análisis (worklist) | DIAG-09, DIAG-03, DIAG-04, DIAG-08 | ✅ Flujos 2 y 3 | ✅ |
| 16 | Detalle de Análisis | DIAG-03, DIAG-04, DIAG-08 | ✅ Flujos 2 y 3 | ✅ |
| 17 | Ingreso de Muestra | DIAG-02 | ✅ Flujo 1 | ✅ |
| 18 | Catálogo Tipos de Análisis/Muestra | DIAG-10 | ❌ No | ✅ |
| 19 | Informes Emitidos | DIAG-04 (post), DIAG-05 | ❌ No | ⚠️ "Reenviar/regenerar" FALTA DEFINIR (reconocido) |
| 20 | Portal de Resultados (paciente) | DIAG-05 | ✅ Flujo 3 (paso 4) | ✅ |
| 21 | Inventario | LAB-05, LAB-08 | ✅ Flujo 4 | ✅ |
| 22 | Ingreso de Insumos | LAB-01 | ✅ Flujo 4 | ✅ |
| 23 | Retiro de Insumos | LAB-02 | ✅ Flujo 4 | ✅ |
| 24 | Devolución de Insumos | LAB-09 | ✅ Flujo 4 | ✅ |
| 25 | Trazabilidad de Movimientos | LAB-07 | ❌ No | ✅ |
| 26 | Catálogos de Inventario | LAB-06, LAB-12, LAB-08 | ❌ No | ⚠️ No incluye categorías de residuos (ver hallazgo F1) |
| 27 | Registro de Residuo | LAB-03 | ❌ No | ✅ |
| 28 | Historial de Residuos | LAB-11 | ❌ No | ✅ |
| 29 | Disposición Final | RF-19 (sin UC dedicado) | ❌ No | ⚠️ Sin UC en requisitos (mapeo lo marca "— (RF-19)") |
| 30 | Reporte Mensual de Residuos | LAB-04 | ❌ No | ✅ |
| 31 | Reportes y Estadísticas | REP-01, LAB-13 | ❌ No | ✅ |
| 32 | Usuarios | SEG-02 | ❌ No | ✅ |
| 33 | Roles y Permisos | SEG-02 | ❌ No | ✅ |
| 34 | Equipos | — (sin UC) | ❌ No | ⚠️ FALTA DEFINIR (reconocido) |

**Resultado:** 34 pantallas. De ellas, solo **5** tienen flujo de trabajo paso a paso en §4 (Ficha/Muestra, Ejecución, Validación, QC inventario, Auditoría). Las otras **29** quedan descritas por acciones/estados pero **sin secuencia de trabajo ni manejo de edge cases por pantalla**.

---

## 3. Hallazgos (concretos y accionables)

### F1 — PANTALLA AUSENTE: Catálogo de Categorías de Residuos 🔴
- **Evidencia:** UC-LAB-10 (Gestionar Categorías de Residuos, Clase I/II/III + instrucciones de almacenamiento) y RF-17 exigen este catálogo. El BRIEF §3 menciona "Catálogos (… residuos …)" como módulo transversal, pero **§5 no tiene ninguna pantalla para gestionar categorías de residuos**.
- **Impacto:** La entidad `CategoriaResiduo` (con `clase_peligrosidad` y `InstruccionAlmacenamiento`) queda sin pantalla; el "Registro de Residuo" (§5) dice "categoría (Clase I/II/III, con instrucciones visibles)" pero no hay de dónde salga ni cómo se administra.
- **Acción:** Agregar pantalla **"Catálogo de Categorías de Residuos"** (Admin) con: nombre, clase de peligrosidad, descripción, pasos secuenciales de instrucción de almacenamiento, baja lógica. Actualizar "Catálogos de Inventario" para que sea "Catálogos de Recursos" o separar claramente.

### F2 — Los flujos de trabajo no están definidos "por pantalla" 🟠
- **Evidencia:** El usuario pidió "flujos de trabajo para cada pantalla". El BRIEF solo define flujos para el núcleo clínico (§4). Pantallas como Login, Usuarios, Roles y Permisos, Catálogos, Trazabilidad, Disposición Final, Historial de Residuos, Configuración, Bloqueos, Indicaciones y Reportes **no tienen secuencia de trabajo definida**.
- **Impacto:** Una IA que construya el sitio interpretará distinto cómo armar cada CRUD, confirmaciones, validaciones y vacíos.
- **Acción:** Para cada pantalla del §5 agregar una subsección **"Flujo de trabajo"** con: pasos numerados, reglas de habilitación/deshabilitado, manejo de estados vacíos y errores, y acciones de confirmación (no solo la lista de "Acciones" actual).

### F3 — Discrepancia de ubicación de pantallas entre §3 (árbol) y §5 🟠
- **Evidencia:**
  - "Nueva Consulta (Ficha Clínica)" aparece bajo **Análisis** en el árbol (§3, línea 111) pero bajo **Pacientes y Ficha Clínica** en §5 (línea 244).
  - El árbol no tiene nodo **"Catálogos"** aunque §3 declara "Catálogos" como módulo transversal (#10) y §5 define 3 pantallas de catálogo (Tipos de Análisis, Inventario, Indicaciones).
  - "Reporte de Inventario" (LAB-13) no aparece como pantalla propia; queda diluido en "Reportes y Estadísticas".
- **Impacto:** Sidebar inconsistente; la IA no sabe bajo qué módulo montar cada pantalla.
- **Acción:** Reflejar en el árbol la ubicación definitiva de cada pantalla de §5 (incluir nodo "Catálogos" transversal y decidir dónde vive "Nueva Consulta").

### F4 — Ambigüedad de roles sin resolver 🟠
- **Evidencia:** Varias pantallas marcan `⚠️` en el "usuario principal": Informes Emitidos ("ver quién lo consulta"), Disposición Final ("Admin/Bioquímico ⚠️"), Registro/Edición de Paciente ("⚠️ recepción"), Portal ("⚠️ doble verificación"). También la pregunta abierta §9 #11 (¿Profesor ve datos clínicos? ¿Admin ve resultados clínicos?).
- **Impacto:** Sin definir la matriz roles×pantallas, la IA no puede implementar permisos por pantalla (necesario para "Roles y Permisos").
- **Acción:** Definir una matriz explícita **Rol → Pantalla → Acción** en §5 o como anexo, antes de construir.

### F5 — Falta el formulario de completar demográficos en el turno 🟠
- **Evidencia:** UCE-REC-15 (paso 6, secuencia Presente) indica que al marcar "Presente" se muestra un formulario ligero para completar datos demográficos faltantes (Alta Temprana). El BRIEF §5 "Detalle/Acciones de Turno" no lo contempla como paso/estado.
- **Acción:** Agregarlo como estado/paso de la pantalla "Detalle/Acciones de Turno" (o modal "Completar datos del paciente").

### F6 — Login: flujo de recuperación de contraseña indefinido 🟡
- **Evidencia:** El BRIEF dice "recuperar (⚠️ sin flujo definido)". Como es la puerta de entrada, debería definirse (¿correo de reset? ¿reseteo por Admin?).
- **Acción:** Decidir y documentar, o eliminar la opción de recuperación de la UI si no aplica.

### F7 — Dashboard y "Informes Emitidos" dependen de preguntas abiertas 🟡
- **Evidencia:** Contenido exacto del dashboard FALTA DEFINIR; "Reenviar/regenerar OTP" FALTA DEFINIR (§9 #7). Estos afectan el diseño real de 2 pantallas.
- **Acción:** Resolver §9 (al menos #6, #7, #11, #12, #14) antes de fijar §5 y §6.

---

## 4. Qué SÍ está bien determinado (para no tocar)

- **Formato uniforme** de cada pantalla (objetivo · usuario · datos · acciones · estados) — excelente base.
- **Núcleo clínico (Ficha → Muestra → Panel → Detalle → Validación)**: pantallas y flujos bien definidos, con edge cases y errores.
- **Inventario (Ingreso/Retiro/Devolución/Inventario)**: reglas FEFO, umbrales y alertas claras (RF-18, LAB-08).
- **Sistema de estados (§6)**: tabla de transiciones completa y con colores semánticos.
- **Anti-patrones (§8) y prompts Figma (§10)**: guía de estilo accionable.

---

## 5. Recomendación de orden de trabajo

1. Cerrar **F1** (agregar pantalla de categorías de residuos) y **F5/F6**.
2. Definir la **matriz de roles × pantallas** (F4) — desbloquea Usuarios, Roles y Permisos y las ambigüedades `⚠️`.
3. Unificar el **árbol de navegación** con las pantallas de §5 (F3).
4. Agregar **"Flujo de trabajo" paso a paso por pantalla** a las 29 que no lo tienen (F2) — es el requisito explícito del usuario.
5. Resolver las preguntas abiertas de §9 que bloquean Dashboard e Informes Emitidos (F7).

---

*Documento de verificación generado a partir del estado actual del BRIEF (17/04/2026 y posteriores). Al aplicar los hallazgos, refinar §5, §6 y §10 como indica la nota final del BRIEF.*
