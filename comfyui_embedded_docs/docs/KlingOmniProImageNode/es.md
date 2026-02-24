> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/es.md)

El nodo Kling Omni Image (Pro) genera o edita imágenes utilizando el modelo de IA Kling. Crea imágenes basadas en una descripción de texto y permite proporcionar imágenes de referencia para guiar el estilo o el contenido. El nodo envía una solicitud a una API externa, que procesa la tarea y devuelve la imagen final.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Sí | `"kling-image-o1"` | El modelo específico de IA Kling a utilizar para la generación de imágenes. |
| `prompt` | STRING | Sí | - | Un texto descriptivo que define el contenido de la imagen. Puede incluir tanto descripciones positivas como negativas. El texto debe tener entre 1 y 2500 caracteres de longitud. |
| `resolution` | COMBO | Sí | `"1K"`<br>`"2K"` | La resolución objetivo para la imagen generada. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | La relación de aspecto (ancho a alto) deseada para la imagen generada. |
| `reference_images` | IMAGE | No | - | Hasta 10 imágenes de referencia adicionales. Cada imagen debe tener al menos 300 píxeles tanto en ancho como en alto, y su relación de aspecto debe estar entre 1:2.5 y 2.5:1. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `image` | IMAGE | La imagen final generada o editada por el modelo de IA Kling. |
