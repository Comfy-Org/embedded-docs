# Google Gemini

Este nodo permite a los usuarios interactuar con los modelos de IA Gemini de Google para generar respuestas de texto. Puedes proporcionar múltiples tipos de entrada, incluyendo texto, imágenes, audio, video y archivos como contexto para que el modelo genere respuestas más relevantes y significativas. El nodo maneja automáticamente toda la comunicación con la API y el análisis de las respuestas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Entradas de texto para el modelo, utilizadas para generar una respuesta. Puedes incluir instrucciones detalladas, preguntas o contexto para el modelo. Valor predeterminado: cadena vacía. | STRING | Sí | - |
| `modelo` | El modelo Gemini a utilizar para generar respuestas. Valor predeterminado: gemini-3-1-pro. | COMBO | Sí | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` |
| `semilla` | Cuando la semilla se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de los parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. De forma predeterminada, se utiliza un valor de semilla aleatorio. Valor predeterminado: 42. | INT | Sí | 0 a 18446744073709551615 |
| `imágenes` | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puedes usar el nodo Batch Images. Valor predeterminado: Ninguno. | IMAGE | No | - |
| `audio` | Audio opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. | AUDIO | No | - |
| `video` | Video opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. | VIDEO | No | - |
| `archivos` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. Valor predeterminado: Ninguno. | GEMINI_INPUT_FILES | No | - |
| `system_prompt` | Instrucciones fundamentales que dictan el comportamiento de una IA. Valor predeterminado: cadena vacía. Este es un parámetro avanzado. | STRING | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `STRING` | La respuesta de texto generada por el modelo Gemini. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/es.md)

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
