# ImagenLatenteChromaRadianceVacía

El nodo `EmptyChromaRadianceLatentImage` crea una imagen latente vacía con las dimensiones especificadas para su uso en flujos de trabajo de chroma radiance. Genera un tensor relleno con ceros que sirve como punto de partida para operaciones en el espacio latente. El nodo le permite definir el ancho, la altura y el tamaño de lote de la imagen latente vacía.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente en píxeles (predeterminado: 1024, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | La altura de la imagen latente en píxeles (predeterminado: 1024, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `tamaño_lote` | La cantidad de imágenes latentes a generar en un lote (predeterminado: 1) | INT | No | 1 a 4096 |

Nota: `width` y `height` se definen con un paso de 16, por lo que deben ser múltiplos de 16.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El tensor de imagen latente vacía generado, relleno con ceros, con la forma batch_size x 3 x height x width | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
