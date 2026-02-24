> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/es.md)

El nodo Batch Images/Masks/Latents combina múltiples entradas del mismo tipo en un solo lote. Detecta automáticamente si las entradas son imágenes, máscaras o representaciones latentes y utiliza el método de agrupación apropiado. Esto es útil para preparar múltiples elementos para su procesamiento por nodos que aceptan entradas en lote.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `inputs` | IMAGE, MASK o LATENT | Sí | 1 a 50 entradas | Una lista dinámica de entradas que se combinarán en un lote. Puede agregar entre 1 y 50 elementos. Todos los elementos deben ser del mismo tipo (todas imágenes, todas máscaras o todos latentes). |

**Nota:** El nodo determina automáticamente el tipo de dato (IMAGE, MASK o LATENT) basándose en el primer elemento de la lista `inputs`. Todos los elementos posteriores deben coincidir con este tipo. El nodo fallará si intenta mezclar diferentes tipos de datos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE, MASK o LATENT | Una única salida en lote. El tipo de dato coincide con el tipo de entrada (IMAGE en lote, MASK en lote o LATENT en lote). |
