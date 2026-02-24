> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/es.md)

El nodo Recraft V4 Text to Vector genera ilustraciones en formato de gráficos vectoriales escalables (SVG) a partir de una descripción de texto. Se conecta a una API externa para utilizar el modelo Recraft V4 o Recraft V4 Pro para la generación de imágenes. El nodo devuelve una o más imágenes SVG basadas en tu indicación (prompt).

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Indicación (prompt) para la generación de la imagen. Máximo 10.000 caracteres. |
| `negative_prompt` | STRING | No | N/A | Una descripción de texto opcional de elementos no deseados en la imagen. |
| `model` | COMBO | Sí | `"recraftv4"`<br>`"recraftv4_pro"` | El modelo a utilizar para la generación. La selección del modelo cambia las opciones disponibles para `size`. |
| `size` | COMBO | Sí | Para `recraftv4`: `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>Para `recraftv4_pro`: `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` | El tamaño de la imagen generada. Las opciones disponibles dependen del `model` seleccionado. El valor por defecto es `"1024x1024"` para `recraftv4` y `"2048x2048"` para `recraftv4_pro`. |
| `n` | INT | Sí | 1 a 6 | El número de imágenes a generar (por defecto: 1). |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. |
| `recraft_controls` | CUSTOM | No | N/A | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza resultados reproducibles desde la API externa.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | SVG | La(s) imagen(es) generada(s) en formato de gráficos vectoriales escalables (SVG). |