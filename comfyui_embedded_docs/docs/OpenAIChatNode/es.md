> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

Este nodo genera respuestas de texto a partir de un modelo OpenAI. Envía tu indicación de texto (y opcionalmente imágenes o archivos) a un modelo OpenAI y devuelve la respuesta de texto generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Entradas de texto para el modelo, utilizadas para generar una respuesta (predeterminado: vacío) |
| `persistir_contexto` | BOOLEAN | Sí | - | Este parámetro está obsoleto y no tiene efecto (predeterminado: Falso) |
| `modelo` | COMBO | Sí | Varios modelos OpenAI disponibles | El modelo utilizado para generar la respuesta |
| `imágenes` | IMAGE | No | - | Imagen(es) opcional(es) para usar como contexto del modelo. Para incluir múltiples imágenes, puedes usar el nodo de Agrupar Imágenes |
| `archivos` | OPENAI_INPUT_FILES | No | - | Archivo(s) opcional(es) para usar como contexto del modelo. Acepta entradas del nodo de Archivos de Entrada de Chat OpenAI |
| `opciones_avanzadas` | OPENAI_CHAT_CONFIG | No | - | Configuración opcional para el modelo. Acepta entradas del nodo de Opciones Avanzadas de Chat OpenAI |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output_text` | STRING | La respuesta de texto generada por el modelo OpenAI |

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
