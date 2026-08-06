# Cambios en `TF_2026_Requerimientos_KLUKA_JORGE.md`

**Fuente:** TODOS los cambios realizados en el archivo a partir (incluido) del commit `"."` (`93867ef`) en adelante, hasta el HEAD actual.

**Rango analizado:** `93867ef~1..HEAD`

**Commits que modificaron el archivo en ese rango:**
- `93867ef` — `.` → introduce el caso de uso estructural **Buscar Paciente** (`UC-REC-S-01` / `UCE-REC-S-01`).
- `89bf80b` — Completitud de los subsistemas **Laboratorio Bioquímico (DIAG)** y **Recursos de Laboratorio (LAB)** (mayoría de los cambios).

Cada cambio está agrupado según la sección del documento a la que corresponde.

---

## 1) Sección 2.2.2 - Descripción de Subsistemas
*(Commit `89bf80b`)*

Cambio de nomenclatura en las descripciones de los subsistemas:

- **Subsistema de Gestión de Pacientes**: renombrado desde "Subsistema de Recepción y Administración de Pacientes".
- **Subsistema de Laboratorio Bioquímico**: renombrado desde "Subsistema de Diagnóstico y Laboratorio Bioquímico"; se corrigió el nombre del módulo "Registro deInformación Clínica" → **"Registro de Información Clínica"**.
- **Subsistema de Acceso y Seguridad**: corregido el texto "Acceso y Seguridades" → "Acceso y Seguridad".

---

## 2) Sección 2.3.2 - Módulos del Proyecto
*(Commit `89bf80b`)*

Ampliación de la descripción de los módulos principales:

- **Registro de Análisis**: se agrega que "Incluye la gestión de tipos de análisis, la cancelación de estudios y un panel de trabajo para visualizar el volumen de análisis por estado".
- **Stock de Insumos Reactivos**: se agrega "incluyendo trazabilidad por lotes, ubicaciones de almacenamiento y devoluciones".
- **Control de Residuos**: se agrega "incluyendo el registro de disposición final y la gestión de categorías de peligrosidad".

---

## 3) Sección 2.4 - Requisitos de Información (IRQ)
*(Commit `89bf80b`)*

### 3.1 Modificaciones a IRQ existentes
- **IRQ-01 Ficha Clínica → Datos específicos**: se reemplaza el conjunto de datos. Sale: "Médico derivante, Institución, Diagnóstico presuntivo"; entran: **"Correo Electrónico"** y **"Obra Social"**.
- **IRQ-02 Análisis Micológico → Datos específicos**: se elimina "Cultivo" y se amplían los estados: ahora **Pendiente, En proceso, Terminado, Validado, Cancelado, Derivado**.
- **IRQ-03 Insumo/Reactivo → Datos específicos**: se agregan **Número de Lote, Unidad de Medida (ml, g, unidades), Categoría, Ubicación de Almacenamiento, Fecha de Ingreso**.

### 3.2 Nuevos IRQ agregados
- **IRQ-05 Catálogo de Tipos de Análisis/Muestra** — Soporta `UC-DIAG-11`. Datos: Nombre, Descripción, Indicaciones asociadas, Estado (Activo/Inactivo).
- **IRQ-06 Movimiento de Inventario** — Soporta `UC-LAB-07`. Datos: Tipo de movimiento (Ingreso/Retiro/Devolución), Fecha, Cantidad, Lote afectado, Usuario responsable, Análisis o práctica asociada.
- **IRQ-07 Categoría de Residuo** — Soporta `UC-LAB-10`. Datos: Nombre, Clase de peligrosidad (Clase I, II, III), Descripción, Instrucciones de almacenamiento.

---

## 4) Sección 2.5 - Requisitos Funcionales
*(Commit `89bf80b`)*

Nuevos requisitos funcionales agregados (RF-16 a RF-21):

- **RF-16 Gestión de Catálogos Clínicos**: el Administrador gestiona tipos de análisis micológicos y tipos de muestra (crear, modificar, desactivar).
- **RF-17 Gestión de Catálogos de Inventario**: el Administrador gestiona categorías de insumos, ubicaciones de almacenamiento y categorías de residuos.
- **RF-18 Trazabilidad de Lotes y Vencimientos**: registro de lotes (nº de lote y vencimiento) al ingresar insumos, alerta de vencimiento y consumo primero del lote con vencimiento más próximo (rotación FEFO).
- **RF-19 Registro de Disposición Final de Residuos**: registrar salida y disposición final con fecha, responsable y método de tratamiento.
- **RF-20 Modificación de Ficha Clínica**: el Bioquímico/Doctor modifica una ficha clínica manteniendo historial de versiones.
- **RF-21 Cancelación de Análisis**: cancelar un análisis en curso (motivo obligatorio) cuando esté en estado "Pendiente" o "En Proceso".

---

## 5) Sección 2.7.2 - Definición de Actores
*(Commit `89bf80b`)*

- **ACT-01 Bioquímico/Doctor**: se agrega que es responsable de "registrar, actualizar, **modificar, cancelar** y validar" el ciclo de vida de los análisis.
- **ACT-02 Profesor**: se agrega que "también registra la generación de residuos químicos producto de las prácticas educativas y puede consultar el inventario y la trazabilidad de movimientos".
- **ACT-03 Administrador**: se agrega la "gestión de catálogos del sistema (tipos de análisis, insumos, categorías, ubicaciones)".

---

## 6) Sección 2.7.3.1 - Subsistema Gestión de Turnos y Atención (UC-REC + UC-CON)
*(Commits `93867ef` y `89bf80b`)*

### 6.1 Cambios del commit `"."` (`93867ef`)
- **UC-REC-17 / UC-REC-19 (Comentarios)**: referencia a "Buscar Paciente" tipificada como `<<include>>` **UC-REC-S-01 (Buscar Paciente)**.
- **Nuevo UC-REC-S-01 Buscar Paciente**: caso de uso estructural (include-only) que recibe criterio de búsqueda (DNI, Nombre o Apellido) y retorna los pacientes coincidentes al caso invocante. Subflujo `<<include>>` de UC-REC-17 y UC-REC-19.

### Cambios del commit `89bf80b`
- **UC-REC-03 Reprogramar Turno**: requisito asociado RF-03 pasa de "Gesti├│n de Lista de Espera por Turnos Liberados" a **"Gestión de Reagendación automática"**.
- **UC-REC-04 Reasignación Automática de Turno Liberado**: misma corrección de referencia RF-03 a "Gestión de Reagendación automática".
- **UC-REC-16 Registrar Paciente**: corrección menor de la estructura de tabla (`|---|---|` → `|---|---|---|`) y del objetivo asociado (OBJ-01).

---

## 7) Sección 2.7.3.2 - Subsistema Laboratorio Bioquímico (UC-DIAG)
*(Commit `89bf80b`)*

Ampliación significativa de casos de uso:

### Modificaciones
- **UC-DIAG-01 Registrar Ficha Clínica**: se agrega comentario "Incluye `<<extend>>` a UC-DIAG-08 (Modificar Ficha Clínica)".
- **UC-DIAG-02 Registrar Ingreso de Muestra**: se aclara la precondición (la Ficha Clínica puede haberse registrado previamente, no necesariamente en la sesión actual).
- **UC-DIAG-04 Validar Análisis**: se agrega RF-08 a requisitos; y en postcondiciones se explicita que el sistema genera el Token OTP y envía el WhatsApp con enlace, instrucciones y OTP (absorbe el flujo del antiguo UC-DIAG-05).
- **UC-DIAG-05**: renombrado de "Notificación de Resultados" a **"Descargar Informe"** (antes UC-DIAG-06). El antiguo UC-DIAG-05 (Notificación de Resultados) se elimina como caso separado y se integra en UC-DIAG-04.
- **UC-DIAG-07**: renombrado de "Consultar Ficha Clínica" a **"Consultar Historial de Paciente"**.

### Nuevos casos de uso
- **UC-DIAG-08 Modificar Ficha Clínica** — soporta RF-20. Restricción: no modificar si hay análisis "Validado" (si ya validado, solo campos no clínicos). Incluye `<<include>>` UC-REC-S-01.
- **UC-DIAG-09 Cancelar Análisis** — soporta RF-21. Estado → "Cancelado"; requiere motivo obligatorio; aplica a estados "Pendiente"/"En Proceso".
- **UC-DIAG-10 Consultar Panel de Análisis** — soporta RF-06. Panel de trabajo filtrable por estado/tipo/fecha/bioquímico; solo lectura; difiere de DIAG-07.
- **UC-DIAG-11 Gestionar Tipos de Análisis y Muestra** — soporta RF-16. Actor: Administrador; sub-flujos Crear/Modificar/Desactivar (baja lógica).

---

## 8) Sección 2.7.3.3 - Subsistema Recursos de Laboratorio (UC-LAB)
*(Commit `89bf80b`)*

### Modificaciones
- **UC-LAB-02 Registrar Retiro de Insumos**: se amplía la descripción para registrar análisis/práctica destino, lote consumido (FIFO/FEFO), ubicación de origen y disposición final de residuos.
- **UC-LAB-04 Generar Reporte Mensual de Residuos**: precondición corregida a "sesión activa con rol de Administrador".

### Nuevos casos de uso
- **UC-LAB-06 Gestionar Catálogo de Insumos** — RF-17. Datos: nombre, descripción, unidad de medida, categoría, umbral de alerta, ubicación.
- **UC-LAB-07 Consultar Trazabilidad de Movimientos** — RF-10. Historial de ingresos/retiros/devoluciones, filtrable (solo lectura).
- **UC-LAB-08 Configurar Umbrales de Alerta** — RF-09. Configura stock mínimo y días de pre-vencimiento por insumo.
- **UC-LAB-09 Registrar Devolución de Insumos** — RF-10. Revierte total/parcialmente un retiro; advierte si el lote ya venció.
- **UC-LAB-10 Gestionar Categorías de Residuos** — RF-17. Catálogo de categorías/clases de peligrosidad.
- **UC-LAB-11 Consultar y Modificar Registro de Residuos** — RF-11. Consulta y corrección antes de consolidar en reporte mensual.
- **UC-LAB-12 Gestionar Categorías de Insumos** — RF-17. Catálogo de categorías (reactivos, medios de cultivo, descartables, equipos).
- **UC-LAB-13 Generar Reporte de Inventario** — RF-10 y RF-09. Reporte PDF/CSV del estado del inventario.

---

## 9) Sección 2.8 - Casos de Uso Extendidos (UCE)
*(Commits `93867ef` y `89bf80b`)*

### 9.1 Reestructuración de subsecciones (commit `89bf80b`)
- Nueva numeración/renombrado de subsecciones:
  - `2.8.1` — "Subsistema Gestión Clínica" → **"Subsistema Gestión de Pacientes"**.
  - `2.8.2` — "Subsistema Recursos de Laboratorio" → **"Subsistema Laboratorio Bioquímico"**.
  - `2.8.3` — "Subsistema Acceso y Seguridad" → **"Subsistema Recursos de Laboratorio"**.
  - Nueva `2.8.4` — "Subsistema Acceso y Seguridad".
  - `2.8.4` (extendida) → `2.8.5` "Subsistema Reportes y Estadísticas".
- En 2.8.3 (Recursos de Laboratorio) se agrega una **nota**: los UCE correspondientes a UC-LAB-01 a UC-LAB-13 están pendientes de desarrollo.

### 9.2 Modificaciones a UCE existentes (commit `89bf80b`)
- **UCE-REC-01 Agendar Turno**: se elimina el `<<include>>` "Enviar Recordatorio de Turno" del paso 8.
- **UCE-REC-03**: referencia RF-03 corregida a "Gestión de Reagendación automática".
- **UCE-REC-04**: referencia RF-03 corregida a "Gestión de Reagendación automática".
- **UCE de atención de turno (Presente)**: reordenación de pasos 5.1/6/7 → 6/7/8 (formulario de datos demográficos incompletos, registro en auditoría, botón iniciar consulta a UC-DIAG-01).
- **UCE-REC-17 / UCE-REC-19**: paso 2 referencia a UCE-REC-S-01 (Buscar Paciente).
- **UCE-REC-20 / REC-21 / REC-22**: se elimina de los comentarios la mención "Reemplaza la funcionalidad … del antiguo UC-REC-09".
- **UCE-REC-11 (Rendimiento)**: paso de rendimiento movido de 6 a 3.
- Se agrega una **nota** en 2.8.1: "No existe UC-REC-09. La numeración salta intencionalmente de UC-REC-08 a UC-REC-10".

### 9.3 Nuevo UCE del commit `"."` (`93867ef`)
- **UCE-REC-S-01 Buscar Paciente**: caso de uso estructural (include-only) con secuencia normal, excepciones y rendimiento. Subflujo `<<include>>` de UC-REC-17 y UC-REC-19.

### 9.4 Cambios en 2.8.2 (Laboratorio Bioquímico) (commit `89bf80b`)
- **UCE-DIAG-01 Registrar Ficha Clínica**: redacción de pasos 3, 5, 7, 8, 9 pasan de referencias a "Backend"/"interfaz" a terminología "El sistema"/"La interfaz".

---

## 10) Sección Glosario de Términos
*(Commit `89bf80b`)*

El glosario (que estaba vacío) se completa con los siguientes términos:

- **Agente IA** — Arquitectura
- **OTP (One-Time Password)** — Seguridad
- **Token** — Seguridad
- **Alta Temprana** — Clínico
- **Baja lógica** — Seguridad / Datos
- **Ficha Clínica** — Clínico
- **Muestra** — Clínico
- **Micología** — Dominio
- **JWT (JSON Web Token)** — Seguridad

---

## Resumen por commit

| Commit | Alcance |
|---|---|
| `93867ef` (`"."`) | Caso de uso estructural **Buscar Paciente**: `UC-REC-S-01`, `UCE-REC-S-01` y sus referencias `<<include>>` en UC-REC-17/19. |
| `89bf80b` | Completitud de subsistemas **DIAG** y **LAB**: nomenclatura de subsistemas, módulos, IRQ-05/06/07, RF-16 a RF-21, actores, UC-DIAG-08 a 11, UC-LAB-06 a 13, reestructuración de la sección 2.8 y Glosario. |
