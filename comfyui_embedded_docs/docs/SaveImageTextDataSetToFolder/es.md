# Guardar conjunto de imágenes y textos en carpeta

El nodo Guardar Imagen y Texto en Carpeta guarda una lista de imágenes y sus correspondientes descripciones de texto en una carpeta especificada dentro del directorio de salida de ComfyUI. Por cada imagen guardada como archivo PNG, se crea un archivo de texto con el mismo nombre base para almacenar su descripción. Esto es útil para crear conjuntos de datos organizados de imágenes generadas y sus descripciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `images` | Lista de imágenes a guardar. | IMAGE | Sí | - |
| `texts` | Lista de descripciones de texto a guardar. | STRING | Sí | - |
| `folder_name` | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). (predeterminado: "dataset") | STRING | No | - |
| `filename_prefix` | Prefijo para los nombres de archivo de las imágenes guardadas. (predeterminado: "image") | STRING | No | - |

**Nota:** Las entradas `images` y `texts` son listas. El nodo espera que la cantidad de descripciones de texto coincida con la cantidad de imágenes proporcionadas. Cada descripción se guardará en un archivo `.txt` correspondiente a su imagen emparejada.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| - | Este nodo no tiene ninguna salida. Guarda archivos directamente en el sistema de archivos. | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/es.md)

---
**Source fingerprint (SHA-256):** `0c76f623e97b1502c850e0a59dc9edd7c241bcd823f5e32a8dcdd8b8160d2e44`
