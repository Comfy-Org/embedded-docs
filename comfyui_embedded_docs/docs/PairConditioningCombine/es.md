> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/es.md)

El nodo PairConditioningCombine combina dos pares de datos de condicionamiento (positivo y negativo) en un solo par. Toma dos pares de condicionamiento separados como entrada y los fusiona utilizando la lógica interna de combinación de condicionamiento de ComfyUI. Este nodo es experimental y se utiliza principalmente para flujos de trabajo avanzados de manipulación de condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo_A` | CONDITIONING | Sí | - | Primera entrada de condicionamiento positivo |
| `negativo_A` | CONDITIONING | Sí | - | Primera entrada de condicionamiento negativo |
| `positivo_B` | CONDITIONING | Sí | - | Segunda entrada de condicionamiento positivo |
| `negativo_B` | CONDITIONING | Sí | - | Segunda entrada de condicionamiento negativo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Salida de condicionamiento positivo combinado |
| `negative` | CONDITIONING | Salida de condicionamiento negativo combinado |