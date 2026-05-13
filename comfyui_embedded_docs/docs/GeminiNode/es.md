> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/es.md)

Este nodo permite a los usuarios interactuar con los modelos de IA Gemini de Google para generar respuestas de texto. Puedes proporcionar múltiples tipos de entrada, incluyendo texto, imágenes, audio, video y archivos como contexto para que el modelo genere respuestas más relevantes y significativas. El nodo maneja automáticamente toda la comunicación con la API y el análisis de las respuestas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Entradas de texto para el modelo, utilizadas para generar una respuesta. Puedes incluir instrucciones detalladas, preguntas o contexto para el modelo. Valor predeterminado: cadena vacía. |
| `modelo` | COMBO | Sí | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` | El modelo Gemini a utilizar para generar respuestas. Valor predeterminado: gemini-3-1-pro. |
| `semilla` | INT | Sí | 0 a 18446744073709551615 | Cuando la semilla se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de los parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. De forma predeterminada, se utiliza un valor de semilla aleatorio. Valor predeterminado: 42. |
| `imágenes` | IMAGE | No | - | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puedes usar el nodo Batch Images. Valor predeterminado: Ninguno. |
| `audio` | AUDIO | No | - | Audio opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. |
| `video` | VIDEO | No | - | Video opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. |
| `archivos` | GEMINI_INPUT_FILES | No | - | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. Valor predeterminado: Ninguno. |
| `system_prompt` | STRING | No | - | Instrucciones fundamentales que dictan el comportamiento de una IA. Valor predeterminado: cadena vacía. Este es un parámetro avanzado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `STRING` | STRING | La respuesta de texto generada por el modelo Gemini. |

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
