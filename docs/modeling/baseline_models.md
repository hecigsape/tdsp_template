
# Descripción del Modelo

El modelo baseline es un enfoque combinado de dos redes neuronales para detectar y validar si una imagen contiene un rostro superpuesto.

El proceso se divide en dos etapas. En la primera etapa, se utiliza una red neuronal más rápida (faster) para identificar la ubicación aproximada del rostro en la imagen. Esta detección es rápida pero menos precisa.

En la segunda etapa, una vez obtenidas las coordenadas aproximadas del rostro, se recorta esa región de la imagen original y se pasa a través de una red neuronal convolucional (CNN) para realizar una validación más precisa. La CNN está diseñada para determinar si el rostro recortado corresponde a una imagen superpuesta o no.

El resultado de la predicción se devuelve como un score (puntuación), que indica la probabilidad de que la imagen contenga un rostro superpuesto. Si el score es mayor o igual a 0.5, se considera que la imagen tiene un rostro superpuesto, y se establece el valor de reco como "TRUE". De lo contrario, se considera que la imagen no tiene un rostro superpuesto, y se establece reco como "FALSE".

El modelo baseline utiliza las siguientes variables de entrada: [Lista de variables de entrada utilizadas en el modelo].

## Evaluación del Modelo

### Métricas de evaluación

El modelo baseline se evalúa utilizando las siguientes métricas:

- Pérdida (Loss): En el conjunto de entrenamiento, la pérdida obtenida fue de 0.2101, mientras que en el conjunto de validación fue de 0.3243. La pérdida es una medida de qué tan lejos están las predicciones del modelo de los valores reales. Un valor de pérdida más bajo indica un mejor rendimiento del modelo.

- Precisión (Accuracy): En el conjunto de entrenamiento, se obtuvo una precisión de 0.9210, mientras que en el conjunto de validación se obtuvo una precisión de 0.8878. La precisión es la proporción de predicciones correctas realizadas por el modelo en relación con el total de muestras. Un valor de precisión más alto indica un mejor rendimiento del modelo.

### Resultados de evaluación

A continuación se muestra una tabla con los resultados de evaluación del modelo baseline:

| Métrica     | Conjunto de entrenamiento | Conjunto de validación |
|-------------|--------------------------|-----------------------|
| Pérdida     | 0.2101                   | 0.3243                |
| Precisión   | 0.9210                   | 0.8878                |

## Análisis de los resultados

El modelo baseline ha mostrado un rendimiento prometedor en la detección de rostros superpuestos. Con una precisión de validación del 88.78%, el modelo es capaz de distinguir de manera efectiva entre imágenes de documentos con rostros superpuestos y sin superponer.

Sin embargo, se observaron algunas limitaciones y áreas de mejora:

- El modelo puede beneficiarse de una mayor cantidad de datos de entrenamiento. Un conjunto de datos más grande y diverso podría ayudar al modelo a aprender características más representativas y mejorar su rendimiento en datos no vistos anteriormente.

- Se deben explorar técnicas adicionales para la detección precisa de rostros superpuestos. La detección inicial basada en el modelo "faster" es rápida pero puede tener limitaciones en la precisión. Investigar enfoques más avanzados, como el uso de redes neuronales más complejas o el ajuste de hiperparámetros, puede mejorar la precisión de la detección inicial.

- Existe la posibilidad de falsos positivos o falsos negativos en la validación final debido a la naturaleza compleja de la detección de rostros superpuestos.

## Conclusiones

En conclusión, el modelo baseline proporciona una línea base para el rendimiento de los modelos posteriores en la detección de rostros superpuestos. Si bien presenta algunas limitaciones, su rendimiento prometedor y alta velocidad hacen de este modelo un buen punto de partida.

Para mejorar el rendimiento, se sugiere explorar técnicas avanzadas de detección y validación de rostros, así como el uso de conjuntos de datos más grandes y diversos para entrenar los modelos.

## Referencias

- Referencia 1: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
