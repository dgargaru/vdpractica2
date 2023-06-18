# Proyecto para análisis de datos meteorológicos en España
## 1. Introducción
Con el fin de elaborar la última práctica de la asignatura de visualización de datos del Máster de ciencias de datos se ha elaborado un proyecto para el análisis del posible cambio climático mediante distintas técnicas de visualización. 
Por medio de las representaciones gráficas el ser humano es capaz de comunicar sencilla y efizcamente una cantidad de datos interpretables y susceptibles de convertirse en información.
Gracias a la conjunción de estas técnicas en un cuadro de mandos o Dashboard se puede obtener información de los procesos previos de obtención y tratamiento de datos provenientes de distintas fuentes.

## 2. Objetivo

El principal objetivo de este proyecto se centra en la posibilidad de poder sacar conclusiones en base a las visualizaciones y poder dar respuesta a preguntas como: 
  - ¿Se ha producido un cambio en el clima en los últimos años?.
  - El cambio climático producido ha sido beneficioso o perjudicial.

## 3.Recursos

### 3.1 Conjunto de datos

La fase de obtención de datos se centra en la adquisición proveniente de la AEMET y en concreto en distintos conjuntos de datos en ficheros en formato csv de los años desde el 2000 hasta el 2022. Dentro de cada fichero existen una amplia variedad de métricas de entre las cuales se han seleccionado las siguientes: 

  - ta_max:    Temperatura máxima absoluta del mes/año y fecha
  - ta_min:    Temperatura mínima absoluta del mes/año y fecha
  - tm_mes:    Temperatura media mensual/anual
  - nt_30:     Nº de días de temperatura máxima mayor o igual que 30 °C
  - n_llu:     Nº de días de lluvia en el mes/año
  - n_nie:     Nº de días de nieve en el mes/año
  - n_tor:     Nº de días de tormenta en el mes/año

### 3.2 Herramientas

Para obtener el proyecto de visualización final se ha usado la aplicación online y gratuita llamada Fluorish que con el plan gratuito y únicamente darse de alta nos permite la elaboración y publicación de múltiples tipos de visualicaciones e incluso historias de visualizaciones. El único inconveniente que se presenta es la imposiblidad de crear proyectos interactivos de múltiples visualizaciones unidas.

El complemente perfecto ha sido la creación de una página web en formato HTML capaz de fusionar las técnicas de visualización creadas en Fluorish con la capacidad de añadir interactividad.

## 4. Procesamiento de datos

En este apartado ha sido necesario unificar los múltiples ficheros en formato csv ya que estaban divididos por ciudad y año. Para ello fue necesario la realización de los siguientes pasos: 
   - La creación de un script en Python capaz de unificar los ficheros csv.
   - Añadir una columna en cada fichero resultante de ciudad con el nombre de la misma.
   - Crear cada conjunto de datos para cada técnica de visualización con los campos correspondientes y poder alimentar a FLuorish.
   - Creación de visualizaciones en Fluorish
   - Creación del fichero html para unificar los distintos trabajos hechos en Fluorish y crear el proyecto final.

## 5. Visualiciones

El proyecto se divide en tres grandes bloques de visualizaciones que representan: 
   - La descripción del proyecto
   - Los gráficos correspondientes a los datos del calentamiento de las temperaturas de las ciudades de Barcelona y Córdoba.
   - Los gráficos de las precipitaciones de las ciudades de Barcelona y Córdoba.
   - Los gráficos de las distintas mediciones de la evolución de temperatura de las ciudades de Barcelona y Córdoba.
     
