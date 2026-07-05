# HunyuanVideo15ImageToVideo

El nodo HunyuanVideo15ImageToVideo prepara los datos de condicionamiento y espacio latente para la generación de video basada en el modelo HunyuanVideo 1.5. Crea una representación latente inicial para una secuencia de video y puede integrar opcionalmente una imagen de inicio o una salida de CLIP vision para guiar el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Los mensajes de condicionamiento positivo que describen lo que debe contener el video. | CONDITIONING | Sí | - |
| `negativo` | Los mensajes de condicionamiento negativo que describen lo que debe evitar el video. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE (Autoencoder Variacional) utilizado para codificar la imagen de inicio en el espacio latente. | VAE | Sí | - |
| `ancho` | El ancho de los fotogramas del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 848) | INT | No | 16 a RESOLUCIÓN_MÁXIMA |
| `alto` | La altura de los fotogramas del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 480) | INT | No | 16 a RESOLUCIÓN_MÁXIMA |
| `longitud` | El número total de fotogramas en la secuencia de video. Debe ser múltiplo de 4. (predeterminado: 33) | INT | No | 1 a RESOLUCIÓN_MÁXIMA |
| `tamaño_de_lote` | La cantidad de secuencias de video a generar en un solo lote. (predeterminado: 1) | INT | No | 1 a 4096 |
| `imagen_inicial` | Una imagen de inicio opcional para inicializar la generación del video. Si se proporciona, se codifica y se utiliza para condicionar los primeros fotogramas. Solo se utilizan los primeros `longitud` fotogramas de la imagen. | IMAGE | No | - |
| `clip_vision_output` | Incrustaciones CLIP vision opcionales para proporcionar condicionamiento visual adicional para la generación. | CLIP_VISION_OUTPUT | No | - |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para que coincida con el `width` y `height` especificados mediante interpolación bilineal. Se utilizan los primeros `length` fotogramas del lote de imágenes. La imagen codificada se agrega tanto al condicionamiento `positive` como al `negative` como un `concat_latent_image` con un `concat_mask` correspondiente. La máscara se establece en 0.0 para los fotogramas cubiertos por la imagen de inicio y en 1.0 para los fotogramas restantes.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado, que ahora puede incluir la imagen de inicio codificada o la salida de CLIP vision. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, que ahora puede incluir la imagen de inicio codificada o la salida de CLIP vision. | CONDITIONING |
| `latent` | Un tensor latente vacío con dimensiones configuradas para el tamaño de lote, la duración del video, el ancho y la altura especificados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
