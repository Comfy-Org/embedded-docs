# Edición de imagen Grok

El nodo Grok Image Edit modifica una imagen existente basándose en un prompt de texto. Utiliza la API de Grok para generar una o más imágenes nuevas que son variaciones de la entrada, guiadas por tu descripción.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo de IA específico que se utilizará para la edición de imágenes. | COMBO | Sí | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | La(s) imagen(es) de entrada que se editarán. Admite hasta 3 imágenes de entrada, excepto para el modelo "pro", que solo admite 1. | IMAGE | Sí |  |
| `prompt` | El prompt de texto utilizado para generar la imagen. Debe tener al menos 1 carácter después de eliminar los espacios en blanco. | STRING | Sí |  |
| `resolution` | La resolución de la imagen de salida. | COMBO | Sí | `"1K"`<br>`"2K"` |
| `number_of_images` | Número de imágenes editadas a generar (predeterminado: 1). | INT | Sí | 1 a 10 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `aspect_ratio` | La relación de aspecto de la imagen de salida. Solo se permite cuando hay varias imágenes conectadas a la entrada de imagen. Si se establece en "auto", la relación de aspecto se determina automáticamente (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Restricciones importantes:**
- La entrada `image` admite hasta 3 imágenes, excepto cuando se utiliza el modelo `grok-imagine-image-pro`, que solo admite 1 imagen de entrada.
- El parámetro `aspect_ratio` solo puede establecerse en un valor personalizado (no "auto") cuando hay varias imágenes conectadas a la entrada `image`. Establecer una relación de aspecto personalizada con una sola imagen de entrada provocará un error.

**Nota:** Este nodo está obsoleto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La(s) imagen(es) editada(s) generadas por el nodo. Si `number_of_images` es mayor que 1, las salidas se concatenan en un lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
