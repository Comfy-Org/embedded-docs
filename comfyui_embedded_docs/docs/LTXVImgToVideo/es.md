El nodo LTXVImgToVideo convierte una imagen de entrada en una representación latente de video para modelos de generación de video. Toma una sola imagen y la extiende a una secuencia de fotogramas utilizando el codificador VAE, luego aplica condicionamiento con control de intensidad para determinar cuánto del contenido de la imagen original se conserva versus se modifica durante la generación del video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamiento positivo para guiar la generación del video | CONDITIONING | Sí | - |
| `negativo` | Prompts de condicionamiento negativo para evitar ciertos elementos en el video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar la imagen de entrada en el espacio latente | VAE | Sí | - |
| `imagen` | Imagen de entrada que se convertirá en fotogramas de video | IMAGE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 768, paso: 32) | INT | No | 64 a MAX_RESOLUTION |
| `altura` | Alto del video de salida en píxeles (predeterminado: 512, paso: 32) | INT | No | 64 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video generado (predeterminado: 97, paso: 8) | INT | No | 9 a MAX_RESOLUTION |
| `tamaño_lote` | Cantidad de videos a generar simultáneamente (predeterminado: 1) | INT | No | 1 a 4096 |
| `fuerza` | Control sobre cuánto del contenido de la imagen original se conserva en el primer fotograma del video generado. Un valor de 1.0 conserva la imagen original por completo, mientras que 0.0 permite la máxima modificación (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo procesado con enmascaramiento de fotogramas de video aplicado | CONDITIONING |
| `negativo` | Condicionamiento negativo procesado con enmascaramiento de fotogramas de video aplicado | CONDITIONING |
| `latente` | Representación latente de video que contiene los fotogramas codificados y la máscara de ruido para la generación del video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/es.md)

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
