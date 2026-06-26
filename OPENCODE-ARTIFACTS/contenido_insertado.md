# Contenido Insertado y Modificado — Subsistema Gestión de Pacientes

Contenido extraído del documento `TF_2026_Requerimientos_KLUKA_JORGE.md` después de los cambios.

---

## SECCIÓN 2.7.3.1 — Definiciones de Casos de Uso

### Insertados: UC-REC-16 a UC-REC-22

```
|**UC–REC-16**|**Registrar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| El personal autorizado registra a un paciente en el sistema con todos sus datos demográficos completos desde la interfaz web interna. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. El paciente no debe existir previamente en la base de datos. |
|**Postcondiciones**| El paciente queda registrado en el sistema con estado "Activo" y disponible para asignación de turnos y consultas. |

|**UC–REC-17**|**Modificar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| El personal autorizado modifica los datos demográficos de un paciente existente en el sistema. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. |
|**Postcondiciones**| Los datos del paciente quedan actualizados en la base de datos. |
|**Comentarios**| Incluye `<<include>>` Buscar Paciente. |

|**UC–REC-18**|**Consultar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| El personal autorizado busca y visualiza los datos demográficos y el historial clínico acumulado de un paciente, incluyendo fichas clínicas previas y análisis asociados. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. |
|**Postcondiciones**| El sistema presenta el perfil completo del paciente con secciones de datos personales, historial de consultas y análisis. Operación de solo lectura. |

|**UC–REC-19**|**Desactivar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero manteniendo la integridad histórica de los registros. |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador. |
|**Postcondiciones**| El paciente queda marcado como "Inactivo" en la base de datos. No puede agendarse nuevos turnos a su nombre. Los registros históricos se conservan. |
|**Comentarios**| Incluye `<<include>>` Buscar Paciente. Se realiza baja lógica para mantener integridad referencial. |

|**UC–REC-20**|**Agendar Turno Manualmente**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos |
|**Descripción**| El personal autorizado agenda un turno a nombre de un paciente directamente desde la interfaz web interna, sin intervención del Agente IA. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. |
|**Postcondiciones**| El turno queda registrado y reservado en el sistema. Se envía notificación de confirmación al paciente vía WhatsApp. |
|**Comentarios**| Si el DNI ingresado no existe, se dispara una extensión a UC-REC-16 (Registrar Paciente). |

|**UC–REC-21**|**Cancelar Turno Manualmente**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos |
|**Descripción**| El personal autorizado cancela un turno existente desde la interfaz web interna. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado vigente. |
|**Postcondiciones**| El turno cambia a estado "Cancelado". El bloque horario queda liberado. Se notifica al paciente. Incluye UC-REC-04 (Reasignación Automática). |

|**UC–REC-22**|**Reprogramar Turno Manualmente**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos |
|**Descripción**| El personal autorizado cambia la fecha y/o hora de un turno existente desde la interfaz web interna. |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado vigente. Debe haber disponibilidad en la agenda. |
|**Postcondiciones**| El turno se actualiza con la nueva fecha/hora. El bloque anterior queda liberado. Se notifica al paciente. Incluye UC-REC-04 (Reasignación Automática). |
```

---

## SECCIÓN 2.8.1 — Casos de Uso Extendidos

### Modificado: UCE-REC-01 — Agendar Turno

```
|**UCE–REC-01**|**Agendar Turno**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA <br>RF-02 Envío de Indicaciones Médicas  |  |
|**Descripción**| El Paciente interactúa de manera asíncrona con el sistema, a través de WhatsApp, para solicitar y registrar un nuevo turno para análisis micológico.  |  |
|**Precondición**| El paciente debe comunicarse vía WhatsApp. <br>El sistema debe contar con disponibilidad de fechas y horarios en la agenda.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El paciente saluda o solicita un turno al Agente IA.  |
|  | 2 | El Agente IA solicita el DNI y Nombre Completo del paciente.  |
|  | 3 | El paciente ingresa los datos solicitados.  |
|  | 4 | El Agente IA consulta la agenda, muestra opciones disponibles y aplica un bloqueo temporal de 10 minutos sobre esos horarios.  |
|  | 5 | El paciente selecciona un horario.  |
|  | 6 | El sistema registra y reserva el turno a nombre del paciente.  |
|  | 7 | El sistema envía automáticamente un mensaje de confirmación y las indicaciones médicas predefinidas.  |
|  | **8** | **El sistema programa en cola el envío de un recordatorio de asistencia (`<<include>>` Enviar Recordatorio de Turno).** |
|**Postcondición**| El turno queda registrado y reservado. |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si el formato del DNI es inválido, el sistema solicita su reingreso iterando este paso.  |
|  | 5 | Si transcurren más de 10 minutos sin respuesta, el sistema libera el bloqueo horario y notifica la cancelación de la solicitud. |
|  | 4 | Si no hay turnos disponibles, el sistema informa y ofrece suscribirse a alertas de cancelación.  |
|**Rendimiento**|**Paso**|  |
|  | 4 |  |
|  | 7 |  |
|**Frecuencia**| Alta (Multiples veces al dia) |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Se permite agendar turnos para familiares ingresando el DNI correspondiente a la persona que se realizará el análisis.  |  |
```

**Cambios:** Se agregó el paso 8 (programación del recordatorio). Se simplificó la postcondición.

---

### Modificado: UCE-REC-10 — Crear Indicación Médica

```
|**UCE–REC-10**|**Crear Indicación Médica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas |  |
|**Descripción**| El Bioquímico/Doctor o Administrador crea una nueva indicación médica predefinida en el sistema para ser enviada automáticamente al paciente al momento de agendar un turno. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Indicaciones Médicas y presiona "Nueva Indicación". |
|  | 2 | **La interfaz despliega un formulario con los campos: Título, Contenido, Tipo de Análisis asociado (obligatorio).** |
|  | 3 | El usuario completa los campos y presiona "Guardar". |
|  | 4 | **El sistema valida que todos los campos obligatorios estén completos (título, contenido y tipo de análisis).** |
|  | 5 | **El sistema ejecuta `<<include>>` Asignar Indicación a Tipo de Análisis: vincula la indicación con el tipo de análisis seleccionado.** |
|  | 6 | **El sistema persiste el registro en la base de datos.** |
|  | 7 | **La interfaz muestra "Indicación creada exitosamente".** |
|**Postcondición**| La nueva indicación médica queda registrada y disponible para ser asignada a turnos futuros. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | **Si el contenido está vacío o no se seleccionó un Tipo de Análisis, el sistema muestra una alerta de validación y no persiste.** |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |
```

**Cambios:** "Tipo de Análisis" pasa de opcional a obligatorio. Se agregaron los pasos 5-7 con `<<include>>` a Asignar Indicación. Excepción actualizada.

---

### Modificado: UCE-REC-15 — Registrar Asistencia a Turno

```
|**UCE–REC-15**|**Registrar Asistencia a Turno**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| El Bioquímico/Doctor o Administrador registra la asistencia o inasistencia del paciente a su turno programado al momento de presentarse en el laboratorio. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. El paciente debe tener un turno en estado "Confirmado" para el día y hora actual. |  |
|**Secuencia normal (Presente)**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Gestión de Agenda y localiza el turno del día. |
|  | 2 | El usuario selecciona el turno y presiona "Registrar Asistencia". |
|  | 3 | El sistema despliega un diálogo con las opciones "Presente" y "Ausente". |
|  | 4 | El usuario selecciona "Presente". |
|  | 5 | El sistema cambia el estado del turno a "Atendido" y registra la hora de atención. |
|  | **5.1** | **El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes antes de continuar.** |
|  | 6 | El sistema registra el evento en la tabla de auditoría. |
|  | 7 | La interfaz confirma la operación y habilita el botón para iniciar la consulta (UC-DIAG-01). |
|**Secuencia normal (Ausente)**|**Paso**|  |
|  | 1 | El usuario sigue los pasos 1 a 3 de la secuencia normal (Presente). |
|  | 2 | El usuario selecciona "Ausente". |
|  | 3 | El sistema solicita un motivo opcional de inasistencia. |
|  | 4 | El usuario ingresa el motivo (opcional) y confirma. |
|  | 5 | El sistema cambia el estado del turno a "No Asistió" y libera el bloque horario. |
|  | 6 | Se dispara internamente UC-REC-04. |
|  | 7 | El sistema registra el evento en la tabla de auditoría. |
|**Postcondición**| El estado del turno se actualiza a "Atendido" o "No Asistió" según corresponda. |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si el turno ya fue marcado previamente, el sistema informa y bloquea la acción. |
|**Rendimiento**|**Paso**|  |
|  | 5 (Presente) | Menos de 1 segundo |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |
```

**Cambio:** Se agregó el paso 5.1 (completitud de datos demográficos del paciente en recepción).

---

### Insertados: UCE-REC-16 a UCE-REC-22

```
|**UCE–REC-16**|**Registrar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El personal autorizado registra a un paciente en el sistema con todos sus datos demográficos completos desde la interfaz web interna. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El paciente no debe existir previamente en la base de datos. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Nuevo Paciente". |
|  | 2 | La interfaz despliega el formulario de registro con los campos: DNI, Nombre, Apellido, Fecha de Nacimiento, Teléfono, Correo Electrónico, Dirección, Obra Social. |
|  | 3 | El usuario completa los campos obligatorios y presiona "Guardar". |
|  | 4 | El sistema valida que el DNI no exista previamente en la base de datos. |
|  | 5 | El sistema persiste el registro del paciente con estado "Activo". |
|  | 6 | La interfaz muestra un mensaje de "Paciente registrado exitosamente". |
|**Postcondición**| El paciente queda registrado con estado "Activo" y disponible para asignación de turnos y consultas. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el DNI ya existe, el sistema notifica "El paciente ya se encuentra registrado", muestra los datos existentes y ofrece modificarlos (REC-17) o cancelar. |
|  | 5 | Si ocurre un error de conexión con la base de datos, el sistema muestra un error 500 y aborta la transacción sin guardar datos parciales. |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|  | 5 | Menos de 1 segundo |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Este caso de uso es disparado opcionalmente desde UC-REC-20 (Agendar Turno Manualmente) cuando el DNI ingresado no existe (relación extiende). |  |
```

```
|**UCE–REC-17**|**Modificar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El personal autorizado modifica los datos demográficos de un paciente existente. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
|  | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido como criterio de búsqueda. |
|  | 3 | El usuario ingresa el criterio de búsqueda. |
|  | 4 | El sistema consulta la base de datos. |
|  | 5 | Si hay múltiples coincidencias, muestra un listado paginado para que el usuario seleccione. Si hay una sola coincidencia, la selecciona automáticamente. |
|  | 6 | El sistema despliega el formulario pre-poblado con los datos actuales del paciente. |
|  | 7 | El usuario modifica los campos deseados y presiona "Guardar Cambios". |
|  | 8 | El sistema valida los campos editados (formato de DNI, teléfono, etc.). |
|  | 9 | El sistema actualiza el registro en la base de datos. |
|  | 10 | La interfaz muestra "Datos actualizados exitosamente". |
|  | 11 | El sistema registra el evento en la tabla de auditoría. |
|**Postcondición**| Los datos del paciente quedan actualizados en la base de datos. Se registra el cambio en auditoría. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si no se encuentra ningún paciente con el criterio ingresado, el sistema muestra "Paciente no encontrado" y ofrece crear uno nuevo (REC-16). |
|  | 8 | Si el DNI modificado ya pertenece a otro paciente, el sistema rechaza el cambio y notifica "El DNI ingresado ya corresponde a otro paciente". |
|  | 9 | Si hay error de base de datos, se aborta la transacción sin guardar cambios parciales. |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|  | 9 | Menos de 1 segundo |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| La Fecha de Nacimiento no puede modificarse si el paciente tiene análisis registrados, para mantener consistencia en la edad calculada al momento del estudio. |  |
```

```
|**UCE–REC-18**|**Consultar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El personal autorizado busca y visualiza el perfil completo de un paciente, incluyendo datos demográficos, fichas clínicas previas, análisis asociados y resultados. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes". |
|  | 2 | El sistema muestra un listado paginado con todos los pacientes registrados. |
|  | 3 | El usuario aplica filtros de búsqueda: DNI, Nombre, Apellido, Estado. |
|  | 4 | El sistema consulta la base de datos y retorna los resultados coincidentes. |
|  | 5 | El usuario selecciona un paciente de la lista. |
|  | 6 | El sistema despliega la vista detallada: Datos Personales, Historial de Consultas, Análisis Micológicos con su estado, Resultados. |
|**Postcondición**| El sistema presenta el perfil completo del paciente. Operación de solo lectura. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si no hay pacientes registrados, la interfaz muestra "No hay pacientes registrados" y habilita el botón para crear uno nuevo (REC-16). |
|  | 4 | Si ningún paciente coincide con los filtros, se muestra "No se encontraron pacientes con los criterios ingresados". |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 2 segundos |
|  | 6 | Menos de 2 segundos |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Caso de uso de solo lectura. La edad se calcula dinámicamente a partir de la Fecha de Nacimiento. |  |
```

```
|**UCE–REC-19**|**Desactivar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero preservando íntegramente el historial clínico y los análisis existentes. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
|  | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido. |
|  | 3 | El usuario ingresa el criterio de búsqueda. |
|  | 4 | El sistema recupera y muestra los datos del paciente. |
|  | 5 | El usuario presiona "Desactivar Paciente". |
|  | 6 | El sistema muestra un diálogo de confirmación solicitando el motivo obligatorio de la desactivación (ej. "Paciente fallecido", "Solicitud de baja", "Registro duplicado"). |
|  | 7 | El usuario ingresa el motivo y confirma la acción. |
|  | 8 | El sistema verifica que el paciente no tenga turnos vigentes futuros. |
|  | 9 | El sistema cambia el estado del paciente a "Inactivo". |
|  | 10 | El sistema registra el evento en la tabla de auditoría con: usuario, fecha, motivo, paciente. |
|  | 11 | La interfaz muestra "Paciente desactivado exitosamente". |
|**Postcondición**| El paciente queda marcado como "Inactivo". No puede agendarse nuevos turnos a su nombre. Los registros históricos se conservan intactos. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el paciente no existe, el sistema informa "Paciente no encontrado" y finaliza. |
|  | 8 | Si el paciente tiene turnos vigentes futuros, el sistema muestra la lista de turnos activos y solicita al Administrador cancelarlos antes de permitir la desactivación. |
|  | 9 | Si ocurre un error de base de datos, se aborta la transacción sin modificar el estado del paciente. |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|  | 8 | Menos de 2 segundos |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| La desactivación es una baja lógica, NO física. Un paciente inactivo no puede recibir nuevos turnos, pero todo su historial permanece accesible para consulta e investigación. |  |
```

```
|**UCE–REC-20**|**Agendar Turno Manualmente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| El personal autorizado agenda un turno a nombre de un paciente directamente desde la interfaz web interna, sin intervención del Agente IA. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Gestión de Agenda y presiona "Nuevo Turno". |
|  | 2 | El sistema solicita el DNI del paciente. |
|  | 3 | El usuario ingresa el DNI. |
|  | 4 | El sistema busca el registro del paciente en la base de datos. |
|  | 5 | El sistema muestra la grilla de disponibilidad horaria para la fecha actual. |
|  | 6 | El usuario selecciona: fecha, horario disponible, tipo de análisis. |
|  | 7 | El usuario presiona "Confirmar Turno". |
|  | 8 | El sistema registra y reserva el turno a nombre del paciente con estado "Confirmado". |
|  | 9 | El sistema envía una notificación de confirmación al paciente vía WhatsApp. |
|  | 10 | El sistema programa el envío del recordatorio de asistencia. |
|  | 11 | El sistema registra el evento en la tabla de auditoría. |
|  | 12 | La interfaz muestra "Turno registrado exitosamente". |
|**Postcondición**| El turno queda registrado, reservado, y el paciente notificado. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el DNI no existe en el sistema, se dispara la extensión UC-REC-16 (Registrar Paciente). Al completar el registro exitosamente, se retorna al paso 5. |
|  | 6 | Si la franja seleccionada fue ocupada entre la consulta y la confirmación, el sistema notifica "El horario seleccionado ya no está disponible" y muestra la grilla actualizada. |
|**Rendimiento**|**Paso**|  |
|  | 8 | Menos de 1 segundo |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Reemplaza la funcionalidad de "Agendar" del antiguo UC-REC-09. Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias. |  |
```

```
|**UCE–REC-21**|**Cancelar Turno Manualmente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| El personal autorizado cancela un turno existente desde la interfaz web interna. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Gestión de Agenda. |
|  | 2 | El usuario localiza el turno en el calendario o mediante el buscador por DNI. |
|  | 3 | El usuario selecciona el turno y presiona "Cancelar Turno". |
|  | 4 | El sistema muestra un diálogo de confirmación: "¿Está seguro de cancelar el turno de [Paciente] el [fecha] a las [hora]?". |
|  | 5 | El usuario confirma la cancelación. |
|  | 6 | El sistema cambia el estado del turno a "Cancelado". |
|  | 7 | El sistema libera el bloque horario en la agenda. |
|  | 8 | El sistema envía notificación al paciente vía WhatsApp informando la cancelación. |
|  | 9 | Se ejecuta internamente UC-REC-04 (Reasignación Automática de Turno Liberado). |
|  | 10 | El sistema registra el evento en la tabla de auditoría. |
|  | 11 | La interfaz muestra "Turno cancelado exitosamente". |
|**Postcondición**| Turno cancelado, bloque liberado, paciente notificado, reasignación automática disparada. |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si el turno está a menos de 24 horas de su horario, el sistema muestra una advertencia y requiere confirmación explícita adicional. |
|  | 5 | Si el usuario cancela la confirmación, se aborta la operación sin modificar el turno. |
|**Rendimiento**|**Paso**|  |
|  | 6-7 | Menos de 1 segundo |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Reemplaza la funcionalidad de "Cancelar" del antiguo UC-REC-09. |  |
```

```
|**UCE–REC-22**|**Reprogramar Turno Manualmente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| El personal autorizado cambia la fecha y/o hora de un turno existente desde la interfaz web interna. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. El turno debe existir y estar en estado "Confirmado" o "Pendiente". Debe haber disponibilidad en la agenda. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Gestión de Agenda. |
|  | 2 | El usuario localiza el turno en el calendario o mediante buscador. |
|  | 3 | El usuario selecciona el turno y presiona "Reprogramar". |
|  | 4 | El sistema verifica que el turno no haya sido reprogramado más de 2 veces. |
|  | 5 | El sistema muestra la grilla de disponibilidad horaria. |
|  | 6 | El usuario selecciona la nueva fecha y hora. |
|  | 7 | El sistema valida que la nueva franja esté disponible. |
|  | 8 | El sistema actualiza el registro del turno con la nueva fecha/hora. |
|  | 9 | El sistema libera el bloque horario original. |
|  | 10 | El sistema envía notificación al paciente vía WhatsApp con la nueva fecha y hora. |
|  | 11 | Se ejecuta internamente UC-REC-04 (Reasignación Automática de Turno Liberado). |
|  | 12 | El sistema registra el evento en la tabla de auditoría. |
|  | 13 | La interfaz muestra "Turno reprogramado exitosamente". |
|**Postcondición**| Turno actualizado, bloque original liberado, paciente notificado. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el turno ya fue reprogramado 2 veces, el sistema muestra una advertencia y requiere confirmación del Administrador. |
|  | 7 | Si la nueva franja fue ocupada entre la consulta y la confirmación, el sistema notifica y solicita una nueva selección. |
|**Rendimiento**|**Paso**|  |
|  | 8 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Reemplaza la funcionalidad de "Reprogramar" del antiguo UC-REC-09. |  |
```