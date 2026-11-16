# Modelo de Esquema de Base de Datos — SIGEMI

> **Estatus**: **fuente de verdad — nivel 3 (persistencia)**, según `AGENTS.md`.
> **Deriva de**: `Diagramas/modelo_dominio_sigemi_unificado.md` (nivel 2) y, en última instancia, de `TF_2026_Requerimientos_KLUKA_JORGE.md` (nivel 1). Si este documento contradice el nivel 2, el nivel 2 gana y este archivo es el defectuoso.
> **Nivel de abstracción**: 3 — Persistencia / Modelo Relacional.
> **Propósito**: definir *cómo se guarda* el sistema en PostgreSQL: tablas, columnas, tipos, claves e índices.
> **Regla de oro**: acá SÍ hay `id`, `FK`, tipos SQL, e índices. Incluye los mecanismos (versionado, auditoría, OTP) que el dominio conceptual excluye.
> **Decisiones fijadas**: claves primarias **UUID**; ORM **SQLAlchemy**; migraciones **Alembic**; versionado de ficha clínica y de análisis en **jsonb**; `version_actual` persistido; roles **prefijados y cerrados** (`bioquimico` \| `profesor` \| `administrador`).
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
| `Muestra` | tabla `muestra` + FK en `analisis_micologico` (`muestra_id`) | **tabla propia** (relación 1:N con `Análisis`) |
| `Reporte` (padre) | `reporte` genérica (`tipo_reporte`) + `reporte_residuos` y `reporte_inventario` especializadas | **especializada** por tabla |
| `Dato Clínico` | `dato_clinico` | directa |
| `Registro de Auditoría` | `auditoria` + `cambio_auditoria` | 1:N |
| `Usuario` ↔ roles | `usuario` + `rol` (catálogo **cerrado** por `codigo`) + `usuario_rol` (N:N) | **divergencia deliberada**: el dominio trata el rol como responsabilidad, el esquema como entidad con catálogo prefijado |

**`Muestra` como tabla propia (1:N).** El nivel 2 define `Muestra` como concepto propio (extraída del paciente, tipificada por `Tipo de Muestra`). Decisión confirmada: una **muestra puede alimentar varios análisis** (ej. examen directo + cultivo de la misma uña), y un análisis se realiza sobre exactamente una muestra. Por eso `Muestra` se materializa en la tabla `muestra`, y `analisis_micologico.muestra_id` apunta a ella. La validación `tipo_analisis × tipo_muestra` se evalúa sobre `analisis_micologico.tipo_analisis_id` × `muestra.tipo_muestra_id`.

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

> **Obligatoriedad (decisión 7 del nivel 2).** Son `NOT NULL`: `numero_registro`, `dni`, `nombre`, `apellido`, `fecha_nacimiento`, `telefono`, `estado`, `fecha_ingreso` y `nivel_registro`. Son nullable `sexo`, `domicilio`, `correo_electronico` y `obra_social`, porque UC–REC-15 paso 6 prevé un formulario ligero que los complete después de la atención. `numero_registro` lo genera la aplicación: ningún UCE lo pide al operador, y hacerlo tecleable convierte un identificador institucional único en un campo que se puede duplicar.

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
| `tipo_analisis_id` | `uuid FK → tipo_analisis` nullable | estudio que motiva el turno (UC–REC-20 paso 6, UC–REC-24 paso 2); nulo cuando lo agenda el Agente IA y nadie lo preguntó |
| `serie_id` | `uuid` nullable | agrupa los turnos de una serie (UC–REC-24 postcondición «vinculados entre sí»); sin FK porque el grupo es el valor compartido, no una entidad |
| `profesional_id` | `uuid FK → profesional` nullable | nulo al crear el turno: ningún UCE–REC elige profesional al agendar (decisión 5 del nivel 2) |
| `espacio_id` | `uuid FK → espacio_atencion` nullable | (se referencia aunque la tabla completa sea de segunda pasada) nulo al crear el turno, por la misma razón que `profesional_id` |
| `fecha_hora` | `timestamptz` | |
| `telefono_contacto` | `varchar` | |
| `estado` | `varchar` | confirmado / pendiente / cancelado / atendido / no_asistio |
| `reprogramaciones` | `int` | |
| `motivo_cancelacion` / `motivo_reprogramacion` / `motivo_inasistencia` | `varchar` | `motivo_inasistencia` es opcional (UC–REC-15 secuencia Ausente, paso 3) |
| `fecha_creacion` / `fecha_atencion` | `timestamptz` | |

### `indicacion_medica`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `titulo` | `varchar` | |
| `contenido` | `text` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` | obligatorio: UC–REC-10 paso 2 lo exige y su excepción rechaza el alta sin él (decisión 6 del nivel 2) |
| `estado` | `varchar` | activa / inactiva (eliminación lógica, ver UC-REC-12) |
| `fecha_creacion` / `fecha_modificacion` | `timestamptz` | |

### `muestra`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `paciente_id` | `uuid FK → paciente` | de quién se extrajo |
| `tipo_muestra_id` | `uuid FK → tipo_muestra` | uña / piel / pelo |
| `usuario_id` | `uuid FK → usuario` | quién registró el ingreso (UC–DIAG-02) |
| `fecha_ingreso` | `timestamptz` | recepción física de la muestra |
| `observaciones` | `text` | observaciones iniciales |

> Una muestra puede alimentar **varios** análisis (1:N): un examen directo y un cultivo de la misma uña son dos `analisis_micologico` apuntando a la misma `muestra`. UC–DIAG-02 registra la muestra y crea el primer análisis sobre ella; los análisis adicionales reutilizan la misma `muestra`. El rechazo de la muestra se expresa a nivel de análisis (`estado = 'invalidado'`, UC–DIAG-14), no como estado propio de `muestra`.

### `analisis_micologico`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `ficha_clinica_id` | `uuid FK → ficha_clinica` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` | |
| `muestra_id` | `uuid FK → muestra` | la muestra física estudiada (1:N; todo análisis tiene exactamente una) |
| `profesional_responsable_id` | `uuid FK → profesional` | quién *realiza* |
| `profesional_validador_id` | `uuid FK → profesional` nullable | quién *valida* (firma) |
| `version_actual` | `int` | puntero a la versión vigente (addendum, UC–DIAG-13) |
| `estado` | `varchar` | pendiente / en_proceso / terminado / validado / invalidado |
| `fecha_creacion` / `fecha_validacion` | `timestamptz` | |
| `motivo_invalidacion` | `varchar` | motivo obligatorio de invalidación o rechazo |

### `hallazgo_analisis`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `analisis_id` | `uuid FK → analisis_micologico` | |
| `tipo_hallazgo` | `varchar` | |
| `dato` | `text` | |
| `estado_alcanzado` | `varchar` | |
| `fecha` | `timestamptz` | |

### `version_analisis`  _(mecanismo de inmutabilidad del análisis)_

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `analisis_id` | `uuid FK → analisis_micologico` | |
| `numero_version` | `int` | |
| `datos_previos` | `jsonb` | snapshot previo (análisis + hallazgos + informe vigente) |
| `datos_nuevos` | `jsonb` | snapshot posterior |
| `usuario_id` | `uuid FK → usuario` | |
| `fecha_modificacion` | `timestamptz` | |
| `motivo` | `varchar` | motivo del addendum / corrección |

> Réplica del versionado de `version_ficha_clinica` (inmutabilidad, RNF-04). El addendum (UC–DIAG-13) crea una **nueva versión del análisis** sin alterar la original; `datos_previos`/`datos_nuevos` capturan en `jsonb` el análisis junto con sus `hallazgo_analisis` y el `informe_resultados` vigente en ese momento, para que la versión sea un snapshot inmutable completo. `hallazgo_analisis` e `informe_resultados` **no** llevan versionado propio: son hechos del análisis y quedan capturados dentro del snapshot de versión.

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

### `usuario` / `rol` / `usuario_rol` / `profesional`

| tabla | columnas | notas |
|---|---|---|
| `rol` | `id uuid PK`, `codigo` unique, `nombre`, `descripcion` | **catálogo cerrado**: `bioquimico` \| `profesor` \| `administrador`. El usuario no modela roles propios ni modifica privilegios |
| `usuario` | `id uuid PK`, `nombre`, `apellido`, `correo_electronico` unique, `contrasena_hash`, `estado`, `intentos_fallidos`, `bloqueado_hasta`, `fecha_registro` | `contrasena_hash` → JWT/BCrypt. Sin `rol_id`: los roles viven en `usuario_rol` |
| `usuario_rol` | `usuario_id FK → usuario`, `rol_id FK → rol`, `UNIQUE(usuario_id, rol_id)` | N:N; un usuario acumula uno o más roles (ej. `administrador` + `bioquimico`) |
| `profesional` | `id uuid PK`, `usuario_id FK (unique)`, `matricula`, `especialidad`, `estado` | 1:1 con `usuario`; aplica **solo** al rol `bioquimico` |

> Regla `usuario`: `correo_electronico` es la **identidad de la cuenta**. Es el dato con el que se inicia sesión (UCE–SEG-01) y el único canal de recuperación de contraseña (UCE–SEG-07), y de ahí salen sus tres invariantes: se persiste **normalizado** (sin espacios en los extremos y en minúsculas), su **formato de buzón** lo valida la aplicación rechazando con el mensaje de error de campo del contrato de respuesta (UCE–SEG-02, excepción del paso 6), y la `UNIQUE` es **insensible a mayúsculas** como consecuencia de la normalización, no por una colación especial. `nombre` y `apellido` son texto libre: este nivel no les fija cota, y la cota de presentación pertenece a la especificación de la pantalla.

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

### `lista_espera`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `paciente_id` | `uuid FK → paciente` | |
| `tipo_analisis_id` | `uuid FK → tipo_analisis` nullable | estudio solicitado; participa del orden de prioridad |
| `fecha_solicitud` | `timestamptz` | base del orden de prioridad |
| `estado` | `varchar` | pendiente / asignado / retirado |
| `usuario_id` | `uuid FK → usuario` nullable | quién la cargó; nulo cuando la creó el Agente IA |
| `observaciones` | `text` | |

> Regla: `prioridad` **no se persiste**. El orden que UC–REC-29 pide («por prioridad (fecha de solicitud y tipo de análisis)») es derivado: `fecha_solicitud` ascendente y, a igualdad, el `tipo_analisis` (decisión 4 del nivel 2). Guardar un valor derivado obliga a recalcularlo en cada alta y lo deja mintiendo en cuanto la cola se reordena.
>
> Regla: la lista de espera existe porque UC–REC-23, 28 y 29 operan sobre ella y UC–REC-04 necesita a quién ofrecer un turno liberado. Sin esta tabla, RF-03 no tiene de dónde elegir.

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
- `lista_espera(estado)`, `lista_espera(fecha_solicitud)` — cola de UC–REC-29.
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
- `muestra(paciente_id)`, `muestra(tipo_muestra_id)` — muestras por paciente y por tipo.
- `analisis_micologico(muestra_id)` — análisis de una muestra.
- `version_analisis(analisis_id)` — historial de versiones del análisis.
- `usuario_rol(usuario_id)`, `usuario_rol(rol_id)` — resolución de roles por usuario y por rol.

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

### `reporte_inventario`

| columna | tipo | notas |
|---|---|---|
| `id` | `uuid PK` | |
| `usuario_id` | `uuid FK → usuario` | quién lo generó |
| `rango_fecha_inicio` | `date` | |
| `rango_fecha_fin` | `date` | |
| `ruta_archivo` | `varchar` | archivo generado |
| `fecha_generacion` | `timestamptz` | |

> Tabla especializada para el **reporte de inventario** (UC–LAB-13), simétrica a `reporte_residuos`. Consolida movimientos y stock por rango de fechas; no se fusiona con `reporte` (que sigue siendo la genérica para las exportaciones transversales, REP-01).

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
| `accion` | `varchar` | **catálogo cerrado**: `crear` \| `modificar` \| `eliminar` \| `consultar` \| `acceder` \| `bloquear` |
| `entidad_afectada` | `varchar` | tabla/clase afectada |
| `entidad_id` | `uuid` | id del registro afectado (sin FK, por ser polimórfico) |

> Regla: la auditoría es un registro **append-only** (nunca se edita ni se borra). `entidad_id` no lleva FK porque apunta a distintas tablas según `entidad_afectada` (relación polimórfica); la integridad referencial la garantiza la aplicación. Índice `(entidad_afectada, entidad_id)` y `(fecha_hora)` para consultas de trazabilidad.

> Regla `accion`: **no es texto libre**. Es el catálogo cerrado de arriba y la aplicación lo verifica al escribir, porque un registro inmutable con un valor inventado no se corrige después. `acceder` es un inicio de sesión exitoso y `bloquear` el bloqueo de una cuenta por intentos fallidos: son eventos distintos y no se etiquetan igual, o la traza afirmaría que alguien entró cuando en realidad se lo bloqueó. La **baja lógica** de una cuenta se audita como `modificar`, porque el registro no se borra; `eliminar` queda reservado a un borrado físico, que hoy ningún flujo ejerce. `consultar` cubre lecturas y exportaciones.


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

> **Nota de modelado**: el nivel 2 define `Reporte` como padre con hijos regionales. La realización es mixta: `reporte` es la tabla **genérica** (exportaciones transversales, REP-01), mientras que `reporte_residuos` y `reporte_inventario` son las tablas especializadas de sus subsistemas (RF-12 y UC–LAB-13). No se fusionan: cubren dominios distintos.

### Índices (Transversales)

- `auditoria(fecha_hora)`, `auditoria(entidad_afectada, entidad_id)`, `auditoria(usuario_id)`.
- `cambio_auditoria(auditoria_id)`.
- `reporte(usuario_id)`, `reporte(fecha_generacion)`.

## Decisiones cerradas (nivel 3)

Los huecos detectados en la revisión quedan resueltos así:

1. **`Reporte de Inventario` (UC–LAB-13)** → tabla especializada `reporte_inventario`, simétrica a `reporte_residuos` (opción coherente con el patrón ya elegido).
2. **Ingreso de muestra (UC–DIAG-02)** → materializado con la tabla `muestra` (`fecha_ingreso`, `observaciones`).
3. **Cardinalidad `Muestra ↔ Análisis`** → **1:N**: una muestra puede alimentar varios análisis; `Muestra` deja de aplanarse y pasa a tabla propia.