> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/es.md)

El nodo WanDancerVideo prepara datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo WanDancer. Combina condicionamiento positivo y negativo con entradas opcionales como una imagen inicial, máscara, incrustaciones CLIP vision y características de audio para controlar el video generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | | El condicionamiento positivo para guiar la generación de video. |
| `negative` | CONDITIONING | Sí | | El condicionamiento negativo para guiar la generación de video. |
| `vae` | VAE | Sí | | El VAE utilizado para codificar la imagen inicial en el espacio latente. |
| `width` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | El ancho del video generado en píxeles (predeterminado: 480). |
| `height` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | La altura del video generado en píxeles (predeterminado: 832). |
| `length` | INT | Sí | 1 a MAX_RESOLUTION (paso: 4) | El número de fotogramas en el video generado. Debe permanecer en 149 para WanDancer (predeterminado: 149). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | | Las incrustaciones CLIP vision para el primer fotograma. |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | No | | Las incrustaciones CLIP vision para la imagen de referencia. |
| `start_image` | IMAGE | No | | La(s) imagen(es) inicial(es) a codificar. Puede ser cualquier número de fotogramas, hasta el `length` especificado. |
| `mask` | MASK | No | | Máscara de condicionamiento de imagen para la(s) imagen(es) inicial(es). Las áreas blancas se conservan, las áreas negras se generan. Se utiliza para generaciones locales. |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | No | | La salida de un codificador de audio, que proporciona características de audio, fps y escala de inyección para la generación condicionada por audio. |

**Nota sobre las restricciones de los parámetros:**
- Las entradas `start_image` y `mask` son opcionales, pero se pueden usar juntas. Cuando se proporciona `start_image`, se codifica y se concatena con el latente. Si también se proporciona `mask`, esta controla qué partes de la imagen inicial se conservan (blanco) y cuáles se regeneran (negro). Si no se proporciona `mask`, se utiliza toda el área de la imagen inicial como guía de condicionamiento.
- Las entradas `clip_vision_output` y `clip_vision_output_ref` son opcionales y se pueden usar juntas para proporcionar contexto visual para el primer fotograma y una imagen de referencia.
- La entrada `audio_encoder_output` es opcional y proporciona características de audio para la generación condicionada por audio.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo con cualquier dato adicional (latente concatenado, CLIP vision, audio) adjunto. |
| `negative` | CONDITIONING | El condicionamiento negativo con cualquier dato adicional (latente concatenado, CLIP vision, audio) adjunto. |
| `latent` | LATENT | Un tensor latente vacío con dimensiones que coinciden con la longitud, altura y ancho del video especificados. |