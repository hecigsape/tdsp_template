# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos del proyecto de reconocimiento de rostros superpuestos en documentos.

## Resumen general de los datos

- Número total de observaciones: 500
- Número de variables: X (variables relevantes para el reconocimiento de rostros superpuestos)
- Tipo de variables: Variables de imagen y variables categóricas (clase objetivo)
- Valores faltantes: No se encontraron valores faltantes en las variables relevantes.
- Distribución de las variables: Las variables de imagen representan rostros en documentos, y la variable categórica indica si el rostro está superpuesto o no.

## Resumen de calidad de los datos

- Valores faltantes: No se encontraron valores faltantes en las variables relevantes.
- Valores extremos: No se identificaron valores extremos en las variables relevantes.
- Errores: No se detectaron errores evidentes en los datos.
- Duplicados: No se encontraron observaciones duplicadas en los datos relevantes.

## Variable objetivo

La variable objetivo es la clasificación de rostros superpuestos en documentos. A continuación, se muestra la distribución de la variable y un gráfico que ayuda a entender mejor su comportamiento.

[Insertar gráfico de distribución de la variable objetivo]

## Variables individuales

A continuación, se presenta un análisis detallado de cada variable individual relevante:

1. Variable de imagen docuemnto superpuesto: 
 imagen ejemplo de un docuemnto superpuesto, se han sensurado las parte sensibles del docuemnto aplicando un filtro gausiano 
![methods](images/example_false.png)

3. Variable de imagen docuemnto real: 
imagen ejemplo de un docuemnto real,se han sensurado las parte sensibles del docuemnto aplicando un filtro gausiano 

![methods](images/example_true.png)

En conclusión, el proyecto tiene como objetivo desarrollar un sistema de reconocimiento de rostros en documentos que pueda clasificar si una imagen de rostro está superpuesta o no. Se busca mejorar la seguridad y confiabilidad de los procesos que dependen de la autenticidad de las imágenes faciales, previniendo situaciones de fraude o manipulación en documentos.
