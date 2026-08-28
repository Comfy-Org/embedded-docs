# Mejorar imagen con Topaz

El nodo Topaz Image Enhance proporciona escalado y mejora de imágenes estándar de la industria. Procesa una única imagen de entrada utilizando un modelo de IA basado en la nube para mejorar la calidad, el detalle y la resolución. El nodo ofrece un control detallado sobre el proceso de mejora, incluyendo opciones para guía creativa, enfoque en el sujeto y preservación facial.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo de IA que se utilizará para la mejora de imágenes. | COMBO | Sí | `"Reimagine"` |
| `imagen` | La imagen de entrada que se va a mejorar. Solo se admite una imagen. | IMAGE | Sí | - |
| `prompt` | Indicación de texto opcional para guiar el escalado creativo (por defecto: vacío). | STRING | No | - |
| `detección_de_sujetos` | Controla en qué parte de la imagen se centra la mejora (por defecto: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `mejora_de_rostros` | Mejora los rostros (si están presentes) durante el procesamiento (por defecto: True). | BOOLEAN | No | - |
| `creatividad_mejora_rostros` | Establece el nivel de creatividad para la mejora de rostros (por defecto: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `intensidad_mejora_rostros` | Controla la nitidez de los rostros mejorados en relación con el fondo (por defecto: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `recortar_para_ajustar` | De forma predeterminada, la imagen se ajusta con barras negras cuando la relación de aspecto de salida difiere. Actívalo para recortar la imagen y rellenar las dimensiones de salida (por defecto: False). | BOOLEAN | No | - |
| `ancho_de_salida` | Un valor de cero significa que se calcula automáticamente (normalmente será el tamaño original u output_height si se especifica) (por defecto: 0). | INT | No | 0 - 32000 |
| `alto_de_salida` | Un valor de cero significa generar con la misma altura que la original o con output width (por defecto: 0). | INT | No | 0 - 32000 |
| `creatividad` | Controla el nivel general de creatividad de la mejora (por defecto: 3). | INT | No | 1 - 9 |
| `preservación_de_rostros` | Preserva la identidad facial de los sujetos (por defecto: True). | BOOLEAN | No | - |
| `preservación_de_color` | Preserva los colores originales (por defecto: True). | BOOLEAN | No | - |

**Nota:** Este nodo solo puede procesar una única imagen de entrada. Proporcionar un lote de varias imágenes provocará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen de salida mejorada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/es.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
