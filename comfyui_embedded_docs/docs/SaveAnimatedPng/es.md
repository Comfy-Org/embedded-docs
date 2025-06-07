
El nodo SaveAnimatedPNG está diseñado para crear y guardar imágenes PNG animadas a partir de una secuencia de fotogramas. Maneja el ensamblaje de fotogramas individuales en una animación coherente, permitiendo la personalización de la duración de los fotogramas, el bucle y la inclusión de metadatos.

## Entradas

| Campo             | Data Type | Descripción                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | Una lista de imágenes que se procesarán y guardarán como un PNG animado. Cada imagen en la lista representa un fotograma en la animación. |
| `filename_prefix` | `STRING`    | Especifica el nombre base para el archivo de salida, que se usará como prefijo para los archivos PNG animados generados. |
| `fps`             | `FLOAT`     | La tasa de fotogramas por segundo para la animación, controlando la rapidez con la que se muestran los fotogramas. |
| `compress_level`  | `INT`       | El nivel de compresión aplicado a los archivos PNG animados, afectando el tamaño del archivo y la claridad de la imagen. |

## Salidas

| Campo | Data Type | Descripción                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Proporciona un componente de UI que muestra las imágenes PNG animadas generadas e indica si la animación es de un solo fotograma o de varios fotogramas. |
