> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/es.md)

Este nodo está diseñado para guardar una secuencia de imágenes como un archivo WEBP animado. Gestiona la agregación de fotogramas individuales en una animación cohesiva, aplicando metadatos específicos y optimizando la salida según la configuración de calidad y compresión.

## Entradas

| Campo             | Tipo de Dato | Descripción                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `imágenes`          | `IMAGE`     | Una lista de imágenes que se guardarán como fotogramas en el WEBP animado. Este parámetro es esencial para definir el contenido visual de la animación. |
| `prefijo_nombre_archivo` | `STRING`    | Especifica el nombre base para el archivo de salida, al cual se le añadirá un contador y la extensión '.webp'. Este parámetro es crucial para identificar y organizar los archivos guardados. |
| `fps`             | `FLOAT`     | La velocidad de fotogramas por segundo de la animación, que influye en la velocidad de reproducción. |
| `sin_pérdidas`        | `BOOLEAN`   | Un valor booleano que indica si se debe usar compresión sin pérdida, afectando el tamaño del archivo y la calidad de la animación. |
| `calidad`         | `INT`       | Un valor entre 0 y 100 que establece el nivel de calidad de compresión, donde valores más altos resultan en mejor calidad de imagen pero archivos de mayor tamaño. |
| `método`          | COMBO[STRING] | Especifica el método de compresión a utilizar, lo que puede afectar la velocidad de codificación y el tamaño del archivo. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Proporciona un componente de interfaz que muestra las imágenes WEBP animadas guardadas junto con sus metadatos, e indica si la animación está habilitada. |