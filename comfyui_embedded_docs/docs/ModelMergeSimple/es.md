> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/es.md)

El nodo ModelMergeSimple está diseñado para fusionar dos modelos combinando sus parámetros en función de una proporción especificada. Este nodo facilita la creación de modelos híbridos que integran las fortalezas o características de ambos modelos de entrada.

El parámetro `ratio` determina la proporción de mezcla entre los dos modelos. Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | El primer modelo a fusionar. Actúa como modelo base sobre el cual se aplican los parches del segundo modelo. |
| `model2`  | `MODEL`     | El segundo modelo cuyos parches se aplican sobre el primer modelo, influenciados por la proporción especificada. |
| `ratio`   | `FLOAT`     | Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo fusionado resultante, que incorpora elementos de ambos modelos de entrada según la proporción especificada. |