# Mapeo Flujo → Paso → Caso de Uso — SIGEMI

Contrato de trazabilidad previo al diagrama de actividades (`diagrama_flujos_sigemi.drawio`).
Cada paso referencia al UC que interviene (código de 2.7.3), su actor y las entidades que toca
(`modelo_dominio_detallado.md` §3).

Convención: `[U]:Sistema`, `[PW]:Paciente (WhatsApp)`, `[OTP]:Paciente (portal)`, `[BQ]:Bioquímico/Doctor`, `[PR]:Profesor`, `[AD]:Administrador`.

---

## Flujo A — Atención del Paciente (Subsistema Gestión de Pacientes)

| Paso | Actividad | UC que interviene | Actor | Entidades |
|---|---|---|---|---|
| A1 | Solicita turno por WhatsApp | — (inicio) | PW | Paciente |
| A2 | Agente IA procesa y crea *Alta Temprana* | UC-REC-01 `«include»` UC-REC-16 | U | Paciente, Turno, TipoAnalisis |
| A3 | Asigna bloque + confirma + envía indicaciones + programa recordatorio | UC-REC-01 (postcondición: REC-10..13) | U | Turno, IndicacionMedica, ConfiguracionAgenda |
| A4 | ¿Anula / reprograma? (decisión) | — | U | |
| A5 | Cancelar / reprogramar por WhatsApp | UC-REC-02 / UC-REC-03 | PW | Turno, Paciente |
| A6 | Cancelar / reprogramar manual en web | UC-REC-21 / UC-REC-22 | BQ/AD | Turno, Paciente |
| A7 | Liberar bloque y ofrecer al turno más postergado | UC-REC-04 (`«include»`) | U | Turno |
| A8 | Registrar asistencia | UC-REC-15 | BQ/AD | Turno, Paciente |
| A9 | ¿Asiste? (decisión) | — | BQ | |
| A10 | Presente → «Atendido» → habilita consulta | UC-REC-15 (postcondición) | BQ | Turno |
| A11 | Ausente → «No Asistió» → libera → UCREC-04 | UC-REC-15 / UC-REC-04 | U | Turno |
| A12 | Cancelación por vencimiento (proceso diario) | UC-REC-14 `«include»` UC-REC-04 | U | Turno |
| A13 | Durante vigencia: consultar turno / reenvío de indicaciones | UC-REC-05 | PW | Turno, IndicacionMedica |
| A14 | Gestión administrativa del paciente (ABM, baja, búsqueda) | UC-REC-16/17/18/19/20, `«include»` UC-REC-S-01 | BQ/AD | Paciente, Usuario |
| A15 | Agenda interna (consulta, configuración, bloqueos) | UC-REC-06/07/08 | AD | ConfiguracionAgenda, BloqueoAgenda, Recurso |

## Flujo B — Diagnóstico y Emisión de Resultados (Subsistema Laboratorio Bioquímico)

| Paso | Actividad | UC que interviene | Actor | Entidades |
|---|---|---|---|---|
| B0 | Entrada: consulta presencial (desde Flujo A) | — | BQ | |
| B1 | Registrar ficha clínica (corrección vía versión) | UC-DIAG-01 `«extend»` UC-DIAG-07 | BQ | FichaClinica, Paciente, Usuario, VersionFichaClinica |
| B2 | Registrar ingreso de muestra → estado «Pendiente» | UC-DIAG-02 | BQ | AnalisisMicologico, FichaClinica, TipoAnalisis |
| B3 | Actualizar estado (En Proceso → Terminado) | UC-DIAG-03 | BQ | AnalisisMicologico |
| B4 | ¿Cancelar análisis? (decisión) | — | BQ | |
| B5 | Validar análisis (cierre clínico) | UC-DIAG-04 | BQ | AnalisisMicologico, Otp, InformeResultados, Usuario |
| B6 | Generar Informe PDF + OTP + notificar WhatsApp | UC-DIAG-04 (postcondición) | U | InformeResultados, Otp |
| B7 | Descargar informe en portal seguro | UC-DIAG-05 | OTP | Otp, InformeResultados, Paciente |
| B8 | Apoyos: panel por estado; historial; catálogo de tipos | UC-DIAG-09 / UC-DIAG-06 / UC-DIAG-10 | BQ/AD | AnalisisMicologico, TipoAnalisis |
| B9 | Cancelación con motivo (solo Pendiente/En Proceso) | UC-DIAG-08 | BQ/AD | AnalisisMicologico |

## Flujo C — Gestión de Insumos / Stock (Subsistema Recursos de Laboratorio)

| Paso | Actividad | UC que interviene | Actor | Entidades |
|---|---|---|---|---|
| C1 | Alta y catálogo de insumos (datos y categorías) | UC-LAB-06 / UC-LAB-12 | AD | Insumo, CategoriaInsumo, UbicacionAlmacenamiento |
| C2 | Configurar umbrales de alerta | UC-LAB-08 | AD | Insumo |
| C3 | Registrar ingreso de insumos (lote, ubicación, FEFO) | UC-LAB-01 | AD | Insumo, Lote, MovimientoInventario, UbicacionAlmacenamiento |
| C4 | Registrar movimiento en trazabilidad | (postcondición LAB-01) | U | MovimientoInventario, Usuario |
| C5 | ¿Retiro para análisis o práctica? (decisión) | — | U | |
| C6 | Retiro asociado a análisis clínico (desde Flujo B) | UC-LAB-02 | BQ | MovimientoInventario, Lote, AnalisisMicologico |
| C7 | Retiro para práctica educativa | UC-LAB-02 | PR | MovimientoInventario, Lote |
| C8 | Deducción stock FEFO + alerta umbral/vencimiento | UC-LAB-02 / UC-LAB-08 | U | Lote, Insumo |
| C9 | ¿Devolución de no utilizados? (decisión) | — | U | |
| C10 | Registrar devolución (revierte retiro) | UC-LAB-09 | PR/BQ/AD | MovimientoInventario, Lote, Insumo |
| C11 | Incremento de stock + movimiento Devolución | (postcondición LAB-09) | U | Lote, MovimientoInventario |
| C12 | Lectura permanente: inventario y trazabilidad | UC-LAB-05 / UC-LAB-07 | BQ/PR/AD | Insumo, Lote, MovimientoInventario |
| C13 | Generar reporte de inventario | UC-LAB-13 | AD/BQ | Reporte, Insumo, MovimientoInventario |

## Flujo D — Residuos Químicos (Subsistema Recursos de Laboratorio)

| Paso | Actividad | UC que interviene | Actor | Entidades |
|---|---|---|---|---|
| D1 | Origen: práctica educativa o análisis clínico (B/C) | — | PR/BQ | ResiduoQuimico |
| D2 | Registrar generación (volumen, peso, categoría) | UC-LAB-03 | PR/BQ | ResiduoQuimico, CategoriaResiduo, AnalisisMicologico |
| D3 | Sistema registra + audita, vincula fecha/usuario | (postcondición LAB-03) | U | ResiduoQuimico, Usuario, Auditoria |
| D4 | Catálogo de categorías de peligrosidad | UC-LAB-10 | AD | CategoriaResiduo |
| D5 | Consultar y modificar registro (corrección previa a consolidar) | UC-LAB-11 | PR/BQ/AD | ResiduoQuimico |
| D6 | Disposición final (RF-19) | — (RF-19) | AD | DisposicionFinal, ResiduoQuimico |
| D7 | Consolidación mensual | (postcondición LAB-04) | U | ResiduoQuimico, Reporte |
| D8 | Generar reporte mensual normativo | UC-LAB-04 | AD | Reporte, ResiduoQuimico |

## Flujo E — Acceso, Seguridad y Reportes (transversal)

| Paso | Actividad | UC que interviene | Actor | Entidades |
|---|---|---|---|---|
| E1 | Iniciar sesión (credenciales) | UC-SEG-01 | BQ/PR/AD | Usuario |
| E2 | Verificar cuenta/estado, hash, emitir JWT | UC-SEG-01 (postcondición) | U | Usuario, Auditoria |
| E3 | Administrar usuarios y roles (con cuenta activa) | UC-SEG-02 | AD | Usuario, Rol |
| E4 | Auditoría automática transversal (RF-14) | — (RF-14) | U | Auditoria, CambioAuditoria |
| E5 | Cerrar sesión | UC-SEG-03 | BQ/PR/AD | Usuario |
| E6 | Invalidar sesión (JWT) | UC-SEG-03 (postcondición) | U | Usuario |
| E7 | Consolidar y exportar datos operativos | UC-REP-01 | BQ/AD | Reporte, Usuario |
| E8 | Cruce de datos + anonimización + exportación | UC-REP-01 (postcondición) | U | Reporte |

## Entidades por flujo (resumen)

| Flujo | Entidades principales |
|---|---|
| A | Paciente, Turno, TipoAnalisis, IndicacionMedica, ConfiguracionAgenda, BloqueoAgenda, Recurso |
| B | FichaClinica, VersionFichaClinica, AnalisisMicologico, TipoAnalisis, Otp, InformeResultados |
| C | Insumo, Lote, MovimientoInventario, CategoriaInsumo, UbicacionAlmacenamiento |
| D | ResiduoQuimico, CategoriaResiduo, DisposicionFinal, Reporte |
| E | Usuario, Rol, Auditoria, CambioAuditoria, Reporte |