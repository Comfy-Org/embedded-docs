> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/es.md)

El nodo WanFirstLastFrameToVideo crea condicionamiento de video combinando fotogramas de inicio y fin con indicaciones de texto. Genera una representación latente para la generación de video codificando el primer y último fotograma, aplicando máscaras para guiar el proceso de generación e incorporando características de visión CLIP cuando están disponibles. Este nodo prepara condicionamiento tanto positivo como negativo para modelos de video con el fin de generar secuencias coherentes entre puntos de inicio y fin especificados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Condicionamiento de texto positivo para guiar la generación de video |
| `negativo` | CONDITIONING | Sí | - | Condicionamiento de texto negativo para guiar la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar imágenes al espacio latente |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida (predeterminado: 832, paso: 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida (predeterminado: 480, paso: 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) |
| `tamaño_lote` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `clip_vision_start_image` | CLIP_VISION_OUTPUT | No | - | Características de visión CLIP extraídas de la imagen de inicio |
| `clip_vision_end_image` | CLIP_VISION_OUTPUT | No | - | Características de visión CLIP extraídas de la imagen de fin |
| `imagen_inicial` | IMAGE | No | - | Imagen del fotograma de inicio para la secuencia de video |
| `imagen_final` | IMAGE | No | - | Imagen del fotograma de fin para la secuencia de video |

**Nota:** Cuando se proporcionan tanto `start_image` como `end_image`, el nodo crea una secuencia de video que realiza una transición entre estos dos fotogramas. Los parámetros `clip_vision_start_image` y `clip_vision_end_image` son opcionales, pero cuando se proporcionan, sus características de visión CLIP se concatenan y se aplican tanto al condicionamiento positivo como al negativo. La `start_image` se recorta a los primeros `length` fotogramas, y la `end_image` se recorta a los últimos `length` fotogramas antes del procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo con codificación de fotogramas de video aplicada y características de visión CLIP |
| `latente` | CONDITIONING | Condicionamiento negativo con codificación de fotogramas de video aplicada y características de visión CLIP |
| `latent` | LATENT | Tensor latente vacío con dimensiones que coinciden con los parámetros de video especificados |

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
