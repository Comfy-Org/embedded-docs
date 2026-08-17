# Guardar conjunto de imágenes y textos en carpeta

Save Image-Text (to Folder) es un nodo de salida que guarda un conjunto de datos de imágenes emparejadas con descripciones de texto en una carpeta dentro del directorio de salida de ComfyUI. Cada imagen se guarda como un archivo PNG y, cuando se proporcionan descripciones, se crea un archivo TXT con el mismo nombre base para cada imagen. Esto es útil para crear conjuntos de datos organizados de imágenes generadas y sus descripciones.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | Lista de imágenes a guardar. | IMAGE | Sí | - |
| `texts` | Lista de descripciones de texto a guardar. Esta entrada es opcional. | STRING | No | - |
| `folder_name` | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). (por defecto: "dataset") | STRING | Sí | - |
| `filename_prefix` | Prefijo para los nombres de archivo de las imágenes guardadas. (por defecto: "image") | STRING | Sí | - |
| `mode` | Si se sobrescriben los archivos existentes o se incrementan los nombres de archivo para evitar sobrescribir. (por defecto: "overwrite") | COMBO | Sí | "overwrite"<br>"increment" |

**Nota:** La entrada `images` es una lista. La entrada `texts` es opcional; si se proporciona, debe ser una lista de descripciones de texto. Las descripciones se emparejan con las imágenes en orden, y cada descripción se guarda como un archivo `.txt` en UTF-8 con el mismo nombre base que la imagen emparejada (por ejemplo, `image_00000.txt` para `image_00000.png`). Si hay menos descripciones que imágenes, las imágenes restantes se guardan sin descripciones; cualquier descripción adicional se ignora.

Las entradas con valores por defecto (`folder_name`, `filename_prefix`, `mode`) no necesitan estar conectadas; sus valores por defecto se utilizan automáticamente.

Cuando `mode` está establecido en `overwrite` (el valor por defecto), las imágenes se guardan con nombres como `image_00000.png`, reemplazando cualquier archivo existente con el mismo nombre. Cuando `mode` está establecido en `increment`, se añade un contador que aumenta automáticamente a los nombres de archivo para que los archivos existentes no se sobrescriban.

El valor de `folder_name` debe resolverse a una ubicación dentro del directorio de salida de ComfyUI. Los nombres de carpeta que intenten salir del directorio de salida (por ejemplo, usando `..`) se rechazan.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| - | Este nodo no tiene salidas. Guarda archivos directamente en el sistema de archivos. | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/es.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
