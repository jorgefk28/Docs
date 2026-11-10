# Modelo de Esquema de Base de Datos — SIGEMI

> **Estatus**: **fuente de verdad — nivel 3 (persistencia)**, según `AGENTS.md`.
> **Deriva de**: `Diagramas/modelo_dominio_sigemi_unificado.md` (nivel 2) y, en última instancia, de `TF_2026_Requerimientos_KLUKA_JORGE.md` (nivel 1). Si este documento contradice el nivel 2, el nivel 2 gana y este archivo es el defectuoso.
> **Nivel de abstracción**: 3 — Persistencia / Modelo Relacional.
> **Propósito**: definir *cómo se guarda* el sistema en PostgreSQL: tablas, columnas, tipos, claves e índices.
> **Regla de oro**: acá SÍ hay `id`, `FK`, tipos SQL, e índices. Incluye los mecanismos (versionado, auditoría, OTP) que el dominio conceptual excluye.
> **Decisiones fijadas**: claves primarias **UUID**; ORM **SQLAlchemy**; migraciones **Alembic**; versionado de ficha clínica en **jsonb**; `version_actual` persistido.
> **Alcance**: sistema completo, por subsistemas.

## Convenciones

- PK = `UUID`, generada en la aplicación (no `uuid_generate_v4()` servidor, para portabilidad).
- Fechas/timestamps en **UTC**.
- `estado` como `VARCHAR` con valores acotados por la aplicación (o `ENUM` nativo si el equipo lo decide; por defecto `VARCHAR` + constraint de app).
- Borrado lógico: `estado = 'inactivo'` / campo `borrado_en` según la tabla, **nunca** delete físico sobre datos clínicos.

## Correspondencia con el modelo de dominio (nivel 2)

Este nivel **traduce** el modelo conceptual; no tiene por qué corresponderle 1:1. Lo obligatorio es que cada aplanamiento o especialización quede **documentado acá**: un aplanamiento no documentado es una contradicción entre niveles.

| Concepto (nivel 2) | Realización (nivel 3) | Tipo de traducción |
|---|---|---|
| `Muestra` | columnas de `analisis_micologico` (`tipo_muestra_id`) | **aplanada** (relación 1:1) |
| `Reporte` (padre) | `reporte` genérica (`tipo_reporte`) + `reporte_residuos` especializada | **especializada** por tabla |
| `Dato Clínico` | `dato_clinico` | directa |
| `Registro de Auditoría` | `auditoria` + `cambio_auditoria` | 1:N |
| `Usuario` ↔ roles | `usuario` + `rol` (`rol_id`) | **divergencia deliberada**: el dominio trata el rol como responsabilidad, el esquema como entidad |

**`Muestra` aplanada.** El nivel 2 define `Muestra` como concepto propio (extraída del paciente, tipificada por `Tipo de Muestra`), con cardinalidad **asumida 1:1** con `Análisis Micológico`. Por ser 1:1, este nivel la aplana en `analisis_micologico.tipo_muestra_id` en vez de crear una tabla propia. **Si esa cardinalidad deja de ser 1:1** (varias muestras por análisis, o una muestra reutilizada), el aplanamiento se rompe y hay que crear la tabla `muestra`.

## Tablas

### `paciente`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `numero_registro` | `varchar` unique | identificador institucional |
| `dni` | `varchar` | dato sensible; justificar necesidad |
| `nombre` / `apellido` | `varchar` | |
| `fecha_nacimiento` | `date` | |
| `sexo` | `varchar` | |
| `domicilio` / `telefono` | `varchar` | `telefono` es clave para contacto WhatsApp |
| `correo_electronico` | `varchar` | |
| `obra_social` | `varchar` | |
| `nivel_registro` | `varchar` | 'temprano' cuando lo crea el Agente IA, 'completo' al registrar ficha |
| `estado` | `varchar` | activo / inactivo (baja lógica) |
| `fecha_ingreso` | `timestamptz` | |

### `ficha_clinica`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `paciente_id` | `uuid FK → paciente` | |
| `profesional_id` | `uuid FK → profesional` | quién registró |
| `fecha_consulta` | `timestamptz` | |
| `version_actual` | `int` | puntero a la versión vigente (se calcula; candidato a derivar en vez de persistir) |
| `estado` | `varchar` | |

### `dato_clinico`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `ficha_clinica_id` | `uuid FK → ficha_clinica` | |
| `campo` | `varchar` | clave del dato (ej. 'sintoma', 'antecendente') |
| `valor` | `text` | |
| `tipo_dato` | `varchar` | |

### `version_ficha_clinica`  _(mecanismo de inmutabilidad)_

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `ficha_clinica_id` | `uuid FK → ficha_clinica` | |
| `numero_version` | `int` | |
| `datos_previos` | `jsonb` | |
| `datos_nuevos` | `jsonb` | |
| `usuario_id` | `uuid FK → usuario` | |
| `fecha_modificacion` | `timestamptz` | |
| `motivo` | `varchar` | |

> Nota: `datos_previos/nuevos` hoy están como `text` en el `.mmd`; acá se proponen `jsonb` por eficiencia de consulta. Se valida en la migración.

### `turno`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `paciente_id` | `uuid FK → paciente` | |
| `indicacion_medica_id` | `uuid FK → indicacion_medica` nullable | |
| `profesional_id` | `uuid FK → profesional` | |
| `espacio_id` | `uuid FK → espacio_atencion` | (se referencia aunque la tabla completa sea de segunda pasada) |
| `fecha_hora` | `timestamptz` | |
| `telefono_contacto` | `varchar` | |
| `estado` | `varchar` | confirmado / pendiente / cancelado / atendido / no_asistio |
| `reprogramaciones` | `int` | |
| `motivo_cancelacion` / `motivo_reprogramacion` | `varchar` | |
| `fecha_creacion` / `fecha_atencion` | `timestamptz` | |

### `indicacion_medica`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `titulo` | `varchar` | |
| `contenido` | `text` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` nullable | |
| `estado` | `varchar` | activa / inactiva (eliminación lógica, ver UC-REC-12) |
| `fecha_creacion` / `fecha_modificacion` | `timestamptz` | |

### `analisis_micologico`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `ficha_clinica_id` | `uuid FK → ficha_clinica` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` | |
| `tipo_muestra_id` | `uuid FK → tipo_muestra` | |
| `profesional_responsable_id` | `uuid FK → profesional` | quién *realiza* |
| `profesional_validador_id` | `uuid FK → profesional` nullable | quién *valida* (firma) |
| `estado` | `varchar` | pendiente / en_proceso / terminado / validado / cancelado |
| `fecha_creacion` / `fecha_validacion` | `timestamptz` | |
| `motivo_cancelacion` | `varchar` | |

### `hallazgo_analisis`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `analisis_id` | `uuid FK → analisis_micologico` | |
| `tipo_hallazgo` | `varchar` | |
| `dato` | `text` | |
| `estado_alcanzado` | `varchar` | |
| `fecha` | `timestamptz` | |

### `informe_resultados`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `analisis_id` | `uuid FK → analisis_micologico` | |
| `ruta_archivo` | `varchar` | |
| `fecha_generacion` | `timestamptz` | |
| `hash_archivo` | `varchar` | integridad del PDF |

### `otp` _(mecanismo de entrega segura)_

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `analisis_id` | `uuid FK → analisis_micologico` | |
| `codigo` | `varchar` | |
| `fecha_generacion` / `fecha_expiracion` | `timestamptz` | TTL 7 días |
| `usado` | `boolean` | |
| `fecha_uso` | `timestamptz` nullable | |

### `usuario` / `rol` / `profesional`

| tabla | columnas | notas |
|---|---|---|
| `rol` | `id uuid PK`, `nombre`, `descripcion` | |
| `usuario` | `id uuid PK`, `rol_id FK`, `nombre`, `apellido`, `correo_electronico`, `contrasena_hash`, `estado`, `intentos_fallidos`, `bloqueado_hasta`, `fecha_registro` | `contrasena_hash` → JWT/BCrypt |
| `profesional` | `id uuid PK`, `usuario_id FK (unique)`, `matricula`, `especialidad`, `estado` | 1:1 con `usuario` |

## Catálogos de Análisis

### `tipo_analisis`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | ej. 'cultivo de uñas', 'directo micológico' |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `tipo_muestra`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | ej. 'uña', 'piel', 'pelo' |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `tipo_analisis_tipo_muestra` _(relación N:N)_

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` | |
| `tipo_muestra_id` | `uuid FK → tipo_muestra` | |
| — | `UNIQUE(tipo_analisis_id, tipo_muestra_id)` | evita pares duplicados |

> Regla de negocio: solo se puede registrar un análisis o agendar un turno si la combinación `tipo_analisis × tipo_muestra` está admitida en esta tabla.

## Agenda y Atención

### `espacio_atencion`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` | |
| `tipo_espacio` | `varchar` | consultorio / box de toma de muestra |
| `capacidad_paralela` | `int` | cuántos turnos simultáneos admite |
| `grupo_espacio_id` | `uuid FK → grupo_espacio` nullable | pertenencia a un grupo (para bloqueo masivo) |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `grupo_espacio`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` | |
| `descripcion` | `text` | |

> Decisión (bache #3 resuelto): un grupo *agrupa* N espacios; la pertenencia vive como FK en `espacio_atencion.grupo_espacio_id` (nullable). No hay ningún campo en `grupo_espacio` apuntando a espacios. Un bloqueo con `grupo_espacio_id` inhabilita todos los espacios del grupo con una sola instrucción.

### `tipo_bloqueo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | feriado, mantenimiento, receso, otro |
| `descripcion` | `text` | |

### `configuracion_agenda`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `dias_habiles` | `varchar[]` | ej. `['L','M','X','J','V']` |
| `horario_inicio_manana` / `horario_fin_manana` | `time` | |
| `horario_inicio_tarde` / `horario_fin_tarde` | `time` | |
| `duracion_turno` | `int` | minutos |
| `intervalo_entre_turnos` | `int` | minutos |
| `max_turnos_por_franja` | `int` | |
| `usuario_modificacion_id` | `uuid FK → usuario` | quién la cambió |
| `fecha_modificacion` | `timestamptz` | |

### `periodo_inhabilitado`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `tipo_bloqueo_id` | `uuid FK → tipo_bloqueo` | |
| `usuario_id` | `uuid FK → usuario` | quién lo declaró |
| `fecha_inicio` / `fecha_fin` | `date` | |
| `hora_inicio` / `hora_fin` | `time` nullable | |
| `motivo` | `varchar` | |
| `recurrencia` | `varchar` | ninguna / semanal / anual |
| `estado` | `varchar` | |

> **Bache #1 resuelto**: `PeriodoInhabilitado` es independiente de `ConfiguracionAgenda`. La config es un singleton que "rige" la agenda (horarios, duración); los períodos son una capa de filtro evaluada por separado, declarados por un `Usuario` (la FK `usuario_id` ya lo refleja). Son **múltiples** (feriados, recesos). La relación `ConfiguracionAgenda → PeriodoInhabilitado` del `.mmd` se descarta.

### `bloqueo_agenda`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `tipo_bloqueo_id` | `uuid FK → tipo_bloqueo` | |
| `espacio_id` | `uuid FK → espacio_atencion` nullable | bloqueo puntual a un espacio |
| `grupo_espacio_id` | `uuid FK → grupo_espacio` nullable | bloqueo a todo un grupo |
| `usuario_id` | `uuid FK → usuario` | quién lo ejecutó |
| `fecha_inicio` / `fecha_fin` | `date` | |
| `hora_inicio` / `hora_fin` | `time` nullable | |
| `motivo` | `varchar` | |
| `estado` | `varchar` | |

### `disponibilidad_profesional`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `profesional_id` | `uuid FK → profesional` | |
| `dia_semana` | `varchar` | 'L'..'D' |
| `horario_inicio_manana` / `horario_fin_manana` | `time` nullable | |
| `horario_inicio_tarde` / `horario_fin_tarde` | `time` nullable | |
| `max_turnos_por_franja` | `int` | |
| `estado` | `varchar` | |

### `ausencia_profesional`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `profesional_id` | `uuid FK → profesional` | |
| `usuario_id` | `uuid FK → usuario` | quién la registró |
| `fecha_inicio` / `fecha_fin` | `date` | |
| `hora_inicio` / `hora_fin` | `time` nullable | |
| `motivo` | `varchar` | vacaciones / licencia |
| `reprogramacion_aplicada` | `boolean` | si ya disparó la oferta de reagendación |
| `estado` | `varchar` | |

### `oferta_reagendacion`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `turno_id` | `uuid FK → turno` | el turno *liberado* que se ofrece (ancla universal) |
| `paciente_ofertado_id` | `uuid FK → paciente` | a quién se le ofrece |
| `motivo_liberacion` | `varchar` | ausencia / cancelacion / no_asistio / vencimiento |
| `ausencia_id` | `uuid FK → ausencia_profesional` nullable | causa, cuando la liberación vino de una ausencia |
| `fecha_oferta` | `timestamptz` | |
| `fecha_vencimiento` | `timestamptz` | plazo estricto para responder |
| `estado` | `varchar` | pendiente / aceptada / rechazada / expirada |
| `pausa_nocturna` | `boolean` | no molestar de noche |

> **Bache #2 resuelto**: la oferta nace de *cualquier* liberación (ausencia, cancelación, no-asistencia → UC-REC-04), no solo de ausencia. El ancla universal es `turno_id` (el hueco liberado), y se registra la causa con `motivo_liberacion` + `ausencia_id` nullable. La relación `AusenciaProfesional → OfertaReagendacion ("dispara")` es semánticamente cierta pero incompleta: la ausencia es una causa entre varias.

---

## Índices sugeridos

- `paciente(dni)`, `paciente(apellido, nombre)` — búsqueda (UC-REC-S-01).
- `turno(fecha_hora)`, `turno(paciente_id)`, `turno(profesional_id)`, `turno(espacio_id)` — agenda y filtros.
- `analisis_micologico(estado)` — panel de trabajo por estado.
- `otp(analisis_id)` — búsqueda del OTP vigente.
- `ficha_clinica(paciente_id)`, `dato_clinico(ficha_clinica_id)`.
- `tipo_analisis_tipo_muestra(tipo_analisis_id)`, `tipo_analisis_tipo_muestra(tipo_muestra_id)` — validación de combinaciones.
- `disponibilidad_profesional(profesional_id)`, `ausencia_profesional(profesional_id)`.
- `bloqueo_agenda(espacio_id)`, `bloqueo_agenda(grupo_espacio_id)`.
- `oferta_reagendacion(turno_id)`, `oferta_reagendacion(estado)`.
- `lote(insumo_id)`, `lote(fecha_vencimiento)` — vencimientos y stock por insumo.
- `movimiento_inventario(lote_id)`, `movimiento_inventario(fecha)` — trazabilidad.
- `insumo(categoria_id)`, `insumo(umbral_minimo)` — filtros y alertas de stock (RF-09).
- `residuo_quimico(fecha_hora)`, `residuo_quimico(categoria_residuo_id)` — consolidación mensual (RF-12).
- `instruccion_almacenamiento(categoria_residuo_id)` — pasos por categoría.

## Decisiones de modelado de la pasada Agenda (resueltas con el cliente)

Los tres baches se resolvieron así (el `.mmd` NO se toca hasta validar en bloque al final):

1. **`PeriodoInhabilitado` es independiente** de `ConfiguracionAgenda` (que es un singleton que "rige" la agenda). El período es una capa de filtro aparte, declarada por `Usuario`, y son múltiples. Se descarta la relación `ConfiguracionAgenda → PeriodoInhabilitado` del `.mmd`.
2. **`OfertaReagendacion` se ancla en `turno_id`** (el hueco liberado, universal), no en `ausencia_id`. La causa se registra con `motivo_liberacion` + `ausencia_id` nullable. La relación con `AusenciaProfesional` es una causa, no la única.
3. **`GrupoEspacio` contiene N espacios** vía `espacio_atencion.grupo_espacio_id` (nullable). Un bloqueo con `grupo_espacio_id` inhabilita todo el grupo con una instrucción. No hace falta tabla intermedia N:N salvo que un espacio deba pertenecer a varios grupos.

## Inventario (Stock de Insumos Reactivos)

### `categoria_insumo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | reactivo, medio de cultivo, descartable |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `ubicacion_almacenamiento`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` | estantería, heladera, armario |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `insumo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` | |
| `descripcion` | `text` | |
| `unidad_medida` | `varchar` | ml, g, unidad |
| `categoria_id` | `uuid FK → categoria_insumo` | |
| `ubicacion_id` | `uuid FK → ubicacion_almacenamiento` | ubicación por defecto |
| `umbral_minimo` | `numeric` | dispara alerta en el dashboard (RF-09) |
| `dias_alerta_vencimiento` | `int` | días previos al vencimiento para alertar |
| `estado` | `varchar` | activo / inactivo |
| `fecha_creacion` | `timestamptz` | |

> **Decisión**: `stock_actual` **no se persiste**; se deriva en consulta como Σ `lote.cantidad_actual`. Se evita un punto de desincronización: a diferencia de `version_actual` (cambia rara vez), el stock se mueve con cada registro de inventario. `umbral_minimo` sí se persiste y es la referencia para las alertas (RF-09).

### `lote`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `insumo_id` | `uuid FK → insumo` | |
| `numero_lote` | `varchar` | identificador del proveedor |
| `fecha_ingreso` | `date` | |
| `fecha_vencimiento` | `date` | dispara alerta por vencimiento |
| `cantidad_inicial` | `numeric` | |
| `cantidad_actual` | `numeric` | lo que queda; se decrementa con cada retiro |
| `estado` | `varchar` | activo / agotado / vencido |

> **Regla de negocio (a refinar con el cliente)**: el vencimiento se **registra** en el lote (columna `fecha_vencimiento` + alerta por `dias_alerta_vencimiento`), pero **no** debe bloquear automáticamente su uso. Hay actividades que no permiten insumos vencidos y otras que sí lo admiten; el listado aún no está definido. Hasta definirlo, el sistema muestra la advertencia de vencimiento y deja la decisión de retirar/descartar en el usuario, sin prohibición hardcodeada. Cuando se sepa qué actividades habilitan insumos vencidos, esa lógica se modela como **regla de la actividad**, no como filtro del lote.

### `movimiento_inventario`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `lote_id` | `uuid FK → lote` | |
| `usuario_id` | `uuid FK → usuario` | quién lo ejecutó |
| `ubicacion_id` | `uuid FK → ubicacion_almacenamiento` | retirado/ingresado en |
| `analisis_id` | `uuid FK → analisis_micologico` nullable | consume asociado a un análisis |
| `devolucion_referencia_id` | `uuid FK → movimiento_inventario` nullable | movimiento que se revierte |
| `tipo_movimiento` | `varchar` | ingreso / retiro / devolucion |
| `cantidad` | `numeric` | |
| `practica_educativa` | `boolean` | indica si el retiro es para práctica de alumnos |
| `fecha` | `timestamptz` | |

> **Decisión**: `practica_educativa` pasa a `boolean` (era `string` en el `.mmd`); solo indica sí/no. Si luego se necesita una entidad "práctica" propia, se promueve a FK. `devolucion_referencia_id` materializa la auto-relación "revierte" del `.mmd` (una devolución referencia al retiro que deshace).

### `insumo_x_ubicacion` _(opcional, solo si un insumo vive en varias ubicaciones)_

> No existe en el `.mmd`. El diagrama modela `Insumo → 1 UbicacionAlmacenamiento`. Se deja 1:N directo (`insumo.ubicacion_id`). **Solo** si el negocio requiere que el mismo insumo esté físicamente en varias ubicaciones a la vez, se promueve a una tabla intermedia N:N. Por ahora no se crea.

## Residuos Químicos

### `categoria_residuo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | |
| `clase_peligrosidad` | `varchar` | clase de peligrosidad (normativa 2026) |
| `descripcion` | `text` | |
| `estado` | `varchar` | activo / inactivo |

### `instruccion_almacenamiento`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `categoria_residuo_id` | `uuid FK → categoria_residuo` | |
| `paso` | `int` | orden del paso (1, 2, 3...) |
| `instruccion` | `text` | |

> Regla: una categoría define N pasos **ordenados** de almacenamiento. `paso` es el ordinal; `UNIQUE(categoria_residuo_id, paso)` evita duplicados de orden.

### `residuo_quimico`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `categoria_residuo_id` | `uuid FK → categoria_residuo` | |
| `usuario_id` | `uuid FK → usuario` | quién lo registró |
| `analisis_id` | `uuid FK → analisis_micologico` nullable | proviene de un análisis/práctica |
| `disposicion_final_id` | `uuid FK → disposicion_final` nullable | disposición aplicada |
| `fecha_hora` | `timestamptz` | |
| `volumen` | `numeric` | volumen exacto (normativa) |
| `peso` | `numeric` | peso exacto (normativa) |
| `descripcion` | `text` | |

### `disposicion_final`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `usuario_id` | `uuid FK → usuario` | quién la ejecutó |
| `fecha` | `timestamptz` | |
| `metodo_tratamiento` | `varchar` | |
| `descripcion` | `text` | |

### `reporte_residuos`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `usuario_id` | `uuid FK → usuario` | quién lo generó |
| `mes_anio` | `varchar` | 'YYYY-MM' (derivable del rango; candidato a no persistir) |
| `rango_fecha_inicio` | `date` | |
| `rango_fecha_fin` | `date` | |
| `ruta_archivo` | `varchar` | archivo generado |
| `fecha_generacion` | `timestamptz` | |

> **Nota de modelado**: `.mmd` dibuja `ResiduoQuimico "N" --> "1" ReporteResiduos : "consolidado en"`, pero `residuo_quimico` **no tiene** `reporte_residuos_id` en sus atributos. El reporte mensual consolida por **rango de fechas** (RF-12), no por FK directa al residuo. Se resuelve como consulta por rango. `mes_anio` es derivable de `rango_fecha_inicio`; se deja por ahora, marcado como candidato a eliminar.

### `tipo_equipo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `nombre` | `varchar` unique | |
| `descripcion` | `text` | |
| `criticidad` | `varchar` | categórico de criticidad del equipo (ej. 'baja', 'media', 'alta', 'critica') |

### `equipo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `tipo_equipo_id` | `uuid FK → tipo_equipo` | |
| `numero_serie` | `varchar` | identificador de fábrica; `unique` si el proveedor lo garantiza |
| `nombre` | `varchar` | |
| `marca` | `varchar` | |
| `proveedor` | `varchar` | |
| `fecha_adquisicion` | `date` | |
| `garantia_inicio` | `date` | inicio del período de garantía |
| `garantia_fin` | `date` | vencimiento del período de garantía |
| `ubicacion_id` | `uuid FK → ubicacion_almacenamiento` | |
| `estado` | `varchar` | operativo / en_mantenimiento / fuera_servicio / inactivo |
| `requisitos_uso` | `text` | |

> **Nota de modelado**: `.mmd` expone `garantia_hasm` como una única `date`. Se interpreta (confirmado) como período con dos fechas: `garantia_inicio` + `garantia_fin`. `garantia_fin >= garantia_inicio` es chequeo de integridad recomendado (constraint de app). `numero_serie` solo lleva `unique` si el proveedor lo garantiza; de lo contrario se deja como `varchar` indexado.

### `mantenimiento_equipo`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `equipo_id` | `uuid FK → equipo` | |
| `prestador` | `varchar` | tercero que realizó el mantenimiento (dato libre, no entidad) |
| `tipo_mantenimiento` | `varchar` | preventivo / correctivo / calibración |
| `fecha` | `timestamptz` | |
| `descripcion` | `text` | |
| `proximo_mantenimiento` | `timestamptz` | |

> Regla: un equipo recibe N mantenimientos a lo largo de su vida útil. El mantenimiento se **terceriza**: no se vincula a `usuario`; se registra el prestador como dato libre (`prestador`). Índice `(equipo_id, fecha)` para consultar el historial por equipo en orden cronológico.

### Índices (Equipos)

- `equipo(tipo_equipo_id)`, `equipo(ubicacion_id)` — joins de clasificación y ubicación.
- `mantenimiento_equipo(equipo_id, fecha)` — historial por equipo.

### `auditoria`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `usuario_id` | `uuid FK → usuario` | quién ejecutó la acción auditada |
| `fecha_hora` | `timestamptz` | |
| `direccion_ip` | `varchar` | |
| `modulo` | `varchar` | subsistema que originó el evento |
| `accion` | `varchar` | ej. crear / modificar / eliminar / consultar |
| `entidad_afectada` | `varchar` | tabla/clase afectada |
| `entidad_id` | `uuid` | id del registro afectado (sin FK, por ser polimórfico) |

> Regla: la auditoría es un registro **append-only** (nunca se edita ni se borra). `entidad_id` no lleva FK porque apunta a distintas tablas según `entidad_afectada` (relación polimórfica); la integridad referencial la garantiza la aplicación. Índice `(entidad_afectada, entidad_id)` y `(fecha_hora)` para consultas de trazabilidad.

### `cambio_auditoria`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `auditoria_id` | `uuid FK → auditoria` | evento al que pertenece el cambio |
| `campo` | `varchar` | atributo modificado |
| `valor_anterior` | `text` | |
| `valor_nuevo` | `text` | |

> Regla: una auditoría puede registrar N cambios de campos (`Auditoria 1 → 0..N CambioAuditoria`). Índice `(auditoria_id)` para recuperar todos los cambios de un evento.

### `reporte`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `usuario_id` | `uuid FK → usuario` | quién lo generó |
| `tipo_reporte` | `varchar` | |
| `rango_fecha_inicio` | `date` | |
| `rango_fecha_fin` | `date` | |
| `ruta_archivo` | `varchar` | archivo generado |
| `formato_archivo` | `varchar` | pdf / xlsx / csv |
| `fecha_generacion` | `timestamptz` | |
| `mes_anio` | `varchar` | 'YYYY-MM' |

> **Nota de modelado**: `.mmd` tiene dos entidades de reporte distintas: `Reporte` (genérica, con `tipo_reporte` y `formato_archivo`) y `ReporteResiduos` (mensual de residuos, ya modelada como `reporte_residuos`). `reporte` es la tabla **genérica** de reportes; `reporte_residuos` sigue siendo la especializada del subsistema de residuos. No se fusionan: cubren dominios distintos.

### Índices (Transversales)

- `auditoria(fecha_hora)`, `auditoria(entidad_afectada, entidad_id)`, `auditoria(usuario_id)`.
- `cambio_auditoria(auditoria_id)`.
- `reporte(usuario_id)`, `reporte(fecha_generacion)`.

## Huecos abiertos (nivel 3)

1. **`Reporte de Inventario` sin realización.** El nivel 2 lo define como hijo de `Reporte` (caso de uso `UC–LAB-13`, requerimiento de reporte de inventario) y el `.mmd` histórico lo escondía dentro de la tabla genérica vía `tipo_reporte`. Este nivel **no lo materializa**. Hay que decidir una de dos y documentarla:
   - **(a)** fila de `reporte` con `tipo_reporte = 'inventario'` (más simple, sin tabla nueva), o
   - **(b)** tabla especializada `reporte_inventario`, como se hizo con `reporte_residuos` (más explícita, coherente con el patrón ya elegido para residuos).
2. **Columnas de ingreso de muestra.** El aplanamiento de `Muestra` pierde hoy la información del caso de uso `UC–DIAG-02 Registrar Ingreso de Muestra`. Para cubrirlo, `analisis_micologico` debería sumar `fecha_ingreso_muestra timestamptz` y `observaciones_muestra text`. Pendiente de aplicar.
3. **Cardinalidad `Muestra ↔ Análisis`.** El aplanamiento del punto anterior depende de que sea 1:1. Es un supuesto heredado del nivel 2, todavía sin confirmar contra el nivel 1.