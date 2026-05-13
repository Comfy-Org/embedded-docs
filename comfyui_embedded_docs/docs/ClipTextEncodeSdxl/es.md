> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/es.md)

Este nodo está diseñado para codificar texto de entrada utilizando un modelo CLIP específicamente personalizado para la arquitectura SDXL. Emplea un sistema de codificación dual (CLIP-L y CLIP-G) para procesar descripciones textuales, lo que resulta en una generación de imágenes más precisa.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `clip` | CLIP | Instancia del modelo CLIP utilizada para la codificación de texto. |
| `width` | INT | Especifica el ancho de la imagen en píxeles, valor predeterminado 1024. |
| `height` | INT | Especifica la altura de la imagen en píxeles, valor predeterminado 1024. |
| `crop_w` | INT | Ancho del área de recorte en píxeles, valor predeterminado 0. |
| `crop_h` | INT | Altura del área de recorte en píxeles, valor predeterminado 0. |
| `target_width` | INT | Ancho objetivo para la imagen de salida, valor predeterminado 1024. |
| `target_height` | INT | Altura objetivo para la imagen de salida, valor predeterminado 1024. |
| `text_g` | STRING | Descripción textual global para la descripción general de la escena. |
| `text_l` | STRING | Descripción textual local para la descripción de detalles. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Contiene el texto codificado y la información condicional necesaria para la generación de imágenes. |