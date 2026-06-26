# Subsistema Gestión de Pacientes — Actualización de Casos de Uso (v2)

## ⚠️ Corrección sobre UC-REC-E-01

**Acordado: `<<include>>`, no `<<extend>>`.**

Siempre que se crea una indicación médica, se debe asociar a un tipo de análisis. No es opcional — una indicación sin tipo de análisis no tiene sentido porque el sistema necesita saber a qué estudios enviarla.

**Cambio concreto:**
- `UC-REC-10 (Crear Indicación Médica) --include--> Asignar Indicación a Tipo de Análisis`
- El campo "Tipo de Análisis" pasa de opcional a **obligatorio**.

---

## 1. Flujo completo del paciente: ¿Cómo se registra un paciente?

Este es el flujo que hoy no está documentado explícitamente y genera superposición. Acá está resuelto:

### Tres momentos de registro, tres niveles de datos

```
Nivel 1: ALTA TEMPRANA (REC-01)           Solo DNI + Nombre + Teléfono
    ↓
Nivel 2: COMPLETITUD DEMOGRÁFICA (DIAG-01)  Todos los datos personales
    ↓
Nivel 3: FICHA CLÍNICA (DIAG-01)           Datos clínicos del estudio
```

### Camino A — Paciente que llega vía WhatsApp (predominante)

```
[WhatsApp]                  [Presencial]                [Consulta]
REC-01 (Agendar Turno)  →  REC-15 (Asistencia)      →  DIAG-01 (Ficha)
    │                          │                          │
    ▼                          ▼                          ▼
Alta Temprana             Marca "Atendido"           El formulario incluye:
(DNI + Nombre                                         • Datos demográficos:
 + Teléfono)                                            pre-poblados desde
                                                        Alta Temprana,
                                                        EDITABLES para
                                                        completar los campos
                                                        faltantes (dirección,
                                                        obra social, etc.)
                                                      • Campos clínicos
                                                        obligatorios
```

### Camino B — Paciente que NO existe (teléfono, presencial, urgencia)

```
[Web Interna]                                       [Si DNI no existe]
REC-20 (Agendar Manualmente)  ──extend──>  REC-16 (Registrar Paciente)
    │                                              │
    ▼                                              ▼
Busca DNI                                      Registro COMPLETO
                                               (todos los datos
                                                demográficos)
    │
    ▼
Se agenda el turno
```

### Camino C — Paciente existente, corrección de datos

```
[Web Interna]
REC-17 (Modificar Paciente)  ──include──>  Buscar Paciente
    │
    ▼
Modifica los datos demográficos que necesite
```

### Mapa conceptual de estados del paciente

```
                    ┌─────────────────────────┐
                    │    NO REGISTRADO         │
                    └──────────┬──────────────┘
                               │
                    ┌──────────▼──────────────┐
                    │ ALTA TEMPRANA (REC-01)  │
                    │ DNI + Nombre + Teléfono │
                    │ Estado: "Pendiente"     │
                    └──────────┬──────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
        REC-16            DIAG-01            REC-17
    (Registro completo)  (Completa datos +   (Modifica datos)
                          Ficha Clínica)
              │                │
              ▼                ▼
    ┌─────────────────┐ ┌─────────────────┐
    │ COMPLETO         │ │ COMPLETO         │
    │ (todos los datos)│ │ (todos los datos)│
    │ Estado: "Activo" │ │ + Ficha Clínica  │
    └─────────────────┘ └─────────────────┘
              │                │
              ▼                ▼
    ┌──────────────────────────────────────────┐
    │         DESACTIVADO (REC-19)              │
    │ Baja lógica. Historial preservado.        │
    └──────────────────────────────────────────┘
```

---

## 2. Modificaciones a UCEs existentes

### 2.1. UCE–REC-01 — Agendar Turno (MODIFICADO)

Se agrega el paso de programación del recordatorio como paso explícito.

| Campo | Detalle |
|---|---|
| **Secuencia normal** | **Paso** | |
| (igual hasta paso 6) | 1-6 | Sin cambios |
| | 7 | El sistema envía automáticamente un mensaje de confirmación y las indicaciones médicas predefinidas. |
| | **8** | **El sistema programa en cola el envío de un recordatorio de asistencia (se ejecuta `<<include>>` Enviar Recordatorio de Turno).** |
| **Postcondición** | El turno queda registrado y reservado. El recordatorio queda programado. |

> **Nota:** El paso 8 se agrega como paso explícito. Antes estaba solo en postcondiciones. Ahora forma parte de la secuencia normal.

---

### 2.2. UCE–REC-10 — Crear Indicación Médica (MODIFICADO)

Ahora incluye obligatoriamente la asignación a un Tipo de Análisis.

| Campo | Detalle |
|---|---|
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Indicaciones Médicas y presiona "Nueva Indicación". |
| | **2** | **La interfaz despliega un formulario con los campos: Título, Contenido, Tipo de Análisis asociado (obligatorio).** |
| | 3 | El usuario completa los campos y presiona "Guardar". |
| | 4 | El sistema valida que todos los campos obligatorios estén completos. |
| | **5** | **El sistema ejecuta `<<include>>` Asignar Indicación a Tipo de Análisis: vincula la indicación con el tipo de análisis seleccionado.** |
| | **6** | El sistema persiste el registro. |
| | **7** | La interfaz muestra "Indicación creada exitosamente". |
| **Excepciones** | **Paso** | |
| | 4 | Si el contenido está vacío o no se seleccionó un Tipo de Análisis, el sistema muestra una alerta de validación y no persiste. |
| **Comentarios** | El Tipo de Análisis es obligatorio. No se puede crear una indicación genérica sin asociación. |

---

### 2.3. UCE–REC-15 — Registrar Asistencia a Turno (MODIFICADO)

Se explicita que al marcar "Presente", se completa el flujo de datos demográficos del paciente si están incompletos.

| Campo | Detalle |
|---|---|
| **Secuencia normal (Presente)** | **Paso** | |
| | 1-4 | Sin cambios |
| | 5 | El sistema cambia el estado del turno a "Atendido" y registra la hora de atención. |
| | **5.1** | **El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes.** |
| | 6 | El sistema registra el evento en la tabla de auditoría. |
| | 7 | La interfaz confirma la operación y habilita el botón para iniciar la consulta (UC-DIAG-01). |

> **Nota:** Este paso adicional evita que el Bioquímico tenga que cargar datos demográficos durante la consulta clínica. El administrativo los completa en recepción.

---

## 3. Nuevos UCEs completos con flujo detallado

### 3.1. UCE–REC-16 — Registrar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado registra a un paciente en el sistema con todos sus datos demográficos completos desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El paciente no debe existir previamente en la base de datos. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Nuevo Paciente". |
| | 2 | La interfaz despliega el formulario de registro con los campos: DNI (*), Nombre (*), Apellido (*), Fecha de Nacimiento (*), Teléfono (*), Correo Electrónico, Dirección, Obra Social. |
| | 3 | El usuario completa los campos obligatorios (*) y presiona "Guardar". |
| | 4 | El sistema valida que el DNI no exista previamente en la base de datos. |
| | 5 | El sistema persiste el registro del paciente con estado "Activo". |
| | 6 | La interfaz muestra un mensaje de "Paciente registrado exitosamente". |
| **Postcondición** | El paciente queda registrado con estado "Activo" y disponible para asignación de turnos y consultas. |
| **Excepciones** | **Paso** | |
| | 4 | Si el DNI ya existe, el sistema notifica "El paciente ya se encuentra registrado", muestra los datos existentes y ofrece modificarlos (REC-17) o cancelar. |
| | 5 | Si hay error de conexión con la base de datos, se muestra error 500 y se aborta la transacción sin guardar datos parciales. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 5 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | Este caso de uso es disparado opcionalmente desde UC-REC-20 (Agendar Turno Manualmente) cuando el DNI ingresado no existe (relación `<<extend>>`). |

---

### 3.2. UCE–REC-17 — Modificar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado modifica los datos demográficos de un paciente existente. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
| | 2 | El sistema ejecuta UC-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido como criterio de búsqueda. |
| | 3 | El usuario ingresa el criterio de búsqueda. |
| | 4 | El sistema consulta la base de datos. |
| | 5 | Si hay múltiples coincidencias, muestra un listado paginado para que el usuario seleccione. Si hay una sola coincidencia, la selecciona automáticamente. |
| | 6 | El sistema despliega el formulario pre-poblado con los datos actuales del paciente. |
| | 7 | El usuario modifica los campos deseados y presiona "Guardar Cambios". |
| | 8 | El sistema valida los campos editados (formato de DNI, teléfono, etc.). |
| | 9 | El sistema actualiza el registro en la base de datos. |
| | 10 | La interfaz muestra "Datos actualizados exitosamente". |
| | 11 | El sistema registra el evento en la tabla de auditoría. |
| **Postcondición** | Los datos del paciente quedan actualizados en la base de datos. Se registra el cambio en auditoría. |
| **Excepciones** | **Paso** | |
| | 4 | Si no se encuentra ningún paciente con el criterio ingresado, el sistema muestra "Paciente no encontrado" y ofrece crear uno nuevo (REC-16). |
| | 8 | Si el DNI modificado ya pertenece a otro paciente, el sistema rechaza el cambio y notifica "El DNI ingresado ya corresponde a otro paciente". |
| | 9 | Si hay error de base de datos, se aborta la transacción sin guardar cambios parciales. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 9 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | La Fecha de Nacimiento no puede modificarse si el paciente tiene análisis registrados, para mantener la consistencia de la edad calculada al momento del estudio. |

---

### 3.3. UCE–REC-18 — Consultar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado busca y visualiza el perfil completo de un paciente, incluyendo datos demográficos, fichas clínicas previas, análisis asociados y resultados. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes". |
| | 2 | El sistema muestra un listado paginado con todos los pacientes registrados (activos e inactivos). |
| | 3 | El usuario aplica filtros de búsqueda: DNI, Nombre, Apellido, Rango de Fechas de registro, Estado (Activo/Inactivo). |
| | 4 | El sistema consulta la base de datos y retorna los resultados coincidentes. |
| | 5 | El usuario selecciona un paciente de la lista. |
| | 6 | El sistema despliega la vista detallada del paciente con las siguientes secciones: |
| | | **a) Datos Personales:** DNI, Nombre, Apellido, Fecha de Nacimiento, Edad calculada, Teléfono, Correo, Dirección, Obra Social, Estado. |
| | | **b) Historial de Consultas:** Listado cronológico de fichas clínicas asociadas (fecha, diagnóstico presuntivo, institución). |
| | | **c) Análisis Micológicos:** Listado de análisis vinculados con su estado actual (Pendiente / En Proceso / Terminado / Validado). |
| | | **d) Resultados:** Enlace a informes validados (si existen). |
| **Postcondición** | El sistema presenta el perfil completo del paciente. Operación de solo lectura. No se modifica ningún dato. |
| **Excepciones** | **Paso** | |
| | 4 | Si no hay pacientes registrados, la interfaz muestra "No hay pacientes registrados" y habilita el botón para crear uno nuevo (REC-16). |
| | 4 | Si ningún paciente coincide con los filtros, se muestra "No se encontraron pacientes con los criterios ingresados". |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 2 segundos |
| | 6 | Menos de 2 segundos |
| **Frecuencia** | Alta |
| **Estabilidad** | Alta |
| **Comentarios** | Caso de uso puro de solo lectura y consulta. La edad se calcula dinámicamente a partir de la Fecha de Nacimiento. |

---

### 3.4. UCE–REC-19 — Desactivar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero preservando íntegramente el historial clínico y los análisis existentes. |
| **Precondición** | El usuario debe tener una sesión activa con rol Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
| | 2 | El sistema ejecuta UC-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido. |
| | 3 | El usuario ingresa el criterio de búsqueda. |
| | 4 | El sistema recupera y muestra los datos del paciente. |
| | 5 | El usuario presiona "Desactivar Paciente". |
| | 6 | El sistema muestra un diálogo de confirmación solicitando el motivo obligatorio de la desactivación (ej. "Paciente fallecido", "Solicitud de baja", "Registro duplicado"). |
| | 7 | El usuario ingresa el motivo y confirma la acción. |
| | 8 | El sistema verifica que el paciente no tenga turnos vigentes futuros (estado "Confirmado" o "Pendiente" con fecha futura). |
| | 9 | El sistema cambia el estado del paciente a "Inactivo". |
| | 10 | El sistema registra el evento en la tabla de auditoría con: usuario, fecha, motivo, paciente. |
| | 11 | La interfaz muestra "Paciente desactivado exitosamente". |
| **Postcondición** | El paciente queda marcado como "Inactivo". No puede agendarse nuevos turnos a su nombre. Los registros históricos (fichas clínicas, análisis, resultados) se conservan intactos. |
| **Excepciones** | **Paso** | |
| | 4 | Si el paciente no existe, el sistema informa "Paciente no encontrado" y finaliza. |
| | 8 | Si el paciente tiene turnos vigentes futuros, el sistema muestra la lista de turnos activos y solicita al Administrador: (a) cancelarlos uno por uno, o (b) cancelarlos todos masivamente. Recién después permite la desactivación. |
| | 9 | Si ocurre un error de base de datos, se aborta la transacción sin modificar el estado del paciente. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 8 | Menos de 2 segundos |
| **Frecuencia** | Baja (excepcional) |
| **Estabilidad** | Alta |
| **Comentarios** | La desactivación es una baja lógica, NO física. No se eliminan registros de la base de datos. Un paciente inactivo no puede recibir nuevos turnos, pero todo su historial permanece accesible para consulta (REC-18) e investigación (REP-01). |

---

### 3.5. UCE–REC-20 — Agendar Turno Manualmente

> Reemplaza la parte de "Agendar" del antiguo UC-REC-09.

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-01, RF-04 |
| **Descripción** | El personal autorizado agenda un turno a nombre de un paciente directamente desde la interfaz web interna, sin intervención del Agente IA. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda y presiona "Nuevo Turno". |
| | 2 | El sistema solicita el DNI del paciente. |
| | 3 | El usuario ingresa el DNI. |
| | 4 | El sistema busca el registro del paciente en la base de datos. |
| | 5 | El sistema muestra la grilla de disponibilidad horaria para la fecha actual. |
| | 6 | El usuario selecciona: fecha, horario disponible, tipo de análisis. |
| | 7 | El usuario presiona "Confirmar Turno". |
| | 8 | El sistema registra y reserva el turno a nombre del paciente con estado "Confirmado". |
| | 9 | El sistema envía una notificación de confirmación al paciente vía WhatsApp. |
| | 10 | El sistema programa el envío del recordatorio de asistencia (`<<include>>` Enviar Recordatorio). |
| | 11 | El sistema registra el evento en la tabla de auditoría. |
| | 12 | La interfaz muestra "Turno registrado exitosamente". |
| **Postcondición** | El turno queda registrado, reservado, y el paciente notificado. |
| **Excepciones** | **Paso** | |
| | 4 | Si el DNI no existe en el sistema, se dispara la extensión `<<extend>>` UC-REC-16 (Registrar Paciente). Al completar el registro exitosamente, se retorna al paso 5. |
| | 6 | Si la franja seleccionada fue ocupada entre la consulta y la confirmación, el sistema notifica "El horario seleccionado ya no está disponible" y muestra la grilla actualizada. |
| | 8 | Si hay error de base de datos, se aborta sin crear el turno. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 8 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias que no pueden usar el Agente IA. |

---

### 3.6. UCE–REC-21 — Cancelar Turno Manualmente

> Reemplaza la parte de "Cancelar" del antiguo UC-REC-09.

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 |
| **Requisitos asociados** | RF-04 |
| **Descripción** | El personal autorizado cancela un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda. |
| | 2 | El usuario localiza el turno en el calendario (vista diaria/semanal/mensual) o mediante el buscador por DNI. |
| | 3 | El usuario selecciona el turno y presiona "Cancelar Turno". |
| | 4 | El sistema muestra un diálogo de confirmación: "¿Está seguro de cancelar el turno de [Paciente] el [fecha] a las [hora]?". |
| | 5 | El usuario confirma la cancelación. |
| | 6 | El sistema cambia el estado del turno a "Cancelado". |
| | 7 | El sistema libera el bloque horario en la agenda. |
| | 8 | El sistema envía notificación al paciente vía WhatsApp informando la cancelación. |
| | 9 | El sistema ejecuta `<<include>>` UC-REC-04 (Reasignación Automática de Turno Liberado). |
| | 10 | El sistema registra el evento en la tabla de auditoría. |
| | 11 | La interfaz muestra "Turno cancelado exitosamente". |
| **Postcondición** | Turno cancelado, bloque liberado, paciente notificado, reasignación automática disparada. |
| **Excepciones** | **Paso** | |
| | 2 | Si el turno está a menos de 24 horas de su horario, el sistema muestra una advertencia: "El turno está a menos de 24 horas. ¿Desea cancelar de todas formas?" y requiere confirmación explícita adicional. |
| | 5 | Si el usuario cancela la confirmación, se aborta la operación sin modificar el turno. |
| **Rendimiento** | **Paso** | |
| | 6-7 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | - |

---

### 3.7. UCE–REC-22 — Reprogramar Turno Manualmente

> Reemplaza la parte de "Reprogramar" del antiguo UC-REC-09.

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 |
| **Requisitos asociados** | RF-04 |
| **Descripción** | El personal autorizado cambia la fecha y/o hora de un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". Debe haber disponibilidad en la agenda para la nueva fecha/hora solicitada. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda. |
| | 2 | El usuario localiza el turno en el calendario o mediante buscador. |
| | 3 | El usuario selecciona el turno y presiona "Reprogramar". |
| | 4 | El sistema verifica que el turno no haya sido reprogramado más de 2 veces. |
| | 5 | El sistema muestra la grilla de disponibilidad horaria. |
| | 6 | El usuario selecciona la nueva fecha y hora. |
| | 7 | El sistema valida que la nueva franja esté disponible. |
| | 8 | El sistema actualiza el registro del turno con la nueva fecha/hora. |
| | 9 | El sistema libera el bloque horario original. |
| | 10 | El sistema envía notificación al paciente vía WhatsApp con la nueva fecha y hora. |
| | 11 | El sistema ejecuta `<<include>>` UC-REC-04 (Reasignación Automática) por el bloque original liberado. |
| | 12 | El sistema registra el evento en la tabla de auditoría. |
| | 13 | La interfaz muestra "Turno reprogramado exitosamente". |
| **Postcondición** | Turno actualizado, bloque original liberado, paciente notificado. |
| **Excepciones** | **Paso** | |
| | 4 | Si el turno ya fue reprogramado 2 veces, el sistema muestra una advertencia: "El turno alcanzó el límite de reprogramaciones. ¿Desea reprogramar de forma excepcional?" y requiere confirmación del Administrador. |
| | 7 | Si la nueva franja fue ocupada entre la consulta y la confirmación, el sistema notifica y solicita una nueva selección. |
| **Rendimiento** | **Paso** | |
| | 8 | Menos de 1 segundo |
| **Frecuencia** | Baja |
| **Estabilidad** | Alta |
| **Comentarios** | - |

---

## 4. UCE de Soporte (include-only)

### 4.1. UCE–REC-S-01 — Buscar Paciente (include-only)

| Campo | Detalle |
|---|---|
| **Descripción** | Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre, Apellido) y retorna el/los pacientes coincidentes. |
| **Precondición** | El caso de uso invocante debe proveer al menos un criterio de búsqueda. |
| **Secuencia normal** | **Paso** | |
| | 1 | El sistema solicita al usuario el criterio de búsqueda (DNI, Nombre o Apellido). |
| | 2 | El usuario ingresa el criterio. |
| | 3 | El sistema consulta la base de datos con el criterio ingresado. |
| | 4a | Si hay una sola coincidencia exacta: el sistema retorna los datos del paciente al UC invocante. |
| | 4b | Si hay múltiples coincidencias: el sistema muestra un listado paginado para que el usuario seleccione. Al seleccionar, retorna los datos. |
| **Postcondición** | Los datos del paciente seleccionado son retornados al UC invocante. |
| **Excepciones** | **Paso** | |
| | 3 | Si ningún paciente coincide, el sistema informa "Paciente no encontrado" al UC invocante para que maneje la situación (ofrecer crear, buscar de nuevo, etc.). |
| | 3 | Si hay error de base de datos, se retorna un error al UC invocante. |
| **Comentarios** | Caso de uso puramente estructural. No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>`. |

### 4.2. UCE–REC-S-02 — Enviar Recordatorio de Turno (include-only)

| Campo | Detalle |
|---|---|
| **Descripción** | Proceso automático del sistema que programa un mensaje recordatorio de asistencia para ser enviado al paciente en la ventana de tiempo previa configurada. |
| **Precondición** | Un turno debe haber sido registrado exitosamente en el sistema. |
| **Secuencia normal** | **Paso** | |
| | 1 | El sistema recibe el ID del turno recién creado. |
| | 2 | El sistema calcula la ventana de envío: [hora del turno - X horas], donde X es un parámetro configurable (ej. 24 horas). |
| | 3 | El sistema crea una tarea programada en la cola de mensajes con fecha de disparo = ventana calculada. |
| | 4 | La tarea programada queda registrada en la base de datos (tabla de tareas pendientes). |
| **Postcondición** | La tarea de envío de recordatorio queda programada para ejecutarse automáticamente en la fecha/hora calculada. |
| **Comentarios** | Cuando la tarea se ejecuta, envía un mensaje WhatsApp al paciente con los datos del turno. Si el turno fue cancelado o reprogramado antes del disparo, la tarea se cancela automáticamente. |

---

## 5. Diagrama Mermaid Actualizado — DCU Completo

```mermaid
usecaseDiagram
    title DCU - Subsistema Gestión de Pacientes

    actor "Bioquímico / Doctor" as BIOQ
    actor "Administrador" as ADMIN
    actor "Paciente (WhatsApp)" as PAC
    actor "Sistema (Automático)" as SYS

    rectangle "Módulo: Gestión de Turnos - Paciente" as TURNOS_PAC {
        usecase "UC-REC-01\nAgendar Turno" as REC01
        usecase "UC-REC-02\nCancelar Turno" as REC02
        usecase "UC-REC-03\nReprogramar Turno" as REC03
        usecase "UC-REC-04\nReasignación Automática\nTurno Liberado" as REC04
        usecase "UC-REC-05\nConsultar Turno" as REC05
        usecase "UC-REC-14\nCancelar Turno\npor Vencimiento" as REC14
    }

    rectangle "Módulo: Gestión de Turnos - Interno" as TURNOS_INT {
        usecase "UC-REC-06\nConsultar Agenda" as REC06
        usecase "UC-REC-07\nConfigurar Parámetros\nde Agenda" as REC07
        usecase "UC-REC-08\nBloquear/Desbloquear\nDías y Franjas" as REC08
        usecase "UC-REC-15\nRegistrar Asistencia\na Turno" as REC15
        usecase "UC-REC-20\nAgendar Turno\nManualmente" as REC20
        usecase "UC-REC-21\nCancelar Turno\nManualmente" as REC21
        usecase "UC-REC-22\nReprogramar Turno\nManualmente" as REC22
    }

    rectangle "Módulo: Indicaciones Médicas" as INDIC {
        usecase "UC-REC-10\nCrear Indicación\nMédica" as REC10
        usecase "UC-REC-11\nModificar Indicación\nMédica" as REC11
        usecase "UC-REC-12\nEliminar Indicación\nMédica" as REC12
        usecase "UC-REC-13\nConsultar Indicaciones\nMédicas" as REC13
    }

    rectangle "Módulo: Gestión de Pacientes" as PACIENTES {
        usecase "UC-REC-16\nRegistrar Paciente" as REC16
        usecase "UC-REC-17\nModificar Paciente" as REC17
        usecase "UC-REC-18\nConsultar Paciente" as REC18
        usecase "UC-REC-19\nDesactivar Paciente" as REC19
    }

    rectangle "Soporte (include/extend only)" as SOPORTE {
        usecase "Buscar\nPaciente" as BUSPAC
        usecase "Enviar\nRecordatorio" as RECORD
        usecase "Asignar Indicación\na Tipo de Análisis" as ASIGIND
    }

    ' === ACTORES ===
    PAC --> REC01
    PAC --> REC02
    PAC --> REC03
    PAC --> REC05

    BIOQ --> REC06
    BIOQ --> REC15
    BIOQ --> REC10
    BIOQ --> REC11
    BIOQ --> REC12
    BIOQ --> REC13
    BIOQ --> REC16
    BIOQ --> REC17
    BIOQ --> REC18
    BIOQ --> REC20
    BIOQ --> REC21
    BIOQ --> REC22

    ADMIN --> REC06
    ADMIN --> REC07
    ADMIN --> REC08
    ADMIN --> REC15
    ADMIN --> REC10
    ADMIN --> REC11
    ADMIN --> REC12
    ADMIN --> REC13
    ADMIN --> REC16
    ADMIN --> REC17
    ADMIN --> REC18
    ADMIN --> REC19
    ADMIN --> REC20
    ADMIN --> REC21
    ADMIN --> REC22

    SYS --> REC04
    SYS --> REC14

    ' === INCLUDE ===
    REC01 ..> RECORD : <<include>>
    REC02 ..> REC04 : <<include>>
    REC03 ..> REC04 : <<include>>
    REC14 ..> REC04 : <<include>>
    REC15 ..> REC04 : <<include>> (si Ausente)
    REC17 ..> BUSPAC : <<include>>
    REC19 ..> BUSPAC : <<include>>
    REC21 ..> REC04 : <<include>>
    REC22 ..> REC04 : <<include>>
    REC10 ..> ASIGIND : <<include>>
    REC20 ..> RECORD : <<include>>

    ' === EXTEND ===
    REC20 ..> REC16 : <<extend>>\n(si DNI no existe)
    REC06 ..> REC20 : <<extend>>\n(desde agenda)
    REC06 ..> REC21 : <<extend>>\n(desde agenda)
    REC06 ..> REC22 : <<extend>>\n(desde agenda)
```

---

## 6. Tabla de Correspondencia Completa

| ID Anterior | ID Nuevo | Nombre | Cambio |
|---|---|---|---|
| — | UC-REC-S-01 | Buscar Paciente | **NUEVO** (include-only) |
| — | UC-REC-S-02 | Enviar Recordatorio de Turno | **NUEVO** (include-only) |
| — | — | Asignar Indicación a Tipo de Análisis | **NUEVO** (include-only, era extend) |
| — | UC-REC-16 | Registrar Paciente | **NUEVO** |
| — | UC-REC-17 | Modificar Paciente | **NUEVO** |
| — | UC-REC-18 | Consultar Paciente | **NUEVO** |
| — | UC-REC-19 | Desactivar Paciente | **NUEVO** |
| UC-REC-09 | UC-REC-20 | Agendar Turno Manualmente | **REEMPLAZA** (parte de REC-09) |
| UC-REC-09 | UC-REC-21 | Cancelar Turno Manualmente | **REEMPLAZA** (parte de REC-09) |
| UC-REC-09 | UC-REC-22 | Reprogramar Turno Manualmente | **REEMPLAZA** (parte de REC-09) |
| UC-REC-09 | — | (eliminado) | **OBSOLETO** |
| UC-REC-01 | UC-REC-01 | Agendar Turno | **MODIFICADO** — paso 8 explícito (recordatorio) |
| UC-REC-10 | UC-REC-10 | Crear Indicación Médica | **MODIFICADO** — include a Asignar Tipo, campo obligatorio |
| UC-REC-15 | UC-REC-15 | Registrar Asistencia | **MODIFICADO** — paso 5.1 (completitud de datos demográficos) |
| UC-REC-02 al 08 | igual | Sin cambios | — |
| UC-REC-11 al 14 | igual | Sin cambios | — |