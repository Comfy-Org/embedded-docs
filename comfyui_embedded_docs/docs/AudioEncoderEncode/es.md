# CodificadorAudioCodificar

El nodo AudioEncoderEncode convierte datos de audio en una representación codificada utilizando un modelo de codificador de audio. Toma un codificador de audio y una entrada de audio sin procesar, luego extrae la forma de onda y la frecuencia de muestreo del audio para producir una salida codificada adecuada para su posterior procesamiento en el pipeline de condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `codificador_audio` | El modelo de codificador de audio utilizado para procesar la entrada de audio | AUDIO_ENCODER | Sí | - |
| `audio` | Los datos de audio que contienen información de forma de onda y frecuencia de muestreo | AUDIO | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La representación de audio codificada generada por el codificador de audio | AUDIO_ENCODER_OUTPUT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/es.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
