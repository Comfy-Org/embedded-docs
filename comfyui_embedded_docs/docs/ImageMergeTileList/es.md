> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/es.md)

Este nodo toma una lista de mosaicos de imagen y los fusiona nuevamente en una sola imagen más grande. Está diseñado para reconstruir una imagen que previamente fue dividida en una cuadrícula de mosaicos superpuestos, utilizando una técnica de fusión ponderada para crear un resultado final sin costuras.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image_list` | IMAGE | Sí | N/A | Una lista de mosaicos de imagen que se van a fusionar. El primer mosaico de la lista se utiliza para determinar las dimensiones y el tipo de dato de los mosaicos para todo el proceso. |
| `final_width` | INT | No | 64 - 32768 | El ancho de la imagen fusionada final en píxeles (por defecto: 1024). |
| `final_height` | INT | No | 64 - 32768 | La altura de la imagen fusionada final en píxeles (por defecto: 1024). |
| `overlap` | INT | No | 0 - 4096 | La cantidad de superposición entre mosaicos adyacentes en píxeles. Un valor mayor que 0 permite un efecto de fusión suave en las uniones de los mosaicos (por defecto: 128). |

**Nota:** `image_list` es una lista de entrada dinámica. El nodo procesará los mosaicos en el orden en que se proporcionen, hasta el número necesario para llenar la cuadrícula definida por `final_width`, `final_height` y las dimensiones del primer mosaico. Si la lista contiene más mosaicos de los necesarios, los mosaicos adicionales se ignoran.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen fusionada final, reconstruida a partir de los mosaicos de entrada. |