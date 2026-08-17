# WanFirstLastFrameToVideo

El nodo WanFirstLastFrameToVideo crea condicionamiento de video al combinar los fotogramas inicial y final con indicaciones de texto. Genera una representación latente para la generación de video codificando el primer y el último fotograma, aplicando máscaras para guiar el proceso de generación e incorporando características de visión de CLIP cuando estén disponibles. Este nodo prepara tanto el condicionamiento positivo como el negativo para modelos de video, con el fin de generar secuencias coherentes entre los puntos inicial y final especificados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamiento de texto positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negative` | Condicionamiento de texto negativo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes al espacio latente | VAE | Sí | - |
| `width` | Ancho del video de salida (por defecto: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video de salida (por defecto: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas en la secuencia de video (por defecto: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (por defecto: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_start_image` | Características de visión de CLIP extraídas de la imagen inicial | CLIP_VISION_OUTPUT | No | - |
| `clip_vision_end_image` | Características de visión de CLIP extraídas de la imagen final | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Imagen del fotograma inicial de la secuencia de video | IMAGE | No | - |
| `end_image` | Imagen del fotograma final de la secuencia de video | IMAGE | No | - |

**Nota:** Cuando se proporcionan tanto `start_image` como `end_image`, el nodo crea una secuencia de video que hace la transición entre estos dos fotogramas. La `start_image` se recorta a los primeros `length` fotogramas, y la `end_image` se recorta a los últimos `length` fotogramas antes del procesamiento. Si solo se proporciona una de ellas, el lado faltante se rellena con fotogramas grises neutros. La máscara se establece en 0 donde están presentes los fotogramas inicial y final, y en 1 en el resto. Los parámetros `clip_vision_start_image` y `clip_vision_end_image` son opcionales; cuando se proporcionan ambos, sus características de visión de CLIP se concatenan y se aplican tanto al condicionamiento positivo como al negativo. Cuando solo se proporciona uno, sus características se usan por sí solas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo con la codificación de fotogramas de video aplicada y las características de visión de CLIP | CONDITIONING |
| `negative` | Condicionamiento negativo con la codificación de fotogramas de video aplicada y las características de visión de CLIP | CONDITIONING |
| `latent` | Tensor latente vacío con dimensiones que coinciden con los parámetros de video especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/es.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
