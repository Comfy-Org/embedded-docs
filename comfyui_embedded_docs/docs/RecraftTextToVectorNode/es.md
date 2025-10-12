> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/es.md)

Genera SVG de forma síncrona basándose en el prompt y la resolución. Este nodo crea ilustraciones vectoriales enviando prompts de texto a la API de Recraft y devuelve el contenido SVG generado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de imagen. (valor por defecto: "") |
| `substyle` | COMBO | Sí | Múltiples opciones disponibles | El estilo de ilustración específico a utilizar para la generación. Las opciones son determinadas por los subestilos de ilustración vectorial disponibles en RecraftStyleV3. |
| `tamaño` | COMBO | Sí | Múltiples opciones disponibles | El tamaño de la imagen generada. (valor por defecto: 1024x1024) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar. (valor por defecto: 1, min: 1, max: 6) |
| `semilla` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (valor por defecto: 0, min: 0, max: 18446744073709551615) |
| `negative_prompt` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen. (valor por defecto: "") |
| `recraft_controls` | CONTROLS | No | - | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls. |

**Nota:** El parámetro `seed` solo controla cuándo el nodo se vuelve a ejecutar pero no hace que los resultados de generación sean deterministas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `SVG` | SVG | La ilustración vectorial generada en formato SVG |
