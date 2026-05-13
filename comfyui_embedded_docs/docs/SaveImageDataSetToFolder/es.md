> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/en.md)

Este nodo guarda una lista de imágenes en una carpeta específica dentro del directorio de salida de ComfyUI. Toma múltiples imágenes como entrada y las escribe en disco con un prefijo de nombre de archivo personalizable.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | N/A | Lista de imágenes a guardar. |
| `folder_name` | STRING | No | N/A | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). El valor predeterminado es "dataset". |
| `filename_prefix` | STRING | No | N/A | Prefijo para los nombres de archivo de las imágenes guardadas. El valor predeterminado es "image". |

**Nota:** La entrada `images` es una lista, lo que significa que puede recibir y procesar múltiples imágenes a la vez. Los parámetros `folder_name` y `filename_prefix` son valores escalares; si se conecta una lista, solo se utilizará el primer valor de esa lista.

## Salidas

Este nodo no tiene ninguna salida. Es un nodo de salida que realiza una operación de guardado en el sistema de archivos.

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`
