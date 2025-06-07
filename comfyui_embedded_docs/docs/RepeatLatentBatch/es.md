
El nodo RepeatLatentBatch está diseñado para replicar un lote dado de representaciones latentes un número específico de veces, potencialmente incluyendo datos adicionales como máscaras de ruido e índices de lote. Esta funcionalidad es crucial para operaciones que requieren múltiples instancias del mismo dato latente, como la augmentación de datos o tareas generativas específicas.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes a replicar. Es esencial para definir los datos que se someterán a repetición. |
| `amount`  | `INT`       | El parámetro 'amount' especifica el número de veces que se deben repetir las muestras de entrada. Influye directamente en el tamaño del lote de salida, afectando así la carga computacional y la diversidad de los datos generados. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las representaciones latentes de entrada, replicadas según el 'amount' especificado. Puede incluir máscaras de ruido replicadas e índices de lote ajustados, si es aplicable. |
