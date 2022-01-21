# Dashboard con App Web (y acceso directo a base de datos del Banco Mundial adicional)
El `objetivo inicial` del proyecto era crear un dashboard de análisis económico haciendo uso de la librería `Dash`.
Además del objetivo principal alcanzamos `otros objetivos alternos`: creamos una `app interactiva` para la consulta del dashboard, creamos un `acceso directo de descarga` de toda la base de datos del Banco Mundial que permite prescindir del uso de archivos csv y creamos un gif para promover la difusión de los resultados.

Se creó la herramienta interactiva de consulta de información económica utilizando la librería Dash, además de las vistas en clase para el manejo de datos: Pandas, Matplotlib y Numpy. Para el dominio de `Dash` nos auxiliamos principalmente del libro [Interactive Dashboards and Data Apps with Plotly and Dash](https://github.com/PES-BG/proyecto-y-operation-ultra-at-bletchley-park/blob/main/Referencias/Interactive%20Dashboard.pdf) y referencias varias.

El dashboard permite analizar la relación entre el PIB per cápita en dólares y tasa de mortalidad infantil de todos los países disponibles en el Banco Mundial para 67 años -1952 a 2019 (la fecha donde todos tienen información actualizada)-. Los "callback" de la app hacen posible acceder a los datos con solo ubicar el cursor sobre la gráfica o haciendo clic en los flitros de año, región y país.

Para conseguir toda la base de datos se hizo uso de un módulo "data-reader" de pandas, que es una herramienta que descubrimos en el proceso de investigación y de la cual se comaprte a los compañeros un [Manual de descarga de datos del Banco Mundial](https://github.com/PES-BG/proyecto-y-operation-ultra-at-bletchley-park/blob/main/Manual%20%20de%20descarga%20de%20data%20de%20Banco%20Mundial.ipynb) porque se considera un recurso de utilidad altamente significativa, ya que perite el acceso a la fuente de origen sin depender de intermediarios, permite vincular el resto del desarrollo de herramientas de análisis de datos a sitios web institucional a la vez que gestiona la información.

Con fines promocionales y para generar interés del público en la herramienta se creó un [GIF](https://github.com/PES-BG/proyecto-y-operation-ultra-at-bletchley-park/blob/main/DashboardWeb_PIBperCapita_Mortalidad_infantil.gif).

Todo lo descrito queda alojado en el repositorio para los buenos usos de los compañeros.

Atentamente,

            Jorge Orenos y Marlon Morales

# Presentación final del curso de Programación I

Este repositorio tiene como propósito servir de contenedor para los archivos de la presentación final del curso. Se deben guardar todos los archivos utilizados para la presentación (vea las condiciones de entrega más adelante). 

*Banco de Guatemala*  
*Maestría en Economía y Finanzas Aplicadas*  
*Pogramación I*  
*Profesor: Rodrigo Chang*  
*Fecha: Enero de 2022*

## Objetivos

El presente proyecto tiene como objetivo que el estudiante conozca nuevos paquetes del lenguaje de Python o que desarrolle lógica de programación necesaria para realizar alguna aplicación interesante utilizando programación científica o métodos de simulación de Monte Carlo. 


## Rúbrica de evaluación 

| Aspecto a evaluar                                                                             |  Punteo |
|:----------------------------------------------------------------------------------------------|--------:|
| Definición y delimitación del proyecto                                                        |      15 |
| Nivel de interés que despierta el tema en el profesor o en los estudiantes.                   |      20 |
| El proyecto requiere conocimientos/esfuerzo adicional al ganado/realizado en el curso         |      20 |
| El proyecto utiliza paquetes u herramientas no vistas en clase                                |      15 |
| Participantes del grupo colaboraron cada uno con confirmaciones (*commits*) en el repositorio |      15 |
| Exposición clara, interacción con el público y manejo de los límites de tiempo (5-10 minutos) |      15 |
| **Total**                                                                                     | **100** |


## Formato de entrega 

- El proyecto debe entregarse utilizando la plataforma de Github, a través de las confirmaciones (*commits*) necesarios por los miembros de cada equipo. 
  - Tomar en cuenta que el repositorio será público. Evitar compartir datos personales, contraseñas u otra información sensible. Los repositorios pueden ser visitados nuevamente en el sitio de la organización `PES-BG` para futuras consultas de parte de todos los estudiantes. 
- Los archivos finales del proyecto se pueden guardar en el directorio raíz del repositorio utilizando cualquier estructura deseada. Sin embargo, si se utilizan archivos de prueba que puedan servir como muestra del procedimiento realizado, pero que no formen parte del proyecto final, se deben guardar en un directorio especial denominado `deprecated`. 
- No cargar archivos al repositorio que sean demasiado grandes (>10MB) como fotografías o vídeos. Utilizar recursos o plataformas web específicamente diseñadas para estos propósitos. La única excepción a esta regla es para el archivo de presentación. 
- Un archivo de presentación es opcional. Si se utiliza una presentación en PowerPoint o PDF, esta debe ser adjuntada en la raíz del proyecto. 
- Al final de la presentación, se dará un tiempo para realizar preguntas, tanto del profesor o de los estudiantes. 
- El nivel de interés que despierta el proyecto puede ser medido por las consultas que haga el profesor o los estudiantes al final de la exposición.
- Atender a otras indicaciones adicionales por parte del instructor al inicio y durante la presentación. 
- La fecha de entrega máxima para realizar las confirmaciones será el **jueves 20 de enero de 2022 a las 23:59 horas**.