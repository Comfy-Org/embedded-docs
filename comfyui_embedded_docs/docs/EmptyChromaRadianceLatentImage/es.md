> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

El nodo EmptyChromaRadianceLatentImage crea una imagen latente en blanco con dimensiones específicas para su uso en flujos de trabajo de cromorradiancia. Genera un tensor lleno de ceros que sirve como punto de partida para operaciones en el espacio latente. El nodo permite definir el ancho, alto y tamaño del lote de la imagen latente vacía.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho de la imagen latente en píxeles (por defecto: 1024, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | El alto de la imagen latente en píxeles (por defecto: 1024, debe ser divisible por 16) |
| `batch_size` | INT | No | 1 a 4096 | El número de imágenes latentes a generar en un lote (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | El tensor de imagen latente vacía generado con las dimensiones especificadas |