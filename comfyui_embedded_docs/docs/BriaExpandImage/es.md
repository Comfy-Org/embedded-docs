# BriaExpandImage

Bria Expand Image expande una imagen más allá de sus bordes originales generando contenido nuevo con Bria. Permite elegir una relación de aspecto objetivo, una relación personalizada o definir un lienzo con colocación manual de la imagen original. La expansión puede guiarse con un prompt de texto, y Bria generará uno automáticamente si el prompt se deja vacío.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen de entrada que se va a expandir. | IMAGE | Sí | — |
| `expand_mode` | Forma objetivo de la imagen expandida: una relación de aspecto predefinida, una relación personalizada o la colocación manual de la imagen original en un lienzo. Manual es el único modo que puede alcanzar un lienzo más alto que 1:2. Seleccionar `custom_ratio` muestra `ratio_width` y `ratio_height`. Seleccionar `manual` muestra el lienzo y los parámetros de colocación de la imagen. | DYNAMIC_COMBO | Sí | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | Lado del ancho de la relación objetivo: 21 y 9 dan 21:9. Predeterminado: 21. | INT | Condicional | 1–100 |
| `ratio_height` | Lado de la altura de la relación objetivo: 21 y 9 dan 21:9. Bria solo acepta relaciones ancho/alto entre 0.5 y 3.0, por lo que cualquier proporción más alta que 1:2 necesita el modo manual. Predeterminado: 9. | INT | Condicional | 1–100 |
| `canvas_width` | Ancho del lienzo de salida en píxeles. Predeterminado: 1000. | INT | Condicional | 64–5000 |
| `canvas_height` | Alto del lienzo de salida en píxeles. Predeterminado: 1000. | INT | Condicional | 64–5000 |
| `image_width` | Ancho de la imagen original dentro del lienzo. Predeterminado: 500. | INT | Condicional | 1–5000 |
| `image_height` | Alto de la imagen original dentro del lienzo. Predeterminado: 500. | INT | Condicional | 1–5000 |
| `image_x` | Posición X de la esquina superior izquierda de la imagen dentro del lienzo; puede quedar fuera del lienzo, recortando la imagen. Predeterminado: 250. | INT | Condicional | -5000–5000 |
| `image_y` | Posición Y de la esquina superior izquierda de la imagen dentro del lienzo; puede quedar fuera del lienzo, recortando la imagen. Predeterminado: 250. | INT | Condicional | -5000–5000 |
| `prompt` | Descripción opcional de la escena expandida; cuando está vacío, Bria genera una a partir de la imagen. Predeterminado: cadena vacía. | STRING | No | Cualquier cadena |
| `negative_prompt` | Un prompt negativo opcional para la expansión. Predeterminado: cadena vacía. | STRING | No | Cualquier cadena |
| `seed` | Semilla para el proceso de generación aleatoria. Predeterminado: 42. | INT | No | 1–2147483647 |
| `moderation` | Configuración de moderación. Cuando está establecido en `true`, se muestran opciones de moderación adicionales. | DYNAMIC_COMBO | No | `"false"`<br>`"true"` |
| `prompt_content_moderation` | Si está habilitado, modera el contenido del prompt. Predeterminado: false. Solo disponible cuando `moderation` es `true`. | BOOLEAN | Condicional | true/false |
| `visual_input_moderation` | Si está habilitado, modera la entrada visual. Predeterminado: false. Solo disponible cuando `moderation` es `true`. | BOOLEAN | Condicional | true/false |
| `visual_output_moderation` | Si está habilitado, modera la salida visual. Predeterminado: false. Solo disponible cuando `moderation` es `true`. | BOOLEAN | Condicional | true/false |

Cuando `expand_mode` es `custom_ratio`, `ratio_width` y `ratio_height` definen una relación de aspecto objetivo. Bria solo acepta relaciones ancho-alto entre 0.5 y 3.0. Si la relación está fuera de este rango, se produce un error y se debe usar el modo `manual` en su lugar.

Cuando `expand_mode` es `manual`, la imagen original se coloca en un lienzo con el tamaño y la posición especificados. La imagen puede extenderse fuera del lienzo, en cuyo caso la parte exterior se recorta.

Cuando `moderation` es `true`, los tres valores booleanos de moderación se envían a Bria. Cuando `moderation` es `false`, se ignoran.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen expandida generada por Bria. | IMAGE |
| `prompt` | El prompt utilizado para la expansión; generado automáticamente por Bria cuando el prompt de entrada está vacío. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/es.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
