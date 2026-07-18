El nodo WanDancerVideo prepara datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo WanDancer. Combina el condicionamiento positivo y negativo con entradas opcionales como una imagen inicial, máscara, incrustaciones CLIP vision y características de audio para controlar el video generado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | El condicionamiento positivo para guiar la generación de video. | CONDITIONING | Sí |  |
| `negativo` | El condicionamiento negativo para guiar la generación de video. | CONDITIONING | Sí |  |
| `vae` | El VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí |  |
| `ancho` | El ancho del video generado en píxeles (predeterminado: 480). | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) |
| `alto` | La altura del video generado en píxeles (predeterminado: 832). | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) |
| `longitud` | El número de fotogramas en el video generado. Debe permanecer en 149 para WanDancer (predeterminado: 149). | INT | Sí | 1 a MAX_RESOLUTION (paso: 4) |
| `clip_vision_output` | Las incrustaciones CLIP vision para el primer fotograma. | CLIP_VISION_OUTPUT | No |  |
| `clip_vision_output_ref` | Las incrustaciones CLIP vision para la imagen de referencia. | CLIP_VISION_OUTPUT | No |  |
| `imagen_inicial` | La(s) imagen(es) inicial(es) a codificar. Puede ser cualquier cantidad de fotogramas, hasta el `longitud` especificado. | IMAGE | No |  |
| `máscara` | Máscara de condicionamiento de imagen para la(s) imagen(es) inicial(es). Las áreas blancas se conservan, las áreas negras se generan. Se utiliza para generaciones locales. | MASK | No |  |
| `audio_encoder_output` | La salida de un codificador de audio, que proporciona características de audio, fps y escala de inyección para la generación condicionada por audio. | AUDIO_ENCODER_OUTPUT | No |  |

**Nota sobre las restricciones de parámetros:**
- Las entradas `start_image` y `mask` son opcionales pero se pueden usar juntas. Cuando se proporciona `start_image`, se codifica y se concatena con el latente. Si también se proporciona `mask`, controla qué partes de la imagen inicial se conservan (blanco) y cuáles se regeneran (negro). Si no se proporciona `mask`, toda el área de la imagen inicial se utiliza como guía de condicionamiento.
- Las entradas `clip_vision_output` y `clip_vision_output_ref` son opcionales y se pueden usar juntas para proporcionar contexto visual para el primer fotograma y una imagen de referencia.
- La entrada `audio_encoder_output` es opcional y proporciona características de audio para la generación condicionada por audio.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo con cualquier dato adicional (latente concatenado, CLIP vision, audio) adjunto. | CONDITIONING |
| `negativo` | El condicionamiento negativo con cualquier dato adicional (latente concatenado, CLIP vision, audio) adjunto. | CONDITIONING |
| `latente` | Un tensor latente vacío con dimensiones que coinciden con la longitud, altura y ancho de video especificados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/es.md)

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
