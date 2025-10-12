> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/es.md)

Genera imágenes de forma síncrona basándose en un prompt y una resolución. Este nodo se conecta a la API de Recraft para crear imágenes a partir de descripciones de texto con dimensiones y opciones de estilo especificadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de imágenes. (valor por defecto: "") |
| `tamaño` | COMBO | Sí | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | El tamaño de la imagen generada. (valor por defecto: "1024x1024") |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar. (valor por defecto: 1) |
| `semilla` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no determinísticos independientemente de la semilla. (valor por defecto: 0) |
| `recraft_style` | COMBO | No | Múltiples opciones disponibles | Selección de estilo opcional para la generación de imágenes. |
| `negative_prompt` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen. (valor por defecto: "") |
| `recraft_controls` | COMBO | No | Múltiples opciones disponibles | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. |

**Nota:** El parámetro `seed` solo controla cuándo el nodo se vuelve a ejecutar pero no hace que la generación de imágenes sea determinística. Las imágenes de salida reales variarán incluso con el mismo valor de semilla.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) como salida de tensor. |