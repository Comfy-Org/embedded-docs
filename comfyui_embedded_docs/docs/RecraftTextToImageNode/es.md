# Recraft Texto a Imagen

Genera imágenes de forma síncrona según el prompt y la resolución. Este nodo se conecta a la API de Recraft para crear imágenes a partir de descripciones de texto con dimensiones especificadas y parámetros opcionales de estilo y control.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt para la generación de la imagen. (por defecto: "") | STRING | Sí | - |
| `size` | El tamaño de la imagen generada. (por defecto: "1024x1024") | COMBO | Sí | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | El número de imágenes a generar. (por defecto: 1) | INT | Sí | 1-6 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (por defecto: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección de estilo opcional para la generación de imágenes. Cuando no se proporciona, se usa por defecto el estilo de imagen realista. | RECRAFT_STYLE | No | Múltiples opciones disponibles |
| `negative_prompt` | Una descripción de texto opcional de elementos no deseados en una imagen. (por defecto: "") | STRING | No | - |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | RECRAFT_CONTROLS | No | Múltiples opciones disponibles |

**Nota:** El parámetro `seed` solo controla cuándo se vuelve a ejecutar el nodo, pero no hace que la generación de imágenes sea determinista. Las imágenes de salida reales variarán incluso con el mismo valor de semilla.

**Nota:** El parámetro `prompt` debe tener entre 1 y 1000 caracteres de longitud.

**Nota:** Si usas un `style_id` de Infinite Style Library, asegúrate de que no sea un estilo de arte vectorial, ya que esto devolverá datos SVG en lugar de una imagen y causará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La(s) imagen(es) generada(s) como salida de tensor por lotes. Cuando se generan múltiples imágenes (n > 1), se concatenan a lo largo de la dimensión del lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `d75b7dd2d8cee70c3bc1d2c64fb07ce814a3672619e8647f4c4c2cdc2635945c`
