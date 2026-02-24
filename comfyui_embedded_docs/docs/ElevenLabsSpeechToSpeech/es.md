> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/es.md)

El nodo ElevenLabs Speech to Speech transforma un archivo de audio de entrada de una voz a otra. Utiliza la API de ElevenLabs para convertir el habla preservando el contenido original y el tono emocional del audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Sí | - | Voz objetivo para la transformación. Conectar desde el Selector de Voz o Clonación Instantánea de Voz. |
| `audio` | AUDIO | Sí | - | Audio fuente a transformar. |
| `stability` | FLOAT | No | 0.0 - 1.0 | Estabilidad de la voz. Valores más bajos dan un rango emocional más amplio, valores más altos producen un habla más consistente pero potencialmente monótona (por defecto: 0.5). |
| `model` | DYNAMICCOMBO | No | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Modelo a utilizar para la transformación de habla a habla. Cada opción proporciona un conjunto específico de ajustes de voz (similarity_boost, style, use_speaker_boost, speed). |
| `output_format` | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio (por defecto: "mp3_44100_192"). |
| `seed` | INT | No | 0 - 4294967295 | Semilla para reproducibilidad (por defecto: 0). |
| `remove_background_noise` | BOOLEAN | No | - | Eliminar ruido de fondo del audio de entrada usando aislamiento de audio (por defecto: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El archivo de audio transformado en el formato de salida especificado. |
