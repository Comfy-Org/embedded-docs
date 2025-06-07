
Este nodo está diseñado para guardar una secuencia de imágenes como un archivo WEBP animado. Maneja la agregación de fotogramas individuales en una animación cohesiva, aplicando metadatos especificados y optimizando la salida según la calidad y configuraciones de compresión.

## Entradas

| Campo             | Data Type | Descripción                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | Una lista de imágenes que se guardarán como fotogramas en el WEBP animado. Este parámetro es esencial para definir el contenido visual de la animación. |
| `filename_prefix` | `STRING`    | Especifica el nombre base para el archivo de salida, al cual se le añadirá un contador y la extensión '.webp'. Este parámetro es crucial para identificar y organizar los archivos guardados. |
| `fps`             | `FLOAT`     | La tasa de fotogramas por segundo para la animación, influyendo en la velocidad de reproducción. |
| `lossless`        | `BOOLEAN`   | Un booleano que indica si se debe usar compresión sin pérdida, afectando el tamaño del archivo y la calidad de la animación. |
| `quality`         | `INT`       | Un valor entre 0 y 100 que establece el nivel de calidad de compresión, con valores más altos resultando en mejor calidad de imagen pero tamaños de archivo más grandes. |
| `method`          | COMBO[STRING] | Especifica el método de compresión a usar, lo cual puede impactar la velocidad de codificación y el tamaño del archivo. |

## Salidas

| Campo | Data Type | Descripción                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Proporciona un componente de interfaz de usuario que muestra las imágenes WEBP animadas guardadas junto con sus metadatos, e indica si la animación está habilitada. |
