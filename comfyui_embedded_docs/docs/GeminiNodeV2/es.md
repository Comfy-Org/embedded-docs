# Google Gemini

Genera respuestas de texto con los modelos Gemini de Google. Proporciona un mensaje de texto y, opcionalmente, una o más imágenes, clips de audio, videos o archivos como contexto multimodal.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Entrada de texto para el modelo. Incluye instrucciones detalladas, preguntas o contexto. | STRING | Sí |  |
| `model` | El modelo Gemini utilizado para generar la respuesta. | COMBO | Sí | `"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `seed` | Semilla para el muestreo. Establécelo en 0 para una semilla aleatoria. No se garantiza una salida determinista. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: "") | STRING | No |  |

**Nota:** Al proporcionar imágenes, audio o video como contexto multimodal, el nodo sube los medios como URL para las primeras 10 entradas. Cualquier medio adicional se envía en línea como datos base64, con una carga útil máxima en línea de 18 MB. Si la carga útil en línea supera este límite, se genera un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `output` | La respuesta de texto generada por el modelo Gemini. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `ec9921f218a726082eb8987cf94b3575f61a3c6cf55fb33aeb81d42fad35d302`
