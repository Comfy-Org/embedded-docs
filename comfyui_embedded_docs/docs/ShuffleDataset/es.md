> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/es.md)

El nodo Shuffle Dataset toma una lista de imágenes y cambia aleatoriamente su orden. Utiliza un valor de semilla para controlar la aleatoriedad, garantizando que el mismo orden de mezcla pueda reproducirse. Esto es útil para aleatorizar la secuencia de imágenes en un conjunto de datos antes de su procesamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | La lista de imágenes que se va a mezclar. |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria. Un valor de 0 producirá una mezcla diferente cada vez. (por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | La misma lista de imágenes, pero en un nuevo orden aleatorio mezclado. |
