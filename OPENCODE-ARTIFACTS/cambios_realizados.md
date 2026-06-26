# Registro de Cambios — Subsistema Gestión de Pacientes

**Documento:** `TF_2026_Requerimientos_KLUKA_JORGE.md`
**Fecha:** 26/06/2026
**Versión:** 1.0 — Actualización de casos de uso del Subsistema Gestión de Pacientes

---

## Resumen General

Se modificó la sección **2.7.3.1** (definiciones de Casos de Uso) y la sección **2.8.1** (Casos de Uso Extendidos) del Subsistema Gestión de Pacientes.

| Métrica | Antes | Después |
|---|---|---|
| Líneas totales del documento | 1.020 | 1.241 |
| UC-REC activos | 15 | 22 |
| UCE-REC activos | 15 | 22 |

---

## Cambios Realizados

### 1. Eliminaciones

| ID Eliminado | Nombre | Motivo |
|---|---|---|
| **UC-REC-09** | Gestionar Turno Manualmente desde Web Interna | Reemplazado por UC-REC-20, 21, 22 (separación de responsabilidades) |
| **UCE-REC-09** | Gestionar Turno Manualmente desde Web Interna | Reemplazado por UCE-REC-20, 21, 22 |

### 2. Nuevos Casos de Uso (sección 2.7.3.1)

Se insertaron **7 nuevos UC** después de UC-REC-15, antes de la sección 2.7.3.2:

| ID | Nombre | Actor | Relaciones |
|---|---|---|---|
| **UC-REC-16** | Registrar Paciente | Bioquímico/Doctor, Administrador | — |
| **UC-REC-17** | Modificar Paciente | Bioquímico/Doctor, Administrador | `<<include>>` Buscar Paciente |
| **UC-REC-18** | Consultar Paciente | Bioquímico/Doctor, Administrador | — |
| **UC-REC-19** | Desactivar Paciente | Administrador | `<<include>>` Buscar Paciente |
| **UC-REC-20** | Agendar Turno Manualmente | Bioquímico/Doctor, Administrador | `<<extend>>` UC-REC-16 |
| **UC-REC-21** | Cancelar Turno Manualmente | Bioquímico/Doctor, Administrador | `<<include>>` UC-REC-04 |
| **UC-REC-22** | Reprogramar Turno Manualmente | Bioquímico/Doctor, Administrador | `<<include>>` UC-REC-04 |

### 3. Nuevos Casos de Uso Extendidos (sección 2.8.1)

Se insertaron **7 nuevos UCE** con flujo completo después de UCE-REC-15:

| ID | Nombre | Pasos | Actor |
|---|---|---|---|
| **UCE-REC-16** | Registrar Paciente | 6 pasos + excepciones | Bioq/Admin |
| **UCE-REC-17** | Modificar Paciente | 11 pasos + excepciones | Bioq/Admin |
| **UCE-REC-18** | Consultar Paciente | 6 pasos + excepciones | Bioq/Admin |
| **UCE-REC-19** | Desactivar Paciente | 11 pasos + excepciones | Admin |
| **UCE-REC-20** | Agendar Turno Manualmente | 12 pasos + excepciones | Bioq/Admin |
| **UCE-REC-21** | Cancelar Turno Manualmente | 11 pasos + excepciones | Bioq/Admin |
| **UCE-REC-22** | Reprogramar Turno Manualmente | 13 pasos + excepciones | Bioq/Admin |

### 4. Modificaciones a Casos de Uso Extendidos Existentes

#### UCE-REC-01 — Agendar Turno (MODIFICADO)
- **Cambio:** Se agregó el **paso 8** en la secuencia normal:
  > `|  | 8 | El sistema programa en cola el envío de un recordatorio de asistencia (<<include>> Enviar Recordatorio de Turno).`
- **Postcondición** simplificada: se eliminó la mención del recordatorio (ahora está en la secuencia normal)

#### UCE-REC-10 — Crear Indicación Médica (MODIFICADO)
- **Cambio 1:** El campo "Tipo de Análisis asociado" pasó de **(opcional)** a **(obligatorio)**
- **Cambio 2:** Se reemplazaron los pasos 4-5 por 3 nuevos pasos:
  - Paso 4: validación de todos los campos obligatorios
  - Paso 5: ejecución de `<<include>>` Asignar Indicación a Tipo de Análisis
  - Pasos 6-7: persistencia y mensaje de éxito
- **Cambio 3:** Excepción actualizada: ahora valida también que se haya seleccionado un Tipo de Análisis

#### UCE-REC-15 — Registrar Asistencia a Turno (MODIFICADO)
- **Cambio:** Se agregó el **paso 5.1** en la secuencia "Presente":
  > `|  | 5.1 | El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes antes de continuar.`

---

## Cambios No Funcionales (Estructurales)

| Cambio | Detalle |
|---|---|
| **Separación de responsabilidades** | UC-REC-09 (monolítico con 3 acciones) → UC-REC-20, 21, 22 (uno por acción) |
| **Creación del módulo Gestión de Pacientes** | Antes era un módulo descripto pero sin casos de uso asignados. Ahora tiene 4 UCs (REC-16 a REC-19) |
| **Patrón include Buscar Paciente** | Se establece el patrón: Modificar y Desactivar incluyen Buscar Paciente, siguiendo el criterio de los ejemplos de referencia |
| **Asignación obligatoria de Tipo de Análisis** | Se cambió de opcional a obligatorio por decisión de diseño: una indicación médica siempre debe saber a qué análisis corresponde |

---

## Impacto en Otros Subsistemas

| Subsistema | Impacto |
|---|---|
| **Laboratorio Bioquímico** | Bajo. UC-DIAG-01 (Registrar Ficha Clínica) se beneficia porque ahora REC-15 completa datos demográficos antes de la consulta |
| **Acceso y Seguridad** | Ninguno. Los roles existentes (Bioquímico/Doctor, Administrador) ya cubren los nuevos UCs |
| **Recursos de Laboratorio** | Ninguno |
| **Reportes y Estadísticas** | Medio. Los nuevos UCs (REC-17, REC-18) generan datos que alimentarán los reportes de investigación |