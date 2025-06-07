
El nodo RebatchImages está diseñado para reorganizar un lote de imágenes en una nueva configuración de lote, ajustando el tamaño del lote según lo especificado. Este proceso es esencial para gestionar y optimizar el procesamiento de datos de imágenes en operaciones por lotes, asegurando que las imágenes se agrupen según el tamaño de lote deseado para un manejo eficiente.

## Entradas

| Campo       | Data Type | Descripción                                                                         |
|-------------|-------------|-------------------------------------------------------------------------------------|
| `images`    | `IMAGE`     | Una lista de imágenes que se reorganizarán. Este parámetro es crucial para determinar los datos de entrada que se someterán al proceso de reorganización. |
| `batch_size`| `INT`       | Especifica el tamaño deseado de los lotes de salida. Este parámetro influye directamente en cómo se agrupan y procesan las imágenes de entrada, impactando la estructura de la salida. |

## Salidas

| Campo | Data Type | Descripción                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | La salida consiste en una lista de lotes de imágenes, reorganizados según el tamaño de lote especificado. Esto permite un procesamiento flexible y eficiente de los datos de imágenes en operaciones por lotes. |
