> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

El nodo Topaz Image Enhance proporciona escalado y mejora de imagen de calidad industrial. Procesa una única imagen de entrada utilizando un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control detallado sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque del sujeto y preservación facial.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"Reimagine"` | El modelo de IA a utilizar para la mejora de imagen. |
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a mejorar. Solo se admite una imagen. |
| `prompt` | STRING | No | - | Un texto opcional para guiar el escalado creativo (por defecto: vacío). |
| `subject_detection` | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` | Controla en qué parte de la imagen se enfoca la mejora (por defecto: "All"). |
| `face_enhancement` | BOOLEAN | No | - | Activar para mejorar los rostros si están presentes en la imagen (por defecto: True). |
| `face_enhancement_creativity` | FLOAT | No | 0.0 - 1.0 | Establece el nivel de creatividad para la mejora facial (por defecto: 0.0). |
| `face_enhancement_strength` | FLOAT | No | 0.0 - 1.0 | Controla cuán nítidos son los rostros mejorados en relación con el fondo (por defecto: 1.0). |
| `crop_to_fill` | BOOLEAN | No | - | Por defecto, la imagen se ajusta con barras negras cuando la relación de aspecto de salida es diferente. Activar para recortar la imagen y llenar las dimensiones de salida en su lugar (por defecto: False). |
| `output_width` | INT | No | 0 - 32000 | El ancho deseado para la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en el `output_height` si se especifica (por defecto: 0). |
| `output_height` | INT | No | 0 - 32000 | La altura deseada para la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en el `output_width` si se especifica (por defecto: 0). |
| `creativity` | INT | No | 1 - 9 | Controla el nivel de creatividad general de la mejora (por defecto: 3). |
| `face_preservation` | BOOLEAN | No | - | Preserva la identidad facial de los sujetos en la imagen (por defecto: True). |
| `color_preservation` | BOOLEAN | No | - | Preserva los colores originales de la imagen de entrada (por defecto: True). |

**Nota:** Este nodo solo puede procesar una única imagen de entrada. Proporcionar un lote de múltiples imágenes resultará en un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida mejorada. |
