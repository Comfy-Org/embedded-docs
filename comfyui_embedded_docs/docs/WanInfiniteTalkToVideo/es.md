# WanInfiniteTalkToVideo

El nodo WanInfiniteTalkToVideo genera un videoclip de una persona hablando a partir de audio. Condiciona un modelo de difusión de video con las características de audio de uno o dos hablantes, opcionalmente utiliza una imagen inicial o fotogramas anteriores como contexto, y devuelve un modelo parcheado, un condicionamiento y un video latente para el muestreo.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `mode` | El modo de audio. Al seleccionar `"single_speaker"` se utiliza una entrada de audio. Al seleccionar `"two_speakers"` se añaden las entradas del segundo hablante que se indican más abajo. | DYNAMIC_COMBO | Sí | `"single_speaker"`<br>`"two_speakers"` |
| `model` | El modelo base de difusión de video a parchear. | MODEL | Sí | - |
| `model_patch` | El parche de modelo que contiene las capas de proyección de audio. | MODELPATCH | Sí | - |
| `positive` | El condicionamiento positivo utilizado para guiar la generación de video. | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo utilizado para guiar la generación de video. | CONDITIONING | Sí | - |
| `vae` | El VAE utilizado para codificar imágenes y fotogramas anteriores en el espacio latente. | VAE | Sí | - |
| `width` | El ancho del video generado en píxeles, en pasos de 16. (predeterminado: 832) | INT | Sí | 16 - MAX_RESOLUTION (step 16) |
| `height` | La altura del video generado en píxeles, en pasos de 16. (predeterminado: 480) | INT | Sí | 16 - MAX_RESOLUTION (step 16) |
| `length` | El número de fotogramas a generar. (predeterminado: 81) | INT | Sí | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | La salida del codificador de audio para el primer hablante, que contiene las características de audio utilizadas para el condicionamiento. | AUDIOENCODEROUTPUT | Sí | - |
| `start_image` | Imagen inicial opcional utilizada para inicializar el comienzo del video. Se redimensiona a `width` y `height`. | IMAGE | No | - |
| `clip_vision_output` | Salida de CLIP vision opcional que se añade tanto al condicionamiento positivo como al negativo. | CLIPVISIONOUTPUT | No | - |
| `motion_frame_count` | Número de fotogramas anteriores a utilizar como contexto de movimiento. (predeterminado: 9) | INT | Sí | 1 - 33 (step 1) |
| `audio_scale` | Factor de escala aplicado al condicionamiento de audio. (predeterminado: 1.0) | FLOAT | Sí | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Fotogramas de video anteriores opcionales utilizados para extender una secuencia existente. El nodo utiliza los últimos `motion_frame_count` fotogramas como contexto de movimiento. | IMAGE | No | - |

### Entradas de un solo hablante

Seleccionar `single_speaker` no añade ninguna entrada adicional.

### Entradas de dos hablantes

Estas entradas están disponibles cuando `mode` es `"two_speakers"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | La salida del codificador de audio para el segundo hablante. Cuando se proporciona, `mask_1` y `mask_2` también deben proporcionarse. | AUDIOENCODEROUTPUT | No | - |
| `mask_1` | Máscara para el primer hablante, requerida si se utilizan dos entradas de audio. | MASK | No | - |
| `mask_2` | Máscara para el segundo hablante, requerida si se utilizan dos entradas de audio. | MASK | No | - |

**Restricciones de parámetros:**

- Si se proporciona `audio_encoder_output_2`, también deben proporcionarse `mask_1` y `mask_2`.
- Si se proporcionan tanto `mask_1` como `mask_2`, también debe proporcionarse `audio_encoder_output_2`.
- Si se proporciona `previous_frames`, debe contener al menos tantos fotogramas como los especificados por `motion_frame_count`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo parcheado con condicionamiento de audio y envoltorios de muestreo aplicados. | MODEL |
| `positive` | El condicionamiento positivo, potencialmente modificado con la imagen inicial o el contexto de CLIP vision. | CONDITIONING |
| `negative` | El condicionamiento negativo, potencialmente modificado con la imagen inicial o el contexto de CLIP vision. | CONDITIONING |
| `latent` | Un tensor latente inicializado a cero que representa el video a generar. | LATENT |
| `trim_image` | El número de fotogramas a recortar desde el inicio al extender desde fotogramas anteriores; 0 cuando se inicia una nueva secuencia. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/es.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
