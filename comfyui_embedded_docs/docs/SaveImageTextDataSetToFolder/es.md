> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/es.md)

El nodo Guardar Conjunto de Datos de Imagen y Texto en Carpeta guarda una lista de imágenes y sus textos descriptivos correspondientes en una carpeta específica dentro del directorio de salida de ComfyUI. Por cada imagen guardada como archivo PNG, se crea un archivo de texto con el mismo nombre base para almacenar su descripción. Esto es útil para crear conjuntos de datos organizados de imágenes generadas y sus descripciones.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | Lista de imágenes a guardar. |
| `texts` | STRING | Sí | - | Lista de textos descriptivos a guardar. |
| `folder_name` | STRING | No | - | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). (por defecto: "dataset") |
| `filename_prefix` | STRING | No | - | Prefijo para los nombres de archivo de las imágenes guardadas. (por defecto: "image") |

**Nota:** Las entradas `images` y `texts` son listas. El nodo espera que el número de textos descriptivos coincida con el número de imágenes proporcionadas. Cada descripción se guardará en un archivo `.txt` correspondiente a su imagen emparejada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| - | - | Este nodo no tiene salidas. Guarda los archivos directamente en el sistema de archivos. |
