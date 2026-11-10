# SIGEMI — Resumen Ejecutivo de Avance

**Sistema Integral de Gestión Micológica**
Módulo de Bioquímica y Farmacia — UNaM

**Fecha de corte:** 19/10/2026
**Autor:** Kluka Jorge Favio
**Fase del proyecto:** Especificación, modelado y diseño

---

## 1. Mensaje ejecutivo

El proyecto completó la **base de requisitos** y el **modelado del dominio y de datos**. El núcleo clínico —Gestión de Pacientes y Laboratorio Bioquímico— tiene sus **casos de uso extendidos al 100%**.

El avance global de especificación detallada es del **69% (34 de 49 UCE)**. El **31% restante se concentra casi por completo en Recursos de Laboratorio (13 UCE)**, con una brecha menor en Acceso y Seguridad (2 UCE).

| Indicador | Valor |
|---|---|
| Subsistemas / Módulos | 5 / 11 |
| Actores identificados | 4 |
| Casos de uso definidos | 49 / 49 (100%) |
| Casos de uso extendidos (UCE) | 34 / 49 (69%) |
| Entidades de dominio | 39 |
| Tablas del modelo de datos | 40 |
| Pantallas identificadas | 34 |
| Pantallas con especificación detallada | 11 / 34 (32%) |

**Conclusión:** la documentación está en condiciones de cerrar la especificación. El esfuerzo pendiente es acotado, identificable y no bloquea el diseño ya validado.

---

## 2. Alcance del sistema

SIGEMI digitaliza la operación del laboratorio de Micología:

| Subsistema | Función principal |
|---|---|
| Gestión de Pacientes (REC) | Turnos por WhatsApp y manuales, agenda, asistencia, pacientes e indicaciones médicas |
| Laboratorio Bioquímico (DIAG) | Ficha clínica, muestras, ciclo de vida del análisis, validación y entrega de resultados |
| Recursos de Laboratorio (LAB) | Inventario, insumos, reactivos, residuos químicos y equipos |
| Acceso y Seguridad (SEG) | Autenticación, usuarios, roles y auditoría |
| Reportes y Estadísticas (REP) | Consolidación y exportación de datos operativos |

**Alcance del informe:** análisis, modelado y diseño. No reporta métricas de código en producción.

---

## 3. Estado global por frente

| Frente | Entregable | Estado | Cobertura |
|---|---|---|---|
| Requisitos | 5 OBJ, 7 IRQ, 21 RF, 5 RNF | Completo | 100% |
| Actores | 4 actores definidos | Completo | 100% |
| Casos de uso | 49 UC definidos | Completo | 100% |
| Casos de uso extendidos | 34 UCE redactados | En curso | 69% |
| Diagramas de casos de uso | Diagrama general y por subsistema | Completo | 100% |
| Modelo conceptual | 39 entidades y relaciones | Completo | 100% |
| Modelo de datos | 40 tablas, atributos y cardinalidades | Completo | 100% |
| Diseño UX/UI | 34 pantallas identificadas; 11 especificadas | En curso | 32% |
| Glosario | 9 términos de dominio | Completo | 100% |

---

## 4. Requisitos: línea base cerrada

- **5 objetivos** del sistema.
- **7 requisitos de información**.
- **21 requisitos funcionales**.
- **5 requisitos no funcionales**.
- **4 actores:** Bioquímico/Doctor, Profesor, Administrador y Paciente.
- **9 términos** en el glosario de dominio.
- Documento versionado, con **9 entradas de cambio (Nro 0 a 8)** entre abril y octubre de 2026.

**Mensaje clave:** la línea base permite derivar y trazar todos los casos de uso y las decisiones de diseño.

---

## 5. Casos de uso: núcleo clínico completo

| Subsistema | UC definidos | UCE redactados | Cobertura UCE |
|---|---:|---:|---:|
| Gestión de Pacientes (REC) | 22 | 22 | 100% |
| Laboratorio Bioquímico (DIAG) | 10 | 10 | 100% |
| Recursos de Laboratorio (LAB) | 13 | 0 | 0% |
| Acceso y Seguridad (SEG) | 3 | 1 | 33% |
| Reportes y Estadísticas (REP) | 1 | 1 | 100% |
| **Total** | **49** | **34** | **69%** |

**Lectura:** 3 de los 5 subsistemas están especificados por completo; REC y DIAG concentran el 65% de los casos de uso del sistema.

---

## 6. Hitos del período

| Fecha | Hito |
|---|---|
| 17/04/2026 | Creación del documento y definición del contexto y objetivos |
| 21/04/2026 | Estructuración en subsistemas y módulos |
| 24/04/2026 | Redacción completa de RF y RNF |
| 10/05/2026 | Diagramas de casos de uso y definición de actores |
| 19/05/2026 | UCE de Gestión de Pacientes |
| 25/05/2026 | UCE de Laboratorio Bioquímico (primera etapa) |
| 30/05/2026 | UCE de Acceso, Seguridad y Reportes |
| 01/06/2026 | Revisión de Recursos de Laboratorio |
| 14–15/09/2026 | Actualización del modelo conceptual y del modelo de datos |
| 16/09/2026 | Verificación de pantallas y flujos del BRIEF UX/UI |
| 04/10/2026 | Completitud de UCE DIAG-03 a DIAG-10 y guía de pantallas v2.0 |

---

## 7. Modelo de dominio y datos consolidado

- **39 entidades de dominio** y **40 tablas físicas** (incluye la tabla asociativa N-N `EspacioGrupo`).
- **Versionado de ficha clínica** con historial inmutable de cambios.
- **Detalle estructurado** de datos clínicos, hallazgos, auditoría e instrucciones de almacenamiento.
- **Agenda por profesional y espacio de atención**, con capacidad paralela y reprogramación automática por ausencia.
- **Bloqueo híbrido de agenda:** cierre global (`PeriodoInhabilitado`) y bloqueo puntual (`BloqueoAgenda`) con precedencia definida.
- **Equipos desacoplados** de la lógica de agenda: activo fijo, garantía y mantenimiento propio.
- **Trazabilidad clínica y de laboratorio:** cada transición de estado registra actor y timestamp.
- **Inventario con lotes y FEFO**, residuos con volumen/peso y disposición final.
- **Seguridad de resultados:** OTP de un solo uso e informe PDF generado al validar.

**Mensaje clave:** el modelo cubre el ciclo completo, desde el turno hasta la disposición final de residuos y la entrega del informe.

---

## 8. Diseño UX/UI: base construida, especificación en curso

- **34 pantallas** identificadas y mapeadas a casos de uso.
- **11 pantallas del módulo Principal** con especificación completa:
  - Panel de Control.
  - Agenda y Turnos (grilla, nuevo turno, detalle, configuración, bloqueos).
  - Pacientes (listado, perfil, registro/edición, desactivación, búsqueda).
- **5 flujos críticos** documentados: ficha/muestra, ejecución de análisis, validación, control de inventario y auditoría.
- **Guía de pantallas v2.0** con layout, datos, acciones, estados, flujos, excepciones, permisos y matriz de roles.
- **10 observaciones adversariales resueltas** (A-01 a A-10) en la versión 2.0.

**Pendiente:** especificación detallada de las **23 pantallas restantes** (LAB, SEG, reportes y catálogos).

---

## 9. Calidad y consistencia

**Avances recientes**

- Completitud de los **8 UCE de DIAG faltantes** (DIAG-03 a DIAG-10).
- Reenvío automático de OTP especificado como **postcondición** de UC-DIAG-04, con respaldo manual.
- **6 correcciones de consistencia** aplicadas en referencias cruzadas y redacción (C1 a C6).
- Revisión adversarial del diseño de pantallas con **10 observaciones resueltas**.

**Brechas detectadas**

- **8 observaciones de pantallas** (G1 a G8) aún abiertas, 2 de severidad alta:
  - Cancelación de análisis habilitada fuera de los estados permitidos.
  - Acción "Regenerar OTP" sin caso de uso que la respalde.
- Casos de uso sin cobertura explícita: informes emitidos, disposición final de residuos y equipos.
- Contenido del dashboard y recuperación de contraseña sin definición final.

---

## 10. Riesgos y brechas principales

| Riesgo | Impacto | Mitigación |
|---|---|---|
| LAB sin UCE (0/13) | Bloquea la especificación de inventario y residuos | Priorizar los 13 UCE en el próximo ciclo |
| SEG incompleto (1/3) | Afecta usuarios, roles y permisos | Redactar SEG-02 y SEG-03 |
| Pantallas vs. UCE inconsistentes (G1–G8) | Retrabajo en UI e implementación | Resolver junto con los UCE faltantes |
| UC ausentes (OTP, informes, residuos, equipos) | Funciones sin respaldo documental | Crear o declarar explícitamente como extensión |
| 23 pantallas sin flujo detallado | Diseño inconsistente entre módulos | Completar guía por módulo |
| Registro de cambios desactualizado | Trazabilidad documental | Corregir entradas de LAB y SEG |

**Riesgo principal:** que la implementación de LAB y SEG avance sin la especificación detallada y genere retrabajo.

---

## 11. Próximos pasos

1. **Redactar los 13 UCE de Recursos de Laboratorio (LAB-01 a LAB-13).**
2. **Completar Acceso y Seguridad:** UCE-SEG-02 (Usuarios y Roles) y UCE-SEG-03 (Cierre de Sesión).
3. **Resolver las observaciones G1–G8** y definir los casos de uso faltantes (OTP, informes emitidos, disposición final, equipos).
4. **Especificar las 23 pantallas restantes** y cerrar la matriz rol–pantalla–acción.
5. **Ejecutar la revisión final de trazabilidad** UC–UCE–RF–pantalla y actualizar el registro de cambios.

**Resultado esperado:** especificación funcional y de diseño al 100%, lista para iniciar la implementación.

---

## 12. Conclusión

- La **base de requisitos está terminada** y el **modelo de dominio y datos está consolidado**.
- El **núcleo clínico está especificado al 100%**: pacientes, turnos, ficha, análisis, validación y entrega de resultados.
- El **69% de los UCE** está redactado; el esfuerzo pendiente es **acotado y concentrado en LAB**.
- El proyecto está **listo para cerrar la especificación** y avanzar a la etapa de implementación.

**Mensaje final:** el avance ya no depende de definir el sistema, sino de completar la documentación de dos subsistemas y alinear las pantallas con sus casos de uso.

---

## Anexo — Artefactos de referencia

| Artefacto | Ubicación |
|---|---|
| Documento de requisitos | `TF_2026_Requerimientos_KLUKA_JORGE.md` |
| Diagrama de casos de uso | `Diagramas/diagrama_casos_uso_sigemi.drawio` |
| Diagrama de flujos | `diagrama_flujos_sigemi.drawio` |
| Modelo conceptual | `Diagramas/modelo_conceptual_sigemi.md` |
| Modelo de datos | `Diagramas/modelo_datos_sigemi.md` |
| Guía de diseño de pantallas | `OPENCODE-ARTIFACTS/GUIA_DISENO_PANTALLAS_PRINCIPAL.md` |
| Verificación de pantallas | `OPENCODE-ARTIFACTS/VERIFICACION_PANTALLAS_BRIEF.md` |
| Cambios UCE DIAG | `OPENCODE-ARTIFACTS/cambios_uce_diag_2_8_2.md` |
| Fichas médicas de referencia | `Diagramas/fichas_medicas_de_micosis.md` |
