El nodo `EmptyHunyuanLatentVideo` es similar al nodo `EmptyLatentImage`. Puedes considerarlo como un lienzo en blanco para la generación de videos, donde el ancho, la altura y la longitud definen las propiedades del lienzo, y el tamaño del lote determina el número de lienzos a crear. Este nodo crea lienzos vacíos listos para tareas posteriores de generación de videos.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|------------|-------------|
| width | INT | Ancho del video, por defecto 848, mínimo 16, máximo nodes.MAX_RESOLUTION, paso de 16. |
| height | INT | Altura del video, por defecto 480, mínimo 16, máximo nodes.MAX_RESOLUTION, paso de 16. |
| length | INT | Longitud del video, por defecto 25, mínimo 1, máximo nodes.MAX_RESOLUTION, paso de 4. |
| batch_size | INT | Tamaño del lote, por defecto 1, mínimo 1, máximo 4096. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|------------|-------------|
| samples | LATENT | Muestras de video latentes generadas que contienen tensores nulos, listas para el procesamiento y generación. |
