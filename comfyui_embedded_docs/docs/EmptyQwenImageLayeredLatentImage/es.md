El nodo "Empty Qwen Image Layered Latent" crea una representación latente en blanco y multicapa para su uso con modelos de imagen Qwen. Genera un tensor lleno de ceros, estructurado con un número específico de capas, tamaño de lote y dimensiones espaciales. Este latente vacío sirve como punto de partida para flujos de trabajo posteriores de generación o manipulación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente a crear. El valor debe ser divisible entre 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | La altura de la imagen latente a crear. El valor debe ser divisible entre 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION |
| `capas` | El número de capas adicionales a añadir a la estructura latente. Esto define la profundidad de la representación latente. (predeterminado: 3) | INT | Sí | 0 a MAX_RESOLUTION |
| `tamaño_lote` | El número de muestras latentes a generar en un lote. (predeterminado: 1) | INT | No | 1 a 4096 |

**Nota:** Los parámetros `width` y `height` se dividen internamente entre 8 para determinar las dimensiones espaciales del tensor latente de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | Un tensor latente lleno de ceros. Su forma es `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `99497e3e4a67bf7b3f650573e7b8eb2d7fad6be5819b7ebbbb8736291dc44e0c`
