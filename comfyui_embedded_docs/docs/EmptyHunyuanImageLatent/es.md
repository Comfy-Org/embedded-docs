> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/es.md)

El nodo EmptyHunyuanImageLatent crea un tensor latente vacío con dimensiones específicas para su uso con modelos de generación de imágenes Hunyuan. Genera un punto de partida en blanco que puede procesarse a través de nodos posteriores en el flujo de trabajo. El nodo permite especificar el ancho, alto y tamaño del lote del espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 64 a MAX_RESOLUTION | El ancho de la imagen latente generada en píxeles (por defecto: 2048, paso: 32) |
| `height` | INT | Sí | 64 a MAX_RESOLUTION | El alto de la imagen latente generada en píxeles (por defecto: 2048, paso: 32) |
| `batch_size` | INT | Sí | 1 a 4096 | El número de muestras latentes a generar en un lote (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Un tensor latente vacío con las dimensiones especificadas para el procesamiento de imágenes Hunyuan |