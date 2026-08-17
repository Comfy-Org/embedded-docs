# WanFunInpaintToVideo

El nodo WanFunInpaintToVideo crea secuencias de video mediante inpainting entre imágenes de inicio y fin. Toma condicionamiento positivo y negativo junto con imágenes de fotogramas opcionales para generar latentes de video. El nodo gestiona la generación de video con dimensiones y parámetros de longitud configurables.

## Entradas

| Parámetro | Descripción | Tipo de dato | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negative` | Prompts de condicionamiento negativo a evitar en la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para operaciones de codificación/decodificación | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (por defecto: 832, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (por defecto: 480, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `length` | Número de fotogramas en la secuencia de video (por defecto: 81, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | Número de videos a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida opcional de CLIP Vision para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Imagen opcional de fotograma inicial para la generación de video | IMAGE | No | - |
| `end_image` | Imagen opcional de fotograma final para la generación de video | IMAGE | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Salida de condicionamiento positivo procesado | CONDITIONING |
| `negative` | Salida de condicionamiento negativo procesado | CONDITIONING |
| `latent` | Representación latente del video generado | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
