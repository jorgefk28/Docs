# Modelo de Roles y Permisos — SIGEMI

> **Estado**: propuesta de modelado (v0.1) — pendiente de volcar al esquema y validar con el cliente.
> **Fuente**: `TF_2026_Requerimientos_KLUKA_JORGE.md` (secciones 2.7.2 Actores y 2.7.3 Casos de Uso).
> **Motivo**: resolver el hueco de modelado #1 detectado en la auditoría — el dominio fagocitaba al actor "Profesor" dentro de "Profesional", y el esquema tenía `rol` como catálogo libre, contradiciendo el requisito de "roles prefijados" (UC-SEG-02).

---

## 1. Actores del sistema (definitivo)

| Actor | Naturaleza | Acceso |
|---|---|---|
| **Bioquímico/Doctor** (ACT-01) | Rol de sistema | Plataforma web interna |
| **Profesor** (ACT-02) | Rol de sistema | Plataforma web interna |
| **Administrador** (ACT-03) | Rol de sistema | Plataforma web interna |
| **Paciente** (ACT-04) | Actor externo, **sin cuenta** | Solo portal OTP + WhatsApp (Agente IA) |

El Paciente **no** es un rol de `usuario`: no posee credenciales ni interactúa con la interfaz interna (ACT-04). Vive fuera del modelo de `usuario`/`rol`.

---

## 2. Decisión de modelado (tomada)

**El Administrador no opera clínico por defecto.** Para cumplir funciones de Bioquímico, un Administrador debe tener asignado **además** el rol `bioquimico`. Esto se resuelve con una relación N:N `usuario_rol`, no con un rol híbrido "admin-bioquimico".

Justificación: ACT-03 dice "además cumple la misma función que un Bioquímico" (capacidad, no identidad fija), mientras los casos de uso solo habilitan al Administrador para cancelar análisis (DIAG-08) y reportes (LAB-13, REP-01), NO para registrar/validar fichas y análisis (DIAG-01..04, DIAG-07). La acumulación opcional de roles reconcilia ambas fuentes.

---

## 3. Modelo relacional propuesto

```
rol         : id (uuid PK), codigo (bioquimico | profesor | administrador), nombre, descripcion
usuario     : (sin cambios) rol_id se ELIMINA → reemplazado por usuario_rol
usuario_rol : usuario_id (FK → usuario), rol_id (FK → rol)   — UNIQUE(usuario_id, rol_id)
profesional : id (uuid PK), usuario_id (FK unique → usuario), matricula, especialidad, estado
              → aplica SOLO al rol bioquimico, no al Profesor
```

### Cambios respecto al esquema actual

1. `usuario.rol_id` (1:N) se reemplaza por la tabla intermedia `usuario_rol` (N:N). Razón: ACT-03 exige acumulación de responsabilidades en un mismo usuario.
2. `rol` deja de ser catálogo libre (`nombre` + `descripcion`) y pasa a ser un catálogo **cerrado** por `codigo` enumerado: `bioquimico`, `profesor`, `administrador`. Razón: UC-SEG-02 "roles prefijados en el sistema".
3. `profesional` queda **desacoplada del Profesor**: la matrícula y especialidad son atributos del Bioquímico/Doctor (concepto clínico), no del Profesor (concepto académico). El Profesor es `usuario` con rol `profesor`, sin fila en `profesional`.

---

## 4. Matriz de permisos por actor

Leyenda: **✍** = escribe/modifica · **👁** = solo lectura · **—** = sin acceso.

| Caso de uso | Bioquímico | Profesor | Administrador | Paciente |
|---|---|---|---|---|
| **Gestión de Pacientes (REC)** | | | | |
| REC-01 Agendar Turno | — | — | — | ✍ (vía IA) |
| REC-02 Cancelar Turno | — | — | — | ✍ (vía IA) |
| REC-03 Reprogramar Turno | — | — | — | ✍ (vía IA) |
| REC-04 Reasignación Automática | — | — | — | — (sistema) |
| REC-05 Consultar Turno | — | — | — | 👁 (vía IA) |
| REC-06 Consultar Agenda | 👁 | — | 👁 | — |
| REC-07 Configurar Parámetros Agenda | — | — | ✍ | — |
| REC-08 Bloquear/Desbloquear Días | — | — | ✍ | — |
| REC-10 Crear Indicación Médica | ✍ | — | ✍ | — |
| REC-11 Modificar Indicación Médica | ✍ | — | ✍ | — |
| REC-12 Eliminar Indicación Médica | ✍ | — | ✍ | — |
| REC-13 Consultar Indicaciones | ✍ | — | ✍ | — |
| REC-14 Cancelar Turno por Vencim. | — | — | — | — (sistema) |
| REC-15 Registrar Asistencia | ✍ | — | ✍ | — |
| REC-16 Registrar Paciente | ✍ | — | ✍ | — |
| REC-17 Modificar Paciente | ✍ | — | ✍ | — |
| REC-18 Consultar Paciente | 👁 | — | 👁 | — |
| REC-19 Desactivar Paciente | — | — | ✍ | — |
| REC-20 Agendar Turno Manual | ✍ | — | ✍ | — |
| REC-21 Cancelar Turno Manual | ✍ | — | ✍ | — |
| REC-22 Reprogramar Turno Manual | ✍ | — | ✍ | — |
| **Laboratorio Bioquímico (DIAG)** | | | | |
| DIAG-01 Registrar Ficha | ✍ | — | — | — |
| DIAG-02 Ingreso de Muestra | ✍ | — | — | — |
| DIAG-03 Actualizar Estado | ✍ | — | — | — |
| DIAG-04 Validar Análisis | ✍ | — | — | — |
| DIAG-05 Descargar Informe | — | — | — | ✍ (OTP) |
| DIAG-06 Consultar Historial | 👁 | — | 👁 | — |
| DIAG-07 Modificar Ficha | ✍ | — | — | — |
| DIAG-08 Cancelar Análisis | ✍ | — | ✍ | — |
| DIAG-09 Panel de Análisis | ✍ | — | — | — |
| DIAG-10 Gestionar Tipos Análisis/Muestra | — | — | ✍ | — |
| **Recursos de Laboratorio (LAB)** | | | | |
| LAB-01 Registrar Ingreso | — | — | ✍ | — |
| LAB-02 Registrar Retiro | ✍ | ✍ | ✍ | — |
| LAB-03 Registrar Residuos | ✍ | ✍ | ✍ | — |
| LAB-04 Reporte Residuos | — | — | ✍ | — |
| LAB-05 Consultar Inventario | 👁 | 👁 | 👁 | — |
| LAB-06 Gestionar Catálogo Insumos | — | — | ✍ | — |
| LAB-07 Consultar Trazabilidad | 👁 | 👁 | 👁 | — |
| LAB-08 Configurar Umbrales | — | — | ✍ | — |
| LAB-09 Registrar Devolución | ✍ | ✍ | ✍ | — |
| LAB-10 Gestionar Categorías Residuos | — | — | ✍ | — |
| LAB-11 Consultar/Modificar Residuos | ✍* | ✍* | ✍* | — |
| LAB-12 Gestionar Categorías Insumos | — | — | ✍ | — |
| LAB-13 Reporte Inventario | ✍ | — | ✍ | — |
| **Acceso y Seguridad (SEG)** | | | | |
| SEG-01 Iniciar Sesión | ✍ | ✍ | ✍ | — |
| SEG-02 Administrar Usuarios y Roles | — | — | ✍ | — |
| **Reportes (REP)** | | | | |
| REP-01 Consolidar/Exportar Datos | ✍* | — | ✍* | — |

`*` = con restricción de atribución registrada en el UC:
- LAB-11: modificar "solo el autor o Administrador".
- REP-01: requiere "privilegios necesarios (Bioquímico/Doctor o Administrador)".

> Nota: el Administrador con rol `bioquimico` acumulado (vía `usuario_rol`) obtiene las capacidades de la columna "Bioquímico" además de las propias.

---

## 5. Frontera semántica clave (evita sobre-exposición de datos)

| Frontera | Regla |
|---|---|
| **Bioquímico vs Profesor** | El Bioquímico mueve inventario por *análisis clínico*; el Profesor por *práctica educativa* (`movimiento_inventario.practica_educativa`). El Profesor **nunca** accede a DIAG ni a fichas clínicas. |
| **Paciente** | Solo portal OTP + WhatsApp. Nunca `usuario`/`rol`. |

Fusión Bioquímico+Profesor → el Profesor heredaría acceso a historias clínicas (dato sensible, Ley 25.326). Es un defecto de seguridad y de alcance, no un matiz de nomenclatura.

---

## 6. Pendientes para cerrar con el cliente

1. Confirmar que el Profesor **no** lleva matrícula profesional (hoy asumido: `profesional` solo para Bioquímico).
2. Confirmar la regla de acumulación Admin+Bioquímico (decisión tomada acá, sujeta a validación).
3. Definir si `practica_educativa` necesita promover a entidad propia (una "práctica" con alumnos/fecha) o sigue como `boolean` sobre el movimiento.
```