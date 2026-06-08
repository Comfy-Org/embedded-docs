El nodo Topaz Image Enhance proporciona mejora y escalado de imágenes de nivel profesional. Procesa una sola imagen de entrada utilizando un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control preciso sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque en el sujeto y preservación facial.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la mejora de imagen. | COMBO | Sí | `"Reimagine"` |
| `imagen` | La imagen de entrada que se va a mejorar. Solo se admite una imagen. | IMAGE | Sí | - |
| `prompt` | Un texto opcional como guía creativa para el escalado (predeterminado: vacío). | STRING | No | - |
| `detección_de_sujetos` | Controla en qué parte de la imagen se enfoca la mejora (predeterminado: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `mejora_de_rostros` | Activar para mejorar rostros si están presentes en la imagen (predeterminado: True). | BOOLEAN | No | - |
| `creatividad_mejora_rostros` | Establece el nivel de creatividad para la mejora facial (predeterminado: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `intensidad_mejora_rostros` | Controla qué tan nítidos son los rostros mejorados en relación con el fondo (predeterminado: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `recortar_para_ajustar` | De forma predeterminada, la imagen se encuadra con barras cuando la relación de aspecto de salida difiere. Activar para recortar la imagen y llenar las dimensiones de salida (predeterminado: False). | BOOLEAN | No | - |
| `ancho_de_salida` | El ancho deseado de la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en `alto_de_salida` si se especifica (predeterminado: 0). | INT | No | 0 - 32000 |
| `alto_de_salida` | La altura deseada de la imagen de salida. Un valor de 0 significa que se calculará automáticamente, generalmente basado en el tamaño original o en `ancho_de_salida` si se especifica (predeterminado: 0). | INT | No | 0 - 32000 |
| `creatividad` | Controla el nivel general de creatividad de la mejora (predeterminado: 3). | INT | No | 1 - 9 |
| `preservación_de_rostros` | Preserva la identidad facial de los sujetos en la imagen (predeterminado: True). | BOOLEAN | No | - |
| `preservación_de_color` | Preserva los colores originales de la imagen de entrada (predeterminado: True). | BOOLEAN | No | - |

**Nota:** Este nodo solo puede procesar una sola imagen de entrada. Proporcionar un lote de múltiples imágenes generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La imagen de salida mejorada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
