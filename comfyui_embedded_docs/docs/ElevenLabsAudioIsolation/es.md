> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/es.md)

El nodo ElevenLabs Voice Isolation elimina el ruido de fondo de un archivo de audio, aislando las voces o el habla. Envía el audio a la API de ElevenLabs para su procesamiento y devuelve el audio limpio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | | Audio a procesar para la eliminación de ruido de fondo. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El audio procesado con el ruido de fondo eliminado. |
