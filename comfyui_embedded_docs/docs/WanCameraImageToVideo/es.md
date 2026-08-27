# WanCameraImageToVideo

El nodo WanCameraImageToVideo prepara los datos de condicionamiento y latentes para la generación de video a partir de imágenes. Toma indicaciones de condicionamiento positivo y negativo, junto con una imagen inicial opcional y controles de cámara opcionales, y produce un condicionamiento modificado además de un tensor latente vacío listo para que un modelo de video lo complete.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Indicaciones de condicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negativo` | Indicaciones de condicionamiento negativo que se deben evitar en la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes al espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_visión_clip` | Salida opcional de CLIP vision para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicio` | Imagen inicial opcional para inicializar la secuencia de video. Cuando se proporciona, los primeros fotogramas del video se basarán en esta imagen, con una máscara aplicada para fusionar los fotogramas iniciales con el contenido generado. La imagen se redimensiona para coincidir con el ancho y alto especificados. | IMAGE | No | - |
| `condiciones_cámara` | Condiciones de incrustación de cámara opcionales para la generación de video. Cuando se proporcionan, estas condiciones se aplican tanto al condicionamiento positivo como al negativo. | WAN_CAMERA_EMBEDDING | No | - |

**Nota:** Cuando se proporciona `start_image`, solo se utilizan los primeros `length` fotogramas de la imagen de entrada para inicializar la secuencia de video, y el nodo aplica una máscara para fusionar estos fotogramas iniciales con el contenido generado. Los parámetros `camera_conditions` y `clip_vision_output` son opcionales, pero cuando se proporcionan, modifican el condicionamiento tanto para las indicaciones positivas como negativas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo modificado con condiciones de cámara, salidas de CLIP vision y/o datos de la imagen inicial aplicados | CONDITIONING |
| `negativo` | Condicionamiento negativo modificado con condiciones de cámara, salidas de CLIP vision y/o datos de la imagen inicial aplicados | CONDITIONING |
| `latente` | Representación latente de video vacía generada para usar con modelos de video. El tensor latente tiene dimensiones [batch_size, 16, frames, height/8, width/8] donde frames se calcula como ((length - 1) // 4) + 1. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
