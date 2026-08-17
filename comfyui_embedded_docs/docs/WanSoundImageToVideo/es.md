# WanSoundImageToVideo

El nodo WanSoundImageToVideo prepara la generación de videos a partir de imágenes con condicionamiento de audio opcional. Toma prompts de condicionamiento positivo y negativo junto con un modelo VAE para construir las entradas de condicionamiento y un tensor latente vacío, y puede incorporar imágenes de referencia, codificación de audio, videos de control y referencias de movimiento para guiar el proceso de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamiento positivo que guían qué contenido debe aparecer en el video generado | CONDITIONING | Sí | - |
| `negative` | Prompts de condicionamiento negativo que especifican qué contenido debe evitarse en el video generado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar y decodificar las representaciones latentes del video | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 832, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) |
| `height` | Alto del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) |
| `length` | Número de fotogramas en el video generado (predeterminado: 77, debe ser divisible por 4) | INT | Sí | 1 a MAX_RESOLUTION (paso: 4) |
| `batch_size` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `audio_encoder_output` | Codificación de audio opcional que puede influir en la generación de video según las características del sonido. Cuando se proporciona, las características de audio se interpolan y se utilizan para condicionar la generación del video. | AUDIOENCODEROUTPUT | No | - |
| `ref_image` | Imagen de referencia opcional que proporciona guía visual para el contenido del video. La imagen se amplía para coincidir con el ancho y alto especificados y luego se codifica en una representación latente. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No | - |
| `control_video` | Video de control opcional que guía el movimiento y la estructura del video generado. El video se amplía y codifica, y luego se utiliza para condicionar la salida. Solo se utilizan los primeros `length` fotogramas. | IMAGE | No | - |
| `ref_motion` | Referencia de movimiento opcional que proporciona guía para los patrones de movimiento en el video. Si la entrada tiene más de 73 fotogramas, solo se utilizan los últimos 73. Si se proporcionan menos de 73 fotogramas, la secuencia se rellena con fotogramas neutrales. | IMAGE | No | - |

**Nota:** Las entradas opcionales (`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`) pueden usarse de forma independiente o combinadas. El condicionamiento por video de control siempre se aplica; cuando no se proporciona ningún `control_video`, se utiliza un video de control vacío (cero).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo procesado y modificado para la generación de video. Cuando se proporcionan las entradas opcionales correspondientes, incluye embeddings de audio, latentes de referencia, referencias de movimiento y condicionamiento por video de control. | CONDITIONING |
| `negative` | Condicionamiento negativo procesado y modificado para la generación de video. Cuando se proporcionan las entradas opcionales correspondientes, incluye embeddings de audio (establecidos en cero), latentes de referencia, referencias de movimiento y condicionamiento por video de control. | CONDITIONING |
| `latent` | Tensor latente vacío que sirve como punto de partida para la generación de video. El latente tiene forma [batch_size, 16, latent_t, height/8, width/8], donde latent_t = ((length - 1) // 4) + 1. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
