> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/es.md)

El nodo Image Grid combina múltiples imágenes en una sola cuadrícula o collage organizado. Toma una lista de imágenes y las organiza en un número específico de columnas, redimensionando cada imagen para ajustarse a un tamaño de celda definido y añadiendo un relleno opcional entre ellas. El resultado es una única imagen nueva que contiene todas las imágenes de entrada en un diseño de cuadrícula.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | Una lista de imágenes que se organizarán en la cuadrícula. El nodo requiere al menos una imagen para funcionar. |
| `columns` | INT | No | 1 - 20 | El número de columnas en la cuadrícula (por defecto: 4). |
| `cell_width` | INT | No | 32 - 2048 | El ancho, en píxeles, de cada celda en la cuadrícula (por defecto: 256). |
| `cell_height` | INT | No | 32 - 2048 | La altura, en píxeles, de cada celda en la cuadrícula (por defecto: 256). |
| `padding` | INT | No | 0 - 50 | La cantidad de relleno, en píxeles, que se colocará entre las imágenes en la cuadrícula (por defecto: 4). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La única imagen de salida que contiene todas las imágenes de entrada organizadas en una cuadrícula. |
