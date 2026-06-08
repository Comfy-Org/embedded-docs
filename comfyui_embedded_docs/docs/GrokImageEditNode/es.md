El nodo Grok Image Edit modifica una imagen existente basándose en un prompt de texto. Utiliza la API de Grok para generar una o más imágenes nuevas que son variaciones de la entrada, guiadas por tu descripción.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA específico a utilizar para la edición de imágenes. | COMBO | Sí | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `imagen` | La(s) imagen(es) de entrada que se editarán. Admite hasta 3 imágenes de entrada, excepto para el modelo "pro" que solo admite 1. | IMAGE | Sí |  |
| `indicación` | El prompt de texto utilizado para generar la imagen editada. Debe tener al menos 1 carácter después de eliminar espacios en blanco. | STRING | Sí |  |
| `resolución` | La resolución de la imagen de salida. | COMBO | Sí | `"1K"`<br>`"2K"` |
| `número de imágenes` | Número de imágenes editadas a generar (predeterminado: 1). | INT | No | 1 a 10 |
| `semilla` | Semilla para determinar si el nodo debe reejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `relación de aspecto` | La relación de aspecto para la imagen de salida. Solo se permite cuando múltiples imágenes están conectadas a la entrada de imagen. Si se establece en "auto", la relación de aspecto se determina automáticamente (predeterminado: "auto"). | COMBO | No | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Restricciones importantes:**
- La entrada `image` admite hasta 3 imágenes, excepto cuando se utiliza el modelo `grok-imagine-image-pro`, que solo admite 1 imagen de entrada.
- El parámetro `aspect_ratio` solo puede establecerse en un valor personalizado (distinto de "auto") cuando múltiples imágenes están conectadas a la entrada `image`. Establecer una relación de aspecto personalizada con una sola imagen de entrada provocará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La(s) imagen(es) editada(s) generada(s) por el nodo. Si `número de imágenes` es mayor que 1, las salidas se concatenan en un lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `021d867e9e04451c0c4ef035c19fa86ebc8d4a3f64572aff33f493324d7fe308`
