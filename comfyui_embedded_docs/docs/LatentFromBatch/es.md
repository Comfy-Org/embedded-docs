
Este nodo está diseñado para extraer un subconjunto específico de muestras latentes de un lote dado basado en el índice de lote y la longitud especificados. Permite el procesamiento selectivo de muestras latentes, facilitando operaciones en segmentos más pequeños del lote para eficiencia o manipulación dirigida.

## Entradas

| Parámetro     | Data Type | Descripción |
|---------------|-------------|-------------|
| `samples`     | `LATENT`    | La colección de muestras latentes de la cual se extraerá un subconjunto. Este parámetro es crucial para determinar el lote fuente de muestras a procesar. |
| `batch_index` | `INT`       | Especifica el índice de inicio dentro del lote desde el cual comenzará el subconjunto de muestras. Este parámetro permite la extracción dirigida de muestras desde posiciones específicas en el lote. |
| `length`      | `INT`       | Define el número de muestras a extraer desde el índice de inicio especificado. Este parámetro controla el tamaño del subconjunto a procesar, permitiendo una manipulación flexible de los segmentos del lote. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | El subconjunto extraído de muestras latentes, ahora disponible para un procesamiento o análisis posterior. |
