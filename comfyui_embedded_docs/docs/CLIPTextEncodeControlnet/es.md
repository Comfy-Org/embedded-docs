# CodificarTextoCLIPControlnet

El nodo CLIPTextEncodeControlnet procesa un prompt de texto utilizando un modelo CLIP y combina la codificación de texto resultante con los datos de condicionamiento existentes. Añade las incrustaciones derivadas del texto a cada entrada de condicionamiento como parámetros de atención cruzada de ControlNet, produciendo una salida de condicionamiento mejorada para aplicaciones de ControlNet.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la tokenización y codificación de texto | CLIP | Sí | - |
| `condicionamiento` | Datos de condicionamiento existentes que se combinarán con la codificación de texto CLIP | CONDITIONING | Sí | - |
| `texto` | El prompt de texto que será procesado por el modelo CLIP. Admite texto multilínea y prompts dinámicos | STRING | Sí | - |

**Nota:** Las tres entradas (`clip`, `conditioning` y `text`) son necesarias para que este nodo funcione. La entrada `text` admite texto multilínea y prompts dinámicos para un procesamiento de texto flexible. Este nodo está marcado como experimental en el código fuente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Datos de condicionamiento mejorados con los parámetros de atención cruzada de ControlNet añadidos (`cross_attn_controlnet` y `pooled_output_controlnet`) derivados de la codificación de texto CLIP | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/es.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
