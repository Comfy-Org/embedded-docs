El nodo `ImageBatch` está diseñado para combinar dos imágenes en un solo lote. Si las dimensiones de las imágenes no coinciden, automáticamente redimensiona la segunda imagen para que coincida con las dimensiones de la primera antes de combinarlas.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image1`  | `IMAGE`     | La primera imagen que se combinará en el lote. Sirve como referencia para las dimensiones a las que se ajustará la segunda imagen si es necesario. |
| `image2`  | `IMAGE`     | La segunda imagen que se combinará en el lote. Se redimensiona automáticamente para coincidir con las dimensiones de la primera imagen si difieren. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El lote combinado de imágenes, con la segunda imagen redimensionada para coincidir con las dimensiones de la primera si es necesario. |
