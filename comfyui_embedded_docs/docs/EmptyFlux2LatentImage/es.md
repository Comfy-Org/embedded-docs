> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/es.md)

El nodo EmptyFlux2LatentImage crea una representación latente en blanco y vacía. Genera un tensor lleno de ceros, que sirve como punto de partida para el proceso de eliminación de ruido del modelo Flux. Las dimensiones del latente están determinadas por el ancho y alto de entrada, reducidas por un factor de 16.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 a 8192 | El ancho de la imagen final a generar. El ancho latente será este valor dividido por 16. El valor por defecto es 1024. |
| `height` | INT | Sí | 16 a 8192 | La altura de la imagen final a generar. La altura latente será este valor dividido por 16. El valor por defecto es 1024. |
| `batch_size` | INT | No | 1 a 4096 | El número de muestras latentes a generar en un solo lote. El valor por defecto es 1. |

**Nota:** Las entradas `width` y `height` deben ser divisibles por 16, ya que el nodo las divide internamente por este factor para crear las dimensiones latentes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tensor latente lleno de ceros. La forma es `[batch_size, 128, height // 16, width // 16]`. |
