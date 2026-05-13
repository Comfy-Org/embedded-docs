> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/es.md)

El nodo Quiver Text to SVG genera una imagen de Gráfico Vectorial Escalable (SVG) a partir de una descripción textual utilizando los modelos de Quiver AI. Opcionalmente, puedes proporcionar imágenes de referencia e instrucciones de estilo para guiar el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción textual del resultado SVG deseado. Esta es la instrucción principal sobre qué generar. |
| `instructions` | STRING | No | N/A | Orientación adicional sobre estilo o formato. Este es un parámetro opcional y avanzado. |
| `reference_images` | IMAGE | No | 0 a 4 imágenes | Hasta 4 imágenes de referencia para guiar la generación. Esta es una entrada opcional. |
| `model` | COMBO | Sí | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` | Modelo a utilizar para la generación de SVG. Las opciones disponibles están determinadas por la API de Quiver. |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla. Valor predeterminado: 0. |

**Nota:** La entrada `reference_images` acepta un máximo de 4 imágenes. Si se proporcionan más, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `SVG` | SVG | La imagen de Gráfico Vectorial Escalable (SVG) generada. |

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`
