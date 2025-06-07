Este nodo está diseñado para codificar las entradas de texto utilizando el modelo CLIP específicamente adaptado para la arquitectura SDXL. Se centra en convertir descripciones textuales en un formato que puede ser utilizado de manera efectiva para generar o manipular imágenes, aprovechando las capacidades del modelo CLIP para entender y procesar texto en el contexto del contenido visual.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
| --- | --- | --- |
| `clip` | `CLIP` | La instancia del modelo CLIP utilizada para codificar el texto. Juega un papel vital en el procesamiento de la entrada de texto y su conversión en un formato adecuado para tareas de generación o manipulación de imágenes. |
| `width` | `INT` | Especifica el ancho de la imagen en píxeles. Determina las dimensiones de la imagen de salida generada o manipulada. |
| `height` | `INT` | Especifica la altura de la imagen en píxeles. Determina las dimensiones de la imagen de salida generada o manipulada. |
| `crop_w` | `INT` | Define el ancho del área de recorte en píxeles. Este parámetro se utiliza para recortar la imagen a un ancho específico antes del procesamiento. |
| `crop_h` | `INT` | Define la altura del área de recorte en píxeles. Este parámetro se utiliza para recortar la imagen a una altura específica antes del procesamiento. |
| `target_width` | `INT` | El ancho objetivo para la imagen de salida después del procesamiento. Permite redimensionar la imagen a un ancho deseado. |
| `target_height` | `INT` | La altura objetivo para la imagen de salida después del procesamiento. Permite redimensionar la imagen a una altura deseada. |
| `text_g` | `STRING` | La descripción textual global que se va a codificar. Esta entrada es crucial para generar las representaciones visuales correspondientes y entender el contenido descrito. |
| `text_l` | `STRING` | La descripción textual local que se va a codificar. Esta entrada proporciona detalles o contexto adicionales a la descripción global, mejorando la especificidad de la imagen generada o manipulada. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | La salida del nodo, que incluye el texto codificado junto con información adicional necesaria para tareas de generación o manipulación de imágenes. |
