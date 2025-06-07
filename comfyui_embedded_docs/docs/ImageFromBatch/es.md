El nodo `ImageFromBatch` está diseñado para extraer un segmento específico de imágenes de un lote basado en el índice y la longitud proporcionados. Permite un control más granular sobre las imágenes en lotes, habilitando operaciones en imágenes individuales o subconjuntos dentro de un lote más grande.

## Entradas

| Campo          | Data Type | Descripción                                                                           |
|----------------|-------------|---------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | El lote de imágenes del cual se extraerá un segmento. Este parámetro es crucial para especificar el lote fuente. |
| `batch_index`  | `INT`       | El índice de inicio dentro del lote desde el cual comienza la extracción. Determina la posición inicial del segmento a extraer del lote. |
| `length`       | `INT`       | El número de imágenes a extraer del lote comenzando desde el batch_index. Este parámetro define el tamaño del segmento a extraer. |

## Salidas

| Campo | Data Type | Descripción                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE`    | El segmento extraído de imágenes del lote especificado. Esta salida representa un subconjunto del lote original, determinado por los parámetros batch_index y length. |
