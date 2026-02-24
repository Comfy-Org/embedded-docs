> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/es.md)

El nodo HunyuanVideo15ImageToVideo prepara los datos de condicionamiento y espacio latente para la generación de video basada en el modelo HunyuanVideo 1.5. Crea una representación latente inicial para una secuencia de video y puede integrar opcionalmente una imagen de inicio o una salida de visión CLIP para guiar el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Los prompts de condicionamiento positivo que describen lo que debe contener el video. |
| `negative` | CONDITIONING | Sí | - | Los prompts de condicionamiento negativo que describen lo que el video debe evitar. |
| `vae` | VAE | Sí | - | El modelo VAE (Autoencoder Variacional) utilizado para codificar la imagen de inicio en el espacio latente. |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho de los fotogramas del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 848) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura de los fotogramas del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 480) |
| `length` | INT | No | 1 a MAX_RESOLUTION | El número total de fotogramas en la secuencia de video. (predeterminado: 33) |
| `batch_size` | INT | No | 1 a 4096 | El número de secuencias de video a generar en un solo lote. (predeterminado: 1) |
| `start_image` | IMAGE | No | - | Una imagen de inicio opcional para inicializar la generación del video. Si se proporciona, se codifica y se utiliza para condicionar los primeros fotogramas. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Incrustaciones de visión CLIP opcionales para proporcionar un condicionamiento visual adicional para la generación. |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para coincidir con el `width` y `height` especificados utilizando interpolación bilineal. Se utilizan los primeros `length` fotogramas del lote de imágenes. La imagen codificada se añade luego tanto al condicionamiento `positive` como al `negative` como un `concat_latent_image` con una `concat_mask` correspondiente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado, que ahora puede incluir la imagen de inicio codificada o la salida de visión CLIP. |
| `negative` | CONDITIONING | El condicionamiento negativo modificado, que ahora puede incluir la imagen de inicio codificada o la salida de visión CLIP. |
| `latent` | LATENT | Un tensor latente vacío con dimensiones configuradas para el tamaño de lote, duración del video, ancho y alto especificados. |
