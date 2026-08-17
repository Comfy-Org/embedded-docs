# CodificarTextoCLIPControlnet

El nodo CLIPTextEncodeControlnet procesa la entrada de texto utilizando un modelo CLIP y la combina con datos de conditioning existentes para crear una salida de conditioning mejorada para aplicaciones de controlnet. Tokeniza el texto de entrada, lo codifica a través del modelo CLIP y añade los embeddings resultantes a los datos de conditioning proporcionados como parámetros de controlnet de atención cruzada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación de texto. | CLIP | Sí | - |
| `conditioning` | Datos de conditioning existentes que se mejorarán con parámetros de controlnet. | CONDITIONING | Sí | - |
| `text` | Texto de entrada que será procesado por el modelo CLIP. Admite texto multilínea y prompts dinámicos. | STRING | Sí | - |

**Nota:** Este nodo requiere las tres entradas (`clip`, `conditioning` y `text`) para funcionar correctamente. La entrada `text` admite prompts dinámicos y texto multilínea para un procesamiento de texto flexible. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `CONDITIONING` | Datos de conditioning mejorados con parámetros de controlnet de atención cruzada añadidos (`cross_attn_controlnet` y `pooled_output_controlnet`) derivados de la codificación de texto del CLIP. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/es.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
