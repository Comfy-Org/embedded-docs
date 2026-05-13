> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/es.md)

El nodo RepeatLatentBatch está diseñado para replicar un lote determinado de representaciones latentes un número específico de veces, incluyendo potencialmente datos adicionales como máscaras de ruido e índices de lote. Esta funcionalidad es crucial para operaciones que requieren múltiples instancias de los mismos datos latentes, como el aumento de datos o tareas generativas específicas.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes que se replicarán. Es esencial para definir los datos que se someterán a repetición. |
| `amount`  | `INT`       | El parámetro 'amount' especifica el número de veces que se deben repetir las muestras de entrada. Influye directamente en el tamaño del lote de salida, afectando así la carga computacional y la diversidad de los datos generados. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las representaciones latentes de entrada, replicadas según el 'amount' especificado. Puede incluir máscaras de ruido replicadas e índices de lote ajustados, si corresponde. |