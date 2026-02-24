> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/es.md)

Este nodo carga un conjunto de datos de imágenes y sus correspondientes descripciones de texto desde una carpeta especificada. Busca archivos de imagen y automáticamente busca archivos `.txt` coincidentes con el mismo nombre base para usarlos como descripciones. El nodo también admite una estructura de carpetas específica donde las subcarpetas pueden nombrarse con un prefijo numérico (como `10_nombre_carpeta`) para indicar que las imágenes en su interior deben repetirse múltiples veces en la salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `folder` | COMBO | Sí | *Cargado dinámicamente desde `folder_paths.get_input_subfolders()`* | La carpeta desde la cual cargar las imágenes. Las opciones disponibles son los subdirectorios dentro del directorio de entrada de ComfyUI. |

**Nota:** El nodo espera una estructura de archivos específica. Para cada archivo de imagen (`.png`, `.jpg`, `.jpeg`, `.webp`), buscará un archivo `.txt` con el mismo nombre para usarlo como descripción. Si no se encuentra un archivo de descripción, se utiliza una cadena vacía. El nodo también admite una estructura especial donde el nombre de una subcarpeta comienza con un número y un guion bajo (por ejemplo, `5_gatos`), lo que hará que todas las imágenes dentro de esa subcarpeta se repitan ese número de veces en la lista de salida final.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | Una lista de tensores de imagen cargados. |
| `texts` | STRING | Una lista de descripciones de texto correspondientes a cada imagen cargada. |
