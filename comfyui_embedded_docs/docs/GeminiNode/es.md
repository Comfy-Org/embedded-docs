# Google Gemini

Este nodo permite a los usuarios interactuar con los modelos de IA Gemini de Google para generar respuestas de texto. Puede proporcionar múltiples tipos de entradas, incluyendo texto, imágenes, audio, vídeo y archivos como contexto para que el modelo genere respuestas más relevantes y significativas. El nodo maneja automáticamente toda la comunicación con la API y el análisis de las respuestas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Entradas de texto para el modelo, utilizadas para generar una respuesta. Puede incluir instrucciones detalladas, preguntas o contexto para el modelo. Valor predeterminado: cadena vacía. | STRING | Sí | - |
| `model` | El modelo Gemini que se utilizará para generar respuestas. Valor predeterminado: gemini-3-1-pro. | COMBO | Sí | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace todo lo posible por proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso si se usa el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. Valor predeterminado: 42. | INT | Sí | 0 a 18446744073709551615 |
| `images` | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir varias imágenes, puede usar el nodo Batch Images. Valor predeterminado: Ninguno. | IMAGE | No | - |
| `audio` | Audio opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. | AUDIO | No | - |
| `video` | Vídeo opcional para usar como contexto para el modelo. Valor predeterminado: Ninguno. | VIDEO | No | - |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. Valor predeterminado: Ninguno. | GEMINI_INPUT_FILES | No | - |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento de una IA. Valor predeterminado: cadena vacía. Este es un parámetro avanzado. | STRING | No | - |

Nota: Este nodo está marcado como obsoleto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `STRING` | La respuesta de texto generada por el modelo Gemini. Si el modelo no devuelve texto, el nodo genera "Empty response from Gemini model...". | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/es.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
