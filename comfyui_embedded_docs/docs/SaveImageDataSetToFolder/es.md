> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/es.md)

Este nodo guarda una lista de imágenes en una carpeta específica dentro del directorio de salida de ComfyUI. Toma múltiples imágenes como entrada y las escribe en el disco con un prefijo de nombre de archivo personalizable.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | N/A | Lista de imágenes a guardar. |
| `folder_name` | STRING | No | N/A | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). El valor por defecto es "dataset". |
| `filename_prefix` | STRING | No | N/A | Prefijo para los nombres de los archivos de imagen guardados. El valor por defecto es "image". |

**Nota:** La entrada `images` es una lista, lo que significa que puede recibir y procesar múltiples imágenes a la vez. Los parámetros `folder_name` y `filename_prefix` son valores escalares; si se conecta una lista, solo se usará el primer valor de esa lista.

## Salidas

Este nodo no tiene ninguna salida. Es un nodo de salida que realiza una operación de guardado en el sistema de archivos.
