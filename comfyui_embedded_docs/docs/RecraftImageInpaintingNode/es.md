> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/es.md)

Este nodo modifica imágenes basándose en un texto descriptivo y una máscara. Utiliza la API de Recraft para editar inteligentemente áreas específicas de una imagen que defines con una máscara, manteniendo el resto de la imagen sin cambios.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que será modificada |
| `mask` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben ser modificadas |
| `prompt` | STRING | Sí | - | Texto descriptivo para la generación de la imagen (valor por defecto: cadena vacía) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (valor por defecto: 1, mínimo: 1, máximo: 6) |
| `semilla` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0, mínimo: 0, máximo: 18446744073709551615) |
| `recraft_style` | STYLEV3 | No | - | Parámetro de estilo opcional para la API de Recraft |
| `negative_prompt` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen (valor por defecto: cadena vacía) |

*Nota: La `image` y la `mask` deben proporcionarse juntas para que la operación de inpainting funcione. La máscara se redimensionará automáticamente para que coincida con las dimensiones de la imagen.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La(s) imagen(es) modificada(s) generada(s) basándose en el texto descriptivo y la máscara |