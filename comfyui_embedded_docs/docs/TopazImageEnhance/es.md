# Mejorar imagen con Topaz

El nodo Topaz Image Enhance proporciona mejora de imagen y escalado de calidad profesional. Procesa una única imagen de entrada utilizando un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control preciso sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque en el sujeto y preservación facial.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de IA a utilizar para la mejora de imágenes. | COMBO | Sí | `"Reimagine"` |
| `image` | La imagen de entrada que se va a mejorar. Solo se admite una imagen. | IMAGE | Sí | - |
| `prompt` | Indicación de texto opcional para guiar el escalado creativo (predeterminado: vacío). | STRING | No | - |
| `subject_detection` | Controla en qué parte de la imagen se centra la mejora (predeterminado: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Mejora los rostros (si están presentes) durante el procesamiento (predeterminado: True). | BOOLEAN | No | - |
| `face_enhancement_creativity` | Define el nivel de creatividad para la mejora facial (predeterminado: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `face_enhancement_strength` | Controla la nitidez de los rostros mejorados en relación con el fondo (predeterminado: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `crop_to_fill` | De forma predeterminada, la imagen se ajusta con barras (letterbox) cuando la relación de aspecto de salida difiere. Actívalo para recortar la imagen y llenar las dimensiones de salida (predeterminado: False). | BOOLEAN | No | - |
| `output_width` | Un valor de cero significa que se calcula automáticamente (generalmente será el tamaño original o `output_height` si se especifica) (predeterminado: 0). | INT | No | 0 - 32000 |
| `output_height` | Un valor de cero significa que se genera con la misma altura que la original o el ancho de salida (predeterminado: 0). | INT | No | 0 - 32000 |
| `creativity` | Controla el nivel de creatividad general de la mejora (predeterminado: 3). | INT | No | 1 - 9 |
| `face_preservation` | Preserva la identidad facial de los sujetos (predeterminado: True). | BOOLEAN | No | - |
| `color_preservation` | Preserva los colores originales (predeterminado: True). | BOOLEAN | No | - |

**Nota:** Este nodo solo puede procesar una única imagen de entrada. Proporcionar un lote de varias imágenes provocará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen de salida mejorada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
