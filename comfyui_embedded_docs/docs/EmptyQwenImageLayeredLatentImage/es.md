> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/es.md)

El nodo Empty Qwen Image Layered Latent crea una representación latente en blanco y multicapa para su uso con modelos de imagen Qwen. Genera un tensor lleno de ceros, estructurado con un número específico de capas, tamaño de lote y dimensiones espaciales. Este latente vacío sirve como punto de partida para flujos de trabajo posteriores de generación o manipulación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho de la imagen latente a crear. El valor debe ser divisible por 16. (por defecto: 640) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | La altura de la imagen latente a crear. El valor debe ser divisible por 16. (por defecto: 640) |
| `layers` | INT | Sí | 0 a MAX_RESOLUTION | El número de capas adicionales para agregar a la estructura latente. Esto define la profundidad de la representación latente. (por defecto: 3) |
| `batch_size` | INT | No | 1 a 4096 | El número de muestras latentes a generar en un lote. (por defecto: 1) |

**Nota:** Los parámetros `width` y `height` se dividen internamente por 8 para determinar las dimensiones espaciales del tensor latente de salida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tensor latente lleno de ceros. Su forma es `[batch_size, 16, layers + 1, height // 8, width // 8]`. |
