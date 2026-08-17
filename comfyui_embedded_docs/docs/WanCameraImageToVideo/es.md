# WanCameraImageToVideo

WanCameraImageToVideo prepara el condicionamiento y los datos latentes para la generación de video a partir de imágenes. Toma indicaciones de condicionamiento positivas y negativas, junto con imágenes iniciales opcionales y controles de cámara, y genera un condicionamiento modificado y un tensor latente vacío listo para que un modelo de video lo complete.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamiento positivos para la generación de video | CONDITIONING | Sí | - |
| `negative` | Prompts de condicionamiento negativos que se deben evitar en la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes al espacio latente | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (valor predeterminado: 832, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `height` | Altura del video de salida en píxeles (valor predeterminado: 480, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `length` | Número de fotogramas en la secuencia de video (valor predeterminado: 81, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (valor predeterminado: 1) | INT | Sí | 1 to 4096 |
| `clip_vision_output` | Salida de CLIP vision opcional para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Imagen inicial opcional para inicializar la secuencia de video. Cuando se proporciona, los primeros fotogramas del video se basarán en esta imagen, con una máscara aplicada para fusionar los fotogramas iniciales con el contenido generado. La imagen se redimensiona para ajustarse al ancho y alto especificados. | IMAGE | No | - |
| `camera_conditions` | Condiciones de incrustación de cámara opcionales para la generación de video. Cuando se proporcionan, estas condiciones se aplican tanto al condicionamiento positivo como al negativo. | WAN_CAMERA_EMBEDDING | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo lo usa para inicializar la secuencia de video y aplica enmascaramiento para fusionar los fotogramas iniciales con el contenido generado. Los parámetros `camera_conditions` y `clip_vision_output` son opcionales, pero cuando se proporcionan, modifican el condicionamiento tanto para los prompts positivos como negativos.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con condiciones de cámara aplicadas, salidas de CLIP vision y/o datos de la imagen inicial | CONDITIONING |
| `negative` | Condicionamiento negativo modificado con condiciones de cámara aplicadas, salidas de CLIP vision y/o datos de la imagen inicial | CONDITIONING |
| `latent` | Representación latente de video vacía generada para usar con modelos de video. El tensor latente tiene dimensiones [batch_size, 16, frames, height/8, width/8], donde frames se calcula como ((length - 1) // 4) + 1. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
