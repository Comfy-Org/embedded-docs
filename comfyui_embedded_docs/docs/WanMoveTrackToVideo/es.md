El nodo WanMoveTrackToVideo prepara datos de condicionamiento y espacio latente para la generación de video, incorporando información opcional de seguimiento de movimiento. Codifica una secuencia de imágenes iniciales en una representación latente y puede combinar datos posicionales de seguimientos de objetos para guiar el movimiento en el video generado. El nodo genera condicionamientos positivo y negativo modificados, junto con un tensor latente vacío listo para un modelo de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo a modificar. | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo a modificar. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí | - |
| `pistas` | Datos opcionales de seguimiento de movimiento que contienen trayectorias de objetos. | TRACKS | No | - |
| `fuerza` | Intensidad del condicionamiento de seguimiento. (predeterminado: 1.0) | FLOAT | No | 0.0 - 100.0 |
| `ancho` | El ancho del video de salida. Debe ser divisible por 16. (predeterminado: 832) | INT | No | 16 - MAX_RESOLUTION |
| `alto` | La altura del video de salida. Debe ser divisible por 16. (predeterminado: 480) | INT | No | 16 - MAX_RESOLUTION |
| `longitud` | El número de fotogramas en la secuencia de video. (predeterminado: 81) | INT | No | 1 - MAX_RESOLUTION |
| `tamaño_lote` | El tamaño del lote para la salida latente. (predeterminado: 1) | INT | No | 1 - 4096 |
| `imagen_inicial` | La imagen inicial o secuencia de imágenes a codificar. | IMAGE | Sí | - |
| `clip_vision_output` | Salida opcional del modelo de visión CLIP para agregar al condicionamiento. | CLIPVISIONOUTPUT | No | - |

**Nota:** El parámetro `strength` solo tiene efecto cuando se proporcionan `tracks`. Si no se proporcionan `tracks` o `strength` es 0.0, el condicionamiento de seguimiento no se aplica. La `start_image` se utiliza para crear una imagen latente y una máscara para el condicionamiento; si no se proporciona, el nodo solo transmite el condicionamiento y genera un latente vacío.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. | CONDITIONING |
| `latente` | Un tensor latente vacío con dimensiones determinadas por las entradas `tamaño_lote`, `longitud`, `alto` y `ancho`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/es.md)

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
