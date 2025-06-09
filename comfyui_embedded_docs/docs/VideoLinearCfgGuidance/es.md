
El nodo VideoLinearCFGGuidance aplica una escala de guía de condicionamiento lineal a un modelo de video, ajustando la influencia de los componentes condicionados y no condicionados en un rango especificado. Esto permite un control dinámico sobre el proceso de generación, permitiendo un ajuste fino de la salida del modelo basado en el nivel deseado de condicionamiento.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El parámetro model representa el modelo de video al que se aplicará la guía CFG lineal. Es crucial para definir el modelo base que será modificado con la escala de guía. |
| `min_cfg` | `FLOAT`     | El parámetro min_cfg especifica la escala mínima de guía de condicionamiento a aplicar, sirviendo como punto de partida para el ajuste de la escala lineal. Juega un papel clave en la determinación del límite inferior de la escala de guía, influyendo en la salida del modelo. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | La salida es una versión modificada del modelo de entrada, con la escala de guía CFG lineal aplicada. Este modelo ajustado es capaz de generar salidas con diferentes grados de condicionamiento, basado en la escala de guía especificada. |
