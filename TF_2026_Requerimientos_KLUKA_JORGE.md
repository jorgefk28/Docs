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
| 8 |  |  | Kluka Jorge |
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
El Subsistema de Recepción y Administración de Pacientes es el componente encargado de la logística de ingreso y el contacto inicial con los Pacientes. Su función principal es organizar el flujo de atención administrativa, comenzando por la agenda y asignación de turnos, hasta la gestión del repositorio centralizado a largo plazo, el cual resguarda el historial clínico acumulado de las personas atendidas. Este subsistema abarca los módulos de**Gestión de Turnos y Atención**, y**Gestión de Pacientes**.
# Subsistema de Laboratorio Bioquímico
El Subsistema de Diagnóstico y Laboratorio Bioquímico es el núcleo clínico y científico destinado al procesamiento de las muestras y la evaluación médica. Su propósito fundamental es sistematizar la recolección de los datos en la ficha clínica al momento de la consulta, trazar el ciclo de vida completo de los estudios microbiológicos (abarcando los estados pendiente, en proceso, terminado y validado) y automatizar la entrega remota y segura de los diagnósticos finales a los pacientes. Este subsistema abarca los módulos de**Registro deInformación Clínica**,**Registro de Análisis**, y**Emisión de Resultados**.
# Subsistema de Recursos de Laboratorio
El Subsistema de Recursos de Laboratorio es el componente encargado de administrar los bienes físicos y químicos del módulo de micología. Este subsistema digitaliza y controla la trazabilidad del inventario, gestionando el ingreso y egreso de los insumos reactivos utilizados por profesores y alumnos en las prácticas. A su vez, sistematiza el registro exacto del volumen y peso de los residuos químicos generados para cumplir con las normativas vigentes. Este subsistema abarca los módulos de**Stock de Insumos Reactivos**y**Control de Residuos**.
# Subsistema de Acceso y Seguridad
El Subsistema de Acceso y Seguridades es el componente transversal encargado de proteger la confidencialidad de los datos y garantizar la transparencia operativa de la aplicación. Su función es gestionar la autenticación y autorización de los usuarios mediante un esquema de roles y permisos, al mismo tiempo que mantiene un registro detallado, cronológico e inmutable de todas las acciones críticas realizadas en la plataforma. Este subsistema abarca los módulos de**Usuarios**,**Roles y Permisos**, y**Auditoría**.
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
Este módulo traza el ciclo de vida completo de las muestras microbiológicas dentro del laboratorio. Registra el tipo de análisis, los parámetros o resultados obtenidos, y permite actualizar los estados del estudio secuencialmente (pendiente, en proceso, terminado y validado por un bioquímico). Su valor reside en asegurar un control riguroso de cada etapa clínica, consolidando toda la información relevante al análisis en un único lugar.
# Emisión de Resultados
Se encarga de automatizar la entrega final y remota de los diagnósticos a los pacientes. Funciona mediante un flujo de notificación asíncrona que envía un enlace y genera criptográficamente un Token (OTP) de un solo uso, permitiendo al paciente descargar su archivo PDF desde un portal web seguro mediante una doble validación de identidad. Este proceso asegura el cumplimiento estricto de la Ley de Protección de los Datos Personales (Ley 25.326) sin forzar el retiro presencial.
# Stock de Insumos Reactivos
Su objetivo es digitalizar la administración del inventario de recursos físicos y químicos. Registra los ingresos y los retiros de insumos realizados por los profesores para las prácticas de los alumnos. Su implementación busca clarificar la trazabilidad operativa para solucionar la actual mala gestión y escasez, evitando problemáticas como el vencimiento de reactivos, el uso ineficiente de materiales nuevos y el desconocimiento de las cantidades exactas.
# Control de Residuos
Su función es sistematizar la recolección de datos sobre los desechos generados en las prácticas de laboratorio. Permite registrar de manera exacta la cantidad (volumen y peso) de los residuos químicos producidos por cada actividad. Esto es vital para garantizar el cumplimiento del nuevo reglamento que entró en vigencia en el año 2026, facilitando la generación de reportes mensuales y el adecuado resguardo de los residuos para su tratamiento
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
|**Datos específicos**| Número de registro<br>Fecha de ingreso<br>Nombre y apellido<br>Fecha de nacimiento<br>Edad (campo calculado)<br>DNI<br>Sexo<br>Domicilio<br>Teléfono de contacto<br>Médico derivante<br>Institución<br>Diagnóstico presuntivo.  |
|  |  |
|**Estabilidad**| alta  |
|**Comentarios**| El campo de edad no se persistirá estáticamente, sino que el sistema lo calculará en tiempo real a partir de la fecha de nacimiento.  |

|**IRQ–02**|**Registro de Análisis Micológico**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis.<br>OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP.  |
|**Descripción**| Entidad que traza el ciclo de vida y consolida los resultados científicos de la muestra extraída al paciente.  |
|**Datos específicos**| Tipo de muestra<br>Cultivo<br>Estado actual (Pendiente, En proceso, Terminado, Validado)<br>Observaciones/Resultados parciales<br>Fecha de validación<br>Bioquímico validador.  |
|  |  |
|**Estabilidad**| Media |
|**Comentarios**| - |

|**IRQ–03**|**Insumo / Reactivo de Laboratorio**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-09 Alertas de Stock en Panel de Control.<br>RF-10 Gestión de Ingresos y Retiros de Inventario. |
|**Descripción**| Entidad que representa los bienes físicos y reactivos químicos gestionados en el inventario del laboratorio.  |
|**Datos específicos**| Nombre del reactivo/insumo<br>Cantidad actual (stock disponible)<br>Umbral mínimo de alerta<br>Fecha de vencimiento.  |
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
|**Descripción**| Una vez validado el análisis, el sistema debe notificar al paciente vía WhatsApp enviando un enlace al portal web seguro, las instrucciones de descarga y un token OTP generado criptográficamente. |
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
|**Descripción**| Usuario del sistema encargado de la atención directa y el procesamiento clínico de las muestras. Posee permisos para registrar consumo de insumos del inventario y la generación de residuos. Gestiona el registro unificado del paciente y su ficha clínica al momento de la consulta, y es el responsable de registrar, actualizar y validar todo el ciclo de vida de los análisis micológicos.  |
|**Comentarios**| - |

|**ACT–02**|**Profesor**|
|---|---|
|**Descripción**| Usuario del sistema perteneciente al ámbito académico. Su responsabilidad operativa radica en interactuar con el módulo de Recursos de Laboratorio para registrar los retiros y egresos físicos de insumos o reactivos destinados a las prácticas educativas.  |
|**Comentarios**| - |

|**ACT–03**|**Administrador**|
|---|---|
|**Descripción**| Usuario responsable de la gestión administrativa, logística y de seguridad del sistema. Sus funciones abarcan el registro de los ingresos al inventario de recursos y la gestión del control de acceso, autorizando cuentas y asignando los roles correspondientes. Además cumple la misma función que un Bioquímico, pudiendo gestionar análisis e inventario. |
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
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos.<br>RF-03 Gestión de Lista de Espera por Turnos Liberados. |
|**Descripción**| El Paciente solicita cambiar la fecha y/o la hora de un turno asignado comunicándose con el Agente IA a través de WhatsApp.  |
|**Precondición**| El paciente debe tener un turno asignado en el sistema.<br>El sistema debe contar con disponibilidad en la agenda para la nueva fecha/hora solicitada. |
|**Postcondiciones**| El turno original del paciente queda liberado y se le asigna el nuevo bloque de tiempo.<br>El sistema envía un mensaje con la confirmación de la nueva fecha y hora.<br>La liberación del turno original dispara automáticamente el proceso interno de "Reasignación Automática de Turno Liberado" (UC-REC-04).  |

|**UC–REC-04**|**Reasignación Automática de Turno Liberado**|
|---|---|
|**Objetivos asociados**| OBJ-01 Automatización de la Gestión de Turnos y Atención. |
|**Requisitos asociados**| RF-03 Gestión de Lista de Espera por Turnos Liberados. |
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

#### 2.7.3.2 Subsistema Laboratorio Bíoquímico
|**UC–DIAG-01**|**Registrar Ficha Clínica**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| El Bioquímico/Doctor ingresa al sistema durante la consulta presencial para completar la información clínica estructurada del paciente, enlazándola con los datos demográficos previamente cargados por el Agente IA.  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.<br>El paciente debe poseer un registro básico en el sistema (Alta Temprana).   |
|**Postcondiciones**| Se genera y almacena la Ficha Clínica estructurada vinculada de forma unívoca al paciente. <br>El historial clínico queda disponible para la carga de futuros análisis micológicos.  |

|**UC–DIAG-02**|**Registrar Ingreso de Muestra**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |
|**Descripción**| El Bioquímico/Doctor registra en el sistema la recepción física de la muestra microbiológica del paciente, indicando el tipo de análisis a realizar e iniciando la trazabilidad del estudio.  |
|**Precondición**| El paciente debe contar con una Ficha Clínica registrada en el sistema. <br>El usuario debe tener una sesión activa con el rol correspondiente.  |
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
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico.<br>RF-07 Notificación de Disponibilidad de Resultados y OTP. |
|**Descripción**| El Bioquímico da por concluido el estudio al emitir su diagnóstico final y aprobar los resultados mediante el sistema, cerrando así el ciclo clínico de la muestra.  |
|**Precondición**| El Análisis Micológico debe encontrarse en estado "Terminado".<br>El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor.  |
|**Postcondiciones**| El estado del análisis cambia permanentemente a "Validado". <br>El sistema compila estáticamente los datos y genera de inmediato el Informe de Resultados en formato PDF, almacenándolo en el servidor seguro. <br>Se dispara automáticamente el proceso interno de "Notificación de Resultados" (UC-DIAG-05).  |

|**UC–DIAG-05**|**Notificación de Resultados**|
|---|---|
|**Objetivos asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos asociados**| RF-07 Notificación de Disponibilidad de Resultados y OTP  |
|**Descripción**| Proceso interno del sistema que se activa inmediatamente tras la validación de un análisis. Se encarga de generar la credencial de acceso temporal y avisar al paciente.  |
|**Precondición**| El caso de uso UC-DIAG-04 (Validar Análisis) debe haber concluido con éxito.  |
|**Postcondiciones**| El sistema genera criptográficamente un Token OTP (One-Time Password) asociado al análisis. <br>Se envía automáticamente un mensaje de WhatsApp al paciente con el enlace al portal web, las instrucciones y el Token OTP.  |

|**UC–DIAG-06**|**Descargar Informe**|
|---|---|
|**Objetivos asociados**| OBJ-03 Emisión Segura y Descarga de Resultados  |
|**Requisitos asociados**| RF-08 Validación de Identidad y Descarga de Informe  |
|**Descripción**| El Paciente, actuando de forma anónima desde el navegador web, ingresa al portal seguro del laboratorio e introduce el código provisto por WhatsApp para acceder a su documento.  |
|**Precondición**| El sistema debe tener el PDF almacenado y un Token OTP válido (no expirado/no usado) asociado a ese informe.  |
|**Postcondiciones**| El sistema coteja el OTP; si es exitoso, autoriza la sesión temporal.<br>Se inicia la descarga segura del Informe de Resultados en formato PDF en el dispositivo del paciente. <br>El Token OTP queda invalidado para prevenir múltiples usos posteriores.  |

|**UC–DIAG-07**|**Consultar Ficha Clínica**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |
|**Descripción**| El personal autorizado accede al repositorio centralizado para buscar y visualizar el historial médico acumulado de un paciente, sus consultas previas y los estados de sus análisis micológicos.  |
|**Precondición**| El usuario debe tener una sesión activa con rol de Bioquímico/Doctor o Administrador.  |
|**Postcondiciones**| El sistema muestra el listado paginado de pacientes y sus respectivas fichas clínicas, permitiendo la búsqueda mediante filtros opcionales (DNI, Nombre, Rango de Fechas). Operación de solo lectura.  |

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
|**Descripción**| El Profesor o el Bioquímico registran el consumo o retiro de reactivos necesarios para las prácticas educativas o los análisis clínicos, deduciendo inmediatamente las cantidades del inventario.  |
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
|**Precondición**| El usuario solicitante debe tener los privilegios administrativos o directivos necesarios.  |
|**Postcondiciones**| Se emite un documento (reporte) que detalla las cantidades y tipos de residuos químicos generados en el mes.  |

|**UC–LAB-05**|**Consultar Inventario**|
|---|---|
|**Objetivos asociados**| OBJ-04 Trazabilidad y Control de Stock de Insumos Reactivos  |
|**Requisitos asociados**| RF-10 Gestión de Ingresos y Retiros de Inventario   |
|**Descripción**| Los usuarios internos acceden al módulo de recursos para visualizar el listado completo de reactivos e insumos físicos disponibles en el laboratorio, conociendo las cantidades exactas y sus estados.  |
|**Precondición**| El usuario debe tener una sesión activa (Administrador, Bioquímico/Doctor o Profesor).  |
|**Postcondiciones**| El sistema despliega una vista paginada del inventario actual, permitiendo aplicar filtros opcionales (por nombre, tipo o insumos próximos a vencer/agotar). Operación de solo lectura sin alteración de datos.  |

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
### 2.8.1 Subsistema Gestión Clínica
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
|**Postcondición**| El turno queda registrado y reservado.<br>El sistema programa en cola el envío de un recordatorio de asistencia. |  |
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
|**Requisitos asociados**| RF-04 Cancelación y Reprogramación de Turnos <br>RF-03 Gestión de Lista de Espera por Turnos Liberados  |  |
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
|**Requisitos asociados**| RF-03 Gestión de Lista de Espera por Turnos Liberados  |  |
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
|  | 6 | Menos de 2 segundos |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

### 2.8.2 Subsistema Recursos de Laboratorio
|**UCE–DIAG-01**|**Registrar Ficha Clínica**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica  |  |
|**Descripción**| El Bioquímico/Doctor ingresa al sistema durante la consulta presencial para completar la información clínica estructurada del paciente.  |  |
|**Precondición**| El usuario debe tener una sesión activa con el rol de Bioquímico/Doctor. <br>El paciente debe poseer un registro básico (Alta Temprana por Agente IA).  |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico ingresa al módulo de Pacientes en la interfaz web y presiona "Nueva Consulta".  |
|  | 2 | El Bioquímico ingresa el DNI del paciente en el buscador.  |
|  | 3 | El Backend consulta la base de datos y recupera los datos demográficos registrados previamente por el Agente IA.  |
|  | 4 | La interfaz despliega el formulario de "Ficha Clínica" pre-poblado con los datos del paciente.  |
|  | 5 | El Bioquímico completa los campos clínicos obligatorios (Institución, Diagnóstico presuntivo, etc.) y presiona "Guardar Ficha".  |
|  | 6 | La interfaz realiza una validación de campos vacíos o formatos incorrectos (Frontend).  |
|  | 7 | El Backend recibe la petición, procesa la persistencia en la base de datos y vincula la Ficha al ID del Paciente.  |
|  | 8 | El Backend envía un código de estado HTTP 200 (Éxito).  |
|  | 9 | interfaz muestra un mensaje de "Ficha guardada exitosamente" y habilita el botón para el paso secuencial de Ingreso de Muestra.  |
|**Postcondición**| Se genera y almacena la Ficha Clínica estructurada vinculada al paciente.  |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si el DNI no existe en el sistema, la interfaz emite una alerta indicando "Paciente no encontrado" y habilita un formulario de registro manual de emergencia.  |
|  | 7 | Si hay un error de conexión con la base de datos, el sistema muestra un error 500 y aborta la transacción sin guardar datos parciales.  |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 1 segundo.  |
|  | 7 | Menos de 2 segundos  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| El campo de "Edad" es calculado en tiempo real por el Backend a partir de la Fecha de Nacimiento, no se guarda estáticamente.  |  |

|**UCE–DIAG-02**|**Registrar Ingreso de Muestra**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis  |  |
|**Requisitos asociados**| RF-06 Actualización de Estados de Análisis Micológico  |  |
|**Descripción**| El Bioquímico/Doctor registra en el sistema la recepción física de la muestra microbiológica del paciente, iniciando la trazabilidad.  |  |
|**Precondición**| El paciente debe contar con una Ficha Clínica registrada en la sesión actual.<br>El usuario debe tener una sesión activa con el rol correspondiente. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El Bioquímico presiona el botón "Ingresar Muestra" habilitado al finalizar el UC-DIAG-01.  |
|  | 2 | La interfaz despliega el formulario de carga de parámetros iniciales.  |
|  | 3 | El Bioquímico selecciona el "Tipo de Muestra" y completa observaciones iniciales.  |
|  | 4 | El Bioquímico presiona "Registrar Muestra".  |
|  | 5 | El Backend crea un nuevo registro en la tabla "Análisis Micológico" y establece su estado en "Pendiente".  |
|  | 6 | El Backend enlaza la clave foránea de este registro con la Ficha Clínica del paciente.  |
|  | 7 | La interfaz confirma la operación y redirige al panel de control de muestras.  |
|**Postcondición**| Se crea un registro de Análisis Micológico con estado inicial "Pendiente".  |  |
|**Excepciones**|**Paso**|  |
|  | - | - |
|**Rendimiento**|**Paso**|  |
|  | 5 | Menos de 1 segundo  |
|**Frecuencia**| Alta |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| - |  |

### 2.8.3 Subsistema Acceso y Seguridad
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

### 2.8.4 Subsistema Reportes y estadísticas
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
|  |  |  |