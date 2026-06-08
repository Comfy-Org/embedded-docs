## Descripción general

Este nodo genera o edita imágenes enviando un mensaje de texto a la API de Vertex AI de Google. Utiliza un modelo Gemini específico para crear imágenes nuevas o modificar las existentes según tus instrucciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. | STRING | Sí | N/A |
| `model` | Selecciona el modelo Gemini a utilizar para la generación de imágenes. Actualmente solo hay una opción disponible. | COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o los ajustes de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. Por defecto, se utiliza un valor de semilla aleatorio. (predeterminado: 42) | INT | Sí | 0 a 18446744073709551615 |
| `response_modalities` | Determina el formato de la respuesta. Elige "IMAGE" para recibir solo una imagen, o "IMAGE+TEXT" para recibir tanto una imagen como una descripción de texto. (predeterminado: "IMAGE") | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Instrucciones fundamentales que dictan el comportamiento de una IA. Este es un parámetro avanzado. | STRING | No | N/A |

**Nota sobre el parámetro `model`:** El parámetro `model` es un combo dinámico que incluye subparámetros adicionales para resolución, relación de aspecto y nivel de pensamiento. Estos subparámetros están definidos dentro de la selección del modelo y no se enumeran como entradas separadas en esta tabla.

**Nota sobre la entrada de imagen:** Puedes proporcionar hasta 14 imágenes como entrada al modelo. Estas imágenes se pasan a través del subcampo de imagen del parámetro `model` y se utilizan para edición o como contexto visual para la generación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La imagen generada o editada. | IMAGE |
| `thought_image` | Una descripción de texto o leyenda generada por el modelo. | STRING |
| `thought_image` | Primera imagen del proceso de pensamiento del modelo. Solo disponible con nivel de pensamiento ALTO y modalidad IMAGE+TEXT. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/es.md)

---
**Source fingerprint (SHA-256):** `6b91afcdd12e08ff0e3afdbb5596bfd63463cda4d2b031019dedf03bd122fa87`
