# Recraft V4 Texto a Vector

El nodo Recraft V4 Texto a Vector genera ilustraciones en formato de Gráficos Vectoriales Escalables (SVG) a partir de una descripción textual. Se conecta a una API externa para utilizar el modelo Recraft V4 o Recraft V4 Pro en la generación de imágenes. El nodo produce una o más imágenes SVG según tu indicación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación para la generación de la imagen. Máximo 10,000 caracteres. | STRING | Sí | N/A |
| `prompt_negativo` | Descripción textual opcional de elementos no deseados en una imagen. | STRING | No | N/A |
| `modelo` | El modelo a utilizar para la generación. Seleccionar un modelo cambia las opciones disponibles de `size`. | COMBO | Sí | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | El tamaño de la imagen generada. Las opciones disponibles dependen del `modelo` seleccionado. El valor predeterminado es `"1024x1024"` para `recraftv4` y `"2048x2048"` para `recraftv4_pro`. | COMBO | Sí | Para `recraftv4`: `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>Para `recraftv4_pro`: `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` |
| `n` | La cantidad de imágenes a generar (predeterminado: 1). | INT | Sí | 1 a 6 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación a través del nodo Controles Recraft. | CUSTOM | No | N/A |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza resultados reproducibles desde la API externa.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La(s) imagen(es) de Gráficos Vectoriales Escalables (SVG) generada(s). | SVG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/es.md)

---
**Source fingerprint (SHA-256):** `ffab67555923cea29b50ae71e3ffaad13340aead4d01973a70244468fae4420d`
