# ImagenLatenteChromaRadianceVacía

El nodo EmptyChromaRadianceLatentImage crea una imagen latente vacía con dimensiones específicas para usar en flujos de trabajo de Chroma Radiance. Genera un tensor relleno de ceros (que contiene 3 canales de color) que sirve como punto de partida para operaciones en el espacio latente. El nodo permite definir el ancho, el alto y el tamaño de lote de la imagen latente vacía.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho de la imagen latente en píxeles (predeterminado: 1024, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `height` | El alto de la imagen latente en píxeles (predeterminado: 1024, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `batch_size` | El número de imágenes latentes a generar en un lote (predeterminado: 1) | INT | No | 1 to 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El tensor de imagen latente vacía generado con las dimensiones especificadas, relleno de ceros | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
