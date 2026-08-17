# Guardar conjunto de imágenes en carpeta

Este nodo guarda una lista de imágenes como archivos PNG en una carpeta especificada dentro del directorio de salida de ComfyUI. Está obsoleto: es redundante y ha sido reemplazado por los nodos Save Image existentes, donde la carpeta de destino se puede especificar en el prefijo del nombre de archivo. El nodo escribe cada imagen recibida en el disco utilizando un prefijo de nombre de archivo personalizable, y puede sobrescribir archivos existentes o generar nombres de archivo incrementados para evitar sobrescribir.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | Lista de imágenes para guardar. | IMAGE | Sí | N/A |
| `folder_name` | Nombre de la carpeta donde guardar las imágenes (dentro del directorio de salida). El valor predeterminado es "dataset". | STRING | No | N/A |
| `filename_prefix` | Prefijo para los nombres de archivo de imagen guardados. El valor predeterminado es "image". | STRING | No | N/A |
| `mode` | Si sobrescribir archivos existentes o incrementar los nombres de archivo para evitar sobrescribir. El valor predeterminado es "overwrite". | COMBO | No | "overwrite"<br>"increment" |

**Nota:** La entrada `images` es una lista, lo que significa que puede recibir y procesar múltiples imágenes a la vez. Todas las entradas se reciben como listas; para `folder_name`, `filename_prefix` y `mode`, solo se utiliza el primer valor de la lista conectada. El `folder_name` debe resolver a una carpeta dentro del directorio de salida de ComfyUI — los nombres de carpeta que escapen de él (por ejemplo, usando "..", una ruta absoluta o una letra de unidad) se rechazan con un error. Las imágenes siempre se guardan en formato PNG. El parámetro `filename_prefix` es una opción avanzada.

## Salidas

Este nodo no tiene salidas de datos. Es un nodo de salida que realiza una operación de guardado en el sistema de archivos.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/es.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
