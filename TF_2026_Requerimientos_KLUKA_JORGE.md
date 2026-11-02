**Sistema Integral de Gestión Micológica**
**SIGEMI**
**Documento de Requisitos del Sistema**
**Versión 0.0.0.1**
**Fecha: 17/04/2026**
Realizado por: Kluka Jorge Favio
Realizado para: Módulo de Bioquímica y Farmacia UNaM
# Lista de Cambios
|**Nro**|**Fecha**|**Descripción**|**Autor**|
|---|---|---|---|
| 0 | 17/04/2026  | Creación del documento. Definición de la Presentación General, Contexto Actual y Objetivos del sistema.  | Kluka Jorge |
| 1 | 21/04/2026 | Estructuración del proyecto. Definición de subsistemas y módulos principales.  | Kluka Jorge |
| 2 | 24/04/2026 | Redacción de todos los requisitos funcionales (RF) y no funcionales (RNF).  | Kluka Jorge |
| 3 | 10/05/2026 | Modelado de diagramas de casos de uso e identificación de los actores.  | Kluka Jorge |
| 4 | 19/05/2026 | Desarrollo de Casos de Uso Extendidos para Gestión de Pacientes.  | Kluka Jorge |
| 5 | 25/05/2026 | Desarrollo de Casos de Uso Extendidos para Laboratorio Bioquímico.  | Kluka Jorge |
| 6 | 30/05/2026 | Desarrollo de Casos de Uso Extendidos para Acceso, Seguridad y Reportes.  | Kluka Jorge |
| 7 | 01/06/2026 | Desarrollo de Casos de Uso Extendidos para Recursos de Laboratorio y revisión.  | Kluka Jorge |
| 8 | 04/10/2026 | Completitud de Casos de Uso Extendidos para Laboratorio Bioquímico (UCE–DIAG-03 a UCE–DIAG-10) y especificación del reenvío automático de OTP como postcondición.  | Kluka Jorge |
| 9 |  |  | Kluka Jorge |
| 10 |  |  | Kluka Jorge |
| 11 |  |  | Kluka Jorge |
| 12 |  |  | Kluka Jorge |
| 13 |  |  | Kluka Jorge |
| 14 |  |  | Kluka Jorge |

# Índice
# 1. Presentación General
El sistema presentado para el módulo de bioquímica y farmacia de la Universidad Nacional de Misiones tiene el propósito de ser una solución para el laboratorio de Micología que digitalice el registro de información clínica, automatice la gestión de turnos con pacientes, registre el historial médico de los pacientes, gestione el stock de insumos reactivos y optimice el control de residuos.
## 1.2 Contexto Actual
En la actualidad, el laboratorio de Micología opera mediante un flujo de trabajo completamente manual. La recepción de pacientes, la asignación de turnos y la confección de historias clínicas se realizan exclusivamente en papel. Esta dependencia del formato físico representa un desafío considerable, especialmente considerando que los análisis microbiológicos tienen tiempos de espera prolongados que varían hasta un mes entero. Además, la institución debe resguardar esta información meticulosamente por exigencias legales y para su uso en investigación.
A las dificultades en la atención clínica se suma la compleja gestión de los recursos físicos del laboratorio. Actualmente se carece de un sistema formal de control de stock para los insumos y reactivos químicos, llevando el registro en hojas sueltas o revisando la disponibilidad de manera informal. Esta falta de trazabilidad agrava la escasez de materiales y provoca un uso ineficiente de los mismos, llevando en ocasiones a la utilización de reactivos con fechas de vencimiento expiradas para las prácticas de la facultad.
Por último, el laboratorio enfrenta una nueva presión a nivel normativo. Un reglamento reciente exige llevar un registro exacto del volumen y peso de los residuos químicos generados para su posterior tratamiento y eliminación. Al día de hoy, los profesores deben anotar esta información manualmente en listas de papel cada vez que generan un residuo.
En este sentido, la necesidad de un sistema para el laboratorio es crítica, no solo para agilizar la atención de los pacientes y garantizar la integridad de los historiales clínicos, sino también para optimizar el uso de insumos limitados y asegurar el cumplimiento de las normativas ambientales y legales vigentes.
# 2. Requisitos
## 2.1 Objetivos del sistema
|**OBJ–01**|**Automatización de la Gestión de Turnos y Atención**|
|---|---|
|**Descripción**| Digitalizar y automatizar integralmente el proceso de atención de pacientes, desde la recepción y agendamiento del turno hasta el envío de indicaciones y facturación.  |
|**Estabilidad**| Alta  |
|**Comentarios**| Soporta la coordinación de citas múltiples para estudios prolongados (ej. análisis de uñas). |

|**OBJ–02**|**Digitalización del Historial Clínico y Registro de Análisis**|
|---|---|
|**Descripción**| Centralizar y almacenar en un sistema digital los datos médicos de los pacientes, su historial clínico y los estados de sus análisis (pendiente, en proceso, terminado, validado).  |
|**Estabilidad**| Alta  |
|**Comentarios**| Elimina la dependencia física del registro en papel . <br>Garantiza el resguardo de la información clínica para exigencias legales y uso en investigación.  |

|**OBJ–03**|**Emisión Segura y Descarga de Resultados**|
|---|---|
|**Descripción**| Proveer un módulo automatizado y asincrónico para la entrega de los resultados finales a los pacientes mediante un portal seguro y un token de un solo uso (OTP).  |
|**Estabilidad**| Alta  |
|**Comentarios**| Asegura el cumplimiento de la Ley de Protección de los Datos Personales (Ley 25.326).   |

|**OBJ–04**|**Trazabilidad y Control de Stock de Insumos Reactivos**|
|---|---|
|**Descripción**| Implementar un sistema formal de control de inventario para gestionar las cantidades y la disponibilidad de los insumos y reactivos químicos utilizados por profesores y alumnos.  |
|**Estabilidad**| Media |
|**Comentarios**| Previene la utilización de reactivos con fechas vencidas.<br>Optimiza la distribución de materiales limitados.  <br>Reemplaza el control informal llevado en hojas sueltas.  |

|**OBJ–05**|**Sistematización del Registro de Residuos Químicos**|
|---|---|
|**Descripción**| Sistematizar el registro exacto del volumen y peso de los residuos químicos generados , para automatizar la generación de la documentación exigida por el reglamento.  |
|**Estabilidad**| Media |
|**Comentarios**| El reglamento que exige la documentación de los residuos entra en vigencia por primera vez este año. |

## 2.2 Subsistemas del Proyecto
El sistema se estructura en componentes lógicos independientes que dividen la funcionalidad en áreas clave: Gestión de Pacientes, Laboratorio Bioquímico, Recursos de Laboratorio y Seguridad.
### 2.2.2 Descripción de Subsistemas
# Subsistema de Gestión de Pacientes
El Subsistema de Gestión de Pacientes es el componente encargado de la logística de ingreso y el contacto inicial con los Pacientes. Su función principal es organizar el flujo de atención administrativa, comenzando por la agenda y asignación de turnos, hasta la gestión del repositorio centralizado a largo plazo, el cual resguarda el historial clínico acumulado de las personas atendidas. Este subsistema abarca los módulos de**Gestión de Turnos y Atención**, y**Gestión de Pacientes**.
# Subsistema de Laboratorio Bioquímico
El Subsistema de Laboratorio Bioquímico es el núcleo clínico y científico destinado al procesamiento de las muestras y la evaluación médica. Su propósito fundamental es sistematizar la recolección de los datos en la ficha clínica al momento de la consulta, trazar el ciclo de vida completo de los estudios microbiológicos (abarcando los estados pendiente, en proceso, terminado y validado) y automatizar la entrega remota y segura de los diagnósticos finales a los pacientes. Este subsistema abarca los módulos de**Registro de Información Clínica**,**Registro de Análisis**, y**Emisión de Resultados**.
# Subsistema de Recursos de Laboratorio
El Subsistema de Recursos de Laboratorio es el componente encargado de administrar los bienes físicos y químicos del módulo de micología. Este subsistema digitaliza y controla la trazabilidad del inventario, gestionando el ingreso y egreso de los insumos reactivos utilizados por profesores y alumnos en las prácticas. A su vez, sistematiza el registro exacto del volumen y peso de los residuos químicos generados para cumplir con las normativas vigentes. Este subsistema abarca los módulos de**Stock de Insumos Reactivos**y**Control de Residuos**.
# Subsistema de Acceso y Seguridad
El Subsistema de Acceso y Seguridad es el componente transversal encargado de proteger la confidencialidad de los datos y garantizar la transparencia operativa de la aplicación. Su función es gestionar la autenticación y autorización de los usuarios mediante un esquema de roles y permisos, al mismo tiempo que mantiene un registro detallado, cronológico e inmutable de todas las acciones críticas realizadas en la plataforma. Este subsistema abarca los módulos de**Usuarios**,**Roles y Permisos**, y**Auditoría**.
# Subsistema de Reportes y Estadísticas
El Subsistema de Reportes y Estadísticas es el componente encargado de procesar y consolidar la información operativa de la plataforma para la toma de decisiones y el cumplimiento normativo. Su función principal es recopilar los datos generados en el día a día para estructurar análisis estadísticos que sirvan como insumo en los trabajos de investigación de la facultad. Este subsistema abarca el módulo de**Estadísticas y Reportes**.
## 2.3 Módulos del Proyecto
### 2.3.2 Descripción de Módulos
#### 2.3.2.1 Módulos Principales
Los Módulos Principales constituyen el núcleo operativo del sistema, diseñados para dar respuesta directa a las necesidades clínicas, administrativas y logísticas del laboratorio de Micología.
# Gestión de Turnos y Atención
Este módulo se encarga de automatizar y optimizar todo el proceso inicial de atención al paciente. Sus funciones abarcan la agenda del turno, el otorgamiento de indicaciones para los análisis, el envío de recordatorios de asistencia, la gestión de reprogramaciones y la administración de una lista de espera que notifica liberaciones de fechas. Su implementación busca brindar un mejor servicio integral al paciente y eliminar la carga de trabajo completamente manual que existe en la recepción en la actualidad.
# Registro de Información Clínica
Su propósito es sistematizar la recolección de los datos médicos iniciales del paciente al momento de su consulta. Opera permitiendo que el doctor ingrese en el sistema una ficha clínica detallada durante el transcurso del turno. Esto garantiza que el laboratorio cuente con la información médica exacta, estructurada y legible con la que posteriormente se realizarán los análisis de micosis.
# Gestión de Pacientes
Su función principal es actuar como el repositorio centralizado del historial de las personas atendidas en el laboratorio. Gestiona el almacenamiento permanente tanto de los datos personales del paciente como de su historial clínico acumulado y resultados previos. Este almacenamiento organizado es crítico para dar respuesta a exigencias legales de resguardo de información y para facilitar la consulta ágil de datos en futuros trabajos de investigación de la facultad.
# Registro de Análisis
Este módulo traza el ciclo de vida completo de las muestras microbiológicas dentro del laboratorio. Registra el tipo de análisis, los parámetros o resultados obtenidos, y permite actualizar los estados del estudio secuencialmente (pendiente, en proceso, terminado y validado por un bioquímico). Su valor reside en asegurar un control riguroso de cada etapa clínica, consolidando toda la información relevante al análisis en un único lugar. Incluye la gestión de tipos de análisis, la cancelación de estudios y un panel de trabajo para visualizar el volumen de análisis por estado.
# Emisión de Resultados
Se encarga de automatizar la entrega final y remota de los diagnósticos a los pacientes. Funciona mediante un flujo de notificación asíncrona que envía un enlace y genera criptográficamente un Token (OTP) de un solo uso, permitiendo al paciente descargar su archivo PDF desde un portal web seguro mediante una doble validación de identidad. Este proceso asegura el cumplimiento estricto de la Ley de Protección de los Datos Personales (Ley 25.326) sin forzar el retiro presencial.
# Stock de Insumos Reactivos
Su objetivo es digitalizar la administración del inventario de recursos físicos y químicos. Registra los ingresos y los retiros de insumos realizados por los profesores y bioquímicos para las prácticas de los alumnos y estudios de laboratorio. Su implementación busca clarificar la trazabilidad operativa para solucionar la actual mala gestión y escasez, evitando problemáticas como el vencimiento de reactivos, el uso ineficiente de materiales nuevos y el desconocimiento de las cantidades exactas. incluyendo trazabilidad por lotes, ubicaciones de almacenamiento y devoluciones.
# Control de Residuos
Su función es sistematizar la recolección de datos sobre los desechos generados en las prácticas de laboratorio. Permite registrar de manera exacta la cantidad (volumen y peso) de los residuos químicos producidos por cada actividad, incluyendo el registro de disposición final y la gestión de categorías de peligrosidad. Esto es vital para garantizar el cumplimiento del nuevo reglamento que entró en vigencia en el año 2026, facilitando la generación de reportes mensuales y el adecuado resguardo de los residuos para su tratamiento.
#### 2.3.2.2 Módulos Adyacentes
Para que estos módulos principales operen de manera cohesionada y presenten una solución de software segura e integral, se apoyan en los siguientes módulos transversales.
# Usuarios
Su propósito es administrar la identidad y las credenciales de todas las personas que interactúan con la plataforma. Gestiona el registro, la modificación y la baja de cuentas, centralizando el proceso de autenticación en el sistema . Representa el pilar inicial de la seguridad de la aplicación, asegurando que únicamente los individuos debidamente identificados puedan ingresar a la plataforma.
# Roles y permisos
Su función es controlar y delimitar el nivel de autorización y los privilegios operativos dentro de la aplicación. Opera definiendo qué pantallas, acciones y datos específicos están disponibles para cada tipo de cuenta. Su implementación es fundamental para garantizar la confidencialidad de la información clínica y prevenir alteraciones no autorizadas, forzando a que cada actor opere estrictamente dentro de sus responsabilidades.
# Estadísticas y Reportes
Este módulo se encarga de procesar y consolidar los datos transaccionales generados por el resto del sistema para su visualización y exportación. Extrae y cruza datos clínicos, de inventario y de desechos para automatizar la emisión de reportes periódicos y proveer la base de información estructurada que alimentará investigaciones académicas.
# Auditoría
Su objetivo es proveer un mecanismo de trazabilidad profundo e inmutable sobre las operaciones críticas que ocurren en el software. Funciona registrando de manera automática, silenciosa y cronológica cada evento significativo, guardando detalles precisos como el usuario responsable, la fecha, la hora, la dirección IP y el cambio específico realizado
## 2.4 Requisitos de Información
|**IRQ–01**|**Ficha Clínica del Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis. |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| Entidad central que almacena la información demográfica y clínica inicial del paciente al momento de su atención médica.  |
|**Datos específicos**| Número de registro<br>Fecha de ingreso<br>Nombre y apellido<br>Fecha de nacimiento<br>Edad (campo calculado)<br>DNI<br>Sexo<br>Domicilio<br>Teléfono de contacto<br>Correo Electrónico<br>Obra Social.  |
|  |  |
|**Estabilidad**| alta  |
|**Comentarios**| El campo de edad no se persistirá estáticamente, sino que el sistema lo calculará en tiempo real a partir de la fecha de nacimiento.  |

|**IRQ–02**|**Registro de Análisis Micológico**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis.<br>OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.  |
|**Descripción**| Entidad que traza el ciclo de vida y consolida los resultados científicos de la muestra extraída al paciente.  |
|**Datos específicos**| Tipo de muestra<br>Estado actual (Pendiente, En proceso, Terminado, Validado, Cancelado)<br>Observaciones/Resultados parciales<br>Fecha de validación<br>Bioquímico validador.  |
|  |  |
|**Estabilidad**| Media |
|**Comentarios**| - |

|**IRQ–03**|**Insumo / Reactivo de Laboratorio**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-09 Alertas de Stock en Panel de Control.<br>RF-10 Gestión de Ingresos y Retiros de Inventario. |
|**Descripción**| Entidad que representa los bienes físicos y reactivos químicos gestionados en el inventario del laboratorio.  |
|**Datos específicos**| Nombre del reactivo/insumo<br>Cantidad actual (stock disponible)<br>Umbral mínimo de alerta<br>Número de Lote<br>Unidad de Medida (ml, g, unidades)<br>Categoría<br>Ubicación de Almacenamiento<br>Fecha de Ingreso<br>Fecha de vencimiento.  |
|  |  |
|**Estabilidad**| Alta |
|**Comentarios**| - |

|**IRQ–04**|**Registro de Residuo Químico**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos  |
|**Requisitos asociados**| RF-11 Registro de Generación de Residuos Químicos.<br>RF-12 Generación de Reporte Mensual de Residuos. |
|**Descripción**| Entidad que documenta la generación de desechos químicos producidos en prácticas y análisis para su posterior consolidación en reportes normativos.  |
|**Datos específicos**| Fecha y hora de generación<br>Usuario responsable<br>Categoría/Clase de peligrosidad del residuo<br>Volumen exacto generado<br>Peso exacto generado.  |
|  |  |
|**Estabilidad**| Alta |
|**Comentarios**| - |

|**IRQ–05**|**Catálogo de Tipos de Análisis/Muestra**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-16 Gestión de Catálogos Clínicos |
|**Descripción**| Catálogo de tipos de análisis micológicos y tipos de muestra disponibles en el sistema. |
|**Datos específicos**| Nombre<br>Descripción<br>Indicaciones asociadas<br>Estado (Activo/Inactivo). |
|  |  |
|**Estabilidad**| Media |
|**Comentarios**| Soporta UC–DIAG-10 (Gestionar Tipos de Análisis y Muestra). |

|**IRQ–06**|**Movimiento de Inventario**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
|**Descripción**| Entidad que registra cada movimiento (ingreso, retiro, devolución) de insumos en el inventario. |
|**Datos específicos**| Tipo de movimiento (Ingreso/Retiro/Devolución)<br>Fecha<br>Cantidad<br>Lote afectado<br>Usuario responsable<br>Análisis o práctica asociada. |
|  |  |
|**Estabilidad**| Media |
|**Comentarios**| Soporta UC–LAB-07 (Consultar Trazabilidad de Movimientos). |

|**IRQ–07**|**Categoría de Residuo**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
|**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
|**Descripción**| Catálogo de categorías y clases de peligrosidad de los residuos químicos. |
|**Datos específicos**| Nombre<br>Clase de peligrosidad (Clase I, II, III)<br>Descripción<br>Instrucciones de almacenamiento. |
|  |  |
|**Estabilidad**| Media |
|**Comentarios**| Soporta UC–LAB-10 (Gestionar Categorías de Residuos). |

## 2.5 Requisitos Funcionales
|**RF-01**|**Agendamiento de Turnos vía Agente IA**|
|---|---|
|**Objetivos Asociados**| OBJ-01  |
|**Descripción**| El sistema debe permitir a los pacientes solicitar y agendar turnos interactuando con un Agente IA exclusivamente a través de la plataforma de mensajería WhatsApp. Tras concretar el agendamiento, el sistema debe enviar automáticamente un mensaje confirmando el turno, el cual incluirá la información necesaria para la visita. |
|**Comentarios**| - |

|**RF-02**|**Envío de Indicaciones Médicas**|
|---|---|
|**Objetivos Asociados**| OBJ-01 |
|**Descripción**| El sistema debe enviar al paciente las indicaciones correspondientes para su análisis a través del mismo chat de WhatsApp utilizado por el Agente IA. |
|**Comentarios**| Las indicaciones enviadas serán de carácter estático y estarán predefinidas en el sistema, aún así existirá la funcionalidad de editar las indicaciones. |

|**RF-03**|**Gestión de Reagendación automática**|
|---|---|
|**Objetivos Asociados**| OBJ-01  |
|**Descripción**| Ante la cancelación o liberación de un turno, el sistema debe notificar vía WhatsApp al paciente que posea el turno asignado más postergado (el más lejano en el calendario) para ofrecerle adelantar su cita. El paciente notificado dispondrá de un plazo estricto de horas para confirmar la reagendación. |
|**Comentarios**| - |

|**RF-04**|**Cancelación y Reprogramación de Turnos**|
|---|---|
|**Objetivos Asociados**| OBJ-01  |
|**Descripción**| El sistema debe permitir al paciente gestionar la reprogramación o cancelación de su turno asignado comunicándose con el Agente IA a través de WhatsApp. |
|**Comentarios**| - |

|**RF-05**|**Registro de Ficha Clínica**|
|---|---|
|**Objetivos Asociados**| OBJ-02  |
|**Descripción**| El sistema debe permitir al profesional médico registrar en un único paso los datos personales/demográficos del paciente junto con su información clínica estructurada al momento de la consulta.  |
|**Comentarios**| Almacena al paciente como un registro centralizado, agilizando la carga de datos sin necesidad de crearle un perfil de usuario <br>Garantiza la legibilidad y disponibilidad de los antecedentes para el análisis  |

|**RF-06**|**Actualización de Estados de Análisis Micológico**|
|---|---|
|**Objetivos Asociados**| OBJ-02 |
|**Descripción**| El sistema debe trazar el ciclo de vida de la muestra, permitiendo al usuario con rol de Bioquímico modificar los estados del análisis (pendiente, en proceso, terminado y validado). |
|**Comentarios**| Asegura el control de calidad al requerir que un profesional habilitado valide los resultados antes de que estos sean considerados definitivos  |

|**RF-07**|**Notificación de Disponibilidad de Resultados y OTP**|
|---|---|
|**Objetivos Asociados**| OBJ-03  |
|**Descripción**| Una vez validado el análisis, el sistema debe notificar al paciente vía WhatsApp enviando un enlace al portal web seguro, las instrucciones de descarga y un token OTP generado criptográficamente. Al expirar el TTL del OTP vigente (7 días) sin que el informe haya sido descargado, el sistema debe generar automáticamente un nuevo OTP (invalidando el anterior) y reenviar la notificación, repitiendo el ciclo hasta la descarga del informe. El reenvío manual queda disponible como mecanismo de respaldo ante fallas del proceso automático o solicitud del paciente. |
|**Comentarios**| Asegura el cumplimiento de la Ley de Protección de los Datos Personales (Ley 25.326)  |

|**RF-08**|**Validación de Identidad y Descarga de Informe**|
|---|---|
|**Objetivos Asociados**| OBJ-03  |
|**Descripción**| El portal web debe requerir el ingreso del token OTP provisto al paciente para validar su identidad y habilitar la descarga del informe de resultados en formato PDF.  |
|**Comentarios**| - |

|**RF-09**|**Alertas de Stock en Panel de Control**|
|---|---|
|**Objetivos Asociados**| OBJ-04  |
|**Descripción**| El sistema debe mostrar alertas visuales dentro del panel de control (dashboard) cuando el inventario de un reactivo alcance un umbral mínimo o se acerque a su fecha de vencimiento. |
|**Comentarios**| - |

|**RF-10**|**Gestión de Ingresos y Retiros de Inventario**|
|---|---|
|**Objetivos Asociados**| OBJ-04  |
|**Descripción**| El sistema debe permitir registrar tanto el ingreso de nuevos insumos como el retiro de reactivos solicitados por los profesores para las prácticas. |
|**Comentarios**| - |

|**RF-11**|**Registro de Generación de Residuos Químicos**|
|---|---|
|**Objetivos Asociados**| OBJ-05  |
|**Descripción**| El sistema debe permitir registrar el volumen y peso exacto de los residuos químicos producidos por cada actividad del laboratorio.  |
|**Comentarios**| Garantiza la recolección de los datos necesarios para cumplir con las normativas legales vigentes.  |

|**RF-12**|**Generación de Reporte Mensual de Residuos**|
|---|---|
|**Objetivos Asociados**| OBJ-05  |
|**Descripción**| El sistema debe consolidar los registros de desechos cargados en el mes y generar automáticamente un reporte de los residuos químicos. |
|**Comentarios**| - |

|**RF-13**|**Gestión de Cuentas y Autenticación**|
|---|---|
|**Objetivos Asociados**| Transversal  |
|**Descripción**| El sistema debe gestionar el registro, la modificación y la baja de cuentas de usuario, centralizando el proceso de autenticación en la plataforma. |
|**Comentarios**| Asegura que únicamente los individuos debidamente identificados puedan ingresar al sistema. |

|**RF-14**|**Registro Automático de Auditoría**|
|---|---|
|**Objetivos Asociados**| Transversal  |
|**Descripción**| El sistema debe registrar de manera automática y cronológica cada evento significativo o crítico, almacenando el usuario responsable, la fecha, la hora, la dirección IP y el cambio específico realizado. |
|**Comentarios**| - |

|**RF-15**|**Consolidación y Exportación de Datos Operativos**|
|---|---|
|**Objetivos Asociados**| Transversal  |
|**Descripción**| El sistema debe procesar, cruzar y permitir la exportación de los datos transaccionales generados (clínicos, de inventario y de desechos) para su visualización y análisis. |
|**Comentarios**| Facilita la toma de decisiones basada en datos operativos reales  |

|**RF-16**|**Gestión de Catálogos Clínicos**|
|---|---|
|**Objetivos Asociados**| OBJ-02  |
|**Descripción**| El sistema debe permitir al Administrador gestionar los tipos de análisis micológicos y tipos de muestra (crear, modificar, desactivar). |
|**Comentarios**| - |

|**RF-17**|**Gestión de Catálogos de Inventario**|
|---|---|
|**Objetivos Asociados**| OBJ-04, OBJ-05  |
|**Descripción**| El sistema debe permitir al Administrador gestionar las categorías de insumos, ubicaciones de almacenamiento y categorías de residuos. |
|**Comentarios**| - |

|**RF-18**|**Trazabilidad de Lotes y Vencimientos**|
|---|---|
|**Objetivos Asociados**| OBJ-04  |
|**Descripción**| El sistema debe permitir registrar lotes al ingresar insumos, con número de lote y fecha de vencimiento, y alertar sobre proximidad de vencimiento. El sistema debe consumir primero el lote con vencimiento más próximo al realizar un retiro. |
|**Comentarios**| Asegura la rotación de inventario y previene el uso de reactivos vencidos. |

|**RF-19**|**Registro de Disposición Final de Residuos**|
|---|---|
|**Objetivos Asociados**| OBJ-05  |
|**Descripción**| El sistema debe permitir registrar la salida y disposición final de los residuos acumulados, con fecha, responsable y método de tratamiento. |
|**Comentarios**| Asegura el cierre del ciclo de vida del residuo para cumplimiento normativo. |

|**RF-20**|**Modificación de Ficha Clínica**|
|---|---|
|**Objetivos Asociados**| OBJ-02  |
|**Descripción**| El sistema debe permitir al Bioquímico/Doctor modificar una ficha clínica registrada, manteniendo un historial de versiones. |
|**Comentarios**| Garantiza la trazabilidad de cambios en el historial clínico del paciente. |

|**RF-21**|**Cancelación de Análisis**|
|---|---|
|**Objetivos Asociados**| OBJ-02  |
|**Descripción**| El sistema debe permitir cancelar un análisis en curso (con motivo obligatorio) cuando esté en estado «Pendiente» o «En Proceso». |
|**Comentarios**| Evita que análisis no viables continúen su procesamiento y libera recursos del laboratorio. |

## 2.6 Requisitos No Funcionales
|**RNF-01**|**Disponibilidad Continua del Agente IA**|
|---|---|
|**Objetivos Asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos Asociados**| RF-01 Agendamiento de Turnos vía Agente IA  |
|**Descripción**| El servicio del Agente IA, encargado de la interacción asíncrona mediante la API de WhatsApp, debe operar con una disponibilidad de 24/7. El procesamiento de mensajes y solicitudes de turnos no se interrumpirá fuera del horario administrativo del laboratorio.  |

|**RNF-02**|**Expiración Estricta de Credenciales**|
|---|---|
|**Objetivos Asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos Asociados**| RF-07 Notificación de Disponibilidad de Resultados y OTP.<br>RF-08 Validación de Identidad y Descarga de Informe. |
|**Descripción**| Por motivos de seguridad y resguardo de la confidencialidad, el Token de un solo uso (OTP) generado criptográficamente para el acceso al portal web tendrá un Tiempo de Vida Útil (TTL) máximo de 7 días corridos desde el instante de su emisión. Superado este período, el sistema invalidará el token automáticamente.  |

|**RNF-03**|**Usabilidad y Diseño Responsivo**|
|---|---|
|**Objetivos Asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos Asociados**| RF-08 Validación de Identidad y Descarga de Informe  |
|**Descripción**| La interfaz gráfica del portal web seguro para la descarga de resultados debe estar desarrollada bajo el paradigma de diseño "Mobile-First". Debe garantizar una adaptabilidad responsiva completa, asegurando legibilidad, accesibilidad y correcta operatividad desde navegadores de dispositivos móviles. |

|**RNF-04**|**Respaldo y Retención Legal de Datos**|
|---|---|
|**Objetivos Asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos Asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| El sistema debe ejecutar rutinas de copia de seguridad (backup) automatizadas de la base de datos con una frecuencia diaria. Asimismo, la arquitectura de la base de datos debe garantizar la inmutabilidad y la retención de las historias clínicas y los análisis validados por un período mínimo legal de 10 años, en estricto cumplimiento con la normativa vigente sobre derechos del paciente.  |

|**RNF-05**|**Arquitectura y Despliegue Local**|
|---|---|
|**Objetivos Asociados**| Transversal (Infraestructura)  |
|**Requisitos Asociados**| Todos los requisitos.  |
|**Descripción**| La totalidad del sistema, incluyendo la base de datos, los archivos de la aplicación y los documentos generados (PDFs), debe estar alojada e implementada exclusivamente en los servidores físicos locales de la Universidad Nacional de Misiones (UNaM), sin depender de servicios de almacenamiento en la nube de terceros.  |

## 2.7 Casos de Uso
### 2.7.1 Diagramas de Casos de Uso
#### 2.7.1.1 Subsistema Gestión de Pacientes
Figura 1 - DCU Subsistema Gestión de Pacientes
#### 2.7.1.2 Subsistema Laboratorio Bioquímico
Figura 2 - DCU Subsistema Laboratorio Bioquímico
#### 2.7.1.3 Subsistema Recursos de Laboratorio
Figura 3 - DCU Subsistema Recursos de Laboratorio
#### 2.7.1.4 Subsistema Acceso y Seguridad
Figura 4 - DCU Subsistema Acceso y Seguridad
#### 2.7.1.5 Subsistema Reportes y Estadísticas
Figura 5 - DCU Subsistema Reportes y Estadísticas
### 2.7.2 Definición de Actores
|**ACT–01**|**Bioquímico / Doctor**|
|---|---|
|**Descripción**| Usuario del sistema encargado de la atención directa y el procesamiento clínico de las muestras. Posee permisos para registrar consumo de insumos del inventario y la generación de residuos. Gestiona el registro unificado del paciente y su ficha clínica al momento de la consulta, y es el responsable de registrar, actualizar, modificar, cancelar y validar todo el ciclo de vida de los análisis micológicos.  |
|**Comentarios**| - |

|**ACT–02**|**Profesor**|
|---|---|
|**Descripción**| Usuario del sistema perteneciente al ámbito académico. Su responsabilidad operativa radica en interactuar con el módulo de Recursos de Laboratorio para registrar los retiros y egresos físicos de insumos o reactivos destinados a las prácticas educativas. También registra la generación de residuos químicos producto de las prácticas educativas y puede consultar el inventario y la trazabilidad de movimientos.  |
|**Comentarios**| - |

|**ACT–03**|**Administrador**|
|---|---|
|**Descripción**| Usuario responsable de la gestión administrativa, logística y de seguridad del sistema. Sus funciones abarcan el registro de los ingresos al inventario de recursos, la gestión de catálogos del sistema (tipos de análisis, insumos, categorías, ubicaciones) y la gestión del control de acceso, autorizando cuentas y asignando los roles correspondientes. Además cumple la misma función que un Bioquímico, pudiendo gestionar análisis e inventario. |
|**Comentarios**| - |

|**ACT–04**|**Paciente**|
|---|---|
|**Descripción**| Actor externo que interactúa con el portal web seguro del sistema de forma anónima (sin poseer una cuenta de usuario registrada en la base de datos) y con el Agente IA via Whatsapp para la autogestión de su turno. En el portal de resultados su única acción es ingresar un token OTP para validar su identidad y descargar el informe de resultados de sus estudios.  |
|**Comentarios**| No posee credenciales de acceso al sistema principal ni interactúa con la interfaz de gestión interna del laboratorio.  |

### 2.7.3 Definición de Casos de Uso
#### 2.7.3.1 Subsistema Gestión de Pacientes
|**UC–REC-01**|**Agendar Turno**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA <br>RF-02 Envío de Indicaciones Médicas  |
|**Descripción**| El Paciente interactúa de manera asíncrona con el sistema, a través de WhatsApp, para solicitar y registrar un nuevo turno para análisis micológico. El Agente IA solicitará los datos demográficos elementales (DNI y Nombre Completo) para crear el registro inicial en la base de datos.  El Agente IA procesa la solicitud, consulta la disponibilidad en la agenda y concreta la asignación.  |
|**Precondición**| El paciente debe comunicarse vía WhatsApp<br>El sistema debe contar con disponibilidad de fechas y horarios en la agenda del laboratorio  |
|**Postcondiciones**| El turno queda registrado y reservado en el sistema a nombre del paciente. <br>El sistema envía automáticamente, en el mismo hilo de chat, un mensaje de confirmación del turno.<br>El sistema envía automáticamente las indicaciones médicas predefinidas correspondientes al análisis.<br>El sistema programa automáticamente en cola el envío de un mensaje recordatorio de asistencia para el paciente, a ejecutarse en la ventana de tiempo previa configurada.   |

|**UC–REC-02**|**Cancelar Turno**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos <br>RF-03 Gestión de Reagendación automática  |
|**Descripción**| El Paciente solicita la anulación de un turno previamente agendado interactuando con el Agente IA mediante WhatsApp.  |
|**Precondición**| El paciente debe tener un turno asignado y vigente (no vencido) en el sistema.  |
|**Postcondiciones**| El estado del turno cambia a "Cancelado" y el bloque de tiempo queda liberado en la agenda<br>El sistema emite un mensaje confirmando la cancelación exitosa. <br>Se dispara automáticamente el proceso interno de "Reasignación Automática de Turno Liberado" (UC-REC-04) para aprovechar el espacio.  |

|**UC–REC-03**|**Reprogramar Turno**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención. |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos.<br>RF-03 Gestión de Reagendación automática. |
|**Descripción**| El Paciente solicita cambiar la fecha y/o la hora de un turno asignado comunicándose con el Agente IA a través de WhatsApp.  |
|**Precondición**| El paciente debe tener un turno asignado en el sistema.<br>El sistema debe contar con disponibilidad en la agenda para la nueva fecha/hora solicitada. |
|**Postcondiciones**| El turno original del paciente queda liberado y se le asigna el nuevo bloque de tiempo.<br>El sistema envía un mensaje con la confirmación de la nueva fecha y hora.<br>La liberación del turno original dispara automáticamente el proceso interno de "Reasignación Automática de Turno Liberado" (UC-REC-04).  |

|**UC–REC-04**|**Reasignación Automática de Turno Liberado**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención. |
|**Requisitos asociados**| RF-03 Gestión de Reagendación automática. |
|**Descripción**| Proceso del sistema que se activa al liberarse un espacio en la agenda (por cancelación o reprogramación). El sistema busca automáticamente al paciente que posea el turno asignado más postergado y le notifica vía WhatsApp ofreciéndole adelantar su cita. Si este no responde en el plazo estricto o rechaza, el sistema iterará ofreciendo el turno al siguiente paciente más lejano.  |
|**Precondición**| Un turno debe haber sido cancelado o liberado. <br>Deben existir pacientes con turnos asignados en fechas posteriores a la fecha del turno que se acaba de liberar. |
|**Postcondiciones**|**Si el paciente acepta en tiempo:**Se reprograma su turno a la nueva fecha, enviando confirmación. El turno lejano que dejó vacante se libera, disparando recursivamente este mismo caso de uso.<br>**Si el paciente rechaza o expira el plazo estricto:**El sistema registra la negativa u omisión y envía la oferta de turno al siguiente paciente con el turno más postergado.  |

|**UC–REC-05**|**Consultar Turno**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA. |
|**Descripción**| El Paciente interactúa con el Agente IA a través de WhatsApp para verificar el estado, la fecha y la hora de sus turnos vigentes, o para volver a solicitar las indicaciones médicas de preparación para el estudio.  |
|**Precondición**| El paciente debe poseer al menos un turno vigente registrado en el sistema asociado a su número de teléfono.  |
|**Postcondiciones**| El Agente IA emite un mensaje con el resumen detallado de los turnos activos del paciente y reenvía las indicaciones médicas correspondientes si es requerido. El estado del sistema y del turno no sufren modificaciones (operación de solo lectura).  |

|**UC–REC-06**|**Consultar Agenda**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos  |
|**Descripción**| El personal clínico o administrativo accede al calendario interno del sistema para visualizar, planificar o gestionar (de ser necesario) los turnos asignados a los pacientes para la toma de muestras o consultas.  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |
|**Postcondiciones**| El sistema presenta la grilla de turnos (vista diaria, semanal o mensual) con capacidades de filtrado opcional (por paciente, estado del turno). Operación de lectura con habilitación de acciones de gestión directa.  |

|**UC–REC-07**|**Configurar Parámetros de Agenda**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA  |
|**Descripción**| El Administrador define los parámetros generales de la agenda del laboratorio, incluyendo los días y horarios hábiles de atención, la duración estándar de los turnos, la cantidad máxima de turnos por franja horaria y los períodos de receso o inhábiles.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |
|**Postcondiciones**| Los parámetros de configuración quedan almacenados en el sistema y son aplicados para el cálculo de disponibilidad horaria del Agente IA.  |

|**UC–REC-08**|**Bloquear/Desbloquear Días y Franjas Horarias**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos  |
|**Descripción**| El Administrador bloquea o desbloquea días completos o franjas horarias específicas en la agenda del laboratorio, inhabilitando temporalmente la asignación de turnos en esos períodos.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |
|**Postcondiciones**| Los días o franjas seleccionados quedan marcados como NO DISPONIBLES en la agenda. El Agente IA no ofrecerá esos horarios al momento de agendar.  |


|**UC–REC-10**|**Crear Indicación Médica**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas  |
|**Descripción**| El Bioquímico/Doctor o Administrador crea una nueva indicación médica predefinida en el sistema para ser enviada automáticamente al paciente al momento de agendar un turno.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador.  |
|**Postcondiciones**| La nueva indicación médica queda registrada en el sistema y disponible para ser asignada a futuros turnos.  |

|**UC–REC-11**|**Modificar Indicación Médica**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas  |
|**Descripción**| El Bioquímico/Doctor o Administrador modifica el contenido de una indicación médica predefinida existente en el sistema.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. Debe existir al menos una indicación médica registrada.  |
|**Postcondiciones**| La indicación médica queda actualizada con el nuevo contenido en la base de datos.  |

|**UC–REC-12**|**Eliminar Indicación Médica**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas  |
|**Descripción**| El Bioquímico/Doctor o Administrador elimina lógicamente una indicación médica predefinida del sistema, desactivándola para que no sea enviada en futuros turnos.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. Debe existir al menos una indicación médica registrada.  |
|**Postcondiciones**| La indicación médica queda marcada como INACTIVA en la base de datos.  |

|**UC–REC-13**|**Consultar Indicaciones Médicas**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas  |
|**Descripción**| El Bioquímico/Doctor o Administrador visualiza el listado completo de indicaciones médicas predefinidas registradas en el sistema, con su contenido y estado actual.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador.  |
|**Postcondiciones**| El sistema presenta el listado paginado de indicaciones médicas. Operación de solo lectura.  |

|**UC–REC-14**|**Cancelar Turno por Vencimiento**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos  |
|**Descripción**| Proceso automático del sistema que se ejecuta diariamente al cierre del horario de atención. Identifica todos los turnos cuyo horario ya transcurrió, que no fueron atendidos ni cancelados, y los marca como "No Asistió", liberando los recursos asociados.  |
|**Precondición**| Debe existir al menos un turno con fecha/hora vencida en estado "Confirmado" o "Pendiente".  |
|**Postcondiciones**| El estado del turno cambia a "No Asistió". El bloque horario queda liberado en la agenda. Se dispara UC-REC-04 para reasignar el espacio liberado.  |

|**UC–REC-15**|**Registrar Asistencia a Turno**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos  |
|**Descripción**| El Bioquímico/Doctor o Administrador registra la asistencia o inasistencia del paciente a su turno programado al momento de presentarse en el laboratorio.  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador. El paciente debe tener un turno en estado "Confirmado" para el día y hora actual.  |
|**Postcondiciones**| Si asiste: el estado del turno cambia a "Atendido" y se habilita el flujo para iniciar la consulta. Si no asiste: el estado del turno cambia a "No Asistió", el bloque horario se libera y se dispara UC-REC-04.  |

|**UC–REC-16**|**Registrar Paciente**|
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |
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
|**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). |

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
|**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Se realiza baja lógica para mantener integridad referencial. |

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

|**UC–REC-S-01**|**Buscar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre o Apellido) y retorna el/los paciente(s) coincidente(s) al caso de uso invocante. |
|**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |
|**Postcondiciones**| Los datos del paciente seleccionado son retornados al caso de uso invocante para continuar su flujo. |
|**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. |

#### 2.7.3.2 Subsistema Laboratorio Bioquímico
|**UC–DIAG-01**|**Registrar Ficha Clínica**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| El Bioquímico/Doctor ingresa al sistema durante la consulta presencial para completar la información clínica estructurada del paciente, enlazándola con los datos demográficos previamente cargados por el Agente IA.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.<br>El paciente debe poseer un registro básico en el sistema (Alta Temprana).   |
|**Postcondiciones**| Se genera y almacena la Ficha Clínica estructurada vinculada de forma unívoca al paciente. <br>El historial clínico queda disponible para la carga de futuros análisis micológicos.  |
|**Comentarios**| Incluye `<<extend>>` a UC–DIAG-07 (Modificar Ficha Clínica). |

|**UC–DIAG-02**|**Registrar Ingreso de Muestra**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |
|**Descripción**| El Bioquímico/Doctor registra en el sistema la recepción física de la muestra microbiológica del paciente, indicando el tipo de análisis a realizar e iniciando la trazabilidad del estudio.  |
|**Precondición**| El paciente debe contar con una Ficha Clínica registrada previamente en el sistema (no necesariamente en la sesión actual). <br>El usuario debe tener una sesión activa con el rol correspondiente.  |
|**Postcondiciones**| Se crea un nuevo registro de Análisis Micológico asociado a la Ficha Clínica del paciente.<br>El estado inicial del análisis se establece automáticamente en "Pendiente".   |

|**UC–DIAG-03**|**Actualizar Estado de Análisis**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |
|**Descripción**| El Bioquímico/Doctor ingresa al módulo clínico para cargar los resultados parciales u observaciones obtenidos durante el procesamiento de la muestra y avanza el estado del estudio en el flujo de trabajo.  |
|**Precondición**| Debe existir un Análisis Micológico en estado "Pendiente" o "En Proceso".  |
|**Postcondiciones**| Los parámetros, observaciones y resultados parciales quedan guardados en la base de datos. <br>El estado del análisis cambia a "En Proceso" o "Terminado", según la selección del usuario.  |

|**UC–DIAG-04**|**Validar Análisis**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis.<br>OBJ-03 Emisión Segura y Descarga de Resultados. |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.<br>RF-08 Validación de Identidad y Descarga de Informe. |
|**Descripción**| El Bioquímico da por concluido el estudio al emitir su diagnóstico final y aprobar los resultados mediante el sistema, cerrando así el ciclo clínico de la muestra.  |
|**Precondición**| El Análisis Micológico debe encontrarse en estado "Terminado".<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.  |
|**Postcondiciones**| El estado del análisis cambia permanentemente a "Validado". <br>El sistema compila estáticamente los datos y genera de inmediato el Informe de Resultados en formato PDF, almacenándolo en el servidor seguro. <br>El sistema genera criptográficamente un Token OTP asociado al análisis y envía automáticamente un mensaje de WhatsApp al paciente con el enlace al portal web, las instrucciones y el Token OTP. <br>El sistema programa automáticamente el reenvío de un nuevo Token OTP al expirar el TTL del Token vigente (7 días, RNF-02) mientras el Informe no haya sido descargado, invalidando el Token anterior en cada ciclo. El reenvío automático es una postcondición del caso de uso; el reenvío manual queda como mecanismo de respaldo.  |

|**UC–DIAG-05**|**Descargar Informe**|
|---|---|
|**Objetivos asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos asociados**| RF-08 Validación de Identidad y Descarga de Informe  |
|**Descripción**| El Paciente, actuando de forma anónima desde el navegador web, ingresa al portal seguro del laboratorio e introduce el código provisto por WhatsApp para acceder a su documento.  |
|**Precondición**| El sistema debe tener el PDF almacenado y un Token OTP válido (no expirado/no usado) asociado a ese informe.  |
|**Postcondiciones**| El sistema coteja el OTP; si es exitoso, autoriza la sesión temporal.<br>Se inicia la descarga segura del Informe de Resultados en formato PDF en el dispositivo del paciente. <br>El Token OTP queda invalidado para prevenir múltiples usos posteriores.  |

|**UC–DIAG-06**|**Consultar Historial de Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| El personal autorizado accede al repositorio centralizado para buscar y visualizar el historial médico acumulado de un paciente, sus consultas previas y los estados de sus análisis micológicos.  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |
|**Postcondiciones**| El sistema muestra el listado paginado de pacientes y sus respectivas fichas clínicas, permitiendo la búsqueda mediante filtros opcionales (DNI, Nombre, Rango de Fechas). Operación de solo lectura.  |

|**UC–DIAG-07**|**Modificar Ficha Clínica**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-20 Modificación de Ficha Clínica |
|**Descripción**| El Bioquímico/Doctor modifica una ficha clínica previamente registrada, corrigiendo errores o agregando información complementaria. |
|**Precondición**| La ficha clínica debe existir y no estar asociada a un análisis en estado «Validado». |
|**Postcondiciones**| Los cambios quedan registrados. Se almacena una versión histórica de la ficha original (audit trail de modificaciones). |
|**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Cuando el análisis ya fue validado, la modificación se restringe a campos no clínicos (ej. observaciones administrativas). |

|**UC–DIAG-08**|**Cancelar Análisis**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-21 Cancelación de Análisis |
|**Descripción**| El Bioquímico/Doctor cancela un análisis micológico en curso, registrando el motivo. |
|**Actor**| Bioquímico/Doctor, Administrador |
|**Precondición**| El análisis debe existir y estar en estado «Pendiente» o «En Proceso» (no «Validado»). |
|**Postcondiciones**| El estado del análisis cambia a «Cancelado». Se registra el motivo obligatorio de cancelación. El análisis cancelado permanece en el historial del paciente. |

|**UC–DIAG-09**|**Consultar Panel de Análisis**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico |
|**Descripción**| El Bioquímico/Doctor accede a un panel de trabajo que lista todos los análisis micológicos, filtrables por estado, tipo de análisis, fecha y bioquímico asignado, sin necesidad de navegar paciente por paciente. |
|**Precondición**| Sesión activa con rol autorizado. |
|**Postcondiciones**| El sistema presenta una tabla paginada y filtrable de análisis. Operación de solo lectura. Desde este panel se puede acceder al detalle de cada análisis y ejecutar acciones (actualizar estado, validar, cancelar). |
|**Comentarios**| Diferente de DIAG-06 (que muestra el historial de un paciente). Este UC muestra el volumen de trabajo del laboratorio. |

|**UC–DIAG-10**|**Gestionar Tipos de Análisis y Muestra**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-16 Gestión de Catálogos Clínicos |
|**Descripción**| El Administrador gestiona el catálogo de tipos de análisis micológicos y tipos de muestra disponibles en el sistema (crear, modificar, desactivar). |
|**Actor**| Administrador |
|**Precondición**| Sesión activa con rol de Administrador. |
|**Postcondiciones**| El catálogo queda actualizado. Los tipos desactivados no pueden seleccionarse en nuevos análisis, pero se preservan en registros históricos. |
|**Comentarios**| Incluye sub-flujos: Crear Tipo, Modificar Tipo, Desactivar Tipo (baja lógica). |

#### 2.7.3.3 Subsistema Recursos de Laboratorio
|**UC–LAB-01**|**Registrar Ingreso de Insumos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario  |
|**Descripción**| El Administrador accede al módulo de inventario para registrar la entrada de nuevos reactivos e insumos físicos al laboratorio, actualizando las existencias disponibles.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |
|**Postcondiciones**| El stock del insumo o reactivo seleccionado se incrementa en la cantidad especificada en la base de datos.<br>Se registra el movimiento en el historial de trazabilidad del inventario.   |

|**UC–LAB-02**|**Registrar Retiro de Insumos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario.<br>RF-09 Alertas de Stock en Panel de Control. |
|**Descripción**| El Profesor o el Bioquímico registran el consumo o retiro de reactivos necesarios para las prácticas educativas o los análisis clínicos, deduciendo inmediatamente las cantidades del inventario. El sistema debe registrar el análisis micológico o la práctica educativa a la que se destina el retiro (trazabilidad), el lote del insumo consumido (FIFO/FEFO), la ubicación de almacenamiento de origen, y si corresponde a la disposición final de un residuo.  |
|**Precondición**| El usuario debe tener una sesión activa con los permisos correspondientes (Profesor, Bioquímico o Administrador). <br>El sistema debe contar con stock disponible igual o mayor a la cantidad que se desea retirar.  |
|**Postcondiciones**| El sistema deduce de forma directa e inmediata la cantidad solicitada del stock activo. <br>Si el stock restante alcanza el umbral mínimo configurado o se acerca a la fecha de vencimiento, el sistema dispara y muestra una alerta visual en el dashboard. |

|**UC–LAB-03**|**Registrar Generación de Residuos**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos. |
|**Requisitos asociados**| RF-11 Registro de Generación de Residuos Químicos. |
|**Descripción**| Tras una actividad de laboratorio o práctica educativa, el Profesor o el Bioquímico ingresan al sistema para asentar el volumen y peso de los desechos químicos producidos.  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Profesor, Bioquímico o Administrador.  |
|**Postcondiciones**| Los datos exactos del residuo generado (volumen y peso) quedan registrados y vinculados a la fecha y al usuario responsable.  |

|**UC–LAB-04**|**Generar Reporte de Residuos**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos  |
|**Requisitos asociados**| RF-12 Generación de Reporte Mensual de Residuos  |
|**Descripción**| El sistema procesa y consolida automáticamente los registros de desechos cargados durante el mes en curso para generar el documento estructurado exigido por las normativas vigentes.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |
|**Postcondiciones**| Se emite un documento (reporte) que detalla las cantidades y tipos de residuos químicos generados en el mes.  |

|**UC–LAB-05**|**Consultar Inventario**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario   |
|**Descripción**| Los usuarios internos acceden al módulo de recursos para visualizar el listado completo de reactivos e insumos físicos disponibles en el laboratorio, conociendo las cantidades exactas y sus estados.  |
|**Precondición**| El usuario debe tener una sesión activa (Administrador, Bioquímico/Doctor o Profesor).  |
|**Postcondiciones**| El sistema despliega una vista paginada del inventario actual, permitiendo aplicar filtros opcionales (por nombre, tipo o insumos próximos a vencer/agotar). Operación de solo lectura sin alteración de datos.  |

|**UC–LAB-06**|**Gestionar Catálogo de Insumos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
|**Descripción**| El Administrador gestiona el catálogo de tipos de insumos y reactivos: crear, modificar y desactivar (baja lógica). |
|**Actor**| Administrador |
|**Precondición**| Sesión activa con rol de Administrador. |
|**Postcondiciones**| El catálogo queda actualizado. Los insumos desactivados no pueden recibir nuevos ingresos o retiros, pero sus movimientos históricos se preservan. |
|**Comentarios**| Datos del insumo: nombre, descripción, unidad de medida (ml, g, unidades), categoría, umbral mínimo de alerta, ubicación de almacenamiento. |

|**UC–LAB-07**|**Consultar Trazabilidad de Movimientos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
|**Descripción**| El usuario autorizado consulta el historial completo de movimientos (ingresos, retiros, devoluciones) de un insumo o de todos los insumos en un rango de fechas. |
|**Actor**| Administrador, Bioquímico/Doctor, Profesor |
|**Precondición**| Sesión activa con rol autorizado. |
|**Postcondiciones**| El sistema presenta una tabla cronológica de movimientos con: fecha, tipo de movimiento, usuario, cantidad, lote afectado, y análisis/práctica asociada. Operación de solo lectura. |
|**Comentarios**| Filtrable por insumo, tipo de movimiento, rango de fechas, usuario. |

|**UC–LAB-08**|**Configurar Umbrales de Alerta**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-09 Alertas de Stock en Panel de Control |
|**Descripción**| El Administrador configura los umbrales mínimos de stock y los días de anticipación para alertas de vencimiento de cada insumo. |
|**Actor**| Administrador |
|**Precondición**| Sesión activa con rol de Administrador. El insumo debe existir en el catálogo. |
|**Postcondiciones**| Los umbrales quedan configurados. El dashboard reflejará alertas cuando el stock esté por debajo del umbral o un lote esté dentro del período de pre-vencimiento. |
|**Comentarios**| Umbrales por defecto: stock mínimo = 1 unidad, alerta de vencimiento = 30 días. El Administrador puede sobrescribirlos por insumo. |

|**UC–LAB-09**|**Registrar Devolución de Insumos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario |
|**Descripción**| El Profesor o Bioquímico registra la devolución de insumos no utilizados al inventario, revirtiendo total o parcialmente un retiro previo. |
|**Actor**| Profesor, Bioquímico/Doctor, Administrador |
|**Precondición**| Debe existir un retiro previo registrado. La cantidad a devolver no puede superar la cantidad retirada. |
|**Postcondiciones**| El stock del insumo se incrementa en la cantidad devuelta. Se registra el movimiento como «Devolución» vinculado al retiro original. |
|**Comentarios**| Si el lote original ya venció, el sistema advierte y la devolución se registra como «Vencido — no utilizable». |

|**UC–LAB-10**|**Gestionar Categorías de Residuos**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
|**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
|**Descripción**| El Administrador gestiona el catálogo de categorías/clases de peligrosidad de residuos químicos (crear, modificar, desactivar). |
|**Actor**| Administrador |
|**Precondición**| Sesión activa con rol de Administrador. |
|**Postcondiciones**| El catálogo queda actualizado. Las categorías desactivadas no pueden seleccionarse en nuevos registros de residuos. |
|**Comentarios**| Datos de la categoría: nombre, clase de peligrosidad (ej. Clase I, II, III), descripción, instrucciones de almacenamiento. |

|**UC–LAB-11**|**Consultar y Modificar Registro de Residuos**|
|---|---|
|**Objetivos asociados**| OBJ-05 Sistematización del Registro de Residuos Químicos |
|**Requisitos asociados**| RF-11 Registro de Generación de Residuos Químicos |
|**Descripción**| El usuario autorizado consulta el historial de residuos generados en un período y, si es necesario, corrige un registro erróneo (antes de que se consolide en el reporte mensual). |
|**Actor**| Administrador, Bioquímico/Doctor, Profesor |
|**Precondición**| Sesión activa con rol autorizado. El registro a modificar no debe haber sido incluido en un reporte mensual ya emitido. |
|**Postcondiciones**| Los datos del residuo quedan actualizados. Se registra la modificación en auditoría. |
|**Comentarios**| Sub-flujos: Consultar (listado filtrable por fecha, categoría, usuario), Modificar (solo el autor o Administrador). |

|**UC–LAB-12**|**Gestionar Categorías de Insumos**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-17 Gestión de Catálogos de Inventario |
|**Descripción**| El Administrador gestiona el catálogo de categorías de insumos (reactivos, medios de cultivo, materiales descartables, equipos). |
|**Actor**| Administrador |
|**Precondición**| Sesión activa con rol de Administrador. |
|**Postcondiciones**| El catálogo queda actualizado. Los insumos pueden clasificarse por categoría. |
|**Comentarios**| Facilita filtros en consultas de inventario (LAB-05) y reportes (LAB-13). |

|**UC–LAB-13**|**Generar Reporte de Inventario**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario.<br>RF-09 Alertas de Stock en Panel de Control |
|**Descripción**| El Administrador genera un reporte del estado del inventario en un momento dado, incluyendo stock actual, movimientos del período, insumos bajo umbral y próximos a vencer. |
|**Actor**| Administrador, Bioquímico/Doctor |
|**Precondición**| Sesión activa con rol autorizado. |
|**Postcondiciones**| El sistema emite un reporte en formato PDF o CSV con el resumen del inventario. |
|**Comentarios**| Complementa a LAB-05 (consulta en pantalla) con una versión exportable para auditorías o planificación de compras. |

#### 2.7.3.4 Subsistema Acceso y Seguridad
|**UC–SEG-01**|**Iniciar Sesión**|
|---|---|
|**Objetivos asociados**| Transversal (Seguridad Operativa)  |
|**Requisitos asociados**| RF-13 Gestión de Cuentas y Autenticación  |
|**Descripción**| El usuario del sistema (Administrador, Bioquímico/Doctor o Profesor) ingresa sus credenciales de acceso para autenticarse en la plataforma web de gestión.  |
|**Precondición**| El usuario debe poseer una cuenta registrada y en estado "Activo" (sin baja lógica) en el sistema.  |
|**Postcondiciones**| El sistema valida las credenciales y redirige al usuario al panel principal (dashboard) con las opciones habilitadas según su rol predefinido.  |

|**UC–SEG-02**|**Administrar Usuario y Roles**|
|---|---|
|**Objetivos asociados**| Transversal (Seguridad Operativa)  |
|**Requisitos asociados**| RF-13 Gestión de Cuentas y Autenticación  |
|**Descripción**| El Administrador gestiona el control de acceso a la plataforma. Permite registrar nuevos usuarios, asignarles uno de los roles prefijados en el sistema y aplicar "Bajas Lógicas" (desactivaciones) a personal que ya no pertenece al laboratorio.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |
|**Postcondiciones**| Los datos de acceso del usuario quedan registrados, modificados o invalidados para futuros inicios de sesión.  |

|**UC–SEG-03**|**Cerrar Sesión**|
|---|---|
|**Objetivos asociados**| Transversal (Seguridad Operativa)  |
|**Requisitos asociados**| RF-13 Gestión de Cuentas y Autenticación  |
|**Descripción**| El usuario finaliza de manera explícita su sesión activa en la plataforma para proteger la confidencialidad de la estación de trabajo.  |
|**Precondición**| El usuario debe poseer una sesión activa en el sistema.  |
|**Postcondiciones**| El sistema invalida la sesion, cerrando el acceso a las pantallas internas y redirigiendo al usuario a la pantalla de inicio de sesión.  |

#### 2.7.3.5 Subsistema Reportes y Estadísticas
|**UC-REP-01**|**Consolidar y Exportar Datos Operativos**|
|---|---|
|**Objetivos asociados**| Transversal (Generación de Información)  |
|**Requisitos asociados**| RF-15 Consolidación y Exportación de Datos Operativos  |
|**Descripción**| El sistema procesa los datos transaccionales acumulados para estructurar análisis estadísticos. Permite cruzar información clínica, de inventario y de desechos, y exportarla como base para trabajos de investigación académica o auditorías.  |
|**Precondición**| El usuario debe tener una sesión activa con los privilegios necesarios (Bioquímico/Doctor o Administrador). <br>Deben existir datos transaccionales previos registrados en la plataforma.  |
|**Postcondiciones**| El sistema emite un conjunto de datos consolidado para su visualización y permite su descarga en formato compatible para análisis externo (exportación).  |

## 2.8 Casos de Uso Extendidos
### 2.8.1 Subsistema Gestión de Pacientes
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
|  | 8 | El sistema programa en cola el envío de un recordatorio de asistencia.  |
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

|**UCE–REC-02**|**Cancelar Turno**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos<br>RF-03 Gestión de Reagendación automática  |  |
|**Descripción**| El Paciente solicita la anulación de un turno previamente agendado interactuando con el Agente IA mediante WhatsApp.  |  |
|**Precondición**| El paciente debe tener un turno asignado y vigente en el sistema <br>La solicitud debe realizarse con más de 24 horas de antelación al turno  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El paciente solicita la cancelación al Agente IA.  |
|  | 2 | El Agente solicita el DNI para listar los turnos vigentes.  |
|  | 3 | El paciente responde con el DNI y selecciona el turno a cancelar.  |
|  | 4 | El sistema cambia el estado del turno a "Cancelado" y libera el bloque en la agenda.  |
|  | 5 | El sistema emite un mensaje confirmando la cancelación exitosa.  |
|  | 6 | Se dispara internamente el caso de uso UC-REC-04.  |
|**Postcondición**| El estado del turno cambia a "Cancelado" y el espacio queda liberado.  |  |
|**Excepciones**|**Paso**|  |
|  | 1 | Si el turno es dentro de las próximas 24 horas, el sistema informa la imposibilidad de cancelación por políticas del laboratorio y aborta el flujo.  |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo. |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-03**|**Reprogramar Turno**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos <br>RF-03 Gestión de Reagendación automática  |  |
|**Descripción**| El Paciente solicita cambiar la fecha y/o la hora de un turno asignado comunicándose con el Agente IA a través de WhatsApp.  |  |
|**Precondición**| El paciente debe tener un turno asignado en el sistema <br>Faltan más de 24 horas para la cita original.<br>El turno no fue reprogramado más de 2 veces previas. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El paciente solicita reprogramar su turno. |
|  | 2 | El Agente IA valida las políticas y muestra los turnos asociados al DNI.  |
|  | 3 | El paciente selecciona el turno.  |
|  | 4 | El Agente IA muestra la nueva disponibilidad horaria y bloquea las opciones (10 min).  |
|  | 5 | El paciente elige la nueva fecha/hora.  |
|  | 6 | El sistema actualiza el registro y libera el turno original.  |
|  | 7 | El sistema envía confirmación de la nueva fecha.  |
|  | 8 | Se dispara internamente el caso de uso UC-REC-04.  |
|**Postcondición**| El turno original del paciente queda liberado y se le asigna el nuevo bloque.  |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si el turno está a menos de 24 hs, o ya se reprogramó 2 veces, el sistema informa el rechazo por políticas internas y finaliza la acción.  |
|  | 5 | Si hay Timeout (10 min) en la elección, el sistema cancela el flujo sin modificar el turno original.  |
|**Rendimiento**|**Paso**|  |
|  | 6 | 1 segundo |
|**Frecuencia**| Media a Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-04**|**Reasignación Automática de Turno Liberado**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-03 Gestión de Reagendación automática  |  |
|**Descripción**| Proceso del sistema que se activa al liberarse un espacio. Busca automáticamente al paciente con el turno asignado más postergado y le ofrece adelantar su cita.  |  |
|**Precondición**| Un turno debe haber sido cancelado o liberado. <br>Deben existir pacientes con turnos en fechas posteriores.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El sistema busca en base de datos al paciente con el turno más lejano válido.  |
|  | 2 | El sistema valida que el horario actual no se encuentre en la ventana nocturna (22:00 a 08:00).  |
|  | 3 | El Agente IA envía un mensaje ofreciendo el nuevo turno.  |
|  | 4 | Inicia el temporizador de 2 horas para respuesta.  |
|  | 5 | El paciente acepta la oferta.  |
|  | 6 | El sistema reprograma el turno y libera el espacio lejano vacante.  |
|  | 7 | Se dispara recursivamente este mismo caso de uso.  |
|**Postcondición**| Se reprograma el turno a la nueva fecha, enviando confirmación.  |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si es horario nocturno, el sistema pausa la ejecución y programa el envío del mensaje para las 08:00 AM del día siguiente.  |
|  | 5 | Si el paciente rechaza o expira el plazo (2 horas), el sistema registra la negativa y reenvía la oferta al siguiente paciente lejano.  |
|**Rendimiento**|**Paso**|  |
|  | 1 | Menos de 3 segundos  |
|**Frecuencia**| Media |  |
|**Estabilidad**| Media |  |
|**Comentarios**| - |  |

|**UCE–REC-05**|**Consultar Turno**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA  |  |
|**Descripción**| El Paciente interactúa con el Agente IA para verificar el estado de sus turnos vigentes o volver a solicitar las indicaciones médicas.  |  |
|**Precondición**| El paciente debe poseer al menos un turno vigente registrado.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El paciente solicita información de sus turnos. |
|  | 2 | El Agente IA solicita el DNI de validación.  |
|  | 3 | El sistema recupera de la base de datos la información asociada.  |
|  | 4 | El Agente IA emite el resumen detallado y reenvía las indicaciones médicas.  |
|**Postcondición**| - |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si el DNI ingresado no posee turnos vigentes, el Agente IA informa la inexistencia de registros activos y ofrece agendar uno nuevo.  |
|**Rendimiento**|**Paso**|  |
|  | 3 | 1 Segundo |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-06**|**Consultar Agenda**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención  |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos. |  |
|**Descripción**| El personal clínico o administrativo accede al calendario interno del sistema para visualizar, planificar o gestionar los turnos asignados.  |  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Gestión de Agenda en la interfaz web.  |
|  | 2 | El sistema consulta la base de datos y recupera los bloques horarios ocupados y libres.  |
|  | 3 | El sistema renderiza la grilla de turnos (vista diaria/semanal/mensual).  |
|  | 4 | El usuario aplica filtros (DNI, estado) si lo requiere.  |
|**Postcondición**| - |  |
|**Excepciones**|**Paso**|  |
|  | - | - |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 2 segundos |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-07**|**Configurar Parámetros de Agenda**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA |  |
|**Descripción**| El Administrador define los parámetros generales de la agenda del laboratorio, incluyendo los días y horarios hábiles de atención, la duración estándar de los turnos, la cantidad máxima de turnos por franja horaria y los períodos de receso o inhábiles. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Administrador ingresa al módulo de Gestión de Agenda y selecciona "Configuración". |
|  | 2 | La interfaz despliega el formulario de configuración con los valores actuales. |
|  | 3 | El Administrador define los días hábiles (ej. lunes a viernes) y horarios de atención (ej. 08:00 a 12:00 y 14:00 a 18:00). |
|  | 4 | El Administrador configura la duración estándar del turno (ej. 30 minutos) y el intervalo entre turnos. |
|  | 5 | El Administrador define los períodos de receso o inhábiles (feriados fijos, receso académico). |
|  | 6 | El Administrador presiona "Guardar Configuración". |
|  | 7 | El sistema valida que los horarios y duraciones sean consistentes y persiste los cambios. |
|  | 8 | El sistema registra el evento en la tabla de auditoría. |
|  | 9 | La interfaz muestra un mensaje de "Configuración guardada exitosamente". |
|**Postcondición**| Los parámetros de agenda quedan almacenados y aplicados al cálculo de disponibilidad del Agente IA. |  |
|**Excepciones**|**Paso**|  |
|  | 7 | Si los horarios ingresados son inconsistentes (ej. hora de fin menor a hora de inicio), el sistema muestra una alerta de validación y no persiste los cambios. |
|**Rendimiento**|**Paso**|  |
|  | 7 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-08**|**Bloquear/Desbloquear Días y Franjas Horarias**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-01 Agendamiento de Turnos vía Agente IA.<br>RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| El Administrador bloquea o desbloquea días completos o franjas horarias específicas en la agenda del laboratorio, inhabilitando temporalmente la asignación de turnos en esos períodos. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Administrador ingresa al calendario y selecciona la opción "Bloquear Día/Franja". |
|  | 2 | La interfaz muestra el calendario mensual con los turnos existentes. |
|  | 3 | El Administrador selecciona el día o rango de fechas a bloquear. |
|  | 4 | El Administrador elige si bloquea el día completo o una franja horaria específica. |
|  | 5 | El Administrador ingresa el motivo del bloqueo y presiona "Confirmar Bloqueo". |
|  | 6 | El sistema valida que no existan turnos activos en el período seleccionado. |
|  | 7 | El sistema marca los bloques como NO DISPONIBLES en la agenda. |
|  | 8 | El sistema registra el evento en la tabla de auditoría. |
|**Postcondición**| Los días o franjas seleccionados quedan marcados como NO DISPONIBLES. |  |
|**Excepciones**|**Paso**|  |
|  | 6 | Si existen turnos activos en el período, el sistema notifica al Administrador y ofrece opciones para cancelar o reprogramar los turnos afectados antes de aplicar el bloqueo. |
|**Rendimiento**|**Paso**|  |
|  | 6 | Menos de 2 segundos |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| El desbloqueo sigue el mismo flujo inverso, seleccionando días bloqueados y presionando "Desbloquear". |  |


*Nota: No existe UC–REC-09. La numeración salta intencionalmente de UC–REC-08 a UC–REC-10.*


|**UCE–REC-10**|**Crear Indicación Médica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas |  |
|**Descripción**| El Bioquímico/Doctor o Administrador crea una nueva indicación médica predefinida en el sistema para ser enviada automáticamente al paciente al momento de agendar un turno. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Indicaciones Médicas y presiona "Nueva Indicación". |
|  | 2 | La interfaz despliega un formulario con los campos: Título, Contenido, Tipo de Análisis asociado (obligatorio). |
|  | 3 | El usuario completa los campos y presiona "Guardar". |
|  | 4 | El sistema valida que todos los campos obligatorios estén completos (título, contenido y tipo de análisis). |
|  | 5 | El sistema ejecuta `<<include>>` Asignar Indicación a Tipo de Análisis: vincula la indicación con el tipo de análisis seleccionado. |
|  | 6 | El sistema persiste el registro en la base de datos. |
|  | 7 | La interfaz muestra "Indicación creada exitosamente". |
|**Postcondición**| La nueva indicación médica queda registrada y disponible para ser asignada a turnos futuros. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el contenido está vacío o no se seleccionó un Tipo de Análisis, el sistema muestra una alerta de validación y no persiste. |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-11**|**Modificar Indicación Médica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas |  |
|**Descripción**| El Bioquímico/Doctor o Administrador modifica el contenido de una indicación médica predefinida existente en el sistema. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. Debe existir al menos una indicación médica registrada. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Indicaciones Médicas y selecciona una del listado. |
|  | 2 | La interfaz despliega el formulario prepoblado con los datos actuales. |
|  | 3 | El usuario modifica los campos deseados y presiona "Guardar Cambios". |
|  | 4 | El sistema valida los campos y actualiza el registro en la base de datos. |
|  | 5 | La interfaz muestra un mensaje de "Indicación actualizada exitosamente". |
|**Postcondición**| La indicación médica queda actualizada con el nuevo contenido. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el contenido queda vacío, el sistema rechaza la modificación y notifica al usuario. |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-12**|**Eliminar Indicación Médica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas |  |
|**Descripción**| El Bioquímico/Doctor o Administrador elimina lógicamente una indicación médica predefinida del sistema, desactivándola para que no sea enviada en futuros turnos. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. Debe existir al menos una indicación médica registrada. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Indicaciones Médicas y selecciona una del listado. |
|  | 2 | El usuario presiona "Eliminar". |
|  | 3 | El sistema solicita confirmación de la eliminación. |
|  | 4 | El usuario confirma la acción. |
|  | 5 | El sistema cambia el estado de la indicación a INACTIVA (baja lógica). |
|  | 6 | La interfaz muestra un mensaje de "Indicación eliminada exitosamente". |
|**Postcondición**| La indicación médica queda marcada como INACTIVA en la base de datos. |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el usuario cancela la confirmación, el sistema aborta la operación sin modificar el registro. |
|**Rendimiento**|**Paso**|  |
|  | 5 | Menos de 1 segundo |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Se realiza baja lógica para mantener la integridad referencial de turnos históricos que utilizaron esa indicación. |  |

|**UCE–REC-13**|**Consultar Indicaciones Médicas**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-02 Envío de Indicaciones Médicas |  |
|**Descripción**| El Bioquímico/Doctor o Administrador visualiza el listado completo de indicaciones médicas predefinidas registradas en el sistema, con su contenido y estado actual. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Indicaciones Médicas. |
|  | 2 | El sistema consulta la base de datos y recupera todas las indicaciones registradas. |
|  | 3 | La interfaz renderiza una tabla paginada con Título, Contenido, Tipo de Análisis y Estado. |
|  | 4 | El usuario aplica filtros opcionales (por estado: activa/inactiva, por tipo de análisis). |
|**Postcondición**| El sistema presenta el listado de indicaciones médicas. Operación de solo lectura. |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si no existen indicaciones registradas, la interfaz muestra el mensaje "No hay indicaciones médicas registradas" y habilita el botón para crear una nueva. |
|**Rendimiento**|**Paso**|  |
|  | 2 | Menos de 1 segundo |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–REC-14**|**Cancelar Turno por Vencimiento**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención |  |
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos |  |
|**Descripción**| Proceso automático del sistema que se ejecuta diariamente al cierre del horario de atención. Identifica todos los turnos cuyo horario ya transcurrió, que no fueron atendidos ni cancelados, y los marca como "No Asistió", liberando los recursos asociados. |  |
|**Precondición**| Debe existir al menos un turno con fecha/hora vencida en estado "Confirmado" o "Pendiente". |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El temporizador del sistema dispara la rutina diaria de depuración de agenda al cierre del horario de atención. |
|  | 2 | El sistema consulta la base de datos y recupera los turnos cuya fecha/hora ya transcurrió y cuyo estado es "Confirmado" o "Pendiente". |
|  | 3 | Para cada turno encontrado, el sistema cambia el estado a "No Asistió". |
|  | 4 | El sistema libera el bloque horario en la agenda. |
|  | 5 | El sistema registra cada cambio en la tabla de auditoría. |
|  | 6 | Se dispara internamente UC-REC-04 por cada bloque liberado. |
|**Postcondición**| Los turnos vencidos no atendidos cambian a "No Asistió" y los bloques quedan liberados. |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si no hay turnos en esas condiciones, la rutina finaliza sin realizar cambios. |
|**Rendimiento**|**Paso**|  |
|  | 2-3 | Hasta 5 segundos dependiendo del volumen de turnos a procesar. |
|**Frecuencia**| Diaria |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| La ejecución se programa como una tarea programada (job) del lado del servidor. |  |

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
|  | 6 | El sistema verifica si el paciente tiene datos demográficos incompletos (falta dirección, obra social, etc.). Si es así, muestra un formulario ligero para que el administrativo complete los datos faltantes antes de continuar. |
|  | 7 | El sistema registra el evento en la tabla de auditoría. |
|  | 8 | La interfaz confirma la operación y habilita el botón para iniciar la consulta (UC-DIAG-01). |
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

|**UCE–REC-17**|**Modificar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El personal autorizado modifica los datos demográficos de un paciente existente. |  |
|**Precondición**| El usuario debe tener una sesión activa con rol Bioquímico/Doctor o Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
|  | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido como criterio de búsqueda. |
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

|**UCE–REC-19**|**Desactivar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| El Administrador desactiva (baja lógica) el registro de un paciente, impidiendo nuevos turnos o análisis pero preservando íntegramente el historial clínico y los análisis existentes. |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Pacientes" y presiona "Buscar Paciente". |
|  | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido. |
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
|**Comentarios**| Gestiona pacientes que llaman por teléfono, adultos mayores sin WhatsApp o urgencias. |  |

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
|**Comentarios**| - |  |

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
|**Comentarios**| - |  |

|**UCE–REC-S-01**|**Buscar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre, Apellido) y retorna el/los pacientes coincidentes al caso de uso invocante. |  |
|**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El sistema solicita al usuario el criterio de búsqueda (DNI, Nombre o Apellido). |
|  | 2 | El usuario ingresa el criterio de búsqueda. |
|  | 3 | El sistema consulta la base de datos con el criterio ingresado. |
|  | 4a | Si hay una sola coincidencia exacta: el sistema retorna los datos del paciente al caso de uso invocante. |
|  | 4b | Si hay múltiples coincidencias: el sistema muestra un listado paginado para que el usuario seleccione. Al seleccionar, retorna los datos. |
|**Postcondición**| Los datos del paciente seleccionado son retornados al caso de uso invocante. |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si ningún paciente coincide con el criterio ingresado, el sistema informa "Paciente no encontrado" al caso de uso invocante para que maneje la situación (ofrecer crear uno nuevo, buscar de nuevo, etc.). |
|  | 3 | Si ocurre un error de conexión con la base de datos, se retorna un error al caso de uso invocante. |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 1 segundo |
|**Frecuencia**| Alta (invocado por Modificar y Desactivar Paciente) |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. La búsqueda es flexible: DNI (coincidencia exacta), Nombre o Apellido (coincidencia parcial). |  |

### 2.8.2 Subsistema Laboratorio Bioquímico
|**UCE–DIAG-01**|**Registrar Ficha Clínica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |  |
|**Descripción**| El Bioquímico/Doctor ingresa al sistema durante la consulta presencial para completar la información clínica estructurada del paciente.  |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor. <br>El paciente debe poseer un registro básico (Alta Temprana por Agente IA).  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico ingresa al módulo de Pacientes en la interfaz web y presiona "Nueva Consulta".  |
|  | 2 | El Bioquímico ingresa el DNI del paciente en el buscador.  |
|  | 3 | El sistema consulta la base de datos y recupera los datos demográficos registrados previamente por el Agente IA.  |
|  | 4 | La interfaz despliega el formulario de "Ficha Clínica" pre-poblado con los datos del paciente.  |
|  | 5 | El Bioquímico completa los campos clínicos obligatorios y presiona "Guardar Ficha".  |
|  | 6 | La interfaz realiza una validación de campos vacíos o formatos incorrectos (Frontend).  |
|  | 7 | El sistema recibe la petición, procesa la persistencia en la base de datos y vincula la Ficha al ID del Paciente.  |
|  | 8 | El sistema envía un código de estado HTTP 200 (Éxito).  |
|  | 9 | La interfaz muestra un mensaje de "Ficha guardada exitosamente" y habilita el botón para el paso secuencial de Ingreso de Muestra.  |
|**Postcondición**| Se genera y almacena la Ficha Clínica estructurada vinculada al paciente.  |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si el DNI no existe en el sistema, la interfaz emite una alerta indicando "Paciente no encontrado" y habilita un formulario de registro manual de emergencia.  |
|  | 7 | Si hay un error de conexión con la base de datos, el sistema muestra un error 500 y aborta la transacción sin guardar datos parciales.  |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 1 segundo.  |
|  | 7 | Menos de 2 segundos  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| El campo de "Edad" es calculado en tiempo real por el sistema a partir de la Fecha de Nacimiento, no se guarda estáticamente.  |  |

|**UCE–DIAG-02**|**Registrar Ingreso de Muestra**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |  |
|**Descripción**| El Bioquímico/Doctor registra en el sistema la recepción física de la muestra microbiológica del paciente, iniciando la trazabilidad.  |  |
|**Precondición**| El paciente debe contar con una Ficha Clínica registrada en la sesión actual.<br>El usuario debe tener una sesión activa con el rol correspondiente. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico presiona el botón "Ingresar Muestra" habilitado al finalizar el UC–DIAG-01.  |
|  | 2 | La interfaz despliega el formulario de carga de parámetros iniciales.  |
|  | 3 | El Bioquímico selecciona el "Tipo de Muestra" y completa observaciones iniciales.  |
|  | 4 | El Bioquímico presiona "Registrar Muestra".  |
|  | 5 | El sistema crea un nuevo registro en la tabla "Análisis Micológico" y establece su estado en "Pendiente".  |
|  | 6 | El sistema enlaza la clave foránea de este registro con la Ficha Clínica del paciente.  |
|  | 7 | La interfaz confirma la operación y redirige al panel de control de muestras.  |
|**Postcondición**| Se crea un registro de Análisis Micológico con estado inicial "Pendiente".  |  |
|**Excepciones**|**Paso**|  |
|  | - | - |
|**Rendimiento**|**Paso**|  |
|  | 5 | Menos de 1 segundo  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

|**UCE–DIAG-03**|**Actualizar Estado de Análisis**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |  |
|**Descripción**| El Bioquímico/Doctor carga los resultados parciales u observaciones obtenidos durante el procesamiento de la muestra y avanza el estado del estudio dentro del flujo de trabajo (Pendiente → En Proceso → Terminado).  |  |
|**Precondición**| Debe existir un Análisis Micológico en estado "Pendiente" o "En Proceso".<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico ingresa al módulo de Análisis o accede desde el Panel de Análisis (UC–DIAG-09).  |
|  | 2 | El sistema muestra el detalle del análisis con su estado actual.  |
|  | 3 | El Bioquímico carga los parámetros, resultados parciales y observaciones.  |
|  | 4 | El Bioquímico selecciona el nuevo estado del estudio (En Proceso o Terminado).  |
|  | 5 | El sistema valida que la transición de estado sea la siguiente en el flujo (Pendiente → En Proceso → Terminado).  |
|  | 6 | El sistema persiste los datos y actualiza el estado del análisis.  |
|  | 7 | El sistema registra el evento en la tabla de auditoría.  |
|  | 8 | La interfaz confirma la actualización y actualiza el panel.  |
|**Postcondición**| Los parámetros, observaciones y resultados parciales quedan guardados en la base de datos. El estado del análisis avanza según la selección del usuario.  |  |
|**Excepciones**|**Paso**|  |
|  | 5 | Si la transición de estado no es válida (por ejemplo, intentar pasar de "Pendiente" directamente a "Terminado"), el sistema rechaza la operación y mantiene el estado actual.  |
|  | 6 | Si el análisis se encuentra en estado "Cancelado" o "Validado", el sistema bloquea la actualización.  |
|  | 6 | Si ocurre un error de conexión con la base de datos, el sistema aborta la transacción sin guardar datos parciales.  |
|**Rendimiento**|**Paso**|  |
|  | 5 | Menos de 1 segundo.  |
|  | 6 | Menos de 1 segundo.  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| El estado "Validado" solo se alcanza mediante UC–DIAG-04. Un análisis cancelado no puede reanudarse sin una nueva muestra.  |  |

|**UCE–DIAG-04**|**Validar Análisis**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis.<br>OBJ-03 Emisión Segura y Descarga de Resultados  |  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.<br>RF-08 Validación de Identidad y Descarga de Informe.  |  |
|**Descripción**| El Bioquímico da por concluido el estudio al emitir su diagnóstico final y aprobar los resultados mediante el sistema, cerrando el ciclo clínico de la muestra. El sistema genera el Informe PDF, el token OTP y notifica al paciente por WhatsApp.  |  |
|**Precondición**| El Análisis Micológico debe encontrarse en estado "Terminado".<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico abre el análisis en estado "Terminado" desde el panel o el historial del paciente.  |
|  | 2 | El sistema muestra los resultados completos y las observaciones cargadas.  |
|  | 3 | El Bioquímico emite el diagnóstico final.  |
|  | 4 | El Bioquímico presiona "Validar Análisis".  |
|  | 5 | El sistema valida que todos los campos requeridos del resultado estén completos.  |
|  | 6 | El sistema cambia el estado a "Validado" y registra la fecha de validación y el bioquímico validador.  |
|  | 7 | El sistema compila los datos y genera el Informe de Resultados en formato PDF, almacenándolo en el servidor seguro.  |
|  | 8 | El sistema genera criptográficamente un token OTP (TTL de 7 días) asociado al informe.  |
|  | 9 | El sistema envía un mensaje de WhatsApp al paciente con el enlace al portal, las instrucciones de descarga y el OTP.  |
|  | 10 | El sistema programa automáticamente el proceso de reenvío de OTP: al expirar el TTL del OTP vigente sin que el informe haya sido descargado, genera un nuevo OTP, invalida el anterior y reenvía la notificación por WhatsApp. El ciclo se repite hasta la descarga del informe.  |
|  | 11 | El sistema registra el evento en la tabla de auditoría.  |
|**Postcondición**| El estado del análisis cambia permanentemente a "Validado". El Informe PDF queda generado y almacenado. El token OTP queda emitido y la notificación enviada al paciente. El sistema queda programado para reenviar automáticamente un nuevo OTP al expirar el TTL del vigente mientras el informe no sea descargado.  |  |
|**Excepciones**|**Paso**|  |
|  | 5 | Si faltan resultados o campos obligatorios, el sistema bloquea la validación e indica los campos pendientes.  |
|  | 9 | Si falla el envío inicial de WhatsApp, el sistema conserva el PDF y el OTP, registra el fallo y encola el reintento automático.  |
|  | 10 | Si el proceso automático de reenvío falla de forma reiterada o el paciente lo solicita (ej. extravío del mensaje o cambio de teléfono), el Bioquímico/Doctor o Administrador puede ejecutar un reenvío manual de la notificación con un nuevo OTP, que invalida el vigente. El reenvío manual es el mecanismo de respaldo ("por las dudas"), no el mecanismo principal.  |
|**Rendimiento**|**Paso**|  |
|  | 7 | Menos de 2 segundos.  |
|  | 8 | Menos de 1 segundo.  |
|  | 9 | Menos de 1 segundo.  |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Solo el rol Bioquímico/Doctor puede validar (control de calidad, RF-06). El OTP tiene un TTL de 7 días (RNF-02); el reenvío automático al expirar el TTL es una postcondición del caso de uso y no constituye un caso de uso independiente.  |  |

|**UCE–DIAG-05**|**Descargar Informe**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |  |
|**Requisitos asociados**| RF-08 Validación de Identidad y Descarga de Informe.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.  |  |
|**Descripción**| El Paciente, actuando de forma anónima desde el navegador, ingresa al portal web seguro del laboratorio e introduce el código OTP provisto por WhatsApp para acceder y descargar su Informe de Resultados en formato PDF.  |  |
|**Precondición**| El sistema debe tener el PDF almacenado y un token OTP válido (no expirado ni usado) asociado a ese informe.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El paciente abre el enlace al portal web seguro desde el mensaje de WhatsApp.  |
|  | 2 | El sistema muestra la pantalla de ingreso del código OTP (interfaz Mobile-First).  |
|  | 3 | El paciente ingresa el código OTP.  |
|  | 4 | El sistema valida el OTP: exactitud, vigencia (TTL de 7 días) y no utilización previa.  |
|  | 5 | El sistema autoriza una sesión temporal de descarga.  |
|  | 6 | El sistema muestra el informe de resultados disponible.  |
|  | 7 | El paciente presiona "Descargar".  |
|  | 8 | El sistema inicia la descarga segura del PDF en el dispositivo del paciente.  |
|  | 9 | El sistema invalida el token OTP para prevenir usos múltiples.  |
|**Postcondición**| El Informe de Resultados queda descargado en el dispositivo del paciente y el token OTP queda invalidado.  |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si el OTP es incorrecto, el sistema muestra un error genérico y permite reingresar.  |
|  | 4 | Si el OTP está vencido (superó los 7 días), el sistema informa la expiración y finaliza el flujo; el paciente recibirá un nuevo OTP mediante el reenvío automático programado en UC–DIAG-04 o, en su defecto, por el reenvío manual de respaldo del personal.  |
|  | 4 | Si el OTP ya fue utilizado, el sistema rechaza el acceso.  |
|  | 4 | Si se superan los intentos fallidos, el sistema bloquea temporalmente el acceso.  |
|**Rendimiento**|**Paso**|  |
|  | 4 | Menos de 1 segundo.  |
|  | 8 | Variable según el tamaño del archivo.  |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| El paciente no posee cuenta ni credenciales del sistema interno (ACT-04). Diseño Mobile-First y responsivo (RNF-03). Cumple la Ley de Protección de los Datos Personales (Ley 25.326).  |  |

|**UCE–DIAG-06**|**Consultar Historial de Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |  |
|**Descripción**| El personal autorizado busca y visualiza el historial médico acumulado de un paciente, incluyendo sus fichas clínicas previas y el estado de sus análisis micológicos.  |  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de Pacientes.  |
|  | 2 | El usuario busca al paciente por DNI, nombre o apellido.  |
|  | 3 | El sistema retorna el perfil del paciente con sus datos demográficos.  |
|  | 4 | El sistema despliega el listado de fichas clínicas previas ordenadas por fecha de ingreso.  |
|  | 5 | El usuario selecciona una ficha para visualizar su detalle clínico.  |
|  | 6 | El sistema muestra los análisis micológicos asociados con su estado actual.  |
|  | 7 | Operación de solo lectura (no modifica datos).  |
|**Postcondición**| El historial clínico completo del paciente es presentado al usuario.  |  |
|**Excepciones**|**Paso**|  |
|  | 2 | Si ningún paciente coincide con el criterio de búsqueda, el sistema informa "Paciente no encontrado".  |
|  | 4 | Si el paciente no posee fichas clínicas registradas, el sistema lo indica y finaliza la consulta.  |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 1 segundo.  |
|  | 4 | Menos de 2 segundos.  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Complementa a UC–DIAG-09 (Panel de Análisis): este UC consulta el historial de un paciente específico, mientras que el panel muestra el volumen de trabajo del laboratorio.  |  |

|**UCE–DIAG-07**|**Modificar Ficha Clínica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-20 Modificación de Ficha Clínica  |  |
|**Descripción**| El Bioquímico/Doctor modifica una ficha clínica previamente registrada, corrigiendo errores o agregando información complementaria. El sistema mantiene un historial de versiones.  |  |
|**Precondición**| La ficha clínica debe existir.<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario busca al paciente y accede a su ficha clínica.  |
|  | 2 | El sistema presenta la ficha en modo edición.  |
|  | 3 | El usuario modifica los campos clínicos o administrativos.  |
|  | 4 | La interfaz valida campos obligatorios y formatos.  |
|  | 5 | El usuario presiona "Guardar Cambios".  |
|  | 6 | El sistema conserva la versión anterior y registra la nueva versión (audit trail de modificaciones).  |
|  | 7 | El sistema actualiza la ficha vigente del paciente.  |
|  | 8 | La interfaz confirma "Ficha actualizada exitosamente".  |
|**Postcondición**| La ficha clínica queda actualizada, la versión histórica conservada y los cambios registrados en auditoría.  |  |
|**Excepciones**|**Paso**|  |
|  | 1 | Si la ficha está asociada a un análisis en estado "Validado", el sistema restringe la edición a campos no clínicos (observaciones administrativas).  |
|  | 7 | Si ocurre un error de conexión con la base de datos, el sistema aborta la transacción sin guardar cambios.  |
|**Rendimiento**|**Paso**|  |
|  | 7 | Menos de 1 segundo.  |
|**Frecuencia**| Media |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Se invoca como `<<extend>>` de UC–DIAG-01 (Registrar Ficha Clínica). El versionado garantiza trazabilidad del historial clínico (RF-20).  |  |

|**UCE–DIAG-08**|**Cancelar Análisis**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-21 Cancelación de Análisis.<br>RF-06 Actualización de Estados de Análisis Micológico.  |  |
|**Descripción**| El Bioquímico/Doctor o Administrador cancela un análisis micológico en curso, registrando obligatoriamente el motivo.  |  |
|**Precondición**| El análisis debe existir y estar en estado "Pendiente" o "En Proceso".<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor o Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario accede al detalle del análisis (desde el panel o el historial del paciente).  |
|  | 2 | El sistema muestra el análisis con su estado actual.  |
|  | 3 | El usuario presiona "Cancelar Análisis".  |
|  | 4 | El sistema solicita el motivo obligatorio de cancelación.  |
|  | 5 | El usuario ingresa el motivo.  |
|  | 6 | El sistema valida que el estado del análisis permita la cancelación.  |
|  | 7 | El sistema cambia el estado del análisis a "Cancelado".  |
|  | 8 | El sistema registra el evento en la tabla de auditoría.  |
|  | 9 | La interfaz confirma la cancelación.  |
|**Postcondición**| El estado del análisis cambia a "Cancelado", el motivo queda registrado y el análisis cancelado permanece en el historial del paciente.  |  |
|**Excepciones**|**Paso**|  |
|  | 6 | Si el análisis está en estado "Validado", el sistema bloquea la cancelación: el análisis validado es definitivo.  |
|  | 6 | Si el análisis ya está "Cancelado", el sistema informa y finaliza.  |
|  | 5 | Si el motivo está vacío, el sistema bloquea el paso.  |
|**Rendimiento**|**Paso**|  |
|  | 7 | Menos de 1 segundo.  |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Una muestra contaminada, extraviada o un paciente que desiste justifican la cancelación (RF-21). Evita que análisis no viables continúen su procesamiento y libera recursos del laboratorio.  |  |

|**UCE–DIAG-09**|**Consultar Panel de Análisis**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |  |
|**Descripción**| El Bioquímico/Doctor accede a un panel de trabajo que lista todos los análisis micológicos, filtrables por estado, tipo de análisis, fecha y bioquímico asignado, sin necesidad de navegar paciente por paciente.  |  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al "Panel de Análisis" del módulo clínico.  |
|  | 2 | El sistema lista todos los análisis de forma paginada.  |
|  | 3 | El usuario aplica filtros (estado, tipo de análisis, rango de fechas, bioquímico).  |
|  | 4 | El sistema filtra y actualiza el listado.  |
|  | 5 | El usuario selecciona un análisis para ver su detalle.  |
|  | 6 | El sistema muestra el detalle con las acciones habilitadas según el estado (actualizar, validar, cancelar).  |
|**Postcondición**| El panel presenta el volumen de trabajo del laboratorio. Operación de solo lectura.  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si no hay análisis que cumplan los filtros, el sistema informa y muestra el listado vacío.  |
|**Rendimiento**|**Paso**|  |
|  | 2 | Menos de 2 segundos.  |
|  | 4 | Menos de 1 segundo.  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Diferente de UC–DIAG-06 (historial de un paciente); este UC muestra el volumen de trabajo del laboratorio. Las acciones de gestión disparan UC–DIAG-03, UC–DIAG-04 u UC–DIAG-08.  |  |

|**UCE–DIAG-10**|**Gestionar Tipos de Análisis y Muestra**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-16 Gestión de Catálogos Clínicos.<br>IRQ-05 Catálogo de Tipos de Análisis/Muestra.  |  |
|**Descripción**| El Administrador gestiona el catálogo de tipos de análisis micológicos y de tipos de muestra disponibles en el sistema (crear, modificar, desactivar).  |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Administrador.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Administrador ingresa al módulo de Catálogos Clínicos.  |
|  | 2 | El sistema lista los tipos de análisis vigentes.  |
|  | 3 | El usuario selecciona la operación: Crear, Modificar o Desactivar.  |
|  | 4 | El usuario ingresa o actualiza los datos (nombre, descripción, indicaciones, estado).  |
|  | 5 | El sistema valida la unicidad del nombre y la coherencia de los datos.  |
|  | 6 | El sistema persiste el cambio y registra el evento en auditoría.  |
|  | 7 | La interfaz confirma la operación.  |
|**Postcondición**| El catálogo queda actualizado. Los tipos desactivados no pueden seleccionarse en nuevos análisis, pero se preservan en registros históricos.  |  |
|**Excepciones**|**Paso**|  |
|  | 5 | Si el nombre ya existe, el sistema rechaza la operación y solicita otro nombre.  |
|  | 6 | Si se intenta desactivar un tipo con análisis históricos, el sistema aplica baja lógica conservando los registros.  |
|**Rendimiento**|**Paso**|  |
|  | 6 | Menos de 1 segundo.  |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Media |  |
|**Comentarios**| Incluye sub-flujos: Crear Tipo, Modificar Tipo, Desactivar Tipo (baja lógica). La relación entre tipo de análisis y tipos de muestra válidos alimenta los selectores de UC–DIAG-02.  |  |

### 2.8.3 Subsistema Recursos de Laboratorio

*UCEs pendientes de desarrollo. Se requiere desarrollar los UCE correspondientes a UC–LAB-01 (Registrar Ingreso de Insumos), UC–LAB-02 (Registrar Retiro de Insumos), UC–LAB-03 (Registrar Generación de Residuos), UC–LAB-04 (Generar Reporte de Residuos), UC–LAB-05 (Consultar Inventario), y los nuevos UC–LAB-06 a UC–LAB-13.*

### 2.8.4 Subsistema Acceso y Seguridad
|**UCE–SEG-01**|**Iniciar Sesion**|  |
|---|---|---|
|**Objetivos asociados**| Transversal (Seguridad Operativa)  |  |
|**Requisitos asociados**| RF-13 Gestión de Cuentas y Autenticación  |  |
|**Descripción**| El usuario del sistema (Administrador, Bioquímico/Doctor o Profesor) ingresa sus credenciales de acceso para autenticarse en la plataforma web de gestión.  |  |
|**Precondición**| El usuario debe poseer una cuenta registrada y en estado "Activo" (sin baja lógica) en el sistema.  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa a la URL del portal interno del laboratorio.  |
|  | 2 | La interfaz muestra el formulario de inicio de sesión requiriendo Correo Electrónico y Contraseña.  |
|  | 3 | El usuario completa sus credenciales y presiona "Ingresar".  |
|  | 4 | El Backend verifica que la cuenta no se encuentre en estado "Bloqueado Temporal" o "Inhabilitado".  |
|  | 5 | El Backend contrasta la contraseña encriptada (Hash) contra la base de datos.  |
|  | 6 | El Backend genera un Token de Sesión JWT (JSON Web Token) y lo inyecta en el navegador.  |
|  | 7 | El sistema registra el evento de inicio de sesión exitoso en la tabla de auditoría  |
|  | 8 | El sistema redirige al usuario al panel principal con las opciones habilitadas según su rol predefinido.  |
|**Postcondición**| El sistema valida las credenciales y redirige al panel principal.  |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si la cuenta está bloqueada por intentos fallidos, el sistema rechaza la petición indicando el tiempo de espera restante.  |
|  | 5 | Si las credenciales son incorrectas, el sistema suma 1 al contador de intentos fallidos. Retorna un error genérico ("Credenciales inválidas"). Si alcanza 5 fallos, cambia el estado a "Bloqueado Temporal" y notifica al usuario en pantalla.  |
|**Rendimiento**|**Paso**|  |
|  | 5 | Menos de 1 segundo |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

### 2.8.5 Subsistema Reportes y Estadísticas
|**UCE–REP-01**|**Consolidar y Exportar Datos Operativos**|  |
|---|---|---|
|**Objetivos asociados**| Transversal (Generación de Información)  |  |
|**Requisitos asociados**| RF-15 Consolidación y Exportación de Datos Operativos  |  |
|**Descripción**| El sistema procesa los datos transaccionales acumulados para estructurar análisis estadísticos. Permite cruzar información y exportarla como base para trabajos de investigación.  |  |
|**Precondición**| El usuario debe tener una sesión activa con los privilegios necesarios (Bioquímico/Doctor o Administrador). <br>Deben existir datos transaccionales previos registrados en la plataforma  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El usuario ingresa al módulo de "Reportes e Investigaciones".  |
|  | 2 | La interfaz ofrece filtros de selección: Tipo de Reporte (Clínico, Inventario, Desechos) y Rango de Fechas.  |
|  | 3 | El usuario configura los parámetros y presiona "Generar Previsualización".  |
|  | 4 | El Backend ejecuta operaciones de cruce de datos complejas sobre la base de datos (JOINs y Agregaciones). |
|  | 5 | Si el reporte es Clínico, el Backend ejecuta la regla de anonimización estricta (remoción de datos sensibles). |
|  | 6 | La interfaz renderiza una vista en tabla de las primeras filas del conjunto de datos procesado.  |
|  | 7 | El usuario presiona el botón "Exportar".  |
|  | 8 | El Backend empaqueta los resultados en formato tabular (.CSV o .XLSX) y transmite el archivo.  |
|  | 9 | El navegador del usuario inicia la descarga del conjunto estructurado.  |
|**Postcondición**| El sistema emite un conjunto de datos consolidado para su visualización y permite su descarga externa.  |  |
|**Excepciones**|**Paso**|  |
|  | 4 | Si la consulta SQL no devuelve resultados para el rango de fechas seleccionado, el sistema notifica en pantalla: "No existen registros transaccionales para los parámetros indicados" y detiene el flujo.  |
|**Rendimiento**|**Paso**|  |
|  | 4 | Hasta 5 segundos (Operación de extracción y procesamiento intensivo dependiente de la cantidad de registros históricos).  |
|**Frecuencia**| Baja |  |
|**Estabilidad**| Media |  |
|**Comentarios**| - |  |

# Glosario de Términos
|**Término**|**Categoría**|**Comentarios**|
|---|---|---|
| Agente IA | Arquitectura | Componente de software que interactúa con los pacientes de forma asíncrona a través de WhatsApp para la autogestión de turnos (agendamiento, cancelación, reprogramación y consulta). |
| OTP (One-Time Password) | Seguridad | Token criptográfico de un solo uso generado por el sistema y enviado al paciente vía WhatsApp. Permite validar su identidad de forma anónima en el portal web de descarga de resultados. |
| Token | Seguridad | Credencial digital generada por el sistema para autenticación o autorización temporal. Incluye tanto el OTP para pacientes como el JWT para sesiones de usuarios internos. |
| Alta Temprana | Clínico | Registro inicial mínimo de un paciente en la base de datos, creado por el Agente IA al momento del agendamiento del turno. Contiene únicamente DNI y Nombre Completo. |
| Baja lógica | Seguridad / Datos | Mecanismo de desactivación de un registro (paciente, usuario, indicación médica) que marca su estado como "Inactivo" sin eliminar físicamente los datos, preservando la integridad referencial y el historial. |
| Ficha Clínica | Clínico | Documento digital estructurado que contiene la información médica del paciente recolectada durante la consulta presencial. Incluye datos demográficos completos y diagnóstico clínico. |
| Muestra | Clínico | Material biológico (ej. uñas, piel, cabello) extraído del paciente para su análisis microbiológico en el laboratorio. |
| Micología | Dominio | Rama de la biología que estudia los hongos. En el contexto del sistema, el laboratorio se especializa en el diagnóstico de infecciones fúngicas (micosis) en pacientes. |
| JWT (JSON Web Token) | Seguridad | Estándar abierto (RFC 7519) utilizado para la autenticación de usuarios internos. El sistema genera un token JWT al iniciar sesión y lo inyecta en el navegador para validar sesiones subsecuentes. |