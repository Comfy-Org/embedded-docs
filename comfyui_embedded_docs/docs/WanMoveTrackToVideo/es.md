# WanMoveTrackToVideo

El nodo WanMoveTrackToVideo prepara datos de acondicionamiento y latentes para la generación de video. Codifica una secuencia de imágenes inicial en el espacio latente utilizando un VAE y puede incorporar opcionalmente información de seguimiento de movimiento para guiar el movimiento de objetos en el video generado. El nodo genera acondicionamiento positivo y negativo modificado junto con un tensor latente vacío listo para un modelo de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | La entrada de acondicionamiento positivo que se modificará. | CONDITIONING | Sí | - |
| `negative` | La entrada de acondicionamiento negativo que se modificará. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí | - |
| `tracks` | Datos opcionales de seguimiento de movimiento que contienen rutas de objetos. | TRACKS | No | - |
| `strength` | Fuerza del acondicionamiento de seguimiento. Solo tiene efecto cuando se proporciona `tracks` y el valor es mayor que 0.0. (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 100.0 |
| `width` | El ancho del video de salida. Se configura en incrementos de 16. (predeterminado: 832) | INT | Sí | 16 - MAX_RESOLUTION |
| `height` | La altura del video de salida. Se configura en incrementos de 16. (predeterminado: 480) | INT | Sí | 16 - MAX_RESOLUTION |
| `length` | El número de fotogramas en la secuencia de video. Se configura en incrementos de 4. (predeterminado: 81) | INT | Sí | 1 - MAX_RESOLUTION |
| `batch_size` | El tamaño del lote para la salida latente. (predeterminado: 1) | INT | Sí | 1 - 4096 |
| `start_image` | La imagen inicial o secuencia de imágenes que se codificará con el VAE. | IMAGE | Sí | - |
| `clip_vision_output` | Salida opcional del modelo de visión CLIP para agregar al acondicionamiento. | CLIP_VISION_OUTPUT | No | - |

Nota: El movimiento basado en seguimiento se aplica solo cuando se proporciona `tracks` y `strength` es mayor que 0.0. De lo contrario, el acondicionamiento recibe la imagen inicial codificada sin modificar. El `start_image` se utiliza para crear una imagen latente y una máscara para el acondicionamiento; si no está disponible, el nodo solo pasa el acondicionamiento y genera un latente vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El acondicionamiento positivo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. | CONDITIONING |
| `negative` | El acondicionamiento negativo modificado, que potencialmente contiene `concat_latent_image`, `concat_mask` y `clip_vision_output`. | CONDITIONING |
| `latent` | Un tensor latente vacío con dimensiones determinadas por las entradas `batch_size`, `length`, `height` y `width`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/es.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
