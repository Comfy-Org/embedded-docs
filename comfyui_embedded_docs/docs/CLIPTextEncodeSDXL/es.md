# CLIPTextEncodeSDXL

Este nodo está diseñado para codificar texto de entrada utilizando un modelo CLIP específicamente personalizado para la arquitectura SDXL. Emplea un sistema de codificación dual (CLIP-L y CLIP-G) para procesar descripciones textuales, lo que resulta en una generación de imágenes más precisa.

## Entradas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `clip` | Instancia del modelo CLIP utilizada para la codificación de texto. | CLIP |
| `ancho` | Especifica el ancho de la imagen en píxeles, valor predeterminado 1024. | INT |
| `alto` | Especifica la altura de la imagen en píxeles, valor predeterminado 1024. | INT |
| `recorte_ancho` | Ancho del área de recorte en píxeles, valor predeterminado 0. | INT |
| `recorte_alto` | Altura del área de recorte en píxeles, valor predeterminado 0. | INT |
| `ancho_objetivo` | Ancho objetivo para la imagen de salida, valor predeterminado 1024. | INT |
| `alto_objetivo` | Altura objetivo para la imagen de salida, valor predeterminado 1024. | INT |
| `texto_g` | Descripción textual global para la descripción general de la escena. | STRING |
| `texto_l` | Descripción textual local para la descripción de detalles. | STRING |

## Salidas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Contiene el texto codificado y la información condicional necesaria para la generación de imágenes. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/es.md)
