# Manifiesto de Infraestructura y Entorno — SIGEMI

> **Estado**: v0.1 — documento vivo de decisiones.
> **Alcance**: decisiones de infraestructura, entorno de desarrollo y despliegue, y tecnología, para el sistema SIGEMI (módulo de Bioquímica y Farmacia, UNaM).
> **Fuentes de verdad vinculadas**: `TF_2026_Requerimientos_KLUKA_JORGE.md` y `Diagramas/diagrama_clases_sigemi.mmd`.
> **Fecha de creación**: 02/11/2026.

---

## 0. Contexto y naturaleza del proyecto

SIGEMI es un sistema **real para un cliente** (el laboratorio de Micología del módulo de Bioquímica y Farmacia de la UNaM), que a su vez será **evaluado académicamente**. Esto eleva el criterio por encima del "prototipo de TP": las decisiones deben ser robustas, defendibles en una mesa de examen, y legalmente correctas frente a un cliente real.

Por lo tanto, este manifiesto registra **decisiones firmes** y **alternativas descartadas con su razón**, para que la defensa evidencie que cada elección fue evaluada y no obedecida "porque sí".

---

## 1. Stack tecnológico base

### Decisiones firmes

| Capa | Tecnología | Motivo principal |
|---|---|---|
| Backend | **FastAPI** (Python) | Framework asíncrono moderno, tipado a través de Pydantic, documentación OpenAPI automática, ideal para APIs consumidas por React |
| Frontend | **React** (TypeScript) | SPA mantenible, ecosistema maduro, tipado estático con TypeScript |
| Base de datos | **PostgreSQL** | Relacional, maduro, transaccional, con soporte nativo para la trazabilidad e inmutabilidad que exige la normativa |
| Asincronía / cola | **Celery** | Trabajadores para tareas de fondo no atadas a una request HTTP |
| Broker / cache | **Redis** | Broker de Celery + cache de la aplicación |
| Scheduler periódico | **Celery Beat** | Despacho de tareas cron (OTP, reportes, backups) |
| Arquitectura de referencia | **MVC (no estricto)** | Modelo-Controller-Service orientado a capas, sin dogma: sirve como guía de organización, no como corset |
| Estructura de repositorio | **Monorepo único** | un repo con `frontend/` y `backend/` |
| Persistencia (ORM) | **SQLAlchemy** | ORM de la capa de datos |
| Migraciones | **Alembic** | Versionado del esquema de base de datos |
| Autenticación | **JWT** | Tokens firmados; contraseñas con hash (BCrypt/argon2) |
| Claves primarias | **UUID** | generadas en la aplicación (portabilidad entre entornos, no expone secuencialidad) |
| Versionado de ficha clínica | **jsonb** | `datos_previos`/`datos_nuevos` como `jsonb` (consultable e indexable para retención de 10 años), no `text` |
| Puntero de versión | **`version_actual` persistido** | se mantiene como campo explícito en `ficha_clinica` (decisión firme del cliente), aun sabiendo que puede derivarse del versionado |

### Arquitectura a grandes rasgos

```
React (SPA)  →  FastAPI (API REST)
                       │
                       ├─→ PostgreSQL (datos transaccionales + auditoría)
                       ├─→ Redis (broker + cache)
                       └─→ Celery workers (tareas de fondo)
                              └─→ Celery Beat (disparador de tareas periódicas)
```

- **FastAPI** es el corazón: recibe HTTP, valida (Pydantic), aplica reglas de negocio y responde.
- **Celery** ejecuta lo que no está atado a una request: regeneración de OTP, notificaciones, reportes mensuales, backups.
- **Celery+Redis+Beat NO reemplazan a FastAPI**: lo acompañan. Son capas distintas del sistema.

### Por qué Stack Completo (Celery + Redis + Beat) y no el liviano

El sistema tiene trabajo de fondo **real y programado**:

- Ciclo de OTP con vencimiento a 7 días y regeneración automática (RF-07).
- Envío asíncrono de notificaciones por WhatsApp (RF-07).
- Generación automática de reporte mensual de residuos (RF-12).
- Backups diarios automatizados (RNF-04).
- Agente IA que atiende solicitudes de turno por WhatsApp (actor externo).

Ninguna de estas es una "tarea corta de request" que `BackgroundTasks` de FastAPI maneja bien. El Stack Completo da: trabajadores separados del proceso web, reintentos, reintentos con backoff, y un scheduler real (Beat) para lo periódico.

### Alternativas descartadas

| Alternativa | Razón de descarte |
|---|---|
| **FastAPI BackgroundTasks + APScheduler** | Suficiente para un TP chico, pero el scheduling queda atado al proceso de la app: no reenvía tareas en fallo con robustez, no escala a múltiples réplicas, y el cron "vive" dentro de un proceso web. Para un cliente real con ciclos programados (OTP 7 días, reportes mensuales) se queda corto en confiabilidad. |
| **Dramatiq + Redis** | Más simple que Celery, pero menor ecosistema, menos documentación de tareas periódicas, y una comunidad más chica. No aporta ventaja decisiva frente a Celery para este caso. |
| **FastAPI + RQ (Redis Queue)** | Más liviano que Celery, pero sin scheduler periódico integrado robusto para el volumen de tareas cron que necesita SIGEMI. |
| **Django + Celery** (en lugar de FastAPI) | Django trae ORM, admin y auth embebidos, pero obliga a un patrón monólito ya resuelto. Se eligió FastAPI por ser más liviano, asíncrono nativo y por alinearse a la combinación Python+React que ya estaba decidida. |

---

## 2. Despliegue: local vs. nube

### Estado de la restricción

RNF-05 exige despliegue exclusivamente en servidores físicos locales de UNaM, sin cloud de terceros. **Esta restricción está sujeta a cambio**, pendiente de confirmación con el cliente. Este manifiesto la deja documentada como "sujeta a revisión".

### Análisis de los dos escenarios (para decidir)

**Escenario A — Despliegue local (servidores UNaM):**

- El hardware y el mantenimiento 24/7 lo aporta la universidad, **no** el desarrollador. No implica "dejar tu PC prendida".
- Ventaja legal: los datos **nunca salen de Argentina**, lo que elimina de raíz el problema de transferencia internacional (ver §5).
- Costo: requiere coordinación con el área de TI de la facultad y da menos control inmediato sobre el entorno de producción.

**Escenario B — Despliegue en nube:**

- **No implica pagar mensualidad sí o sí**: existen free tiers permanentes (Vercel, Render, Railway, Fly.io, Supabase, Neon) aptos para el TP con tráfico bajo.
- Pay-as-you-go es la forma más honesta de pago, pero **no tiene techo duro** de gasto; los free tiers son más seguros para un TP.
- Desventaja legal: si el proveedor está fuera de Argentina (casi todos), se dispara la **transferencia internacional de datos** de la Ley 25.326, relevante solo si se cargan datos de pacientes **reales**.

### Decisión para esta etapa

- **Desarrollo**: local, con **Docker Compose** (ver §4).
- **Producción conceptual / TP**: free tier en nube como camino más práctico, o Docker en un servidor UNaM si se mantiene RNF-05.
- **Posición firme**: la decisión de producción queda **pendiente de la confirmación del cliente** sobre RNF-05; el código debe estar preparado para cualquiera de los dos (configuración por variables de entorno, sin acoplamiento a un proveedor).

### Alternativas descartadas

| Alternativa | Razón de descarte |
|---|---|
| **Servidor VPS dedicado con mensualidad fija** | Sobredimensionado para esta etapa; solo se justifica si el cliente pone el sistema en producción real con usuarios. |
| **Asumir nube o local sin confirmar con el cliente** | Sacar una decisión de infraestructura crítica sin validar al responsable es un riesgo operativo y legal. |
| **Despliegue en un servicio PaaS acoplado al framework** (heroku-style lock-in) | Genera dependencia de un proveedor; se prefiere una imagen Docker portable que corre igual en UNaM o en cualquier nube. |

---

## 3. Canal de notificación y Agente IA (WhatsApp)

### Alcance

El Agente IA está **en el alcance real del sistema** (RF-07 y actor "Paciente" vía WhatsApp). Por lo tanto, la pasarela de WhatsApp debe elegirse ahora, no dejarse en un hueco.

### Decisión firme

Usar la **API oficial de WhatsApp Business (Meta Cloud API)**, con el objetivo de que el número del cliente sea de tipo **WhatsApp Business** y esté correctamente registrado.

### Alternativas evaluadas y descartadas

| Alternativa | Razón de descarte |
|---|---|
| **Self-hosted no oficial (Baileys / Evolution API / WPPConnect)** | Simulan un cliente web de WhatsApp. **Viola los Términos de Servicio de WhatsApp** y conlleva riesgo de **baneo del número**. Inaceptable para un cliente real. Solo admisible para prototipar con un número de descarte, sabiendo que no es producción. |
| **BSP / proveedores intermediarios (Twilio, 360dialog, Gupshup)** | Legítimos (son intermediarios autorizados por Meta), pero son **cloud de terceros**, lo que reabre la transferencia internacional y choca con RNF-05. Se descartan como canal primario; podrían reevaluarse como "proveedor de mensajería" si la API directa resultara operativamente inviable. |
| **Email/SMS en lugar de WhatsApp** | No cumplen el requisito explícito del documento (RF-07 nombra WhatsApp). |

### Regla de minimización de datos por el canal (obligatoria)

Por WhatsApp **solo** viaja:

- Anuncio "tu resultado está listo",
- enlace al portal seguro,
- token OTP de un solo uso.

**Nunca** viaja contenido clínico (el resultado en sí). El dato de salud se entrega cifrado (TLS) en el portal, con doble validación de identidad (OTP). Esta regla se registra en el manifiesto como **minimización** exigida por la Ley 25.326.

---

## 4. Entorno de desarrollo y reproducibilidad

### Decisiones firmes

- **Docker + Docker Compose** para levantar el entorno completo de forma reproducible: `web` (FastAPI), `worker` (Celery), `beat` (Celery Beat), `db` (PostgreSQL), `redis` (Redis), y el frontend React en su propio contenedor o en modo dev con Vite.
- **Variables de entorno** para toda la configuración (credenciales, URLs, secretos), nunca valores hardcodeados.
- **Migraciones de base de datos** versionadas (Alembic junto a SQLAlchemy, o el mecanismo que finalmente se adopte) para evolución controlada del esquema.
- Separación estricta de **dev / staging / producción** por configuración, no por código.

### Estructura de directorios propuesta (referencial, no definitiva)

```
sigemi/
├── backend/          # FastAPI + Celery + Alembic
├── frontend/         # React + TypeScript
├── docker-compose.yml
├── .env.example
└── docs/             # documentación técnica y manifiesto
```

### Alternativas descartadas

| Alternativa | Razón de descarte |
|---|---|
| **Instalación nativa sin contenedores** | Deriva en el clásico "en mi máquina funciona". Un cliente real y una mesa de evaluación necesitan un entorno reproducible. |
| **Solo Docker, sin Compose** | Compose es el mínimo viable para orquestar los 5+ servicios que el Stack Completo exige. |

---

## 5. Marco legal aplicable

### Normativa principal

- **Ley 25.326 — Protección de Datos Personales** (con su reglamentación): los datos clínicos son **datos sensibles** (art. 2). Máximo nivel de protección.
- **Ley 26.529 — Derechos del Paciente** (y **Ley 27.350** si se atienden menores): consentimiento, historia clínica única, retención y confidencialidad.
- Relevar la correspondencia con la **AAIP** (autoridad de aplicación) para transferencia internacional y registro del responsable.

### Obligaciones que se traducen en requisitos de arquitectura

1. **Consentimiento informado** del paciente para el tratamiento de sus datos y para el contacto por WhatsApp.
2. **Minimización de datos**: recolectar y transmitir solo lo necesario; nunca contenido clínico por WhatsApp.
3. **Seguridad razonable**: cifrado en tránsito (TLS/HTTPS en todas partes) y en reposo; control de acceso por roles (ya modelado: `Rol`, `Usuario`).
4. **Trazabilidad e inmutabilidad**: retención de historias clínicas y análisis validados por un mínimo de **10 años** (RNF-04). El modelo ya lo refleja en `VersionFichaClinica`, `Auditoria` y `CambioAuditoria`: nada se sobrescribe sin dejar rastro.
5. **Responsabilidad del resultado**: separación entre quién *realiza* y quién *valida* el análisis (`profesional_responsable_id` vs `profesional_validador_id`). La validación por bioquímico habilitado con OTP (RF-08) es la "firma" del informe.
6. **Transferencia internacional (art. 12)**: solo relevante si el despliegue sale de Argentina o la mensajería usa proveedores extranjeros. Debe declararse y encuadrarse en el escenario de producción real.

### Posición del desarrollador

El desarrollador actúa como **encargado de tratamiento**; el cliente (la cátedra/laboratorio) es el **responsable del tratamiento**. El manifiesto sirve como evidencia de que el diseño *habilita* el cumplimiento normativo (minimización, cifrado, auditoría, versionado), pero la decisión jurídica final sobre titularidad, consentimiento y transferencia internacional corresponde al responsable y, eventualmente, a un profesional del derecho.

---

## 6. Decisiones pendientes (backlog de decisión)

1. Confirmar si RNF-05 (despliegue local) se mantiene o se relaja → define el escenario de producción y el análisis de transferencia internacional.
2. Registro y verificación del número de WhatsApp Business del cliente → habilita la API oficial de Meta.
3. Estrategia de respaldo (backup) concreta sobre PostgreSQL alineada a RNF-04 (diario, retención 10 años).
4. Definir el alcance exacto del "Agente IA" de WhatsApp (qué flujos atiende: solo turnos, o también consulta de resultados).

---

## 7. Registro de cambios

- **v0.1 (02/11/2026)** — Creación inicial. Decisiones base del stack (FastAPI + React + PostgreSQL + Celery/Redis/Beat), despliegue, canal de WhatsApp (API oficial), entorno Docker, y marco legal (Ley 25.326). Con alternativas descartadas.
- **v0.2 (02/11/2026)** — Se fijan decisiones de implementación: SQLAlchemy + Alembic + JWT, monorepo único (`frontend/`+`backend/`), claves primarias UUID, versionado de ficha clínica en `jsonb`, y `version_actual` persistido. Se inicia el modelado completo del dominio y esquema de BD por subsistemas en `Diagramas/modelo_dominio_nucleo_clinico.md` y `Diagramas/modelo_esquema_bd_nucleo_clinico.md`.