# WanFirstLastFrameToVideo

El nodo WanFirstLastFrameToVideo crea condicionamiento de video combinando fotogramas de inicio y fin con indicaciones de texto. Genera una representación latente para la generación de video codificando el primer y último fotograma, aplicando máscaras para guiar el proceso de generación e incorporando características de visión CLIP cuando están disponibles. Este nodo prepara condicionamiento tanto positivo como negativo para modelos de video con el fin de generar secuencias coherentes entre puntos de inicio y fin especificados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamiento de texto positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negativo` | Condicionamiento de texto negativo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes al espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_start_image` | Características de visión CLIP extraídas de la imagen de inicio | CLIP_VISION_OUTPUT | No | - |
| `clip_vision_end_image` | Características de visión CLIP extraídas de la imagen de fin | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicial` | Imagen del fotograma de inicio para la secuencia de video | IMAGE | No | - |
| `imagen_final` | Imagen del fotograma de fin para la secuencia de video | IMAGE | No | - |

**Nota:** Cuando se proporcionan tanto `start_image` como `end_image`, el nodo crea una secuencia de video que realiza una transición entre estos dos fotogramas. Los parámetros `clip_vision_start_image` y `clip_vision_end_image` son opcionales, pero cuando se proporcionan, sus características de visión CLIP se concatenan y se aplican tanto al condicionamiento positivo como al negativo. La `start_image` se recorta a los primeros `length` fotogramas, y la `end_image` se recorta a los últimos `length` fotogramas antes del procesamiento.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo con codificación de fotogramas de video aplicada y características de visión CLIP | CONDITIONING |
| `latente` | Condicionamiento negativo con codificación de fotogramas de video aplicada y características de visión CLIP | CONDITIONING |
| `latent` | Tensor latente vacío con dimensiones que coinciden con los parámetros de video especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/es.md)

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
