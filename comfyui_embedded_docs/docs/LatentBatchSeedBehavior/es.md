El nodo LatentBatchSeedBehavior está diseñado para modificar el comportamiento de la semilla de un lote de muestras latentes. Permite aleatorizar o fijar la semilla en todo el lote, influyendo así en el proceso de generación al introducir variabilidad o mantener la consistencia en los resultados generados.

## Entradas

| Parámetro       | Data Type | Descripción |
|-----------------|--------------|-------------|
| `samples`       | `LATENT`     | El parámetro 'samples' representa el lote de muestras latentes a procesar. Su modificación depende del comportamiento de la semilla elegido, afectando la consistencia o variabilidad de los resultados generados. |
| `seed_behavior`  | COMBO[STRING] | El parámetro 'seed_behavior' dicta si la semilla para el lote de muestras latentes debe ser aleatorizada o fijada. Esta elección impacta significativamente el proceso de generación al introducir variabilidad o asegurar consistencia en todo el lote. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las muestras latentes de entrada, con ajustes realizados según el comportamiento de la semilla especificado. Mantiene o altera el índice del lote para reflejar el comportamiento de la semilla elegido. |
