El nodo CLIPTextEncodeControlnet procesa la entrada de texto utilizando un modelo CLIP y lo combina con datos de condicionamiento existentes para generar una salida de condicionamiento mejorada para aplicaciones de controlnet. Tokeniza el texto de entrada, lo codifica a través del modelo CLIP y agrega las incrustaciones resultantes a los datos de condicionamiento proporcionados como parámetros de controlnet de atención cruzada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación de texto | CLIP | Sí | - |
| `condicionamiento` | Datos de condicionamiento existentes que se mejorarán con parámetros de controlnet | CONDITIONING | Sí | - |
| `texto` | Entrada de texto a procesar por el modelo CLIP. Admite texto multilínea y prompts dinámicos | STRING | Sí | - |

**Nota:** Este nodo requiere las tres entradas (`clip`, `conditioning` y `text`) para funcionar correctamente. La entrada `text` admite prompts dinámicos y texto multilínea para un procesamiento de texto flexible.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Datos de condicionamiento mejorados con parámetros adicionales de controlnet de atención cruzada (`cross_attn_controlnet` y `pooled_output_controlnet`) derivados de la codificación de texto CLIP | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/es.md)

---
**Source fingerprint (SHA-256):** `dd6f68d822cc38e27c826b634c938d62e07b075e18a0f46f80b462aecca0b70b`
