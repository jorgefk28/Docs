# Subsistema Gestión de Pacientes — Actualización de Casos de Uso

## 1. Resumen de Cambios

| Acción | Detalle |
|---|---|
| **NUEVOS** | UC-REC-16, UC-REC-17, UC-REC-18, UC-REC-19 (Gestión de Pacientes) |
| **NUEVOS** | UC-REC-20, UC-REC-21, UC-REC-22 (Reemplazan UC-REC-09) |
| **NUEVO (include-only)** | Buscar Paciente |
| **NUEVO (include-only)** | Enviar Recordatorio de Turno |
| **NUEVO (extend-only)** | Asignar Indicación a Tipo de Análisis |
| **OBSOLETO** | UC-REC-09 (Gestionar Turno Manualmente) — se elimina |

---

## 2. Nuevos Casos de Uso (Definiciones)

### 2.1. Buscar Paciente (include-only, sin actor directo)

Este caso de uso **no es invocado por ningún actor humano directamente**. Existe únicamente como subflujo reutilizable incluido por otros casos de uso.

| Campo | Valor |
|---|---|
| **ID** | UC-REC-S-01 (Soporte) |
| **Nombre** | Buscar Paciente |
| **Descripción** | Subproceso que recibe un criterio de búsqueda (DNI, Nombre, Apellido) y retorna los datos del paciente coincidente. Si hay múltiples coincidencias, retorna un listado para selección. |
| **Incluido por** | UC-REC-17 (Modificar Paciente), UC-REC-19 (Desactivar Paciente) |

---

### 2.2. Enviar Recordatorio de Turno (include-only, proceso automático)

| Campo | Valor |
|---|---|
| **ID** | UC-REC-S-02 (Soporte) |
| **Nombre** | Enviar Recordatorio de Turno |
| **Descripción** | Proceso automático del sistema que, tras agendar un turno, programa en cola un mensaje recordatorio de asistencia para ser enviado al paciente en la ventana de tiempo previa configurada. |
| **Incluido por** | UC-REC-01 (Agendar Turno) |

---

### 2.3. Asignar Indicación a Tipo de Análisis (extend-only)

| Campo | Valor |
|---|---|
| **ID** | UC-REC-E-01 (Extensión) |
| **Nombre** | Asignar Indicación a Tipo de Análisis |
| **Descripción** | Durante la creación de una indicación médica, el usuario puede asociarla opcionalmente a un tipo de análisis específico. Si no se asigna, la indicación se envía genéricamente a todo turno. |
| **Extiende a** | UC-REC-10 (Crear Indicación Médica) |

---

### 2.4. UC-REC-16 — Registrar Paciente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado registra a un paciente en el sistema con todos sus datos demográficos completos desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El paciente no debe existir previamente en la base de datos. |
| **Postcondiciones** | El paciente queda registrado en el sistema con estado "Activo". |
| **Relaciones** | — |

---

### 2.5. UC-REC-17 — Modificar Paciente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado modifica los datos demográficos de un paciente existente en el sistema. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Postcondiciones** | Los datos del paciente quedan actualizados en la base de datos. |
| **Relaciones** | `<<include>>` UC-REC-S-01 (Buscar Paciente) |

---

### 2.6. UC-REC-18 — Consultar Paciente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado busca y visualiza los datos demográficos y el historial clínico acumulado de un paciente. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Postcondiciones** | El sistema presenta el perfil del paciente con sus datos personales y un resumen de su historial. Operación de solo lectura. |
| **Relaciones** | — |

---

### 2.7. UC-REC-19 — Desactivar Paciente

| Campo | Valor |
|---|---|
| **Actor primario** | Administrador |
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero manteniendo la integridad histórica. |
| **Precondición** | El usuario debe tener una sesión activa con rol Administrador. |
| **Postcondiciones** | El paciente queda marcado como "Inactivo" en la base de datos. No puede agendarse nuevos turnos a su nombre. Los registros históricos (fichas clínicas, análisis) se conservan. |
| **Relaciones** | `<<include>>` UC-REC-S-01 (Buscar Paciente) |

---

### 2.8. UC-REC-20 — Agendar Turno Manualmente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-01 Agendamiento de Turnos vía Agente IA, RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado agenda un turno a nombre de un paciente directamente desde la interfaz web interna, sin intervención del Agente IA. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Postcondiciones** | El turno queda registrado y reservado en el sistema. Se envía notificación de confirmación al paciente vía WhatsApp. |
| **Relaciones** | `<<extend>>` UC-REC-16 (Registrar Paciente) — si el DNI ingresado no existe en el sistema |

---

### 2.9. UC-REC-21 — Cancelar Turno Manualmente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado cancela un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado vigente. |
| **Postcondiciones** | El turno cambia a estado "Cancelado". El bloque horario queda liberado. Se notifica al paciente. |
| **Relaciones** | `<<include>>` UC-REC-04 (Reasignación Automática de Turno Liberado) |

---

### 2.10. UC-REC-22 — Reprogramar Turno Manualmente

| Campo | Valor |
|---|---|
| **Actor primario** | Bioquímico/Doctor, Administrador |
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado cambia la fecha y/o hora de un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado vigente. Debe haber disponibilidad en la agenda. |
| **Postcondiciones** | El turno se actualiza con la nueva fecha/hora. El bloque anterior queda liberado. Se notifica al paciente. |
| **Relaciones** | `<<include>>` UC-REC-04 (Reasignación Automática de Turno Liberado) |

---

## 3. Casos de Uso Extendidos (UCE)

### 3.1. UCE–REC-16 — Registrar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado registra a un paciente en el sistema con todos sus datos demográficos completos desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El paciente no debe existir previamente en la base de datos. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Nuevo Paciente". |
| | 2 | La interfaz despliega el formulario de registro con los campos: DNI, Nombre, Apellido, Fecha de Nacimiento, Teléfono, Correo Electrónico (opcional), Dirección (opcional), Obra Social (opcional). |
| | 3 | El usuario completa los campos obligatorios y presiona "Guardar". |
| | 4 | El sistema valida que el DNI no exista previamente en la base de datos. |
| | 5 | El sistema persiste el registro del paciente con estado "Activo". |
| | 6 | La interfaz muestra un mensaje de "Paciente registrado exitosamente". |
| **Postcondición** | El paciente queda registrado en el sistema con estado "Activo" y disponible para asignación de turnos y consultas. |
| **Excepciones** | **Paso** | |
| | 4 | Si el DNI ya existe en la base de datos, el sistema notifica "El paciente ya se encuentra registrado" y muestra los datos existentes, ofreciendo modificar o cancelar. |
| | 5 | Si ocurre un error de conexión con la base de datos, el sistema muestra un error 500 y aborta la transacción sin guardar datos parciales. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 5 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | Este caso de uso es disparado opcionalmente desde UC-REC-20 (Agendar Turno Manualmente) cuando el DNI ingresado no existe. |

---

### 3.2. UCE–REC-17 — Modificar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado modifica los datos demográficos de un paciente existente. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y selecciona "Buscar Paciente". |
| | 2 | El sistema ejecuta UC-REC-S-01 (Buscar Paciente): solicita DNI o nombre del paciente. |
| | 3 | El usuario ingresa el criterio de búsqueda. |
| | 4 | El sistema recupera los datos del paciente y los despliega en un formulario editable. |
| | 5 | El usuario modifica los campos deseados y presiona "Guardar Cambios". |
| | 6 | El sistema valida los campos y actualiza el registro en la base de datos. |
| | 7 | La interfaz muestra un mensaje de "Datos actualizados exitosamente". |
| **Postcondición** | Los datos del paciente quedan actualizados en la base de datos. |
| **Excepciones** | **Paso** | |
| | 4 | Si no se encuentra el paciente, el sistema muestra "Paciente no encontrado" y ofrece crear uno nuevo (UC-REC-16). |
| | 6 | Si el DNI modificado ya pertenece a otro paciente, el sistema rechaza el cambio y notifica el conflicto. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 6 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | La fecha de nacimiento es el único campo que no puede modificarse si el paciente tiene análisis registrados, para mantener consistencia en la edad calculada al momento del estudio. |

---

### 3.3. UCE–REC-18 — Consultar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El personal autorizado busca y visualiza el perfil completo de un paciente, incluyendo datos demográficos, fichas clínicas previas y el estado de sus análisis. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y visualiza un listado paginado con todos los pacientes registrados. |
| | 2 | El usuario utiliza los filtros de búsqueda (DNI, Nombre, Apellido, Rango de Fechas). |
| | 3 | El sistema consulta la base de datos y retorna los resultados coincidentes. |
| | 4 | El usuario selecciona un paciente de la lista. |
| | 5 | El sistema despliega la vista detallada del paciente: datos personales, fichas clínicas asociadas (en orden cronológico), análisis vinculados con sus estados. |
| **Postcondición** | El sistema presenta el perfil del paciente. Operación de solo lectura. |
| **Excepciones** | **Paso** | |
| | 3 | Si no hay pacientes registrados, la interfaz muestra "No hay pacientes registrados" y habilita el botón para crear uno nuevo (UC-REC-16). |
| **Rendimiento** | **Paso** | |
| | 3 | Menos de 2 segundos |
| **Frecuencia** | Alta |
| **Estabilidad** | Alta |
| **Comentarios** | Caso de uso de solo lectura. No modifica ningún dato del sistema. |

---

### 3.4. UCE–REC-19 — Desactivar Paciente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-02 Digitalización del Historial Clínico |
| **Requisitos asociados** | RF-05 Registro de Ficha Clínica |
| **Descripción** | El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero preservando la integridad histórica de los datos. |
| **Precondición** | El usuario debe tener una sesión activa con rol Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de "Pacientes" y selecciona "Buscar Paciente". |
| | 2 | El sistema ejecuta UC-REC-S-01 (Buscar Paciente): solicita DNI o nombre. |
| | 3 | El usuario ingresa el criterio de búsqueda. |
| | 4 | El sistema recupera y muestra los datos del paciente. |
| | 5 | El usuario presiona "Desactivar Paciente". |
| | 6 | El sistema solicita confirmación y el motivo de la desactivación (obligatorio). |
| | 7 | El usuario ingresa el motivo y confirma. |
| | 8 | El sistema verifica que el paciente no tenga turnos vigentes futuros. |
| | 9 | El sistema cambia el estado del paciente a "Inactivo". |
| | 10 | El sistema registra el evento en la tabla de auditoría. |
| | 11 | La interfaz muestra "Paciente desactivado exitosamente". |
| **Postcondición** | El paciente queda marcado como "Inactivo". Los datos históricos se conservan íntegros. |
| **Excepciones** | **Paso** | |
| | 4 | Si el paciente no existe, el sistema informa "Paciente no encontrado". |
| | 8 | Si el paciente tiene turnos vigentes futuros, el sistema lista los turnos y solicita al Administrador cancelarlos o reprogramarlos antes de desactivar. |
| | 9 | Si ocurre un error de base de datos, se aborta la transacción sin modificar el estado del paciente. |
| **Rendimiento** | **Paso** | |
| | 4 | Menos de 1 segundo |
| | 8 | Menos de 2 segundos |
| **Frecuencia** | Baja |
| **Estabilidad** | Alta |
| **Comentarios** | Se realiza baja lógica, no física, para mantener la integridad referencial de fichas clínicas y análisis históricos. Un paciente inactivo no puede recibir nuevos turnos. |

---

### 3.5. UCE–REC-20 — Agendar Turno Manualmente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-01 Agendamiento de Turnos vía Agente IA, RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado agenda un turno a nombre de un paciente directamente desde la interfaz web interna, sin intervención del Agente IA. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda y presiona "Nuevo Turno". |
| | 2 | El sistema solicita el DNI del paciente. |
| | 3 | El usuario ingresa el DNI; el sistema busca el registro del paciente. |
| | 4 | El sistema muestra la grilla de disponibilidad horaria. |
| | 5 | El usuario selecciona fecha, hora y tipo de análisis. |
| | 6 | El sistema registra y reserva el turno a nombre del paciente. |
| | 7 | El sistema envía una notificación de confirmación al paciente vía WhatsApp. |
| | 8 | El sistema programa el envío del recordatorio de asistencia. |
| **Postcondición** | El turno queda registrado y reservado. Se envía confirmación al paciente. |
| **Excepciones** | **Paso** | |
| | 3 | Si el DNI no existe en el sistema se dispara la extensión `<<extend>>` UC-REC-16 (Registrar Paciente). Al completar el registro, se retorna al paso 4. |
| | 5 | Si la franja seleccionada fue ocupada entre la consulta y la confirmación, el sistema notifica y solicita una nueva selección. |
| **Rendimiento** | **Paso** | |
| | 6 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | Reemplaza la funcionalidad de "Agendar" que estaba mezclada en el antiguo UC-REC-09. Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias. |

---

### 3.6. UCE–REC-21 — Cancelar Turno Manualmente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado cancela un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda y localiza el turno en el calendario. |
| | 2 | El usuario selecciona el turno y presiona "Cancelar Turno". |
| | 3 | El sistema solicita confirmación de la cancelación. |
| | 4 | El usuario confirma. |
| | 5 | El sistema cambia el estado del turno a "Cancelado", libera el bloque horario y notifica al paciente vía WhatsApp. |
| | 6 | El sistema registra el evento en la tabla de auditoría. |
| | 7 | Se ejecuta `<<include>>` UC-REC-04 (Reasignación Automática de Turno Liberado). |
| **Postcondición** | El turno queda cancelado, el bloque liberado y el paciente notificado. |
| **Excepciones** | **Paso** | |
| | 2 | Si el turno está a menos de 24 horas, el sistema advierte al usuario y solicita confirmación explícita antes de proceder. |
| **Rendimiento** | **Paso** | |
| | 5 | Menos de 1 segundo |
| **Frecuencia** | Media |
| **Estabilidad** | Alta |
| **Comentarios** | Reemplaza la funcionalidad de "Cancelar" del antiguo UC-REC-09. |

---

### 3.7. UCE–REC-22 — Reprogramar Turno Manualmente

| Campo | Detalle |
|---|---|
| **Objetivos asociados** | OBJ-01 Automatización de la Gestión de Turnos y Atención |
| **Requisitos asociados** | RF-04 Cancelación y Reprogramación de Turnos |
| **Descripción** | El personal autorizado cambia la fecha y/o hora de un turno existente desde la interfaz web interna. |
| **Precondición** | El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". Debe haber disponibilidad en la agenda para la nueva fecha/hora. |
| **Secuencia normal** | **Paso** | |
| | 1 | El usuario ingresa al módulo de Gestión de Agenda y localiza el turno en el calendario. |
| | 2 | El usuario selecciona el turno y presiona "Reprogramar". |
| | 3 | El sistema muestra la nueva disponibilidad horaria. |
| | 4 | El usuario selecciona la nueva fecha y hora. |
| | 5 | El sistema valida la disponibilidad y actualiza el turno. |
| | 6 | El sistema notifica al paciente vía WhatsApp con la nueva fecha/hora. |
| | 7 | El sistema registra el evento en la tabla de auditoría. |
| | 8 | Se ejecuta `<<include>>` UC-REC-04 (Reasignación Automática de Turno Liberado) por el bloque original liberado. |
| **Postcondición** | El turno se actualiza con la nueva fecha/hora. El paciente es notificado. |
| **Excepciones** | **Paso** | |
| | 4 | Si el turno ya fue reprogramado 2 veces previamente, el sistema advierte al usuario y solicita confirmación explícita para una excepción. |
| **Rendimiento** | **Paso** | |
| | 5 | Menos de 1 segundo |
| **Frecuencia** | Baja |
| **Estabilidad** | Alta |
| **Comentarios** | Reemplaza la funcionalidad de "Reprogramar" del antiguo UC-REC-09. |

---

## 4. Diagrama Mermaid — DCU Completo del Subsistema Gestión de Pacientes

```mermaid
usecaseDiagram
    title DCU - Subsistema Gestión de Pacientes

    actor "Bioquímico / Doctor" as BIOQ
    actor "Administrador" as ADMIN
    actor "Paciente (WhatsApp)" as PAC
    actor "Sistema (Automático)" as SYS

    rectangle "Gestión de Turnos - Paciente" as TURNOS_PAC {
        usecase "UC-REC-01\nAgendar Turno" as REC01
        usecase "UC-REC-02\nCancelar Turno" as REC02
        usecase "UC-REC-03\nReprogramar Turno" as REC03
        usecase "UC-REC-04\nReasignación Automática\nde Turno Liberado" as REC04
        usecase "UC-REC-05\nConsultar Turno" as REC05
        usecase "UC-REC-14\nCancelar Turno\npor Vencimiento" as REC14
    }

    rectangle "Gestión de Turnos - Interno" as TURNOS_INT {
        usecase "UC-REC-06\nConsultar Agenda" as REC06
        usecase "UC-REC-07\nConfigurar Parámetros\nde Agenda" as REC07
        usecase "UC-REC-08\nBloquear/Desbloquear\nDías y Franjas" as REC08
        usecase "UC-REC-15\nRegistrar Asistencia\na Turno" as REC15
        usecase "UC-REC-20\nAgendar Turno\nManualmente" as REC20
        usecase "UC-REC-21\nCancelar Turno\nManualmente" as REC21
        usecase "UC-REC-22\nReprogramar Turno\nManualmente" as REC22
    }

    rectangle "Gestión de Indicaciones Médicas" as INDIC {
        usecase "UC-REC-10\nCrear Indicación\nMédica" as REC10
        usecase "UC-REC-11\nModificar Indicación\nMédica" as REC11
        usecase "UC-REC-12\nEliminar Indicación\nMédica" as REC12
        usecase "UC-REC-13\nConsultar Indicaciones\nMédicas" as REC13
    }

    rectangle "Gestión de Pacientes" as PACIENTES {
        usecase "UC-REC-16\nRegistrar Paciente" as REC16
        usecase "UC-REC-17\nModificar Paciente" as REC17
        usecase "UC-REC-18\nConsultar Paciente" as REC18
        usecase "UC-REC-19\nDesactivar Paciente" as REC19
    }

    rectangle "Soporte (include/extend only)" as SOPORTE {
        usecase "Buscar Paciente" as BUSPAC
        usecase "Enviar Recordatorio\nde Turno" as RECORD
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

    ' === EXTEND ===
    REC20 ..> REC16 : <<extend>>\n(si DNI no existe)
    REC10 ..> ASIGIND : <<extend>>
    REC06 ..> REC20 : <<extend>>\n(desde agenda)
    REC06 ..> REC21 : <<extend>>\n(desde agenda)
    REC06 ..> REC22 : <<extend>>\n(desde agenda)
```

---

## 5. Tabla de Correspondencia: Antiguo vs Nuevo

| Antiguo | Nuevo | Estado |
|---|---|---|
| — | UC-REC-S-01 (Buscar Paciente) | **NUEVO** |
| — | UC-REC-S-02 (Enviar Recordatorio) | **NUEVO** |
| — | UC-REC-E-01 (Asignar Indicación a Tipo de Análisis) | **NUEVO** |
| — | UC-REC-16 (Registrar Paciente) | **NUEVO** |
| — | UC-REC-17 (Modificar Paciente) | **NUEVO** |
| — | UC-REC-18 (Consultar Paciente) | **NUEVO** |
| — | UC-REC-19 (Desactivar Paciente) | **NUEVO** |
| UC-REC-09 (Gestionar Turno Manualmente) | UC-REC-20 (Agendar Turno Manualmente) | **REEMPLAZADO** |
| UC-REC-09 (Gestionar Turno Manualmente) | UC-REC-21 (Cancelar Turno Manualmente) | **REEMPLAZADO** |
| UC-REC-09 (Gestionar Turno Manualmente) | UC-REC-22 (Reprogramar Turno Manualmente) | **REEMPLAZADO** |
| UC-REC-01 a UC-REC-08 | Sin cambios | — |
| UC-REC-10 a UC-REC-15 | Sin cambios | — |