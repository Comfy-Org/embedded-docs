> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/en.md)

## Resumen

Este nodo genera o edita imágenes enviando un mensaje de texto a la API de Vertex AI de Google. Utiliza un modelo Gemini específico para crear nuevas imágenes o modificar las existentes según tus instrucciones.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. |
| `model` | COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Selecciona el modelo Gemini a utilizar para la generación de imágenes. Actualmente solo hay una opción disponible. |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Cuando la semilla se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o los ajustes de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. De forma predeterminada, se utiliza un valor de semilla aleatorio. (predeterminado: 42) |
| `response_modalities` | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` | Determina el formato de la respuesta. Elige "IMAGE" para recibir solo una imagen, o "IMAGE+TEXT" para recibir tanto una imagen como una descripción de texto. (predeterminado: "IMAGE") |
| `system_prompt` | STRING | No | N/A | Instrucciones fundamentales que dictan el comportamiento de una IA. Este es un parámetro avanzado. |

**Nota sobre el parámetro `model`:** El parámetro `model` es un combo dinámico que incluye subparámetros adicionales para resolución, relación de aspecto y nivel de razonamiento. Estos subparámetros se definen dentro de la selección del modelo y no se enumeran como entradas separadas en esta tabla.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La imagen generada o editada. |
| `STRING` | STRING | Una descripción de texto o título generado por el modelo. |
| `thought_image` | IMAGE | Primera imagen del proceso de razonamiento del modelo. Solo disponible con thinking_level HIGH y modalidad IMAGE+TEXT. |