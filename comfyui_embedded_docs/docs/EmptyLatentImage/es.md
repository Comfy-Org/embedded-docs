> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/es.md)

El nodo `EmptyLatentImage` está diseñado para generar una representación de espacio latente en blanco con dimensiones y tamaño de lote especificados. Este nodo sirve como paso fundamental en la generación o manipulación de imágenes en el espacio latente, proporcionando un punto de partida para procesos posteriores de síntesis o modificación de imágenes.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `width`   | `INT`       | Especifica el ancho de la imagen latente a generar. Este parámetro influye directamente en las dimensiones espaciales de la representación latente resultante. |
| `height`  | `INT`       | Determina la altura de la imagen latente a generar. Este parámetro es crucial para definir las dimensiones espaciales de la representación del espacio latente. |
| `batch_size` | `INT` | Controla la cantidad de imágenes latentes a generar en un solo lote. Esto permite la generación simultánea de múltiples representaciones latentes, facilitando el procesamiento por lotes. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un tensor que representa un lote de imágenes latentes en blanco, que sirve como base para la generación o manipulación adicional de imágenes en el espacio latente. |