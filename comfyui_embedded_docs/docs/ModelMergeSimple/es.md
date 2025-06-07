
El nodo ModelMergeSimple está diseñado para fusionar dos modelos mediante la mezcla de sus parámetros según una proporción especificada. Este nodo facilita la creación de modelos híbridos que combinan las fortalezas o características de ambos modelos de entrada.

El parámetro `ratio` determina la proporción de mezcla entre los dos modelos. Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | El primer modelo a fusionar. Sirve como el modelo base sobre el cual se aplican parches del segundo modelo. |
| `model2`  | `MODEL`     | El segundo modelo cuyos parches se aplican al primer modelo, influenciado por la proporción especificada. |
| `ratio`   | `FLOAT`     | Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo resultante de la fusión, que incorpora elementos de ambos modelos de entrada según la proporción especificada. |
