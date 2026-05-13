> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/es.md)

Genera imágenes de forma síncrona basándose en un prompt y resolución. Este nodo se conecta a la API de Recraft para crear imágenes a partir de descripciones de texto con dimensiones específicas y parámetros opcionales de estilo y control.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de la imagen. (valor predeterminado: "") |
| `size` | COMBO | Sí | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | El tamaño de la imagen generada. (valor predeterminado: "1024x1024") |
| `n` | INT | Sí | 1-6 | La cantidad de imágenes a generar. (valor predeterminado: 1) |
| `seed` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (valor predeterminado: 0) |
| `recraft_style` | RECRAFT_STYLE | No | Múltiples opciones disponibles | Selección opcional de estilo para la generación de imágenes. Cuando no se proporciona, se establece por defecto el estilo "realistic_image". |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen. (valor predeterminado: "") |
| `recraft_controls` | RECRAFT_CONTROLS | No | Múltiples opciones disponibles | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. |

**Nota:** El parámetro `seed` solo controla cuándo se re-ejecuta el nodo, pero no hace que la generación de imágenes sea determinista. Las imágenes de salida reales variarán incluso con el mismo valor de semilla.

**Nota:** El parámetro `prompt` debe tener una longitud entre 1 y 1000 caracteres.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) como una salida de tensor por lotes. Cuando se generan múltiples imágenes (n > 1), se concatenan a lo largo de la dimensión del lote. |

---
**Source fingerprint (SHA-256):** `28c510ccfad13ddb50700b465af14deaa3c7c1f8597fef048d89094fd24fcd7d`
