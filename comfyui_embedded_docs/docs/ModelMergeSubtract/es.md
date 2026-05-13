> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/es.md)

Este nodo está diseñado para operaciones avanzadas de fusión de modelos, específicamente para restar los parámetros de un modelo de otro según un multiplicador especificado. Permite personalizar los comportamientos del modelo ajustando la influencia de los parámetros de un modelo sobre otro, facilitando la creación de nuevos modelos híbridos.

## Entradas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `model1`      | `MODEL`     | El modelo base del cual se restarán los parámetros. |
| `model2`      | `MODEL`     | El modelo cuyos parámetros se restarán del modelo base. |
| `multiplier`  | `FLOAT`     | Un valor de punto flotante que escala el efecto de sustracción sobre los parámetros del modelo base. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo resultante después de restar los parámetros de un modelo de otro, escalados por el multiplicador. |