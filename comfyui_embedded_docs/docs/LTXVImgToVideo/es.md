# LTXVImgToVideo

LTXVImgToVideo convierte una imagen de entrada en una representación latente de video para modelos de generación de video. Redimensiona la imagen al ancho y alto solicitados, la codifica con el VAE y coloca los fotogramas codificados al inicio de un latente de video lleno de ceros. El control de fuerza (strength) determina cuánto del contenido de la imagen original se conserva frente a lo que se modifica durante la generación del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamientos positivos para guiar la generación del video | CONDITIONING | Sí | - |
| `negativo` | Condicionamientos negativos para evitar ciertos elementos en el video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar la imagen de entrada en el espacio latente | VAE | Sí | - |
| `imagen` | Imagen de entrada que se convertirá en fotogramas de video | IMAGE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 768, paso: 32) | INT | No | 64 a MAX_RESOLUTION |
| `altura` | Alto del video de salida en píxeles (predeterminado: 512, paso: 32) | INT | No | 64 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video generado (predeterminado: 97, paso: 8) | INT | No | 9 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | No | 1 a 4096 |
| `fuerza` | Control sobre cuánto del contenido de la imagen original se conserva en los primeros fotogramas del video generado. Un valor de 1.0 conserva la imagen original por completo, mientras que 0.0 permite la modificación máxima (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |

Nota: `width` y `height` cambian en pasos de 32 píxeles, y `length` cambia en pasos de 8 fotogramas, lo que corresponde a la compresión del latente de video (32x en las dimensiones espaciales y 8x en la dimensión temporal). El latente de video contiene ((length - 1) // 8) + 1 fotogramas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo se transmite sin cambios para usarse con el latente generado | CONDITIONING |
| `negativo` | El condicionamiento negativo se transmite sin cambios para usarse con el latente generado | CONDITIONING |
| `latente` | Representación latente de video que contiene los fotogramas de imagen codificados y una máscara de ruido que controla la intensidad con la que se aplica el condicionamiento durante la generación del video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/es.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
