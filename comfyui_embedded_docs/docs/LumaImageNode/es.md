> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/es.md)

Genera imágenes de forma síncrona basándose en el prompt y la relación de aspecto. Este nodo crea imágenes utilizando descripciones de texto y permite controlar las dimensiones y el estilo de la imagen a través de varias entradas de referencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de imágenes (valor por defecto: cadena vacía) |
| `model` | COMBO | Sí | Múltiples opciones disponibles | Selección del modelo para la generación de imágenes |
| `aspect_ratio` | COMBO | Sí | Múltiples opciones disponibles | Relación de aspecto para la imagen generada (valor por defecto: relación 16:9) |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0) |
| `style_image_weight` | FLOAT | No | 0.0 a 1.0 | Peso de la imagen de estilo. Se ignora si no se proporciona style_image (valor por defecto: 1.0) |
| `image_luma_ref` | LUMA_REF | No | - | Conexión del nodo Luma Reference para influir en la generación con imágenes de entrada; se pueden considerar hasta 4 imágenes |
| `style_image` | IMAGE | No | - | Imagen de referencia de estilo; solo se utilizará 1 imagen |
| `character_image` | IMAGE | No | - | Imágenes de referencia de personajes; puede ser un lote de múltiples imágenes, se pueden considerar hasta 4 imágenes |

**Restricciones de Parámetros:**

- El parámetro `image_luma_ref` puede aceptar hasta 4 imágenes de referencia
- El parámetro `character_image` puede aceptar hasta 4 imágenes de referencia de personajes
- El parámetro `style_image` acepta solo 1 imagen de referencia de estilo
- El parámetro `style_image_weight` solo se utiliza cuando se proporciona `style_image`

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada basada en los parámetros de entrada |
