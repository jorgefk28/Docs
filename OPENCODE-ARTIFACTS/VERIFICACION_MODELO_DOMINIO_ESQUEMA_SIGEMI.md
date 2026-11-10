# Verificación del modelo de dominio (N2) y del esquema de BD (N3) contra los requisitos (N1)

> **Artefacto de análisis** — no es fuente de verdad. Vive en `OPENCODE-ARTIFACTS/` según `AGENTS.md`.
> **Fecha**: 2026-11-04
> **Fuente de verdad usada**: `TF_2026_Requerimientos_KLUKA_JORGE.md` (N1), `Diagramas/modelo_dominio_sigemi_unificado.md` (N2), `Diagramas/modelo_esquema_bd_sigemi.md` (N3).
> **Alcance de esta ronda**: verificación de cobertura, consistencia entre niveles y aptitud para iniciar codificación.
> **No se modificó ningún archivo de N1, N2 ni N3.**

## Método

1. Lectura completa de N1 (1.674 líneas): objetivos, subsistemas, módulos, IRQ-01..07, RF-01..21, RNF-01..05, actores ACT-01..04, UC-REC/DIAG/LAB/SEG/REP, UCE de Pacientes, Bioquímico, Seguridad y Reportes, glosario.
2. Lectura completa de N2 (215 líneas) y N3 (578 líneas, 44 tablas).
3. Trazabilidad inversa: cada RF, IRQ, UC y actor se buscó en N2 y en N3; cada concepto de N2 se buscó en N3.
3. Búsqueda dirigida de términos críticos en N1 para confirmar presencia o ausencia (`equipo`, `mantenimiento`, `garantía`, `espacio`, `facturación`, `lista de espera`, `recordatorio`, `actividad`, `diagnóstico`, `parámetro`, `hallazgo`, `bloqueo temporal`).
4. Contraste de las reglas que los propios documentos se imponen: N3 exige que todo aplanamiento de N2 esté documentado en "Correspondencia con el modelo de dominio" (N3:18-30); N2 exige que su diagrama exprese el negocio sin mecanismos (N2:7).

## Veredicto

**Los dos modelos NO están listos para iniciar codificación.** La estructura general es sólida —los cinco subsistemas de N1 están representados, las 44 tablas de N3 cubren la mayoría de los IRQ y el aparato de auditoría, versionado y OTP está bien pensado—, pero hay **8 hallazgos bloqueantes, 15 altos y ~20 medios** que generarán retrabajo de esquema y de código si se implementan tal cual.

Los tres problemas de fondo, en orden de impacto:

1. **Falta un subsistema completo: notificaciones y envíos por WhatsApp.** N1 lo exige en RF-01, RF-02, RF-03, RF-07 y en las postcondiciones de UC-REC-01, UC-REC-04 y UC-DIAG-04 ("programa en cola", "reintento automático", "ciclo hasta la descarga"). Ni N2 ni N3 tienen una sola entidad para eso. Es el hueco más caro: sin él, cuatro requerimientos funcionales no son implementables ni auditables.
2. **El turno no puede persistir lo que el propio flujo le exige.** No tiene `tipo_analisis_id` (UC-REC-20 p6 lo pide explícitamente), exige `profesional_id` y `espacio_id` que el Agente IA nunca elige, no tiene bloqueo temporal de 10 minutos y no se vincula al análisis que origina.
3. **N2 y N3 se contradicen en al menos cuatro puntos** (Agenda, Configuración→Período, Regla de Admisión, Turno→Análisis), y N3 incumple la regla de documentar todo aplanamiento.

Además hay **dos áreas sobre-modeladas sin respaldo en N1** (Equipos/Mantenimiento y Espacios/Grupos de espacios) y **un área sub-modelada con impacto normativo** (Actividad/Práctica, que RF-11 exige "por cada actividad").

---

## 1. Hallazgos bloqueantes

| ID | Hallazgo | Evidencia N1 | Evidencia N2/N3 | Impacto |
|---|---|---|---|---|
| **B-01** | **No existe modelo de notificaciones/recordatorios.** No hay entidad para mensaje enviado, cola, reintento, recordatorio programado ni historial de entrega. | RF-01 (L183), RF-02 (L189), RF-03 (L195), RF-07 (L219); UC-REC-01 postcondición "programa en cola el envío de un recordatorio" (L378, L811); UCE-DIAG-04 p9-p10 "registra el fallo y encola el reintento", "ciclo hasta la descarga" (L1438-1445); módulo 2.3.2.1 "envío de recordatorios" (L85) | Ausente en N2 (sección AGENDA/TRANSVERSALES, L29-77). Ausente en N3 (inventario completo de tablas, L34-565) | Cuatro RF no implementables; no se puede auditar la entrega ni el reenvío; no se puede cumplir RNF-01 (24/7) |
| **B-02** | **No existe el bloqueo temporal de 10 minutos.** El agente retiene horarios mientras el paciente elige. | UCE-REC-01 p4 "aplica un bloqueo temporal de 10 minutos" y excepción p5 "libera el bloqueo horario" (L807, L815); UCE-REC-03 p4 y excepción p5 (L856, L864) | Ausente en N2 y N3 | Doble reserva del mismo horario entre dos conversaciones simultáneas; no hay dónde poner el estado del bloqueo ni su expiración |
| **B-03** | **`turno` no registra el tipo de análisis solicitado.** | UCE-REC-01 (agendamiento para "análisis micológico"); UC-REC-20 p6 "selecciona: fecha, horario disponible, tipo de análisis" (L1248); RF-02 envía "las indicaciones correspondientes para su análisis" (L189) | N3 `turno` (L87-101) solo tiene `indicacion_medica_id` nullable; `indicacion_medica.tipo_analisis_id` es nullable (L110) | Se pierde qué estudio se reservó; la indicación enviada no es determinable con certeza; el panel y la agenda no pueden filtrar por estudio |
| **B-04** | **`analisis_micologico` no referencia al turno que lo origina, aunque N2 lo declara.** | UC-REC-15 p5 "habilita el botón para iniciar la consulta (UC-DIAG-01)" (L1110); UC-DIAG-02 "iniciando la trazabilidad del estudio" (L567) | N2: `Turno -->|"deriva en"| Analisis` (L104); N3 `analisis_micologico` (L114-127) sin `turno_id` | Contradicción N2→N3 no documentada; se pierde el vínculo reserva→estudio (trazabilidad de atención, métricas de conversión, auditoría) |
| **B-05** | **`turno.profesional_id` y `turno.espacio_id` son NOT NULL, pero ningún flujo los determina.** | UCE-REC-01: el Agente IA consulta "la agenda" y ofrece horarios; nunca pregunta por profesional ni espacio (L804-811) | N3 `turno` L94-95; `espacio_atencion` L201-211 | RF-01 (agendamiento por IA) no puede persistir el turno; obliga a decidir profesional y espacio en el flujo conversacional, cosa que N1 no pide |
| **B-06** | **No hay lugar definido para el diagnóstico final, los parámetros y las observaciones del análisis.** | IRQ-02 "Observaciones/Resultados parciales" (L124); UC-DIAG-03 "carga los parámetros, resultados parciales y observaciones" (L577, L1405); UC-DIAG-04 p3 "emite el diagnóstico final" y p5 "valida que todos los campos requeridos del resultado estén completos" (L1432-1434); glosario "Ficha Clínica … incluye … diagnóstico clínico" (L1671) | N3 `analisis_micologico` (L114-127) no tiene observaciones ni diagnóstico; `hallazgo_analisis` (L128-137) tiene `tipo_hallazgo`/`dato`/`estado_alcanzado`, sin relación declarada con "diagnóstico final" ni con "parámetros" | El PDF del informe se genera desde datos que no existen con nombre y forma definidos; la validación de "campos requeridos" no tiene contra qué validar |
| **B-07** | **Los campos clínicos estructurados de la ficha no están definidos en ningún nivel.** | IRQ-01 enumera **solo** datos demográficos (L109-117); RF-05 pide "información clínica estructurada" (L207); glosario exige "diagnóstico clínico" (L1671) | N2 se limita al concepto `Dato Clínico` (L16, L81); N3 lo resuelve como EAV `dato_clinico(campo, valor, tipo_dato)` (L62-70) | No se puede construir el formulario de ficha clínica ni validar obligatorios: falta la decisión de producto sobre qué campos clínicos existen |
| **B-08** | **Nada registra si el informe fue descargado, condición de corte del reenvío automático de OTP.** | RF-07 "repitiendo el ciclo hasta la descarga del informe" (L219); UCE-DIAG-04 p10 (L1439); UCE-DIAG-05 postcondición (L1470) | N3 `informe_resultados` (L139-147): sin `descargado_en` ni `descargas`; `otp.usado` (L157) es el único proxy, y se usa también para invalidación por reemisión | El ciclo automático no tiene condición de corte verificable; se reenviarían OTP indefinidamente o se cortaría por un dato semánticamente ajeno |

---

## 2. Hallazgos altos

| ID | Hallazgo | Evidencia |
|---|---|---|
| **A-01** | **El actor Profesor (ACT-02) no existe en N2.** N1 le asigna retiros de insumos, registro de residuos y consulta de inventario/trazabilidad. N2 solo modela `Profesional` y `Administrador`. | ACT-02 (L355-358); N2 `PERSONAS Y ACCESO` (L23-27) y relaciones L92-97 |
| **A-02** | **N2 atribuye `Movimiento de Inventario` solo a `Profesional`,** contradiciendo a N1: los ingresos los hace el Administrador y los retiros el Profesor o el Bioquímico. | UC-LAB-01 (L645-647), UC-LAB-02 (L653-655); N2 L138 `Profesional --> ejecuta Movimiento` |
| **A-03** | **El Agente IA no está modelado como componente/actor.** Crea el paciente en Alta Temprana y el turno, y opera 24/7. Sin él no se explica el origen de `nivel_registro='temprano'` ni quién ejecuta el agendamiento. | RF-01 (L183), RNF-01 (L311), glosario "Alta Temprana" (L1669), UC-REC-01 (L376); ausente en N2 y N3 |
| **A-04** | **Subsistema Equipos completo sin respaldo en N1.** N1 no tiene requisito, módulo, caso de uso ni IRQ de equipos, mantenimiento ni garantías. La única aparición de "equipo" es como *ejemplo de categoría de insumo*. N2 le dedica un subgrafo y N3 tres tablas. | N1: `equipo` aparece 1 vez, como categoría (L745); `mantenimiento` 0 veces; N2 subgrafo EQUIPOS (L65-69, L149-152); N3 `tipo_equipo`/`equipo`/`mantenimiento_equipo` (L476-516) |
| **A-05** | **Espacios de atención, grupos de espacios y bloqueo por espacio sin respaldo en N1.** N1 solo conoce "cantidad máxima de turnos por franja" en la configuración de agenda; "espacio" aparece siempre como "espacio en la agenda" (sentido temporal). | UC-REC-07 (L424), UC-REC-08 (L432); N1 `espacio` (L386-883, todas coloquiales); N2 `Espacio`/`GrupoEspacio` (L37-38); N3 `espacio_atencion`/`grupo_espacio` (L201-221) |
| **A-06** | **Tres fuentes de capacidad simultáneas sin regla de precedencia:** `configuracion_agenda.max_turnos_por_franja`, `espacio_atencion.capacidad_paralela` y `disponibilidad_profesional.max_turnos_por_franja`. El cálculo de disponibilidad (postcondición de UC-REC-07) queda indeterminado. | N3 L241, L208, L283; UC-REC-07 "aplicados para el cálculo de disponibilidad horaria del Agente IA" (L426) |
| **A-07** | **`auditoria.usuario_id` NOT NULL no cubre a los actores reales.** Hay eventos generados por procesos automáticos (UC-REC-14 p5), por el Agente IA (agendamiento del paciente) y por el Paciente (portal OTP); ninguno es un `usuario`. | UCE-REC-14 p5 (L1085); UC-REC-01 (agente); UCE-DIAG-05 (paciente anónimo); N3 `auditoria` L528 |
| **A-08** | **`paciente.dni` sin restricción UNIQUE**, aunque el flujo exige unicidad explícitamente. | UCE-REC-16 p4 "valida que el DNI no exista previamente" (L1138) y excepción (L1143); UCE-REC-17 excepción (L1173); N3 L40 `dni varchar` y solo índice sugerido (L319) |
| **A-09** | **La Alta Temprana es incompatible con la nulabilidad implícita de `paciente`.** El agente crea el registro con DNI y Nombre Completo; el resto de los campos (fecha de nacimiento, domicilio, obra social, correo, `numero_registro`) llega después. N3 no declara nulabilidad y `numero_registro` es `unique` sin regla de generación. | Glosario (L1669), UCE-REC-01 p2 (L805), UCE-REC-15 p6 "datos demográficos incompletos" (L1108); N3 `paciente` L39-41 |
| **A-10** | **`indicacion_medica.tipo_analisis_id` es nullable en N3, pero N1 lo exige obligatorio.** | UCE-REC-10 p2 "(obligatorio)" y p4 validación (L996-998, L1004); N3 L110 |
| **A-11** | **No existe el concepto Actividad / Práctica educativa, y RF-11 pide residuos "por cada actividad".** `practica_educativa` es un booleano (no identifica la práctica) y el residuo solo puede vincularse a un análisis. Se pierde la trazabilidad que UC-LAB-07 muestra como columna. | RF-11 (L243), UC-LAB-03 (L661), UC-LAB-02 (L653), IRQ-06 "análisis o práctica asociada" (L164), UC-LAB-07 (L698); N3 `movimiento_inventario.practica_educativa boolean` (L406) y `residuo_quimico` sin vínculo a práctica (L438-450) |
| **A-12** | **Contradicción N2 ↔ N3: `Configuración de Agenda → Período Inhábil`.** N2 la declara; N3 dice que se descarta. Gana N2 (nivel superior), así que N3 está defectuoso —o hay que corregir N2, que es lo correcto si la decisión se mantiene. | N2 L106 `ConfigAgenda -->|"declara"| Periodo`; N3 L258 "La relación `ConfiguracionAgenda → PeriodoInhabilitado` del `.mmd` se descarta" |
| **A-13** | **El concepto `Agenda` de N2 no tiene realización en N3 ni está documentado como aplanamiento.** N2 hace que Configuración "rija" la Agenda y que Períodos y Bloqueos la inhabiliten. En N3 no hay tabla `agenda`. | N2 L32, L100, L105-112; N3 no tiene `agenda`; tabla de correspondencia (L22-30) no lo menciona |
| **A-14** | **`otp.codigo` se almacena en claro.** RF-07 y RNF-02 exigen generación criptográfica y trato seguro; un OTP en claro en BD es una credencial de acceso a datos clínicos. | RF-07 (L219), RNF-02 (L317); N3 L155 |
| **A-15** | **No está definida la representación de la reprogramación/reasignación**, y de ella dependen RF-03 (recursión), `turno.reprogramaciones` y la auditoría. Si se mueve la fila, se pierde quién tenía el horario; si se crea otra, `oferta_reagendacion.turno_id` queda apuntando a un turno cancelado. | RF-03 (L195), UCE-REC-04 p6-p7 (L883-884), UCE-REC-22 (L1300-1313); N3 `oferta_reagendacion.turno_id` (L304), `turno.reprogramaciones` (L99) |

---

## 3. Hallazgos medios

| ID | Hallazgo | Evidencia |
|---|---|---|
| **M-01** | `usuario.correo_electronico` sin UNIQUE, aunque es el identificador de login. | UCE-SEG-01 p2 (L1620); N3 L165 |
| **M-02** | `usuario.rol_id` es un único FK, pero ACT-03 dice que el Administrador "cumple la misma función que un Bioquímico". Hay que documentar si la acumulación se resuelve por jerarquía de permisos o por N:M. | ACT-03 (L362); N3 L165 |
| **M-03** | **Aplanamiento no documentado: `Regla de Admisión` (N2) → `tipo_analisis_tipo_muestra` (N3).** N2 la trata como concepto con relaciones propias; N3 como tabla de pares. La tabla de correspondencia no lo registra, y N3 se autoimpone documentarlo. | N2 L47, L123-124; N3 L188-197, regla en L20 |
| **M-04** | **Traducción no documentada: `Motivo de Bloqueo` (N2) → `tipo_bloqueo` + `motivo` libre (N3).** Además el catálogo `tipo_bloqueo` no existe en N2. | N2 L36, L108-110; N3 L223-229, L254, L271 |
| **M-05** | **La devolución de un lote vencido no tiene marca de "no utilizable".** UC-LAB-09 pide registrar la devolución como "Vencido — no utilizable", pero el único efecto modelado es incrementar stock. | UCE-LAB-09 comentario (L719); N3 `movimiento_inventario` L394-409 |
| **M-06** | **Parámetros de negocio sin lugar:** política de 24 h, límite de 2 reprogramaciones, ventana previa del recordatorio ("configurada"), ventana nocturna 22:00–08:00, TTL OTP 7 días, plazo de 2 h de la oferta, 5 intentos de login. Quedan como constantes dispersas en código. | UCE-REC-02 excepción (L839), UCE-REC-03 (L851, L863), UCE-REC-01 postcondición (L378), UCE-REC-04 p2 (L879), RNF-02 (L317), UCE-SEG-01 excepción (L1630) |
| **M-07** | **`reporte_residuos.usuario_id` NOT NULL contra "generar automáticamente" (RF-12).** Un job programado no tiene usuario. | RF-12 (L249), UC-LAB-04 (L670); N3 L467 |
| **M-08** | **UC-LAB-11 exige "no incluido en un reporte ya emitido", pero no hay vínculo residuo→reporte.** Se resuelve por superposición de rangos de fecha, lo que es frágil y no impide reportes solapados. | UCE-LAB-11 precondición (L737); N3 nota de modelado (L474) |
| **M-09** | **Estrategia mixta para los hijos de `Reporte`:** un hijo como tabla especializada (`reporte_residuos`), otro como fila genérica (`tipo_reporte`), otro inexistente (`reporte_inventario`). Además `reporte_residuos` duplica casi todas las columnas de `reporte` sin FK entre ambas: dos fuentes para el mismo artefacto. | N2 L73-76, L158-160; N3 L462-474, L550-564, hueco 1 (L574-576) |
| **M-10** | **`muestra` 1:1 no es un supuesto seguro.** OBJ-01 menciona "citas múltiples para estudios prolongados (ej. análisis de uñas)" y OBJ-02/contexto hablan de esperas de hasta un mes: un estudio puede requerir varias visitas/tomas. El aplanamiento depende de 1:1. | OBJ-01 comentarios (L41), contexto (L31), OBJ-02 (L45); N2 hueco 1 (L214); N3 hueco 3 (L577-578) |
| **M-11** | **`dato_clinico` (EAV) sin regla de actualización ni unicidad**, y `ficha_clinica.version_actual` sigue "candidato a derivar". No está definido qué representa la tabla: ¿estado actual, o histórico? | N3 L59, L62-70 |
| **M-12** | **`otp.analisis_id` cuando UC-DIAG-04 dice "asociado al informe".** Inconsistente entre niveles y semánticamente distinto ante regeneraciones. | UCE-DIAG-04 p8 (L1437); N3 L154 |
| **M-13** | **N2 solo permite que el Administrador defina indicaciones**; N1 da esa capacidad también al Bioquímico/Doctor. | UC-REC-10 (L441), UC-REC-11 (L449), UC-REC-12 (L457); N2 L96 |
| **M-14** | **`turno` no registra el motivo de inasistencia**, que UC-REC-15 pide capturar (opcional). | UCE-REC-15 Ausente p3-p4 (L1114-1115); N3 L100 solo tiene motivo de cancelación/reprogramación |
| **M-15** | **Reglas de lote sin documentar:** `UNIQUE(insumo_id, numero_lote)` no declarada y la regla FEFO de RF-18 no aparece como regla del modelo. | RF-18 (L285); N3 `lote` L379-392 |
| **M-16** | **Unicidades faltantes en relaciones 1:1/1:N:** `informe_resultados(analisis_id)`, `version_ficha_clinica(ficha_clinica_id, numero_version)`, `dato_clinico(ficha_clinica_id, campo)`, `otp(codigo)`. | UCE-DIAG-04 (un informe por análisis), RF-20 (versiones), N3 L72-85, L139-158 |
| **M-16b** | **`configuracion_agenda` se describe como singleton pero no lo declara ni lo restringe.** | N3 L231-243, L258 |
| **M-17** | **RNF-04 (retención 10 años e inmutabilidad) solo está como convención.** No hay mecanismo declarado (sin `borrado_en` en tablas clínicas, sin política de purga, sin triggers). | RNF-04 (L329); N3 convenciones (L16) |
| **M-18** | **La anonimización de reportes clínicos no está modelada ni documentada.** UC-REP-01 p5 la exige como regla del backend. | UCE-REP-01 p5 (L1649), UC-REP-01 (L791) |
| **M-19** | **`tipo_bloqueo` vs `motivo` libre duplican el mismo dato** (dos formas de decir por qué se bloquea). | N3 L265, L271 |
| **M-20** | **`categoria_insumo` incluye "equipos" como ejemplo, contradiciendo la existencia de un subsistema Equipos separado.** | N1 L745; N3 L349 |
| **M-21** | **OBJ-01 menciona "facturación" y ningún RF/UC la cubre.** Es una ambigüedad de alcance de N1 que los modelos resuelven omitiéndola: hay que confirmarlo. | OBJ-01 (L39) |

---

## 4. Hallazgos bajos y defectos documentales

| ID | Hallazgo |
|---|---|
| **b-01** | N2 §5.1 invoca `TrazabilidadAnalisis` como si existiera; no está en el diagrama ni en N3. |
| **b-02** | N2 §4.9 afirma que `Equipo → Ubicación` se "unificó" con el catálogo de inventario: correcto, pero el desenvolvimiento en N3 agrega `equipo.ubicacion_id` obligatorio sin regla de baja. |
| **b-03** | `hallazgo_analisis.estado_alcanzado` no tiene semántica declarada en ningún nivel. |
| **b-04** | `reporte.tipo_reporte` no tiene dominio de valores declarado (clínico/inventario/desechos según UC-REP-01). |
| **b-05** | `usuario.estado` no declara valores (falta "bloqueado temporal", exigido por UCE-SEG-01). |
| **b-06** | `lote.estado` (activo/agotado/vencido) es derivable de `cantidad_actual` y `fecha_vencimiento`: decidir si se persiste. |
| **b-07** | `analisis_micologico` no registra fecha de inicio de proceso ni de término (solo creación y validación), lo que limita filtros del panel por fecha de trabajo. |
| **b-08** | `paciente.numero_registro` no tiene regla de generación (¿institucional, secuencial, por año?). |
| **b-09** | `informe_resultados` no declara unicidad y `otp` no declara índice por `codigo` para la validación del portal. |
| **b-10** | UC-SEG-03 (cerrar sesión) con JWT stateless no tiene mecanismo de revocación declarado; aceptable por convención, pero conviene dejarlo escrito. |
| **b-11** | `turno` no registra el canal de origen (Agente IA vs. manual), útil para auditoría y para distinguir el flujo. |
| **b-12** | `version_ficha_clinica` no declara que `datos_previos/nuevos` contienen la ficha completa o solo el delta. |
| **b-13** | N3 hueco 2 (columnas de ingreso de muestra) y hueco 1 (reporte de inventario) siguen abiertos: son decisiones, no defectos, pero deben cerrarse antes de codificar. |

---

## 5. Matriz de cobertura

### 5.1 Requisitos funcionales

| RF | Cobertura | Observación |
|---|---|---|
| RF-01 Agente IA | **Parcial** | Falta bloqueo temporal (B-02), `tipo_analisis` en turno (B-03), profesional/espacio obligatorios (B-05), notificaciones (B-01) |
| RF-02 Indicaciones | **Sí** | `indicacion_medica` OK; falta que el turno conserve el tipo de estudio (B-03) |
| RF-03 Reagendación | **Parcial** | `oferta_reagendacion` bien anclada en turno; falta notificación, ventana nocturna parametrizada (M-06) y representación de reprogramación (A-15) |
| RF-04 Cancelar/Reprogramar | **Sí** | Estados y motivos presentes |
| RF-05 Ficha clínica | **Parcial** | Datos demográficos completos; campos clínicos indefinidos (B-07) |
| RF-06 Estados análisis | **Sí** | Estados y transiciones representables |
| RF-07 OTP + reenvío | **Parcial** | Falta marca de descarga (B-08), log de notificaciones (B-01), intentos/bloqueo del portal (A-12→ver M) |
| RF-08 Descarga PDF | **Parcial** | `hash_archivo` bien; falta bloqueo por intentos fallidos del OTP |
| RF-09 Alertas stock | **Sí** | `umbral_minimo`, `dias_alerta_vencimiento` |
| RF-10 Ingresos/retiros | **Sí** | `movimiento_inventario` completo |
| RF-11 Residuos por actividad | **Parcial** | Falta Actividad (A-11) |
| RF-12 Reporte mensual | **Parcial** | `reporte_residuos` existe; `usuario_id` NOT NULL vs automático (M-07); vínculo residuo→reporte (M-08) |
| RF-13 Cuentas | **Sí** | Con M-01, M-02 |
| RF-14 Auditoría | **Parcial** | Bien estructurada; actor no cubierto (A-07) |
| RF-15 Consolidar/exportar | **Parcial** | `reporte` genérica; anonimización no modelada (M-18) |
| RF-16 Catálogos clínicos | **Sí** | `tipo_analisis`, `tipo_muestra`, N:N |
| RF-17 Catálogos inventario | **Sí** | Categorías insumo, ubicaciones, categorías residuo |
| RF-18 Lotes y FEFO | **Parcial** | `lote` completo; FEFO sin documentar (M-15) |
| RF-19 Disposición final | **Sí** | `disposicion_final` N:1 |
| RF-20 Modificación ficha | **Sí** | `version_ficha_clinica` (con M-11) |
| RF-21 Cancelar análisis | **Sí** | Estado + motivo |

### 5.2 Requisitos de información

| IRQ | Cobertura | Observación |
|---|---|---|
| IRQ-01 Ficha/paciente | **Parcial** | Demográficos OK; "Edad" correctamente no persistida; falta nulabilidad de Alta Temprana (A-09) |
| IRQ-02 Análisis | **Parcial** | Tipo de muestra y estados OK; faltan observaciones/resultados/diagnóstico (B-06) y fecha de ingreso de muestra (hueco declarado) |
| IRQ-03 Insumo | **Sí** | `stock_actual` derivado, decisión documentada |
| IRQ-04 Residuo | **Sí** | Volumen, peso, fecha/hora, usuario, categoría |
| IRQ-05 Catálogo clínico | **Sí** | Con indicaciones vía `indicacion_medica` |
| IRQ-06 Movimiento | **Parcial** | Falta identidad de la práctica (A-11) |
| IRQ-07 Categoría residuo | **Sí** | Con instrucciones ordenadas |

### 5.3 Casos de uso

- **UC-REC (23):** cubiertos, con B-02, B-03, B-05, A-08, A-09, M-13, M-14.
- **UC-DIAG (10)**: UC-DIAG-01..10 cubiertos, con B-06, B-07, B-08, A-12/M-12.
- **UC-LAB-01..13**: 01-12 cubiertos con A-11, M-05, M-08; **UC-LAB-13 (Reporte de Inventario) sin realización** (hueco declarado en N3).
- **UC-SEG-01..03**: cubiertos con M-01, M-02, b-10.
- **UC-REP-01**: cubierto con M-18.

### 5.3 Actores

| Actor | N2 | N3 |
|---|---|---|
| ACT-01 Bioquímico/Doctor | **Sí** (`Profesional`) | **Sí** (`profesional`) |
| ACT-02 Profesor | **No** (A-01) | **Sí**, como fila de `rol` |
| ACT-03 Administrador | **Sí** | **Sí**, con M-02 |
| ACT-04 Paciente | **Sí** | **Sí**, sin credenciales |
| Agente IA (sistema) | **No** (A-03) | **No** |

---

## 6. Decisiones que hay que cerrar antes de escribir código

Ordenadas por cuánto bloquean.

1. **Notificaciones (B-01).** ¿Entidad `notificacion` persistida (canal, plantilla, estado, intentos, error, fecha programada, fecha de envío, entidad origen) o solo cola técnica? Recomendación: persistirla. Es la única forma de cumplir "programa en cola", "registra el fallo y encola el reintento" y de auditar entregas.
2. **Bloqueo temporal de horario (B-02).** Tabla de retención con `expira_en` + índice único parcial por franja, o estado `reservado_temporal` en el turno. Recomendación: retención separada, para no ensuciar el ciclo de vida del turno.
3. **Turno: qué guarda (B-03, B-05, A-15).** Decidir si `tipo_analisis_id` es obligatorio en `turno`, si `profesional_id`/`espacio_id` son nullable (o si la agenda es por profesional/espacio, lo que cambia el modelo de disponibilidad), y si reprogramar mueve la fila o crea una nueva.
4. **Resultado del análisis (B-06).** Definir si el par `hallazgo_analisis` es el resultado estructurado (con catálogo de tipos de hallazgo y valores) y agregar explícitamente `diagnostico_final`/`observaciones` en `analisis_micologico`, o documentar que todo vive en `hallazgo`.
5. **Campos clínicos de la ficha (B-07).** Es una decisión de producto: qué campos estructurados tiene la ficha (síntomas, antecedentes, lesión, diagnóstico presuntivo…) y si se modelan como catálogo de campos + EAV (lo actual) o como columnas tipadas. Sin esto, el EAV no tiene contrato.
6. **Descarga del informe (B-08).** Agregar `descargado_en`/`descargas` a `informe_resultados` y usarlo como corte del ciclo de OTP.
7. **Alcance de Equipos y Espacios (A-04, A-05).** Tres opciones: (a) se eliminan de N2/N3; (b) se agregan a N1 como requisitos explícitos; (c) se declaran como extensión fuera del alcance de la tesis. Recomendación: (a) o (c), porque hoy son 3 tablas y un subgrafo sin actor ni RF.
8. **Actividad / Práctica educativa (A-11).** Si la trazabilidad "por actividad" se exige (RF-11 la nombra), promover a entidad con su propio registro y FK desde movimiento y residuo.
9. **Unicidad y nulabilidad (A-08, A-09, M-01, M-16).** Fijar constraints: `paciente.dni` UNIQUE; `usuario.correo_electronico` UNIQUE; `paciente` nullable en todo lo que la Alta Temprana no trae; `numero_registro` generado o nullable.
10. **Reportes (M-07, M-08, M-09).** Una sola estrategia: colapsar `reporte_residuos` en `reporte` con `tipo_reporte`, o crear `reporte_inventario` y dejar tres tablas especializadas. Definir además `usuario_id` nullable para reportes automáticos y si el bloqueo de UC-LAB-11 se logra por rango o por vínculo explícito.
10b. **Auditoría (A-07).** `usuario_id` nullable + campos `actor_tipo` (usuario/paciente/sistema/agente) y `actor_id`, o un usuario técnico del sistema.
11. **OTP (A-14, M-12).** Guardar hash del código, asociarlo al informe, y agregar intentos/bloqueo por OTP.
12. **Lista de espera (no listada arriba como bloqueante pero decidir):** el módulo 2.3.2.1 promete "lista de espera que notifica liberaciones de fechas" y UCE-REC-01 ofrece "suscribirse a alertas de cancelación". Nada lo modela. ¿Se implementa o se recorta del alcance?
13. **Facturación (M-21) y cardinalidad muestra↔análisis (M-10).** Dos preguntas de alcance que conviene hacer al cliente antes de congelar el esquema.

---

## 7. Lo que está bien y conviene no tocar

- La **jerarquía de tres niveles** está bien aplicada: N2 sin claves ni mecanismos, N3 con tipos, índices y decisiones explícitas.
- La **decisión de derivar `stock_actual`** y no persistirlo está bien fundada y documentada.
- El **aplanamiento de `Muestra`** está documentado con su condición de ruptura (N3:30): eso es exactamente cómo debe tratarse un aplanamiento.
- El tratamiento de **`Reporte` como padre con `Informe de Resultados` fuera** (N2:208) es correcto conceptualmente.
- La **auditoría append-only con `cambio_auditoria`** cubre RF-14 con buena granularidad.
- El **versionado de ficha con snapshots jsonb** cubre RF-20 y la inmutabilidad de N1.
- La **separación tipo/instancia** en análisis, muestras, equipos y residuos es consistente.
- Las **decisiones de Agenda** (período independiente de la configuración, oferta anclada al turno liberado, grupo por FK) son acertadas; solo falta propagar dos de ellas a N2 (A-12, A-13).

---

## Resumen numérico

| Severidad | Cantidad |
|---|---|
| Bloqueantes | 8 |
| Altos | 15 |
| Medios | 21 |
| Bajos / documentales | 13 |
| **Total** | **57** |
