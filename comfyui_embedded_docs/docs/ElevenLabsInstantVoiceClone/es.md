> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/es.md)

El nodo ElevenLabs Instant Voice Clone crea un nuevo modelo de voz único mediante el análisis de 1 a 8 grabaciones de audio de la voz de una persona. Envía estas muestras a la API de ElevenLabs, que las procesa para generar un clon de voz que puede utilizarse para la síntesis de texto a voz.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | Sí | 1 a 8 archivos | Grabaciones de audio para la clonación de voz. Debes proporcionar entre 1 y 8 archivos de audio. |
| `remove_background_noise` | BOOLEAN | No | True / False | Elimina el ruido de fondo de las muestras de voz mediante aislamiento de audio. (por defecto: False) |

**Nota:** Debes proporcionar al menos un archivo de audio, y puedes proporcionar hasta ocho. El nodo creará automáticamente ranuras de entrada para los archivos de audio que añadas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | El identificador único para el modelo de voz clonado recién creado. Esta salida puede conectarse a otros nodos de texto a voz de ElevenLabs. |