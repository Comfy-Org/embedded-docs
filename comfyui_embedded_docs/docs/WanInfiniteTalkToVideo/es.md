> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/es.md)

El nodo WanInfiniteTalkToVideo genera secuencias de video a partir de entrada de audio. Utiliza un modelo de difusión de video, condicionado por características de audio extraídas de uno o dos hablantes, para producir una representación latente de un video de persona hablando. El nodo puede generar una secuencia nueva o extender una existente usando fotogramas anteriores como contexto de movimiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `mode` | COMBO | Sí | `"single_speaker"`<br>`"two_speakers"` | El modo de entrada de audio. `"single_speaker"` utiliza una entrada de audio. `"two_speakers"` habilita entradas para un segundo hablante y sus máscaras correspondientes. |
| `model` | MODEL | Sí | - | El modelo base de difusión de video. |
| `model_patch` | MODELPATCH | Sí | - | El parche del modelo que contiene las capas de proyección de audio. |
| `positive` | CONDITIONING | Sí | - | El condicionamiento positivo para guiar la generación. |
| `negative` | CONDITIONING | Sí | - | El condicionamiento negativo para guiar la generación. |
| `vae` | VAE | Sí | - | El VAE utilizado para codificar imágenes hacia y desde el espacio latente. |
| `width` | INT | No | 16 - MAX_RESOLUTION | El ancho del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 832) |
| `height` | INT | No | 16 - MAX_RESOLUTION | La altura del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 480) |
| `length` | INT | No | 1 - MAX_RESOLUTION | El número de fotogramas a generar. (predeterminado: 81) |
| `clip_vision_output` | CLIPVISIONOUTPUT | No | - | Salida opcional de CLIP vision para condicionamiento adicional. |
| `start_image` | IMAGE | No | - | Una imagen de inicio opcional para inicializar la secuencia de video. |
| `audio_encoder_output_1` | AUDIOENCODEROUTPUT | Sí | - | La salida principal del codificador de audio que contiene las características del primer hablante. |
| `motion_frame_count` | INT | No | 1 - 33 | Número de fotogramas anteriores a utilizar como contexto de movimiento al extender una secuencia. (predeterminado: 9) |
| `audio_scale` | FLOAT | No | -10.0 - 10.0 | Factor de escala aplicado al condicionamiento de audio. (predeterminado: 1.0) |
| `previous_frames` | IMAGE | No | - | Fotogramas de video anteriores opcionales para extender la secuencia. |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | No | - | La segunda salida del codificador de audio. Obligatorio cuando `mode` está configurado en `"two_speakers"`. |
| `mask_1` | MASK | No | - | Máscara para el primer hablante, obligatoria si se utilizan dos entradas de audio. |
| `mask_2` | MASK | No | - | Máscara para el segundo hablante, obligatoria si se utilizan dos entradas de audio. |

**Restricciones de Parámetros:**

* Cuando `mode` está configurado en `"two_speakers"`, los parámetros `audio_encoder_output_2`, `mask_1` y `mask_2` se vuelven obligatorios.
* Si se proporciona `audio_encoder_output_2`, también deben proporcionarse tanto `mask_1` como `mask_2`.
* Si se proporcionan `mask_1` y `mask_2`, también debe proporcionarse `audio_encoder_output_2`.
* Si se proporciona `previous_frames`, debe contener al menos tantos fotogramas como los especificados por `motion_frame_count`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo parcheado con el condicionamiento de audio aplicado. |
| `positive` | CONDITIONING | El condicionamiento positivo, potencialmente modificado con contexto adicional (ej. imagen de inicio, CLIP vision). |
| `negative` | CONDITIONING | El condicionamiento negativo, potencialmente modificado con contexto adicional. |
| `latent` | LATENT | La secuencia de video generada en el espacio latente. |
| `trim_image` | INT | El número de fotogramas desde el inicio del contexto de movimiento que deben recortarse al extender una secuencia. |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
