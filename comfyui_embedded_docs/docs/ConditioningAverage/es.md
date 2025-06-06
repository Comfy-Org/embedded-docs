El nodo ConditioningAverage está diseñado para mezclar dos conjuntos de datos de condicionamiento, aplicando un promedio ponderado basado en una fuerza especificada. Este proceso permite el ajuste dinámico de la influencia del condicionamiento, facilitando el ajuste fino del contenido o características generadas.
## Tipos de entrada

| Parámetro             | Comfy dtype        | Descripción |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Representa el conjunto principal de datos de condicionamiento al que se aplicará la mezcla. Sirve como base para la operación de promedio ponderado. |
| `conditioning_from`   | `CONDITIONING`     | Denota el conjunto secundario de datos de condicionamiento que se mezclará en el conjunto principal. Estos datos influyen en el resultado final basado en la fuerza especificada. |
| `conditioning_to_strength` | `FLOAT` | Un valor escalar que determina la fuerza de la mezcla entre los datos de condicionamiento primarios y secundarios. Influye directamente en el equilibrio del promedio ponderado. |

## Tipos de salida

| Parámetro            | Comfy dtype        | Descripción |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | El resultado de mezclar los datos de condicionamiento primarios y secundarios, produciendo un nuevo conjunto de condicionamiento que refleja el promedio ponderado. |