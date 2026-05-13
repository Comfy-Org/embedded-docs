> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/es.md)

El nodo LTXVImgToVideo convierte una imagen de entrada en una representación latente de video para modelos de generación de video. Toma una sola imagen y la extiende a una secuencia de fotogramas utilizando el codificador VAE, luego aplica condicionamiento con control de intensidad para determinar cuánto del contenido de la imagen original se conserva versus se modifica durante la generación del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Prompts de condicionamiento positivo para guiar la generación del video |
| `negativo` | CONDITIONING | Sí | - | Prompts de condicionamiento negativo para evitar ciertos elementos en el video |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar la imagen de entrada en el espacio latente |
| `imagen` | IMAGE | Sí | - | Imagen de entrada que se convertirá en fotogramas de video |
| `ancho` | INT | No | 64 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 768, paso: 32) |
| `altura` | INT | No | 64 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 512, paso: 32) |
| `longitud` | INT | No | 9 a MAX_RESOLUTION | Número de fotogramas en el video generado (predeterminado: 97, paso: 8) |
| `tamaño_lote` | INT | No | 1 a 4096 | Cantidad de videos a generar simultáneamente (predeterminado: 1) |
| `fuerza` | FLOAT | No | 0.0 a 1.0 | Control sobre cuánto del contenido de la imagen original se conserva en el primer fotograma del video generado. Un valor de 1.0 conserva la imagen original por completo, mientras que 0.0 permite la máxima modificación (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo procesado con enmascaramiento de fotogramas de video aplicado |
| `latente` | CONDITIONING | Condicionamiento negativo procesado con enmascaramiento de fotogramas de video aplicado |
| `latent` | LATENT | Representación latente de video que contiene los fotogramas codificados y la máscara de ruido para la generación del video |

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
