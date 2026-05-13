> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/es.md)

Este nodo toma una lista de teselas de imagen y las fusiona nuevamente en una sola imagen más grande. Está diseñado para reconstruir una imagen que previamente se dividió en una cuadrícula de teselas superpuestas, utilizando una técnica de mezcla ponderada para crear un resultado final sin costuras.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image_list` | IMAGE | Sí | N/A | Una lista de teselas de imagen que se fusionarán. La primera tesela de la lista se utiliza para determinar las dimensiones de las teselas y el tipo de dato para todo el proceso. |
| `final_width` | INT | Sí | 64 - 32768 | El ancho de la imagen fusionada final en píxeles (valor predeterminado: 1024). |
| `final_height` | INT | Sí | 64 - 32768 | La altura de la imagen fusionada final en píxeles (valor predeterminado: 1024). |
| `overlap` | INT | Sí | 0 - 4096 | La cantidad de superposición entre teselas adyacentes en píxeles. Un valor mayor que 0 permite un efecto de mezcla suave en las uniones de las teselas (valor predeterminado: 128). |

**Nota:** La `image_list` es una lista de entrada dinámica. El nodo procesará las teselas en el orden en que se proporcionen, hasta la cantidad necesaria para llenar la cuadrícula definida por `final_width`, `final_height` y las dimensiones de la primera tesela. Si la lista contiene más teselas de las necesarias, las teselas adicionales se ignoran.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen fusionada final, reconstruida a partir de las teselas de entrada. |

---
**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`
