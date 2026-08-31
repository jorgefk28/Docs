# Resumen de Cambios — Modelo de Datos SIGEMI

Evolución desde el modelo de dominio original (`modelo_dominio_sigemi.md`) hacia el modelo
conceptual (`modelo_conceptual_sigemi.md`) y el modelo de datos (`modelo_datos_sigemi.md`).

---

## 1. Conversión de atributos `text` estructurado a tablas de detalle

| Atributo `text` original | Tabla de detalle creada | Qué guarda |
|---|---|---|
| FichaClinica.`datos_clinicos` | **DatoClinico** | Campos clínicos pares `campo` / `valor` / `tipo_dato` |
| ConfiguracionAgenda.`periodos_inhabiles` | **PeriodoInhabilitado** | Cierres globales: `fecha_inicio`, `fecha_fin`, `hora_inicio/fin`, `motivo`, `recurrencia` |
| AnalisisMicologico.`observaciones` + `resultado_final` | **HallazgoAnalisis** | Observaciones y resultados como filas `tipo_hallazgo` / `dato` / `fecha` |
| Auditoria.`cambio_realizado` | **CambioAuditoria** | Detalle por campo: `campo` / `valor_anterior` / `valor_nuevo` |
| CategoriaResiduo.`instrucciones_almacenamiento` | **InstruccionAlmacenamiento** | Pasos secuenciales `paso` / `instruccion` |

Los `text` descriptivos cortos (`descripcion`, `contenido`, snapshots de versión) **no** se convirtieron.

Eliminado además **`TipoAnalisis.indicaciones_asociadas`**, redundante con la relación ya existente `IndicacionMedica → TipoAnalisis`.

---

## 2. Nueva lógica de bloqueo de agenda (enfoque híbrido)

Se separaron **dos conceptos que antes estaban mezclados en `BloqueoAgenda`**:

1. **`PeriodoInhabilitado`** — cierre **global** de agenda por rango de fecha/franja.
   - Un solo registro cierra **todo** el laboratorio. Resuelve mantenimientos masivos y feriados sin instanciar por recurso.
2. **`BloqueoAgenda`** — bloqueo **puntual** contra un `Recurso` o un `GrupoRecurso`.
   - Nueva tabla **`TipoBloqueo`** (catálogo: Día Completo / Franja Horaria) usada por ambos.

Se agregaron:
- **`Recurso`** — espacio físico de agenda (Sala / Consultorio / Laboratorio). `Turno` ahora se asigna a un recurso.
- **`GrupoRecurso`** + tabla asociativa **`RecursoGrupo`** (N-N) — para bloquear un conjunto de recursos a la vez.
- Campo **`precedencia`** (Global > Grupo > Recurso) que define el ganador ante solapamientos.

**Resultado clave:** «Cerrar los 50 laboratorios» = **1** registro (un `PeriodoInhabilitado` global), no 50 instancias de `BloqueoAgenda`.

### Excepciones que el modelo original no resolvía y ahora sí
| Caso | Modelo original (problema) | Modelo nuevo (solución) |
|---|---|---|
| Cierre masivo de N salas | N filas de BloqueoAgenda | 1 PeriodoInhabilitado global |
| Cierre recurrente (domingos, feriados) | N filas repetidas o sin soporte | `recurrencia` en PeriodoInhabilitado |
| Bloqueo de una sala puntual dentro de grupo | No diferenciable (todo o nada) | BloqueoAgenda precutual sobre Recurso/Grupo + precedencia |
| Solapamiento de bloqueos | Sin regla | `precedencia` determinística |

---

## 3. Incorporación de equipos (activos no consumibles)

**`Equipo`** es la nueva entidad de activo fijo, **desvinculada** del inventario consumible y de la lógica de bloqueo.

| Tabla | Propósito |
|---|---|
| **Equipo** | Microscopio, autoclave, centrífuga. Campos de activo fijo: `numero_serie`, `nombre`, `marca`, `proveedor`, `fecha_adquisicion`, `garantia_hasta`, `estado` (Operativo/En Mantenimiento/Inhabilitado), `requisitos_uso`, `ubicacion` |
| **TipoEquipo** | Catálogo de categorías con `descripcion` y `criticidad` |
| **MantenimientoEquipo** | Historial de tareas: `tipo_mantenimiento` (preventivo/correctivo), `fecha`, `descripcion`, `proximo_mantenimiento`, `responsable` |

- **No se introduce FK de equipos hacia la agenda/bloqueo**: `Equipo` no participa en `BloqueoAgenda` ni `PeriodoInhabilitado`.
- Se eliminó la relación `Recurso → Equipo` del modelo conceptual: `Recurso` representa únicamente espacios de la agenda.
- `Insumo` queda exclusivamente como consumible (con `lote`/`stock`/`vencimiento`); el equipo no usa esos campos.

---

## 4. Otras decisiones del conceptual materializadas en el modelo de datos

- **`Turno` gana `recurso_id`** (FK a Recurso): cada cita se asigna a un espacio físico real.
- El modelo de datos ahora tiene **34 tablas** (vs 22 del original) y usa **FK para modelar** las nuevas relaciones.
- La matriz de relaciones y el diagrama Mermaid del modelo de datos incluyen **cardinalidad** y marcado **PK/FK**, a diferencia del conceptual (sin card)).
- Los snapshots de versión (`datos_previos`/`datos_nuevos`) se mantienen en `VersionFichaClinica` como `text` JSON por ser estado inmutable.

---

## Nota
El **bloqueo de agenda solo aplica a la agenda** (recursos/espacios y fechas), y la gestión de **equipos se mantiene como flujo independiente** en el modelo de datos (estado, garantía, mantenimiento).
