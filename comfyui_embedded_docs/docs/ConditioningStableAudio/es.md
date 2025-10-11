> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/es.md)

El nodo ConditioningStableAudio agrega información de temporización tanto a las entradas de condicionamiento positivo como negativo para la generación de audio. Establece los parámetros de tiempo de inicio y duración total que ayudan a controlar cuándo y durante cuánto tiempo debe generarse el contenido de audio. Este nodo modifica los datos de condicionamiento existentes añadiendo metadatos de temporización específicos para audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo que se modificará con información de temporización de audio |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo que se modificará con información de temporización de audio |
| `seconds_start` | FLOAT | Sí | 0.0 a 1000.0 | El tiempo de inicio en segundos para la generación de audio (valor por defecto: 0.0) |
| `seconds_total` | FLOAT | Sí | 0.0 a 1000.0 | La duración total en segundos para la generación de audio (valor por defecto: 47.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado con la información de temporización de audio aplicada |
| `negative` | CONDITIONING | El condicionamiento negativo modificado con la información de temporización de audio aplicada |