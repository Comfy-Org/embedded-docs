> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/es.md)

El nodo Runway Text to Image genera imágenes a partir de prompts de texto utilizando el modelo Gen 4 de Runway. Puedes proporcionar una descripción de texto y opcionalmente incluir una imagen de referencia para guiar el proceso de generación de imágenes. El nodo maneja la comunicación con la API y devuelve la imagen generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt de texto para la generación (valor por defecto: "") |
| `ratio` | COMBO | Sí | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" | Relación de aspecto para la imagen generada |
| `reference_image` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación |

**Nota:** La imagen de referencia debe tener dimensiones que no excedan 7999x7999 píxeles y una relación de aspecto entre 0.5 y 2.0. Cuando se proporciona una imagen de referencia, esta guía el proceso de generación de imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada basada en el prompt de texto y la imagen de referencia opcional |
