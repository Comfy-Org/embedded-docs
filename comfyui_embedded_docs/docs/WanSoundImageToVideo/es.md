# WanSoundImageToVideo

El nodo WanSoundImageToVideo genera contenido de video a partir de imágenes con condicionamiento de audio opcional. Toma indicaciones de condicionamiento positivas y negativas junto con un modelo VAE para crear latentes de video, y puede incorporar imágenes de referencia, codificación de audio, videos de control y referencias de movimiento para guiar el proceso de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Indicaciones de condicionamiento positivas que guían qué contenido debe aparecer en el video generado | CONDITIONING | Sí | - |
| `negativo` | Indicaciones de condicionamiento negativas que especifican qué contenido debe evitarse en el video generado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar y decodificar las representaciones latentes del video | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Altura del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video generado (predeterminado: 77, debe ser divisible por 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_codificador_audio` | Codificación de audio opcional que puede influir en la generación de video según las características del sonido. Cuando se proporciona, las características de audio se interpolan y se utilizan para condicionar la generación de video. | AUDIO_ENCODER_OUTPUT | No | - |
| `imagen_ref` | Imagen de referencia opcional que proporciona guía visual para el contenido del video. La imagen se amplía para coincidir con el ancho y la altura especificados, y luego se codifica en una representación latente. Solo se utiliza la primera imagen de la entrada como referencia. | IMAGE | No | - |
| `video_control` | Video de control opcional que guía el movimiento y la estructura del video generado. El video se amplía y se codifica, y luego se utiliza para condicionar la salida. Solo se utilizan los primeros `length` fotogramas. | IMAGE | No | - |
| `movimiento_ref` | Referencia de movimiento opcional que proporciona guía para los patrones de movimiento en el video. Si la entrada tiene más de 73 fotogramas, solo se utilizan los últimos 73. Si se proporcionan menos de 73 fotogramas, la secuencia se rellena con fotogramas neutros. | IMAGE | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo procesado que ha sido modificado para la generación de video, incluyendo embeddings de audio, latentes de referencia, referencias de movimiento y condicionamiento de video de control. | CONDITIONING |
| `negativo` | Condicionamiento negativo procesado que ha sido modificado para la generación de video, incluyendo embeddings de audio (puestos a cero), latentes de referencia, referencias de movimiento y condicionamiento de video de control. | CONDITIONING |
| `latente` | Representación de video generada en el espacio latente que puede decodificarse en fotogramas de video finales. El tensor latente tiene forma [batch_size, 16, latent_t, height/8, width/8], donde `latent_t` se deriva del parámetro `length`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
