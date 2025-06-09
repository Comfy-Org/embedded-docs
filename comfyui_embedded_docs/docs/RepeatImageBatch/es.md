
El nodo RepeatImageBatch está diseñado para replicar una imagen dada un número específico de veces, creando un lote de imágenes idénticas. Esta funcionalidad es útil para operaciones que requieren múltiples instancias de la misma imagen, como el procesamiento por lotes o la ampliación de datos.

## Entradas

| Campo   | Data Type | Descripción                                                                 |
|---------|-------------|-----------------------------------------------------------------------------|
| `image` | `IMAGE`     | El parámetro 'image' representa la imagen que se va a replicar. Es crucial para definir el contenido que se duplicará en todo el lote. |
| `amount`| `INT`       | El parámetro 'amount' especifica el número de veces que la imagen de entrada debe replicarse. Influye directamente en el tamaño del lote de salida, permitiendo una creación de lotes flexible. |

## Salidas

| Campo | Data Type | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La salida es un lote de imágenes, cada una idéntica a la imagen de entrada, replicada según el 'amount' especificado. |
