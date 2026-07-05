# WanInfiniteTalkToVideo

El nodo WanInfiniteTalkToVideo genera secuencias de video a partir de entrada de audio. Utiliza un modelo de difusión de video, condicionado por características de audio extraídas de uno o dos hablantes, para producir una representación latente de un video de persona hablando. El nodo puede generar una secuencia nueva o extender una existente usando fotogramas anteriores como contexto de movimiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modo` | El modo de entrada de audio. `"single_speaker"` utiliza una entrada de audio. `"two_speakers"` habilita entradas para un segundo hablante y sus máscaras correspondientes. | COMBO | Sí | `"single_speaker"`<br>`"two_speakers"` |
| `modelo` | El modelo base de difusión de video. | MODEL | Sí | - |
| `parche de modelo` | El parche del modelo que contiene las capas de proyección de audio. | MODELPATCH | Sí | - |
| `positivo` | El condicionamiento positivo para guiar la generación. | CONDITIONING | Sí | - |
| `negativo` | El condicionamiento negativo para guiar la generación. | CONDITIONING | Sí | - |
| `vae` | El VAE utilizado para codificar imágenes hacia y desde el espacio latente. | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 832) | INT | No | 16 - MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles. Debe ser divisible por 16. (predeterminado: 480) | INT | No | 16 - MAX_RESOLUTION |
| `longitud` | El número de fotogramas a generar. (predeterminado: 81) | INT | No | 1 - MAX_RESOLUTION |
| `salida de clip visión` | Salida opcional de CLIP vision para condicionamiento adicional. | CLIPVISIONOUTPUT | No | - |
| `imagen inicial` | Una imagen de inicio opcional para inicializar la secuencia de video. | IMAGE | No | - |
| `salida codificador de audio 1` | La salida principal del codificador de audio que contiene las características del primer hablante. | AUDIOENCODEROUTPUT | Sí | - |
| `número de fotogramas de movimiento` | Número de fotogramas anteriores a utilizar como contexto de movimiento al extender una secuencia. (predeterminado: 9) | INT | No | 1 - 33 |
| `escala de audio` | Factor de escala aplicado al condicionamiento de audio. (predeterminado: 1.0) | FLOAT | No | -10.0 - 10.0 |
| `fotogramas anteriores` | Fotogramas de video anteriores opcionales para extender la secuencia. | IMAGE | No | - |
| `audio_encoder_output_2` | La segunda salida del codificador de audio. Obligatorio cuando `modo` está configurado en `"two_speakers"`. | AUDIOENCODEROUTPUT | No | - |
| `mask_1` | Máscara para el primer hablante, obligatoria si se utilizan dos entradas de audio. | MASK | No | - |
| `mask_2` | Máscara para el segundo hablante, obligatoria si se utilizan dos entradas de audio. | MASK | No | - |

**Restricciones de Parámetros:**

* Cuando `mode` está configurado en `"two_speakers"`, los parámetros `audio_encoder_output_2`, `mask_1` y `mask_2` se vuelven obligatorios.
* Si se proporciona `audio_encoder_output_2`, también deben proporcionarse tanto `mask_1` como `mask_2`.
* Si se proporcionan `mask_1` y `mask_2`, también debe proporcionarse `audio_encoder_output_2`.
* Si se proporciona `previous_frames`, debe contener al menos tantos fotogramas como los especificados por `motion_frame_count`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo parcheado con el condicionamiento de audio aplicado. | MODEL |
| `positivo` | El condicionamiento positivo, potencialmente modificado con contexto adicional (ej. imagen de inicio, CLIP vision). | CONDITIONING |
| `negativo` | El condicionamiento negativo, potencialmente modificado con contexto adicional. | CONDITIONING |
| `latente` | La secuencia de video generada en el espacio latente. | LATENT |
| `imagen recortada` | El número de fotogramas desde el inicio del contexto de movimiento que deben recortarse al extender una secuencia. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/es.md)

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
