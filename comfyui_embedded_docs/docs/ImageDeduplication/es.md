> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/es.md)

Este nodo elimina imágenes duplicadas o muy similares de un lote. Funciona creando un hash perceptual para cada imagen —una huella digital numérica simple basada en su contenido visual— y luego comparándolos. Las imágenes cuyos hashes sean más similares que un umbral establecido se consideran duplicadas y se filtran.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | El lote de imágenes a procesar para la deduplicación. |
| `similarity_threshold` | FLOAT | No | 0.0 - 1.0 | Umbral de similitud (0-1). Un valor más alto significa mayor similitud. Las imágenes por encima de este umbral se consideran duplicadas. (por defecto: 0.95) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | La lista filtrada de imágenes con los duplicados eliminados. |
