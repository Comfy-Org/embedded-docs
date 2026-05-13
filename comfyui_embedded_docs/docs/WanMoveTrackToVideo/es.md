> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/es.md)

El nodo WanMoveTrackToVideo prepara datos de condicionamiento y espacio latente para la generación de video, incorporando información opcional de seguimiento de movimiento. Codifica una secuencia de imágenes iniciales en una representación latente y puede combinar datos posicionales de seguimientos de objetos para guiar el movimiento en el video generado. El nodo genera condicionamientos positivo y negativo modificados, junto con un tensor latente vacío listo para un modelo de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo a modificar. |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo a modificar. |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente. |
| `tracks` | TRACKS | No | - | Datos opcionales de seguimiento de movimiento que contienen trayectorias de objetos. |
| `strength` | FLOAT | No | 0.0 - 100.0 | Intensidad del condicionamiento de seguimiento. (predeterminado: 1.0) |
| `width` | INT | No | 16 - MAX_RESOLUTION | El ancho del video de salida. Debe ser divisible por 16. (predeterminado: 832) |
| `height` | INT | No | 16 - MAX_RESOLUTION | La altura del video de salida. Debe ser divisible por 16. (predeterminado: 480) |
| `length` | INT | No | 1 - MAX_RESOLUTION | El número de fotogramas en la secuencia de video. (predeterminado: 81) |
| `batch_size` | INT | No | 1 - 4096 | El tamaño del lote para la salida latente. (predeterminado: 1) |
| `start_image` | IMAGE | Sí | - | La imagen inicial o secuencia de imágenes a codificar. |
| `clip_vision_output` | CLIPVISIONOUTPUT | No | - | Salida opcional del modelo de visión CLIP para agregar al condicionamiento. |

**Nota:** El parámetro `strength` solo tiene efecto cuando se proporcionan `tracks`. Si no se proporcionan `tracks` o `strength` es 0.0, el condicionamiento de seguimiento no se aplica. La `start_image` se utiliza para crear una imagen latente y una máscara para el condicionamiento; si no se proporciona, el nodo solo transmite el condicionamiento y genera un latente vacío.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. |
| `negative` | CONDITIONING | El condicionamiento negativo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. |
| `latent` | LATENT | Un tensor latente vacío con dimensiones determinadas por las entradas `batch_size`, `length`, `height` y `width`. |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
