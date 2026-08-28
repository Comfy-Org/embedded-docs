# Guardar conjunto de imágenes y textos en carpeta

Save Image-Text (to Folder) guarda una lista de imágenes y sus descripciones de texto correspondientes en una carpeta específica dentro del directorio de salida de ComfyUI. Por cada imagen guardada como archivo PNG, se crea un archivo TXT con el mismo nombre base para almacenar su descripción, lo que resulta útil para crear conjuntos de datos organizados de imágenes generadas junto con sus descripciones.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Lista de imágenes a guardar. | IMAGE | Sí | - |
| `texts` | Lista de descripciones de texto a guardar. Esta entrada es opcional. | STRING | No | - |
| `folder_name` | Nombre de la carpeta donde se guardarán las imágenes (dentro del directorio de salida). (predeterminado: "dataset") | STRING | Sí | - |
| `filename_prefix` | Prefijo para los nombres de archivo de las imágenes guardadas. (predeterminado: "image") | STRING | Sí | - |
| `modo` | Indica si se sobrescriben los archivos existentes o si se incrementan los nombres de archivo para evitar sobrescribirlos. (predeterminado: "overwrite") | COMBO | Sí | "overwrite"<br>"increment" |

**Nota:** La entrada `images` es una lista. La entrada `texts` es opcional; si se proporciona, debe ser una lista de descripciones de texto y debe contener el mismo número de elementos que `images`. Cada descripción se guarda como un archivo `.txt` correspondiente a su imagen emparejada. En el modo `overwrite`, los archivos se nombran `{filename_prefix}_{index}.png` y reemplazan cualquier archivo existente con el mismo nombre. En el modo `increment`, se añade un contador único a los nombres de archivo para que los archivos existentes no se sobrescriban. El `folder_name` debe resolverse a una ruta dentro del directorio de salida; los nombres de carpeta que intenten escapar de él (por ejemplo, con `..`) se rechazan.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| - | Este nodo no devuelve datos. Guarda los archivos directamente en el sistema de archivos. | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/es.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
