# Guardar conjunto de imágenes en carpeta

Este nodo guarda una lista de imágenes en una carpeta especificada dentro del directorio de salida de ComfyUI. Escribe cada imagen en el disco como un archivo PNG utilizando un prefijo de nombre de archivo configurable. Este nodo está obsoleto y ha sido reemplazado por los nodos Save Image existentes, donde la carpeta de destino se puede especificar en el prefijo del nombre de archivo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `images` | Lista de imágenes a guardar. | IMAGE | Sí | N/A |
| `folder_name` | Nombre de la carpeta en la que se guardarán las imágenes (dentro del directorio de salida). Por defecto: "dataset". | STRING | No | N/A |
| `filename_prefix` | Prefijo para los nombres de archivo de las imágenes guardadas. Por defecto: "image". Parámetro avanzado. | STRING | No | N/A |
| `modo` | Indica si se sobrescriben los archivos existentes o se incrementan los nombres de archivo para evitar sobrescrituras. Por defecto: "overwrite". | COMBO | No | "overwrite"<br>"increment" |

**Notas:**

- La entrada `images` es una lista, por lo que se pueden guardar varias imágenes en una sola ejecución.
- Los parámetros `folder_name`, `filename_prefix` y `mode` son valores escalares; si se conecta una lista, solo se utiliza el primer valor de esa lista.
- `folder_name` debe resolverse a una ubicación dentro del directorio de salida de ComfyUI. Los valores que escapan del directorio de salida (por ejemplo, rutas que contengan `..` o rutas absolutas) se rechazan con un error.
- En el modo "overwrite", los archivos se guardan como `{prefix}_00000.png`, `{prefix}_00001.png`, etc., reemplazando cualquier archivo existente. En el modo "increment", se inserta un contador en el nombre del archivo para que no se sobrescriban los archivos existentes.

## Salidas

Este nodo no tiene salidas. Es un nodo de salida que realiza una operación de guardado en el sistema de archivos.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/es.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
