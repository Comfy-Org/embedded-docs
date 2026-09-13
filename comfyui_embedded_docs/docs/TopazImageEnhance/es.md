# Mejorar imagen con Topaz

El nodo Topaz Image Enhance proporciona escalado y mejora de imágenes de estándar industrial. Procesa una única imagen de entrada mediante un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control detallado sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque del sujeto y preservación facial.

Este nodo es una versión heredada y está marcado como obsoleto en la interfaz.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo de IA que se usará para la mejora de la imagen. | COMBO | Sí | `"Reimagine"` |
| `image` | La imagen de entrada que se va a mejorar. Solo se admite una imagen. | IMAGE | Sí | - |
| `prompt` | Prompt de texto opcional para guiar el escalado creativo (predeterminado: vacío). | STRING | No | - |
| `subject_detection` | Controla en qué parte de la imagen se centra la mejora (predeterminado: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Mejora los rostros (si los hay) durante el procesamiento (predeterminado: True). | BOOLEAN | No | - |
| `face_enhancement_creativity` | Establece el nivel de creatividad para la mejora de rostros (predeterminado: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `face_enhancement_strength` | Controla cuán nítidos son los rostros mejorados en relación con el fondo (predeterminado: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `crop_to_fill` | De forma predeterminada, la imagen se muestra con barras negras cuando la relación de aspecto de salida difiere. Actívelo para recortar la imagen y llenar las dimensiones de salida (predeterminado: False). | BOOLEAN | No | - |
| `output_width` | Un valor de cero significa calcular automáticamente (normalmente será el tamaño original o output_height si se especifica) (predeterminado: 0). | INT | No | 0 - 32000 |
| `output_height` | Un valor de cero significa generar con la misma altura que la original o el ancho de salida (predeterminado: 0). | INT | No | 0 - 32000 |
| `creativity` | Controla el nivel general de creatividad de la mejora (predeterminado: 3). | INT | No | 1 - 9 |
| `face_preservation` | Preserva la identidad facial de los sujetos (predeterminado: True). | BOOLEAN | No | - |
| `color_preservation` | Preserva los colores originales (predeterminado: True). | BOOLEAN | No | - |

**Nota:** Este nodo solo puede procesar una única imagen de entrada. Proporcionar un lote de varias imágenes dará como resultado un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen de salida mejorada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
