# WanDancerVideo

WanDancerVideo prepara los datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo WanDancer. Toma el condicionamiento positivo y negativo y, opcionalmente, los combina con una imagen inicial, una máscara, incrustaciones de visión CLIP y características de audio para controlar el video generado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo para guiar la generación de video. | CONDITIONING | Sí |  |
| `negative` | El condicionamiento negativo para guiar la generación de video. | CONDITIONING | Sí |  |
| `vae` | El VAE utilizado para codificar la imagen inicial en el espacio latente. | VAE | Sí |  |
| `width` | El ancho del video generado en píxeles (por defecto: 480). | INT | Sí | 16 to MAX_RESOLUTION (step: 16) |
| `height` | El alto del video generado en píxeles (por defecto: 832). | INT | Sí | 16 to MAX_RESOLUTION (step: 16) |
| `length` | El número de fotogramas en el video generado. Debe permanecer en 149 para WanDancer (por defecto: 149). | INT | Sí | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | Las incrustaciones de visión CLIP para el primer fotograma. | CLIP_VISION_OUTPUT | No |  |
| `clip_vision_output_ref` | Las incrustaciones de visión CLIP para la imagen de referencia. | CLIP_VISION_OUTPUT | No |  |
| `start_image` | La(s) imagen(es) inicial(es) que se codificarán, puede ser cualquier número de fotogramas. | IMAGE | No |  |
| `mask` | Máscara de condicionamiento de imagen para la(s) imagen(es) inicial(es). El blanco se conserva, el negro se genera. Se utiliza para las generaciones locales. | MASK | No |  |
| `audio_encoder_output` | La salida de un codificador de audio, que proporciona características de audio, FPS y escala de inyección de audio para la generación condicionada por audio. | AUDIO_ENCODER_OUTPUT | No |  |

**Nota sobre las restricciones de parámetros:**
- Cuando se proporciona `start_image`, se redimensiona a `width` × `height`, se limita a `length` fotogramas y se codifica en un latente que se adjunta a ambos condicionamientos junto con una máscara de concatenación.
- `mask` solo tiene efecto cuando también se proporciona `start_image`. En la máscara, las áreas blancas se conservan y las áreas negras se generan. Cuando no se proporciona `mask`, el área de la imagen inicial se utiliza como guía de condicionamiento y el resto de fotogramas se generan.
- `clip_vision_output_ref` se aplica solo cuando se proporciona `clip_vision_output`.
- `audio_encoder_output` adjunta características de audio, FPS y una escala de inyección de audio (por defecto 1.0) a ambos condicionamientos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo con cualquier dato adicional (latente de concatenación, visión CLIP, audio) adjunto. | CONDITIONING |
| `negative` | El condicionamiento negativo con cualquier dato adicional (latente de concatenación, visión CLIP, audio) adjunto. | CONDITIONING |
| `latent` | Un tensor latente vacío con dimensiones que coinciden con la longitud, altura y ancho del video especificado. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/es.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
