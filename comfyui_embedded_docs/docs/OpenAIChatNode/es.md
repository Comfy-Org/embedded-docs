# OpenAI ChatGPT

Este nodo genera respuestas de texto a partir de un modelo OpenAI. Envía tu mensaje de texto y, opcionalmente, imágenes o archivos, a un modelo OpenAI y devuelve la respuesta de texto generada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Entradas de texto al modelo, utilizadas para generar una respuesta (predeterminado: vacío) | STRING | Sí | - |
| `persistir_contexto` | Este parámetro está obsoleto y no tiene efecto (predeterminado: False) | BOOLEAN | Sí | - |
| `modelo` | El modelo utilizado para generar la respuesta (predeterminado: `gpt-5`) | COMBO | Sí | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `imágenes` | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir varias imágenes, puede usar el nodo Batch Images | IMAGE | No | - |
| `archivos` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo OpenAI Chat Input Files | OPENAI_INPUT_FILES | No | - |
| `opciones_avanzadas` | Configuración opcional para el modelo. Acepta entradas del nodo OpenAI Chat Advanced Options | OPENAI_CHAT_CONFIG | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output_text` | La respuesta de texto generada por el modelo OpenAI | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
