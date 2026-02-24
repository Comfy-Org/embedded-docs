> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/es.md)

Este nodo crea un tensor latente vacío específicamente formateado para su uso con el modelo HunyuanVideo 1.5. Genera un punto de partida en blanco para la generación de video al asignar un tensor de ceros con el recuento de canales y las dimensiones espaciales correctas para el espacio latente del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | - | El ancho del fotograma de video en píxeles. |
| `height` | INT | Sí | - | La altura del fotograma de video en píxeles. |
| `length` | INT | Sí | - | El número de fotogramas en la secuencia de video. |
| `batch_size` | INT | No | - | El número de muestras de video a generar en un lote (valor predeterminado: 1). |

**Nota:** Las dimensiones espaciales del tensor latente generado se calculan dividiendo el `width` y `height` de entrada por 16. La dimensión temporal (fotogramas) se calcula como `((length - 1) // 4) + 1`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tensor latente vacío con dimensiones adecuadas para el modelo HunyuanVideo 1.5. El tensor tiene una forma de `[batch_size, 32, frames, height//16, width//16]`. |
