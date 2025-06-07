El nodo `ImageCompositeMasked` está diseñado para componer imágenes, permitiendo la superposición de una imagen fuente sobre una imagen de destino en coordenadas especificadas, con redimensionamiento y enmascaramiento opcionales.

## Entradas

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `destination` | `IMAGE` | La imagen de destino sobre la cual se compondrá la imagen fuente. Sirve como fondo para la operación de composición. |
| `source` | `IMAGE` | La imagen fuente que se compondrá sobre la imagen de destino. Esta imagen puede ser opcionalmente redimensionada para ajustarse a las dimensiones de la imagen de destino. |
| `x` | `INT` | La coordenada x en la imagen de destino donde se colocará la esquina superior izquierda de la imagen fuente. |
| `y` | `INT` | La coordenada y en la imagen de destino donde se colocará la esquina superior izquierda de la imagen fuente. |
| `resize_source` | `BOOLEAN` | Una bandera booleana que indica si la imagen fuente debe ser redimensionada para coincidir con las dimensiones de la imagen de destino. |
| `mask` | `MASK` | Una máscara opcional que especifica qué partes de la imagen fuente deben componerse sobre la imagen de destino. Esto permite operaciones de composición más complejas, como mezclas o superposiciones parciales. |

## Salidas

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `image` | `IMAGE` | La imagen resultante después de la operación de composición, que combina elementos de ambas
