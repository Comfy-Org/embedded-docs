# HunyuanVideo15ImageToVideo

El nodo **HunyuanVideo15ImageToVideo** prepara los datos de condicionamiento y espacio latente para la generación de vídeo basada en el modelo HunyuanVideo 1.5. Crea una representación latente inicial para una secuencia de vídeo y puede integrar opcionalmente una imagen inicial o una salida de visión CLIP para guiar el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Los condicionamientos positivos que describen lo que debe contener el vídeo. | CONDITIONING | Sí | - |
| `negative` | Los condicionamientos negativos que describen lo que el vídeo debe evitar. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE (autoencoder variacional) utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí | - |
| `width` | El ancho de los fotogramas de vídeo de salida en píxeles. Debe ser divisible por 16. (por defecto: 848) | INT | Sí | 16 to MAX_RESOLUTION, step: 16 |
| `height` | La altura de los fotogramas de vídeo de salida en píxeles. Debe ser divisible por 16. (por defecto: 480) | INT | Sí | 16 to MAX_RESOLUTION, step: 16 |
| `length` | El número total de fotogramas en la secuencia de vídeo. El valor aumenta en pasos de 4. (por defecto: 33) | INT | Sí | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | El número de secuencias de vídeo a generar en un solo lote. (por defecto: 1) | INT | Sí | 1 to 4096 |
| `start_image` | Una imagen inicial opcional para inicializar la generación de vídeo. Si se proporciona, se codifica y se utiliza para condicionar los primeros fotogramas. Solo se utilizan los primeros `length` fotogramas de la imagen. | IMAGE | No | - |
| `clip_vision_output` | Incrustaciones de visión CLIP opcionales para proporcionar condicionamiento visual adicional para la generación. | CLIP_VISION_OUTPUT | No | - |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para que coincida con el `width` y `height` especificados mediante interpolación bilineal, y solo se utilizan sus canales RGB. Se utilizan los primeros `length` fotogramas del lote de imágenes. La imagen codificada se añade tanto al condicionamiento `positive` como al `negative` como un `concat_latent_image` con un `concat_mask` correspondiente. La máscara se establece en 0.0 para los fotogramas cubiertos por la imagen inicial y en 1.0 para los fotogramas restantes. Cuando se proporciona un `clip_vision_output`, también se añade tanto al condicionamiento `positive` como al `negative`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado, que ahora puede incluir la imagen inicial codificada o la salida de visión CLIP. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, que ahora puede incluir la imagen inicial codificada o la salida de visión CLIP. | CONDITIONING |
| `latent` | Un tensor latente vacío con dimensiones configuradas para el tamaño de lote, la longitud del vídeo, el ancho y la altura especificados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
