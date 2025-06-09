El nodo `EmptyLatentImage` está diseñado para generar una representación de espacio latente en blanco con dimensiones y tamaño de lote especificados. Este nodo sirve como un paso fundamental en la generación o manipulación de imágenes en el espacio latente, proporcionando un punto de partida para procesos adicionales de síntesis o modificación de imágenes.

## Entradas

| Parámetro   | Data Type | Descripción |
|-------------|-------------|-------------|
| `width`     | `INT`       | Especifica el ancho de la imagen latente a generar. Este parámetro influye directamente en las dimensiones espaciales de la representación latente resultante. |
| `height`    | `INT`       | Determina la altura de la imagen latente a generar. Este parámetro es crucial para definir las dimensiones espaciales de la representación del espacio latente. |
| `batch_size`| `INT`       | Controla el número de imágenes latentes a generar en un solo lote. Esto permite la generación de múltiples representaciones latentes simultáneamente, facilitando el procesamiento por lotes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un tensor que representa un lote de imágenes latentes en blanco, sirviendo como base para la generación o manipulación adicional de imágenes en el espacio latente. |
