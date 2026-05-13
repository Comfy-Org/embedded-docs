> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/es.md)

ModelMergeBlocks está diseñado para operaciones avanzadas de fusión de modelos, permitiendo la integración de dos modelos con proporciones de mezcla personalizables para diferentes partes de los mismos. Este nodo facilita la creación de modelos híbridos al fusionar selectivamente componentes de dos modelos fuente según parámetros específicos.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `modelo1`  | `MODEL`     | El primer modelo a fusionar. Sirve como modelo base sobre el cual se aplican los parches del segundo modelo. |
| `modelo2`  | `MODEL`     | El segundo modelo del cual se extraen y aplican parches al primer modelo, según las proporciones de mezcla especificadas. |
| `entrada`   | `FLOAT`     | Especifica la proporción de mezcla para la capa de entrada de los modelos. Determina cuánto de la capa de entrada del segundo modelo se fusiona en el primer modelo. |
| `medio`  | `FLOAT`     | Define la proporción de mezcla para las capas intermedias de los modelos. Este parámetro controla el nivel de integración de las capas intermedias de los modelos. |
| `salida`     | `FLOAT`     | Determina la proporción de mezcla para la capa de salida de los modelos. Afecta la salida final ajustando la contribución de la capa de salida del segundo modelo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | El modelo fusionado resultante, que es un híbrido de los dos modelos de entrada con parches aplicados según las proporciones de mezcla especificadas. |