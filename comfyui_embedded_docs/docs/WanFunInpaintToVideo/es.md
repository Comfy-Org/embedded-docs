# WanFunInpaintToVideo

El nodo WanFunInpaintToVideo crea secuencias de video mediante la técnica de inpainting entre las imágenes de inicio y fin. Acepta condicionamientos positivos y negativos junto con imágenes de cuadro opcionales para generar latentes de video. El nodo maneja la generación de video con dimensiones y parámetros de longitud configurables.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negativo` | Condicionamiento negativo para evitar en la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para operaciones de codificación/decodificación | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (por defecto: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (por defecto: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de cuadros en la secuencia de video (por defecto: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_de_lote` | Número de videos a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida de visión CLIP opcional utilizada como condicionamiento para la imagen de inicio | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicial` | Imagen de cuadro inicial opcional para la generación de video | IMAGE | No | - |
| `imagen_final` | Imagen de cuadro final opcional para la generación de video | IMAGE | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Salida de condicionamiento positivo procesado | CONDITIONING |
| `negativo` | Salida de condicionamiento negativo procesado | CONDITIONING |
| `latente` | Representación latente de video generada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
