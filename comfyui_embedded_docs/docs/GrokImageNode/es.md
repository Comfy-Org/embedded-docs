El nodo Grok Image genera una o más imágenes basadas en una descripción textual utilizando el modelo de IA Grok. Envía tu indicación a un servicio externo y devuelve las imágenes generadas como tensores que pueden utilizarse en tu flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo Grok específico a utilizar para la generación de imágenes. Diferentes modelos pueden ofrecer distinta calidad, velocidad o características. | COMBO | Sí | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `indicación` | La indicación de texto utilizada para generar la imagen. Esta descripción guía a la IA sobre qué crear. Debe tener al menos 1 carácter de longitud. | STRING | Sí | N/A |
| `relación de aspecto` | La relación ancho-alto deseada para la imagen generada. | COMBO | Sí | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `número de imágenes` | Número de imágenes a generar (predeterminado: 1). | INT | No | 1 a 10 |
| `semilla` | Un valor de semilla para determinar si el nodo debe re-ejecutarse. Los resultados reales de la imagen son no deterministas y variarán incluso con la misma semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `resolución` | La resolución de salida deseada para las imágenes generadas (predeterminado: "1K"). | COMBO | No | `"1K"`<br>`"2K"` |

**Nota:** El parámetro `seed` se utiliza principalmente para controlar cuándo el nodo se re-ejecuta dentro de un flujo de trabajo. Debido a la naturaleza del servicio de IA externo, las imágenes generadas no serán reproducibles ni idénticas entre ejecuciones, incluso con una semilla idéntica.

**Nota sobre precios:** El costo de generar imágenes depende del `model`, la `resolution` y el `number_of_images` seleccionados. Por ejemplo, el modelo "grok-imagine-image-quality" con resolución "1K" cuesta $0.05 por imagen, mientras que la resolución "2K" cuesta $0.07 por imagen. El modelo "grok-imagine-image-pro" cuesta $0.07 por imagen, y otros modelos cuestan $0.02 por imagen.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La imagen generada o un lote de imágenes. Si `número de imágenes` es 1, se devuelve un tensor de imagen único. Si es mayor que 1, se devuelve un lote de tensores de imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/es.md)

---
**Source fingerprint (SHA-256):** `5c8a76d3636dea8bcc6ade0d8adb6e6d1610b518a31e15fc7fce3f107fe63953`
