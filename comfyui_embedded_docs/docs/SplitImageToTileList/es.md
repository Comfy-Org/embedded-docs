> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/es.md)

El nodo **Dividir Imagen en Lista de Teselas** divide una única imagen de entrada en una serie de secciones rectangulares más pequeñas y superpuestas llamadas teselas. Crea una lista por lotes de estas teselas, que pueden procesarse individualmente mediante otros nodos. Se puede especificar el tamaño de cada tesela y la cantidad de superposición entre ellas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se dividirá en teselas. |
| `tile_width` | INT | Sí | 64 a 1048576 | El ancho de cada tesela de salida en píxeles (predeterminado: 1024). |
| `tile_height` | INT | Sí | 64 a 1048576 | La altura de cada tesela de salida en píxeles (predeterminado: 1024). |
| `overlap` | INT | Sí | 0 a 4096 | La cantidad de píxeles que se superpondrán las teselas adyacentes (predeterminado: 128). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | Una lista por lotes que contiene todas las teselas de imagen individuales. |

---
**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`
