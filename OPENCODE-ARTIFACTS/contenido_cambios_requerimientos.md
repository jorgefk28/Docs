# Contenido de los cambios en `TF_2026_Requerimientos_KLUKA_JORGE.md`

**Rango:** desde el commit `"."` (`93867ef`) en adelante hasta el HEAD.
Cada cambio incluye el **texto eliminado** y el **texto agregado/reemplazante** real, según la sección del documento a la que corresponde.

---

## 1) Sección 2.2.2 — Descripción de Subsistemas

### 1.1 Subsistema de Gestión de Pacientes *(modificación)*
**Texto eliminado:**
> El Subsistema de Recepción y Administración de Pacientes es el componente encargado de la logística de ingreso y el contacto inicial con los Pacientes. Su función principal es organizar el flujo de atención administrativa, comenzando por la agenda y asignación de turnos, hasta la gestión del repositorio centralizado a largo plazo, el cual resguarda el historial clínico acumulado de las personas atendidas. Este subsistema abarca los módulos de **Gestión de Turnos y Atención**, y **Gestión de Pacientes**.

**Texto agregado:**
> El Subsistema de Gestión de Pacientes es el componente encargado de la logística de ingreso y el contacto inicial con los Pacientes. Su función principal es organizar el flujo de atención administrativa, comenzando por la agenda y asignación de turnos, hasta la gestión del repositorio centralizado a largo plazo, el cual resguarda el historial clínico acumulado de las personas atendidas. Este subsistema abarca los módulos de **Gestión de Turnos y Atención**, y **Gestión de Pacientes**.

### 1.2 Subsistema de Laboratorio Bioquímico *(modificación)*
**Texto eliminado:**
> El Subsistema de Diagnóstico y Laboratorio Bioquímico es el núcleo clínico y científico destinado al procesamiento de las muestras y la evaluación médica. Su propósito fundamental es sistematizar la recolección de los datos en la ficha clínica al momento de la consulta, trazar el ciclo de vida completo de los estudios microbiológicos (abarcando los estados pendiente, en proceso, terminado y validado) y automatizar la entrega remota y segura de los diagnósticos finales a los pacientes. Este subsistema abarca los módulos de **Registro deInformación Clínica**, **Registro de Análisis**, y **Emisión de Resultados**.

**Texto agregado:**
> El Subsistema de Laboratorio Bioquímico es el núcleo clínico y científico destinado al procesamiento de las muestras y la evaluación médica. Su propósito fundamental es sistematizar la recolección de los datos en la ficha clínica al momento de la consulta, trazar el ciclo de vida completo de los estudios microbiológicos (abarcando los estados pendiente, en proceso, terminado y validado) y automatizar la entrega remota y segura de los diagnósticos finales a los pacientes. Este subsistema abarca los módulos de **Registro de Información Clínica**, **Registro de Análisis**, y **Emisión de Resultados**.

### 1.3 Subsistema de Acceso y Seguridad *(modificación)*
**Texto eliminado:**
> El Subsistema de Acceso y Seguridades es el componente transversal encargado de proteger la confidencialidad de los datos…

**Texto agregado:**
> El Subsistema de Acceso y Seguridad es el componente transversal encargado de proteger la confidencialidad de los datos…

---

## 2) Sección 2.3.2 — Módulos del Proyecto

### 2.1 Registro de Análisis *(agregado al final)*
**Texto agregado:**
> …Incluye la gestión de tipos de análisis, la cancelación de estudios y un panel de trabajo para visualizar el volumen de análisis por estado.

### 2.2 Stock de Insumos Reactivos *(agregado al final)*
**Texto agregado:**
> …incluyendo trazabilidad por lotes, ubicaciones de almacenamiento y devoluciones.

### 2.3 Control de Residuos *(agregado al final)*
**Texto agregado:**
> …incluyendo el registro de disposición final y la gestión de categorías de peligrosidad.

---

## 3) Sección 2.4 — Requisitos de Información (IRQ)

### 3.1 IRQ-01 Ficha Clínica — Datos específicos *(modificación)*
**Texto eliminado:**
> Número de registro<br>Fecha de ingreso<br>Nombre y apellido<br>Fecha de nacimiento<br>Edad (campo calculado)<br>DNI<br>Sexo<br>Domicilio<br>Teléfono de contacto<br>Médico derivante<br>Institución<br>Diagnóstico presuntivo.

**Texto agregado:**
> Número de registro<br>Fecha de ingreso<br>Nombre y apellido<br>Fecha de nacimiento<br>Edad (campo calculado)<br>DNI<br>Sexo<br>Domicilio<br>Teléfono de contacto<br>Correo Electrónico<br>Obra Social.

### 3.2 IRQ-02 Análisis Micológico — Datos específicos *(modificación)*
**Texto eliminado:**
> Tipo de muestra<br>Cultivo<br>Estado actual (Pendiente, En proceso, Terminado, Validado)<br>Observaciones/Resultados parciales<br>Fecha de validación<br>Bioquímico validador.

**Texto agregado:**
> Tipo de muestra<br>Estado actual (Pendiente, En proceso, Terminado, Validado, Cancelado, Derivado)<br>Observaciones/Resultados parciales<br>Fecha de validación<br>Bioquímico validador.

### 3.3 IRQ-03 Insumo/Reactivo — Datos específicos *(modificación)*
**Texto eliminado:**
> Nombre del reactivo/insumo<br>Cantidad actual (stock disponible)<br>Umbral mínimo de alerta<br>Fecha de vencimiento.

**Texto agregado:**
> Nombre del reactivo/insumo<br>Cantidad actual (stock disponible)<br>Umbral mínimo de alerta<br>Número de Lote<br>Unidad de Medida (ml, g, unidades)<br>Categoría<br>Ubicación de Almacenamiento<br>Fecha de Ingreso<br>Fecha de vencimiento.

### 3.4 Nuevo IRQ-05 — Catálogo de Tipos de Análisis/Muestra *(agregado)*
> |**IRQ–05**|**Catálogo de Tipos de Análisis/Muestra**|
> |---|---|
> |**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
> |**Requisitos asociados**| RF-16 Gestión de Catálogos Clínicos |
> |**Descripción**| Catálogo de tipos de análisis micológicos y tipos de muestra disponibles en el sistema. |
> |**Datos específicos**| Nombre<br>Descripción<br>Indicaciones asociadas<br>Estado (Activo/Inactivo). |
> |**Estabilidad**| Media |
> |**Comentarios**| Soporta UC–DIAG-11 (Gestionar Tipos de Análisis y Muestra). |

### 3.5 Nuevo IRQ-06 — Movimiento de Inventario *(agregado)*
> |**IRQ–06**|**Movimiento de Inventario**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
> |**Descripción**| Entidad que registra cada movimiento (ingreso, retiro, devolución) de insumos en el inventario. |
> |**Datos específicos**| Tipo de movimiento (Ingreso/Retiro/Devolución)<br>Fecha<br>Cantidad<br>Lote afectado<br>Usuario responsable<br>Análisis o práctica asociada. |
> |**Estabilidad**| Media |
> |**Comentarios**| Soporta UC–LAB-07 (Consultar Trazabilidad de Movimientos). |

### 3.6 Nuevo IRQ-07 — Categoría de Residuo *(agregado)*
> |**IRQ–07**|**Categoría de Residuo**|
> |---|---|
> |**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
> |**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
> |**Descripción**| Catálogo de categorías y clases de peligrosidad de los residuos químicos. |
> |**Datos específicos**| Nombre<br>Clase de peligrosidad (Clase I, II, III)<br>Descripción<br>Instrucciones de almacenamiento. |
> |**Estabilidad**| Media |
> |**Comentarios**| Soporta UC–LAB-10 (Gestionar Categorías de Residuos). |

---

## 4) Sección 2.5 — Requisitos Funcionales *(agregados RF-16 a RF-21)*

### RF-16 Gestión de Catálogos Clínicos
> |**RF-16**|**Gestión de Catálogos Clínicos**|
> |---|---|
> |**Objetivos Asociados**| OBJ-02 |
> |**Descripción**| El sistema debe permitir al Administrador gestionar los tipos de análisis micológicos y tipos de muestra (crear, modificar, desactivar). |
> |**Comentarios**| - |

### RF-17 Gestión de Catálogos de Inventario
> |**RF-17**|**Gestión de Catálogos de Inventario**|
> |---|---|
> |**Objetivos Asociados**| OBJ-04, OBJ-05 |
> |**Descripción**| El sistema debe permitir al Administrador gestionar las categorías de insumos, ubicaciones de almacenamiento y categorías de residuos. |
> |**Comentarios**| - |

### RF-18 Trazabilidad de Lotes y Vencimientos
> |**RF-18**|**Trazabilidad de Lotes y Vencimientos**|
> |---|---|
> |**Objetivos Asociados**| OBJ-04 |
> |**Descripción**| El sistema debe permitir registrar lotes al ingresar insumos, con número de lote y fecha de vencimiento, y alertar sobre proximidad de vencimiento. El sistema debe consumir primero el lote con vencimiento más próximo al realizar un retiro. |
> |**Comentarios**| Asegura la rotación de inventario y previene el uso de reactivos vencidos. |

### RF-19 Registro de Disposición Final de Residuos
> |**RF-19**|**Registro de Disposición Final de Residuos**|
> |---|---|
> |**Objetivos Asociados**| OBJ-05 |
> |**Descripción**| El sistema debe permitir registrar la salida y disposición final de los residuos acumulados, con fecha, responsable y método de tratamiento. |
> |**Comentarios**| Asegura el cierre del ciclo de vida del residuo para cumplimiento normativo. |

### RF-20 Modificación de Ficha Clínica
> |**RF-20**|**Modificación de Ficha Clínica**|
> |---|---|
> |**Objetivos Asociados**| OBJ-02 |
> |**Descripción**| El sistema debe permitir al Bioquímico/Doctor modificar una ficha clínica registrada, manteniendo un historial de versiones. |
> |**Comentarios**| Garantiza la trazabilidad de cambios en el historial clínico del paciente. |

### RF-21 Cancelación de Análisis
> |**RF-21**|**Cancelación de Análisis**|
> |---|---|
> |**Objetivos Asociados**| OBJ-02 |
> |**Descripción**| El sistema debe permitir cancelar un análisis en curso (con motivo obligatorio) cuando esté en estado «Pendiente» o «En Proceso». |
> |**Comentarios**| Evita que análisis no viables continúen su procesamiento y libera recursos del laboratorio. |

---

## 5) Sección 2.7.2 — Definición de Actores

### ACT-01 Bioquímico / Doctor *(modificación)*
**Texto eliminado (fragmento):**
> …es el responsable de registrar, actualizar y validar todo el ciclo de vida de los análisis micológicos.

**Texto agregado (fragmento):**
> …es el responsable de registrar, actualizar, modificar, cancelar y validar todo el ciclo de vida de los análisis micológicos.

### ACT-02 Profesor *(agregado al final)*
**Texto agregado:**
> También registra la generación de residuos químicos producto de las prácticas educativas y puede consultar el inventario y la trazabilidad de movimientos.

### ACT-03 Administrador *(agregado en el medio)*
**Texto agregado:**
> …la gestión de catálogos del sistema (tipos de análisis, insumos, categorías, ubicaciones)…

---

## 6) Sección 2.7.3.1 — Subsistema Gestión de Turnos y Atención

### 6.1 UC-REC-03 Reprogramar Turno — Requisitos asociados *(modificación)*
**Texto eliminado:**
> RF-04 Cancelación y Reprogramación de Turnos.<br>RF-03 Gestión de Lista de Espera por Turnos Liberados.

**Texto agregado:**
> RF-04 Cancelación y Reprogramación de Turnos.<br>RF-03 Gestión de Reagendación automática.

### 6.2 UC-REC-04 Reasignación Automática de Turno Liberado — Requisitos asociados *(modificación)*
**Texto eliminado:**
> RF-03 Gestión de Lista de Espera por Turnos Liberados.

**Texto agregado:**
> RF-03 Gestión de Reagendación automática.

### 6.3 UC-REC-16 Registrar Paciente — Objetivos asociados *(modificación)*
**Texto eliminado:**
> OBJ-02 Digitalización del Historial Clínico y Registro de Análisis

**Texto agregado:**
> OBJ-01 Automatización de la Gestión de Turnos y Atención

### 6.4 UC-REC-17 Modificar Paciente — Comentarios *(modificación)* *(commit `"."`)*
**Texto eliminado:**
> Incluye `<<include>>` Buscar Paciente.

**Texto agregado:**
> Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente).

### 6.5 UC-REC-19 Desactivar Paciente — Comentarios *(modificación)* *(commit `"."`)*
**Texto eliminado:**
> Incluye `<<include>>` Buscar Paciente. Se realiza baja lógica para mantener integridad referencial.

**Texto agregado:**
> Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Se realiza baja lógica para mantener integridad referencial.

### 6.6 Nuevo UC-REC-S-01 Buscar Paciente *(agregado)* *(commit `"."`)*
> |**UC–REC-S-01**|**Buscar Paciente**|
> |---|---|
> |**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre o Apellido) y retorna el/los paciente(s) coincidente(s) al caso de uso invocante. |
> |**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |
> |**Postcondiciones**| Los datos del paciente seleccionado son retornados al caso de uso invocante para continuar su flujo. |
> |**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. |

---

## 7) Sección 2.7.3.2 — Subsistema Laboratorio Bioquímico (UC-DIAG)

### 7.1 UC-DIAG-01 Registrar Ficha Clínica — Comentarios *(agregado)*
**Texto agregado:**
> Incluye `<<extend>>` a UC–DIAG-08 (Modificar Ficha Clínica).

### 7.2 UC-DIAG-02 Registrar Ingreso de Muestra — Precondición *(modificación)*
**Texto eliminado:**
> El paciente debe contar con una Ficha Clínica registrada en el sistema. <br>El usuario debe tener una sesión activa con el rol correspondiente.

**Texto agregado:**
> El paciente debe contar con una Ficha Clínica registrada previamente en el sistema (no necesariamente en la sesión actual). <br>El usuario debe tener una sesión activa con el rol correspondiente.

### 7.3 UC-DIAG-04 Validar Análisis *(modificación)*
**Requisitos asociados — texto eliminado:**
> RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.

**Requisitos asociados — texto agregado:**
> RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.<br>RF-08 Validación de Identidad y Descarga de Informe.

**Postcondiciones — texto eliminado:**
> El estado del análisis cambia permanentemente a "Validado". <br>El sistema compila estáticamente los datos y genera de inmediato el Informe de Resultados en formato PDF, almacenándolo en el servidor seguro. <br>Se dispara automáticamente el proceso interno de "Notificación de Resultados" (UC-DIAG-05).

**Postcondiciones — texto agregado:**
> El estado del análisis cambia permanentemente a "Validado". <br>El sistema compila estáticamente los datos y genera de inmediato el Informe de Resultados en formato PDF, almacenándolo en el servidor seguro. <br>El sistema genera criptográficamente un Token OTP asociado al análisis y envía automáticamente un mensaje de WhatsApp al paciente con el enlace al portal web, las instrucciones y el Token OTP.

### 7.4 UC-DIAG-05 (antiguo "Notificación de Resultados") *(eliminado y reemplazado por "Descargar Informe")*
**Bloque eliminado (UC–DIAG-05 Notificación de Resultados):**
> |**UC–DIAG-05**|**Notificación de Resultados**|
> |---|---|
> |**Objetivos asociados**| OBJ-03 Emisión Segura y Descarga de Resultados |
> |**Requisitos asociados**| RF-07 Notificación de Disponibilidad de Resultados y OTP |
> |**Descripción**| Proceso interno del sistema que se activa inmediatamente tras la validación de un análisis. Se encarga de generar la credencial de acceso temporal y avisar al paciente. |
> |**Precondición**| El caso de uso UC-DIAG-04 (Validar Análisis) debe haber concluido con éxito. |
> |**Postcondiciones**| El sistema genera criptográficamente un Token OTP (One-Time Password) asociado al análisis. <br>Se envía automáticamente un mensaje de WhatsApp al paciente con el enlace al portal web, las instrucciones y el Token OTP. |

**Reemplazo agregado (UC-DIAG-05 → "Descargar Informe", antes UC-DIAG-06):** se conserva el contenido de "Descargar Informe" pero re-numerado como **UC–DIAG-05**.

### 7.5 UC-DIAG-07 (renombrado)
**Texto eliminado del título:**
> UC–DIAG-07 **Consultar Ficha Clínica**

**Texto agregado del título:**
> UC–DIAG-07 **Consultar Historial de Paciente**

### 7.6 Nuevo UC-DIAG-08 Modificar Ficha Clínica *(agregado)*
> |**UC–DIAG-08**|**Modificar Ficha Clínica**|
> |---|---|
> |**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
> |**Requisitos asociados**| RF-20 Modificación de Ficha Clínica |
> |**Descripción**| El Bioquímico/Doctor modifica una ficha clínica previamente registrada, corrigiendo errores o agregando información complementaria. |
> |**Precondición**| La ficha clínica debe existir y no estar asociada a un análisis en estado «Validado». |
> |**Postcondiciones**| Los cambios quedan registrados. Se almacena una versión histórica de la ficha original (audit trail de modificaciones). |
> |**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Cuando el análisis ya fue validado, la modificación se restringe a campos no clínicos (ej. observaciones administrativas). |

### 7.7 Nuevo UC-DIAG-09 Cancelar Análisis *(agregado)*
> |**UC–DIAG-09**|**Cancelar Análisis**|
> |---|---|
> |**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
> |**Requisitos asociados**| RF-21 Cancelación de Análisis |
> |**Descripción**| El Bioquímico/Doctor cancela un análisis micológico en curso, registrando el motivo. |
> |**Actor**| Bioquímico/Doctor, Administrador |
> |**Precondición**| El análisis debe existir y estar en estado «Pendiente» o «En Proceso» (no «Validado»). |
> |**Postcondiciones**| El estado del análisis cambia a «Cancelado». Se registra el motivo obligatorio de cancelación. El análisis cancelado permanece en el historial del paciente. |

### 7.8 Nuevo UC-DIAG-10 Consultar Panel de Análisis *(agregado)*
> |**UC–DIAG-10**|**Consultar Panel de Análisis**|
> |---|---|
> |**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
> |**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico |
> |**Descripción**| El Bioquímico/Doctor accede a un panel de trabajo que lista todos los análisis micológicos, filtrables por estado, tipo de análisis, fecha y bioquímico asignado, sin necesidad de navegar paciente por paciente. |
> |**Precondición**| Sesión activa con rol autorizado. |
> |**Postcondiciones**| El sistema presenta una tabla paginada y filtrable de análisis. Operación de solo lectura. Desde este panel se puede acceder al detalle de cada análisis y ejecutar acciones (actualizar estado, validar, cancelar). |
> |**Comentarios**| Diferente de DIAG-07 (que muestra el historial de un paciente). Este UC muestra el volumen de trabajo del laboratorio. |

### 7.9 Nuevo UC-DIAG-11 Gestionar Tipos de Análisis y Muestra *(agregado)*
> |**UC–DIAG-11**|**Gestionar Tipos de Análisis y Muestra**|
> |---|---|
> |**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
> |**Requisitos asociados**| RF-16 Gestión de Catálogos Clínicos |
> |**Descripción**| El Administrador gestiona el catálogo de tipos de análisis micológicos y tipos de muestra disponibles en el sistema (crear, modificar, desactivar). |
> |**Actor**| Administrador |
> |**Precondición**| Sesión activa con rol de Administrador. |
> |**Postcondiciones**| El catálogo queda actualizado. Los tipos desactivados no pueden seleccionarse en nuevos análisis, pero se preservan en registros históricos. |
> |**Comentarios**| Incluye sub-flujos: Crear Tipo, Modificar Tipo, Desactivar Tipo (baja lógica). |

---

## 8) Sección 2.7.3.3 — Subsistema Recursos de Laboratorio (UC-LAB)

### 8.1 UC-LAB-02 Registrar Retiro de Insumos — Descripción *(modificación)*
**Texto eliminado:**
> El Profesor o el Bioquímico registran el consumo o retiro de reactivos necesarios para las prácticas educativas o los análisis clínicos, deduciendo inmediatamente las cantidades del inventario.

**Texto agregado:**
> El Profesor o el Bioquímico registran el consumo o retiro de reactivos necesarios para las prácticas educativas o los análisis clínicos, deduciendo inmediatamente las cantidades del inventario. El sistema debe registrar el análisis micológico o la práctica educativa a la que se destina el retiro (trazabilidad), el lote del insumo consumido (FIFO/FEFO), la ubicación de almacenamiento de origen, y si corresponde a la disposición final de un residuo.

### 8.2 UC-LAB-04 Generar Reporte Mensual de Residuos — Precondición *(modificación)*
**Texto eliminado:**
> El usuario solicitante debe tener los privilegios administrativos o directivos necesarios.

**Texto agregado:**
> El usuario debe tener una sesión activa con el rol de Administrador.

### 8.3 Nuevo UC-LAB-06 Gestionar Catálogo de Insumos *(agregado)*
> |**UC–LAB-06**|**Gestionar Catálogo de Insumos**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
> |**Descripción**| El Administrador gestiona el catálogo de tipos de insumos y reactivos: crear, modificar y desactivar (baja lógica). |
> |**Actor**| Administrador |
> |**Precondición**| Sesión activa con rol de Administrador. |
> |**Postcondiciones**| El catálogo queda actualizado. Los insumos desactivados no pueden recibir nuevos ingresos o retiros, pero sus movimientos históricos se preservan. |
> |**Comentarios**| Datos del insumo: nombre, descripción, unidad de medida (ml, g, unidades), categoría, umbral mínimo de alerta, ubicación de almacenamiento. |

### 8.4 Nuevo UC-LAB-07 Consultar Trazabilidad de Movimientos *(agregado)*
> |**UC–LAB-07**|**Consultar Trazabilidad de Movimientos**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
> |**Descripción**| El usuario autorizado consulta el historial completo de movimientos (ingresos, retiros, devoluciones) de un insumo o de todos los insumos en un rango de fechas. |
> |**Actor**| Administrador, Bioquímico/Doctor, Profesor |
> |**Precondición**| Sesión activa con rol autorizado. |
> |**Postcondiciones**| El sistema presenta una tabla cronológica de movimientos con: fecha, tipo de movimiento, usuario, cantidad, lote afectado, y análisis/práctica asociada. Operación de solo lectura. |
> |**Comentarios**| Filtrable por insumo, tipo de movimiento, rango de fechas, usuario. |

### 8.5 Nuevo UC-LAB-08 Configurar Umbrales de Alerta *(agregado)*
> |**UC–LAB-08**|**Configurar Umbrales de Alerta**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-09 Alertas de Stock en Panel de Control |
> |**Descripción**| El Administrador configura los umbrales mínimos de stock y los días de anticipación para alertas de vencimiento de cada insumo. |
> |**Actor**| Administrador |
> |**Precondición**| Sesión activa con rol de Administrador. El insumo debe existir en el catálogo. |
> |**Postcondiciones**| Los umbrales quedan configurados. El dashboard reflejará alertas cuando el stock esté por debajo del umbral o un lote esté dentro del período de pre-vencimiento. |
> |**Comentarios**| Umbrales por defecto: stock mínimo = 1 unidad, alerta de vencimiento = 30 días. El Administrador puede sobrescribirlos por insumo. |

### 8.6 Nuevo UC-LAB-09 Registrar Devolución de Insumos *(agregado)*
> |**UC–LAB-09**|**Registrar Devolución de Insumos**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
> |**Descripción**| El Profesor o Bioquímico registra la devolución de insumos no utilizados al inventario, revirtiendo total o parcialmente un retiro previo. |
> |**Actor**| Profesor, Bioquímico/Doctor, Administrador |
> |**Precondición**| Debe existir un retiro previo registrado. La cantidad a devolver no puede superar la cantidad retirada. |
> |**Postcondiciones**| El stock del insumo se incrementa en la cantidad devuelta. Se registra el movimiento como «Devolución» vinculado al retiro original. |
> |**Comentarios**| Si el lote original ya venció, el sistema advierte y la devolución se registra como «Vencido — no utilizable». |

### 8.7 Nuevo UC-LAB-10 Gestionar Categorías de Residuos *(agregado)*
> |**UC–LAB-10**|**Gestionar Categorías de Residuos**|
> |---|---|
> |**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
> |**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
> |**Descripción**| El Administrador gestiona el catálogo de categorías/clases de peligrosidad de residuos químicos (crear, modificar, desactivar). |
> |**Actor**| Administrador |
> |**Precondición**| Sesión activa con rol de Administrador. |
> |**Postcondiciones**| El catálogo queda actualizado. Las categorías desactivadas no pueden seleccionarse en nuevos registros de residuos. |
> |**Comentarios**| Datos de la categoría: nombre, clase de peligrosidad (ej. Clase I, II, III), descripción, instrucciones de almacenamiento. |

### 8.8 Nuevo UC-LAB-11 Consultar y Modificar Registro de Residuos *(agregado)*
> |**UC–LAB-11**|**Consultar y Modificar Registro de Residuos**|
> |---|---|
> |**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
> |**Requisitos asociados**| RF-11 Registro de Generación de Residuos Químicos |
> |**Descripción**| El usuario autorizado consulta el historial de residuos generados en un período y, si es necesario, corrige un registro erróneo (antes de que se consolide en el reporte mensual). |
> |**Actor**| Administrador, Bioquímico/Doctor, Profesor |
> |**Precondición**| Sesión activa con rol autorizado. El registro a modificar no debe haber sido incluido en un reporte mensual ya emitido. |
> |**Postcondiciones**| Los datos del residuo quedan actualizados. Se registra la modificación en auditoría. |
> |**Comentarios**| Sub-flujos: Consultar (listado filtrable por fecha, categoría, usuario), Modificar (solo el autor o Administrador). |

### 8.9 Nuevo UC-LAB-12 Gestionar Categorías de Insumos *(agregado)*
> |**UC–LAB-12**|**Gestionar Categorías de Insumos**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
> |**Descripción**| El Administrador gestiona el catálogo de categorías de insumos (reactivos, medios de cultivo, materiales descartables, equipos). |
> |**Actor**| Administrador |
> |**Precondición**| Sesión activa con rol de Administrador. |
> |**Postcondiciones**| El catálogo queda actualizado. Los insumos pueden clasificarse por categoría. |
> |**Comentarios**| Facilita filtros en consultas de inventario (LAB-05) y reportes (LAB-13). |

### 8.10 Nuevo UC-LAB-13 Generar Reporte de Inventario *(agregado)*
> |**UC–LAB-13**|**Generar Reporte de Inventario**|
> |---|---|
> |**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
> |**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario.<br>RF-09 Alertas de Stock en Panel de Control |
> |**Descripción**| El Administrador genera un reporte del estado del inventario en un momento dado, incluyendo stock actual, movimientos del período, insumos bajo umbral y próximos a vencer. |
> |**Actor**| Administrador, Bioquímico/Doctor |
> |**Precondición**| Sesión activa con rol autorizado. |
> |**Postcondiciones**| El sistema emite un reporte en formato PDF o CSV con el resumen del inventario. |
> |**Comentarios**| Complementa a LAB-05 (consulta en pantalla) con una versión exportable para auditorías o planificación de compras. |

---

## 9) Sección 2.8 — Casos de Uso Extendidos (UCE)

### 9.1 Reestructuración de subsecciones *(modificación de títulos)*
- `### 2.8.1 Subsistema Gestión Clínica` → **`### 2.8.1 Subsistema Gestión de Pacientes`**
- `### 2.8.2 Subsistema Recursos de Laboratorio` → **`### 2.8.2 Subsistema Laboratorio Bioquímico`**
- `### 2.8.3 Subsistema Acceso y Seguridad` → **`### 2.8.3 Subsistema Recursos de Laboratorio`**
- Nueva `### 2.8.4 Subsistema Acceso y Seguridad`
- `### 2.8.4 Subsistema Reportes y estadísticas` → **`### 2.8.5 Subsistema Reportes y Estadísticas`**

### 9.2 Nota agregada en 2.8.3 (Recursos de Laboratorio) *(agregado)*
> UCEs pendientes de desarrollo. Se requiere desarrollar los UCE correspondientes a UC–LAB-01 (Registrar Ingreso de Insumos), UC–LAB-02 (Registrar Retiro de Insumos), UC–LAB-03 (Registrar Generación de Residuos), UC–LAB-04 (Generar Reporte de Residuos), UC–LAB-05 (Consultar Inventario), y los nuevos UC–LAB-06 a UC–LAB-13.

### 9.3 UCE-REC-01 Agendar Turno — Paso 8 *(modificación)*
**Texto eliminado:**
> | 8 | El sistema programa en cola el envío de un recordatorio de asistencia (`<<include>>` Enviar Recordatorio de Turno). |

**Texto agregado:**
> | 8 | El sistema programa en cola el envío de un recordatorio de asistencia. |

### 9.4 UCE-REC-03 — Requisitos asociados *(modificación)*
**Texto eliminado:**
> RF-04 Cancelación y Reprogramación de Turnos <br>RF-03 Gestión de Lista de Espera por Turnos Liberados

**Texto agregado:**
> RF-04 Cancelación y Reprogramación de Turnos <br>RF-03 Gestión de Reagendación automática

### 9.5 UCE-REC-04 — Requisitos asociados *(modificación)*
**Texto eliminado:**
> RF-03 Gestión de Lista de Espera por Turnos Liberados

**Texto agregado:**
> RF-03 Gestión de Reagendación automática

### 9.6 UCE de atención de turno (Secuencia "Presente") *(modificación)*
**Texto eliminado (pasos 5.1/6/7):**
> | 5.1 | El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes antes de continuar. |
> | 6 | El sistema registra el evento en la tabla de auditoría. |
> | 7 | La interfaz confirma la operación y habilita el botón para iniciar la consulta (UC-DIAG-01). |

**Texto agregado (pasos 6/7/8):**
> | 6 | El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes antes de continuar. |
> | 7 | El sistema registra el evento en la tabla de auditoría. |
> | 8 | La interfaz confirma la operación y habilita el botón para iniciar la consulta (UC-DIAG-01). |

### 9.7 Nota agregada en 2.8.1 *(agregado)*
> Nota: No existe UC–REC-09. La numeración salta intencionalmente de UC–REC-08 a UC–REC-10.

### 9.8 UCE-REC-17 — Paso 2 *(modificación)* *(commit `"."`)*
**Texto eliminado:**
> | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido como criterio de búsqueda. |

**Texto agregado:**
> | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido como criterio de búsqueda. |

### 9.9 UCE-REC-19 — Paso 2 *(modificación)* *(commit `"."`)*
**Texto eliminado:**
> | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido. |

**Texto agregado:**
> | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido. |

### 9.10 UCE-REC-20 — Comentarios *(modificación)*
**Texto eliminado:**
> Reemplaza la funcionalidad de "Agendar" del antiguo UC-REC-09. Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias.

**Texto agregado:**
> Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias.

### 9.11 UCE-REC-21 — Comentarios *(modificación)*
**Texto eliminado:**
> Reemplaza la funcionalidad de "Cancelar" del antiguo UC-REC-09.

**Texto agregado:**
> -

### 9.12 UCE-REC-22 — Comentarios *(modificación)*
**Texto eliminado:**
> Reemplaza la funcionalidad de "Reprogramar" del antiguo UC-REC-09.

**Texto agregado:**
> -

### 9.13 Caso de uso "Crear Indicación Médica" (UCE-REC-10) — Rendimiento *(modificación)*
**Texto eliminado:**
> | 6 | Menos de 2 segundos |

**Texto agregado:**
> | 3 | Menos de 2 segundos |

### 9.14 Nuevo UCE-REC-S-01 Buscar Paciente *(agregado)* *(commit `"."`)*
> |**UCE–REC-S-01**|**Buscar Paciente**| |
> |---|---|---|
> |**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre, Apellido) y retorna el/los pacientes coincidentes al caso de uso invocante. |
> |**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |
> |**Secuencia normal**| | |
> | | 1 | El sistema solicita al usuario el criterio de búsqueda (DNI, Nombre o Apellido). |
> | | 2 | El usuario ingresa el criterio de búsqueda. |
> | | 3 | El sistema consulta la base de datos con el criterio ingresado. |
> | | 4a | Si hay una sola coincidencia exacta: el sistema retorna los datos del paciente al caso de uso invocante. |
> | | 4b | Si hay múltiples coincidencias: el sistema muestra un listado paginado para que el usuario seleccione. Al seleccionar, retorna los datos. |
> |**Postcondición**| Los datos del paciente seleccionado son retornados al caso de uso invocante. |
> |**Excepciones**| | |
> | | 3 | Si ningún paciente coincide con el criterio ingresado, el sistema informa "Paciente no encontrado" al caso de uso invocante para que maneje la situación (ofrecer crear uno nuevo, buscar de nuevo, etc.). |
> | | 3 | Si ocurre un error de conexión con la base de datos, se retorna un error al caso de uso invocante. |
> |**Rendimiento**| | |
> | | 3 | Menos de 1 segundo |
> |**Frecuencia**| Alta (invocado por Modificar y Desactivar Paciente) |
> |**Estabilidad**| Alta |
> |**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. La búsqueda es flexible: DNI (coincidencia exacta), Nombre o Apellido (coincidencia parcial). |

### 9.15 UCE-DIAG-01 Registrar Ficha Clínica *(modificación de redacción de pasos)*
**Pasos modificados (texto eliminado → texto agregado):**
- Paso 3: "El **Backend** consulta la base de datos…" → "**El sistema** consulta la base de datos…"
- Paso 5: "El Bioquímico completa los campos clínicos obligatorios (**Institución, Diagnóstico presuntivo, etc.**) y presiona 'Guardar Ficha'." → "El Bioquímico completa los campos clínicos obligatorios y presiona 'Guardar Ficha'."
- Paso 7: "El **Backend** recibe la petición…" → "**El sistema** recibe la petición…"
- Paso 8: "El **Backend** envía un código de estado HTTP 200…" → "**El sistema** envía un código de estado HTTP 200…"
- Paso 9: "**interfaz** muestra…" → "**La interfaz** muestra…"

---

## 10) Sección Glosario de Términos *(agregado)*

El glosario (vacío previamente) se completa con:

> | Agente IA | Arquitectura | Componente de software que interactúa con los pacientes de forma asíncrona a través de WhatsApp para la autogestión de turnos (agendamiento, cancelación, reprogramación y consulta). |
> | OTP (One-Time Password) | Seguridad | Token criptográfico de un solo uso generado por el sistema y enviado al paciente vía WhatsApp. Permite validar su identidad de forma anónima en el portal web de descarga de resultados. |
> | Token | Seguridad | Credencial digital generada por el sistema para autenticación o autorización temporal. Incluye tanto el OTP para pacientes como el JWT para sesiones de usuarios internos. |
> | Alta Temprana | Clínico | Registro inicial mínimo de un paciente en la base de datos, creado por el Agente IA al momento del agendamiento del turno. Contiene únicamente DNI y Nombre Completo. |
> | Baja lógica | Seguridad / Datos | Mecanismo de desactivación de un registro (paciente, usuario, indicación médica) que marca su estado como "Inactivo" sin eliminar físicamente los datos, preservando la integridad referencial y el historial. |
> | Ficha Clínica | Clínico | Documento digital estructurado que contiene la información médica del paciente recolectada durante la consulta presencial. Incluye datos demográficos completos y diagnóstico clínico. |
> | Muestra | Clínico | Material biológico (ej. uñas, piel, cabello) extraído del paciente para su análisis microbiológico en el laboratorio. |
> | Micología | Dominio | Rama de la biología que estudia los hongos. En el contexto del sistema, el laboratorio se especializa en el diagnóstico de infecciones fúngicas (micosis) en pacientes. |
> | JWT (JSON Web Token) | Seguridad | Estándar abierto (RFC 7519) utilizado para la autenticación de usuarios internos. El sistema genera un token JWT al iniciar sesión y lo inyecta en el navegador para validar sesiones subsecuentes. |

---

## Nota sobre el commit `"."` (`93867ef`)
Los únicos cambios aportados por el commit `"."` son los referidos a **Buscar Paciente**: UC-REC-S-01, UCE-REC-S-01 y las referencias `<<include>>`/paso 2 en UC-REC-17/19 y UCE-REC-17/19 (secciones 6.4, 6.5, 6.6, 9.8, 9.9 y 9.14). Todo lo demás corresponde al commit `89bf80b`.
