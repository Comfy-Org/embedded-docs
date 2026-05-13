> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/es.md)

El nodo SaveAnimatedPNG está diseñado para crear y guardar imágenes PNG animadas a partir de una secuencia de fotogramas. Gestiona el ensamblaje de fotogramas de imagen individuales en una animación cohesiva, permitiendo la personalización de la duración de los fotogramas, el bucle y la inclusión de metadatos.

## Entradas

| Campo             | Tipo de Dato | Descripción                                                                         |
|-------------------|--------------|-------------------------------------------------------------------------------------|
| `imágenes`          | `IMAGE`      | Una lista de imágenes que se procesarán y guardarán como un PNG animado. Cada imagen en la lista representa un fotograma de la animación. |
| `prefijo_nombre_archivo` | `STRING`     | Especifica el nombre base del archivo de salida, que se utilizará como prefijo para los archivos PNG animados generados. |
| `fps`             | `FLOAT`      | La velocidad de fotogramas por segundo de la animación, que controla la rapidez con la que se muestran los fotogramas. |
| `nivel_compresión`  | `INT`        | El nivel de compresión aplicado a los archivos PNG animados, que afecta el tamaño del archivo y la claridad de la imagen. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                                       |
|-------|--------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A          | Proporciona un componente de interfaz de usuario que muestra las imágenes PNG animadas generadas e indica si la animación es de un solo fotograma o de múltiples fotogramas. |