> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

Este nodo genera imágenes a partir de descripciones de texto utilizando los modelos de IA Recraft V4 o V4 Pro. Envía su *prompt* a una API externa y devuelve las imágenes generadas. Puede controlar la salida especificando el modelo, el tamaño de la imagen y el número de imágenes a crear.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | *Prompt* para la generación de la imagen. Máximo 10.000 caracteres. |
| `negative_prompt` | STRING | No | N/A | Una descripción de texto opcional de elementos no deseados en la imagen. |
| `model` | COMBO | Sí | `"recraftv4"`<br>`"recraftv4_pro"` | El modelo a utilizar para la generación. La selección del modelo determina los tamaños de imagen disponibles. |
| `size` | COMBO | Sí | Varía según el modelo | El tamaño de la imagen generada. Las opciones disponibles dependen del modelo seleccionado. Para `recraftv4`, el valor por defecto es "1024x1024". Para `recraftv4_pro`, el valor por defecto es "2048x2048". |
| `n` | INT | Sí | 1 a 6 | El número de imágenes a generar (por defecto: 1). |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). |
| `recraft_controls` | CUSTOM | No | N/A | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza salidas de imagen reproducibles.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen o lote de imágenes generadas. |
