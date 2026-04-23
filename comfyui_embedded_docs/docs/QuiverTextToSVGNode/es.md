> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/es.md)

El nodo Quiver Text to SVG genera una imagen de gráficos vectoriales escalables (SVG) a partir de una descripción de texto utilizando los modelos de Quiver AI. Opcionalmente, se pueden proporcionar imágenes de referencia e instrucciones de estilo para guiar el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción de texto de la salida SVG deseada. Esta es la instrucción principal sobre qué generar. |
| `instructions` | STRING | No | N/A | Guía adicional de estilo o formato. Este es un parámetro avanzado opcional. |
| `reference_images` | IMAGE | No | N/A | Hasta 4 imágenes de referencia para guiar la generación. Esta es una entrada opcional. |
| `model` | COMBO | Sí | Múltiples opciones disponibles | Modelo a utilizar para la generación de SVG. Las opciones disponibles las determina la API de Quiver. |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. Valor por defecto: 0. |

**Nota:** La entrada `reference_images` acepta un máximo de 4 imágenes. Si se proporcionan más, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `SVG` | SVG | La imagen de gráficos vectoriales escalables (SVG) generada. |