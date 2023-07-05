# Diccionario de datos

## Se tiene 3 datageneradors como se describen a continuacion:

| Generador       | Descripción                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| `train_generator` | Generador de datos para el conjunto de entrenamiento. Contiene 291 imágenes validadas pertenecientes a 2 clases. |
| `test_generator`  | Generador de datos para el conjunto de prueba. Contiene 97 imágenes validadas pertenecientes a 2 clases.         |
| `val_generator`   | Generador de datos para el conjunto de validación. Contiene 98 imágenes validadas pertenecientes a 2 clases.      |

Estos generadores de datos son utilizados para alimentar el modelo de aprendizaje automático durante el entrenamiento, prueba y validación del mismo.

La función `create_data_generator` toma como entrada la siguiente ruta: `/content/drive/MyDrive/DIPLOMADO/DATA-SUPER/DATA_ORG/`. Esta ruta contiene subdirectorios correspondientes a las clases "True" y "False".
