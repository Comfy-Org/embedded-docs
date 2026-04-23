> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/es.md)

El nodo Dividir Imagen en Lista de Mosaicos divide una única imagen de entrada en una serie de secciones rectangulares más pequeñas y superpuestas llamadas mosaicos. Crea una lista agrupada (batch) de estos mosaicos, que pueden ser procesados individualmente por otros nodos. Se puede especificar el tamaño de cada mosaico y la cantidad de superposición entre ellos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se dividirá en mosaicos. |
| `tile_width` | INT | No | 64 a 1048576 | El ancho de cada mosaico de salida en píxeles (valor por defecto: 1024). |
| `tile_height` | INT | No | 64 a 1048576 | La altura de cada mosaico de salida en píxeles (valor por defecto: 1024). |
| `overlap` | INT | No | 0 a 4096 | El número de píxeles que se superpondrán entre mosaicos adyacentes (valor por defecto: 128). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | Una lista agrupada (batch) que contiene todos los mosaicos de imagen individuales. |