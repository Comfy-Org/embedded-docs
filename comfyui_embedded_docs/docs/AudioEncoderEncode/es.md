# CodificadorAudioCodificar

El nodo AudioEncoderEncode procesa datos de audio codificándolos mediante un modelo de codificador de audio. Toma una entrada de audio y la convierte en una representación codificada que puede utilizarse para procesamiento posterior en el pipeline de condicionamiento. Este nodo transforma formas de onda de audio sin procesar en un formato adecuado para aplicaciones de aprendizaje automático basadas en audio.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio_encoder` | El modelo de codificador de audio utilizado para procesar la entrada de audio | AUDIO_ENCODER | Sí | - |
| `audio` | Los datos de audio que contienen información de forma de onda y frecuencia de muestreo | AUDIO | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La representación de audio codificada generada por el codificador de audio | AUDIO_ENCODER_OUTPUT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/es.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
