> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/es.md)

El nodo ElevenLabs Voice Selector permite elegir una voz específica de una lista predefinida de voces de síntesis de voz de ElevenLabs. Toma un nombre de voz como entrada y devuelve el identificador de voz correspondiente necesario para la generación de audio. Este nodo simplifica el proceso de selección de una voz compatible para su uso con otros nodos de audio de ElevenLabs.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | Sí | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Elige una voz de la lista predefinida de voces de ElevenLabs. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `voice` | STRING | El identificador único para la voz de ElevenLabs seleccionada, que puede pasarse a otros nodos para la generación de texto a voz. |
