> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/es.md)

El nodo **ElevenLabs Voice Selector** permite elegir una voz específica de una lista predefinida de voces de texto a voz de ElevenLabs. Toma un nombre de voz como entrada y genera el identificador de voz correspondiente necesario para la generación de audio. Este nodo simplifica el proceso de seleccionar una voz compatible para usar con otros nodos de audio de ElevenLabs.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `voice` | STRING | Sí | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Elige una voz de la lista predefinida de voces de ElevenLabs. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `voice` | STRING | El identificador único de la voz seleccionada de ElevenLabs, que puede pasarse a otros nodos para la generación de texto a voz. |

---
**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`
