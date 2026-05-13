> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/es.md)

El nodo WanCameraImageToVideo convierte imágenes en secuencias de video generando representaciones latentes para la generación de video. Procesa las entradas de condicionamiento e imágenes de inicio opcionales para crear latentes de video que pueden utilizarse con modelos de video. El nodo admite condiciones de cámara y salidas de visión CLIP para un control mejorado de la generación de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento positivo para la generación de video |
| `negativo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento negativo a evitar en la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para codificar imágenes al espacio latente |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) |
| `tamaño_lote` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `salida_visión_clip` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para condicionamiento adicional |
| `imagen_inicio` | IMAGE | No | - | Imagen de inicio opcional para inicializar la secuencia de video. Cuando se proporciona, los primeros fotogramas del video se basarán en esta imagen, con una máscara aplicada para fusionar los fotogramas iniciales con el contenido generado. La imagen se redimensiona para coincidir con el ancho y alto especificados. |
| `condiciones_cámara` | WAN_CAMERA_EMBEDDING | No | - | Condiciones de incrustación de cámara opcionales para la generación de video. Cuando se proporcionan, estas condiciones se aplican tanto al condicionamiento positivo como al negativo. |

**Nota:** Cuando se proporciona `start_image`, el nodo lo utiliza para inicializar la secuencia de video y aplica un enmascaramiento para fusionar los fotogramas iniciales con el contenido generado. Los parámetros `camera_conditions` y `clip_vision_output` son opcionales, pero cuando se proporcionan, modifican el condicionamiento tanto para las indicaciones positivas como negativas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo modificado con condiciones de cámara y salidas de visión CLIP aplicadas |
| `latente` | CONDITIONING | Condicionamiento negativo modificado con condiciones de cámara y salidas de visión CLIP aplicadas |
| `latent` | LATENT | Representación latente de video generada para usar con modelos de video. El tensor latente tiene dimensiones [batch_size, 16, frames, height/8, width/8] donde frames se calcula como ((length - 1) // 4) + 1. |

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
