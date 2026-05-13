> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

El nodo Topaz Image Enhance proporciona mejora y escalado de imágenes de nivel profesional. Procesa una sola imagen de entrada utilizando un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control preciso sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque en el sujeto y preservación facial.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"Reimagine"` | El modelo de IA a utilizar para la mejora de imagen. |
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a mejorar. Solo se admite una imagen. |
| `prompt` | STRING | No | - | Un texto opcional como guía creativa para el escalado (predeterminado: vacío). |
| `detección_de_sujetos` | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` | Controla en qué parte de la imagen se enfoca la mejora (predeterminado: "All"). |
| `mejora_de_rostros` | BOOLEAN | No | - | Activar para mejorar rostros si están presentes en la imagen (predeterminado: True). |
| `creatividad_mejora_rostros` | FLOAT | No | 0.0 - 1.0 | Establece el nivel de creatividad para la mejora facial (predeterminado: 0.0). |
| `intensidad_mejora_rostros` | FLOAT | No | 0.0 - 1.0 | Controla qué tan nítidos son los rostros mejorados en relación con el fondo (predeterminado: 1.0). |
| `recortar_para_ajustar` | BOOLEAN | No | - | De forma predeterminada, la imagen se encuadra con barras cuando la relación de aspecto de salida difiere. Activar para recortar la imagen y llenar las dimensiones de salida (predeterminado: False). |
| `ancho_de_salida` | INT | No | 0 - 32000 | El ancho deseado de la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en `alto_de_salida` si se especifica (predeterminado: 0). |
| `alto_de_salida` | INT | No | 0 - 32000 | La altura deseada de la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en `ancho_de_salida` si se especifica (predeterminado: 0). |
| `creatividad` | INT | No | 1 - 9 | Controla el nivel general de creatividad de la mejora (predeterminado: 3). |
| `preservación_de_rostros` | BOOLEAN | No | - | Preserva la identidad facial de los sujetos en la imagen (predeterminado: True). |
| `preservación_de_color` | BOOLEAN | No | - | Preserva los colores originales de la imagen de entrada (predeterminado: True). |

**Nota:** Este nodo solo puede procesar una sola imagen de entrada. Proporcionar un lote de múltiples imágenes generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------------|---------------|-------------|
| `imagen` | IMAGE | La imagen de salida mejorada. |

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
