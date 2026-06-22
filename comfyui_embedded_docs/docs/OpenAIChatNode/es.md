# OpenAI ChatGPT

Este nodo genera respuestas de texto a partir de un modelo OpenAI. Envía tu indicación de texto (y opcionalmente imágenes o archivos) a un modelo OpenAI y devuelve la respuesta de texto generada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Entradas de texto para el modelo, utilizadas para generar una respuesta (predeterminado: vacío) | STRING | Sí | - |
| `persistir_contexto` | Este parámetro está obsoleto y no tiene efecto (predeterminado: Falso) | BOOLEAN | Sí | - |
| `modelo` | El modelo utilizado para generar la respuesta | COMBO | Sí | Varios modelos OpenAI disponibles |
| `imágenes` | Imagen(es) opcional(es) para usar como contexto del modelo. Para incluir múltiples imágenes, puedes usar el nodo de Agrupar Imágenes | IMAGE | No | - |
| `archivos` | Archivo(s) opcional(es) para usar como contexto del modelo. Acepta entradas del nodo de Archivos de Entrada de Chat OpenAI | OPENAI_INPUT_FILES | No | - |
| `opciones_avanzadas` | Configuración opcional para el modelo. Acepta entradas del nodo de Opciones Avanzadas de Chat OpenAI | OPENAI_CHAT_CONFIG | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output_text` | La respuesta de texto generada por el modelo OpenAI | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
