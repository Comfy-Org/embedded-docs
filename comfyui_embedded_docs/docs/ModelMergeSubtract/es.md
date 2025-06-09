
Este nodo está diseñado para operaciones avanzadas de fusión de modelos, específicamente para restar los parámetros de un modelo de otro basado en un multiplicador especificado. Permite la personalización de los comportamientos del modelo ajustando la influencia de los parámetros de un modelo sobre otro, facilitando la creación de nuevos modelos híbridos.

## Entradas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|------------|-------------|
| `model1`      | `MODEL`    | El modelo base del cual se restarán los parámetros. |
| `model2`      | `MODEL`    | El modelo cuyos parámetros se restarán del modelo base. |
| `multiplier`  | `FLOAT`    | Un valor de punto flotante que escala el efecto de la resta sobre los parámetros del modelo base. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|------------|-------------|
| `model`   | `MODEL`    | El modelo resultante después de restar los parámetros de un modelo de otro, escalado por el multiplicador.
