> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/es.md)

El nodo AudioEncoderEncode procesa datos de audio codificándolos mediante un modelo de codificador de audio. Toma una entrada de audio y la convierte en una representación codificada que puede utilizarse para procesamiento adicional en el pipeline de acondicionamiento. Este nodo transforma formas de onda de audio sin procesar en un formato adecuado para aplicaciones de aprendizaje automático basadas en audio.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Requerido | - | - | El modelo de codificador de audio utilizado para procesar la entrada de audio |
| `audio` | AUDIO | Requerido | - | - | Los datos de audio que contienen información de forma de onda y tasa de muestreo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | La representación de audio codificada generada por el codificador de audio |
