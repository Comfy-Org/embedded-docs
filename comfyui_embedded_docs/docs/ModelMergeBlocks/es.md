
ModelMergeBlocks está diseñado para operaciones avanzadas de fusión de modelos, permitiendo la integración de dos modelos con proporciones de mezcla personalizables para diferentes partes de los modelos. Este nodo facilita la creación de modelos híbridos al fusionar selectivamente componentes de dos modelos fuente según parámetros especificados.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|------------|-------------|
| `model1`  | `MODEL`    | El primer modelo a fusionar. Sirve como el modelo base sobre el cual se aplican parches del segundo modelo. |
| `model2`  | `MODEL`    | El segundo modelo del cual se extraen parches y se aplican al primer modelo, según las proporciones de mezcla especificadas. |
| `input`   | `FLOAT`    | Especifica la proporción de mezcla para la capa de entrada de los modelos. Determina cuánto de la capa de entrada del segundo modelo se fusiona en el primer modelo. |
| `middle`  | `FLOAT`    | Define la proporción de mezcla para las capas intermedias de los modelos. Este parámetro controla el nivel de integración de las capas intermedias de los modelos. |
| `out`     | `FLOAT`    | Determina la proporción de mezcla para la capa de salida de los modelos. Afecta la salida final ajustando la contribución de la capa de salida del segundo modelo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|------------|-------------|
| `model`   | `MODEL`    | El modelo resultante de la fusión, que es un híbrido de los dos modelos de entrada con parches aplicados según las proporciones de mezcla especificadas. |
