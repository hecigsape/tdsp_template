# Descripción del Modelo

El modelo baseline es un enfoque combinado de dos redes neuronales para detectar y validar si una imagen contiene un rostro superpuesto.

El proceso se divide en dos etapas. En la primera etapa, se utiliza una red neuronal más rápida (faster) para identificar la ubicación aproximada del rostro en la imagen. Esta detección es rápida pero menos precisa.

En la segunda etapa, una vez obtenidas las coordenadas aproximadas del rostro, se recorta esa región de la imagen original y se pasa a través de una red neuronal convolucional (CNN) para realizar una validación más precisa. La CNN está diseñada para determinar si el rostro recortado corresponde a una imagen superpuesta o no.

El resultado de la predicción se devuelve como un score (puntuación), que indica la probabilidad de que la imagen contenga un rostro superpuesto. Si el score es mayor o igual a 0.5, se considera que la imagen tiene un rostro superpuesto, y se establece el valor de reco como "TRUE". De lo contrario, se considera que la imagen no tiene un rostro superpuesto, y se establece reco como "FALSE".

El modelo baseline utiliza las siguientes variables de entrada: [Lista de variables de entrada utilizadas en el modelo].


## Evaluación del modelo

### Métricas de evaluación

El modelo baseline se evalúa utilizando las siguientes métricas:

- Loss (Pérdida): 0.2349
- Accuracy (Exactitud): 0.9107
- Val_loss (Pérdida en validación): 0.3774
- Val_accuracy (Exactitud en validación): 0.8673

### Resultados de evaluación

A continuación se muestra una tabla con los resultados de evaluación del modelo baseline:

| Métrica       | Resultado |
|---------------|-----------|
| Loss          | 0.2349    |
| Accuracy      | 0.9107    |
| Val_loss      | 0.3774    |
| Val_accuracy  | 0.8673    |

## Análisis de los Resultados

El modelo baseline ha demostrado un rendimiento prometedor en la detección de rostros superpuestos. Entre sus fortalezas se destacan:
- Alta precisión con una exactitud de entrenamiento del 91.07%.
- Buen rendimiento en la validación con una exactitud de validación del 86.73%.

Sin embargo, el modelo baseline también tiene algunas limitaciones:
- La pérdida en validación (val_loss) es mayor que la pérdida en entrenamiento (loss), lo que indica una posible sobreajuste del modelo.

## Conclusiones

En conclusión, el modelo baseline proporciona una línea base para el rendimiento de los modelos posteriores en la detección de rostros superpuestos. Si bien presenta algunas limitaciones, su rendimiento prometedor y alta precisión hacen de este modelo un buen punto de partida.

Para mejorar el rendimiento, se sugiere explorar técnicas de regularización y ajuste de hiperparámetros para reducir el sobreajuste y obtener un mejor equilibrio entre la pérdida y la exactitud en entrenamiento y validación.

## Referencias

- Referencia 1: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
