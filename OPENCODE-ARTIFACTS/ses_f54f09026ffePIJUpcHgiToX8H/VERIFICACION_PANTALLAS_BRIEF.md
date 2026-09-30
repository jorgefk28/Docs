

---

## ANEXO — Correcciones aplicadas al BRIEF (post-verificación)

Se corrigió `BRIEF_DISENO_UX_UI_SIGEMI.md` según los hallazgos:

| Hallazgo | Corrección aplicada |
|---|---|
| F1 (pantalla ausente) | Agregada pantalla **Catálogo de Categorías de Residuos** (UC-LAB-10/RF-17) en §5 y en el árbol de navegación. |
| F2 (flujos por pantalla) | Se añadió el campo **"Flujo:"** paso a paso a las 34 pantallas de §5 (no solo las 5 críticas). |
| F3 (árbol inconsistente) | Movida "Nueva Consulta" a Pacientes; agregados nodos "Detalle/Acciones de Turno", "Catálogos (transversal)" y "Reporte de Inventario" en el árbol. |
| F4 (ambigüedad de roles) | Añadida **§5.1 Matriz de roles × pantallas** (Bioquímico/Profesor/Admin) con supuestos por defecto; resueltos los marcadores `⚠️` de Informes Emitidos, Disposición Final y Registro de Paciente. |
| F5 (completar demográficos) | Añadido paso "Completar datos del paciente" en el flujo de Detalle/Acciones de Turno (UCE-REC-15). |
| F6 (login recuperación) | Decidido: recuperación **solo vía reseteo por Admin** desde Usuarios (despliegue local). |

**Quedan pendientes (dependen del stakeholder, §9):** Dashboard (F7), reenvío/regeneración de OTP (F7), y confirmación de la matriz de roles (supuestos en §5.1).
