> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/es.md)

El nodo Kling Omni Image (Pro) crea o edita imágenes utilizando el modelo más reciente de Kling AI. Genera imágenes basándose en una descripción textual y puede usar opcionalmente imágenes de referencia para guiar el estilo o el contenido. El nodo envía una solicitud a una API externa, que procesa la tarea y devuelve la(s) imagen(es) final(es).

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-image-o1"` | El modelo específico de Kling AI a utilizar para la generación de imágenes. |
| `prompt` | STRING | Sí | - | Una descripción textual que describe el contenido de la imagen. Puede incluir tanto descripciones positivas como negativas. El texto debe tener entre 1 y 2500 caracteres de longitud. |
| `resolution` | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` | La resolución objetivo para la imagen generada. Nota: La resolución 4K no es compatible con el modelo `kling-image-o1`. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | La relación de aspecto deseada (ancho a alto) para la imagen generada. |
| `cantidad_de_series` | COMBO | Sí | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` | Generar una serie de imágenes. Esta función no es compatible con el modelo `kling-image-o1`. (valor predeterminado: "disabled") |
| `reference_images` | IMAGE | No | - | Hasta 10 imágenes de referencia adicionales. Cada imagen debe tener al menos 300 píxeles tanto de ancho como de alto, y su relación de aspecto debe estar entre 1:2.5 y 2.5:1. |
| `semilla` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe reejecutarse; los resultados no son deterministas independientemente de la semilla. (valor predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `image` | IMAGE | La(s) imagen(es) final(es) generada(s) o editada(s) por el modelo Kling AI. Si se solicitó una serie, se devuelven múltiples imágenes como un lote. |

---
**Source fingerprint (SHA-256):** `7bbed260436bc60e284c99e091cd28b2b0cf50e98e876f94278f1ac2834e61f8`
