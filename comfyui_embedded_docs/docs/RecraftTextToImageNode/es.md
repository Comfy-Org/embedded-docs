Genera imágenes de forma síncrona basándose en un prompt y resolución. Este nodo se conecta a la API de Recraft para crear imágenes a partir de descripciones de texto con dimensiones específicas y parámetros opcionales de estilo y control.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para la generación de la imagen. (valor predeterminado: "") | STRING | Sí | - |
| `tamaño` | El tamaño de la imagen generada. (valor predeterminado: "1024x1024") | COMBO | Sí | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | La cantidad de imágenes a generar. (valor predeterminado: 1) | INT | Sí | 1-6 |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (valor predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección opcional de estilo para la generación de imágenes. Cuando no se proporciona, se establece por defecto el estilo "realistic_image". | RECRAFT_STYLE | No | Múltiples opciones disponibles |
| `negative_prompt` | Una descripción textual opcional de elementos no deseados en una imagen. (valor predeterminado: "") | STRING | No | - |
| `recraft_controls` | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. | RECRAFT_CONTROLS | No | Múltiples opciones disponibles |

**Nota:** El parámetro `seed` solo controla cuándo se re-ejecuta el nodo, pero no hace que la generación de imágenes sea determinista. Las imágenes de salida reales variarán incluso con el mismo valor de semilla.

**Nota:** El parámetro `prompt` debe tener una longitud entre 1 y 1000 caracteres.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La(s) imagen(es) generada(s) como una salida de tensor por lotes. Cuando se generan múltiples imágenes (n > 1), se concatenan a lo largo de la dimensión del lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `28c510ccfad13ddb50700b465af14deaa3c7c1f8597fef048d89094fd24fcd7d`
