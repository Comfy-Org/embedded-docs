# Cargar conjunto de imágenes y texto desde carpeta

Este nodo carga un conjunto de datos de imágenes y sus correspondientes leyendas de texto desde una carpeta especificada. Busca archivos de imagen y automáticamente localiza archivos `.txt` coincidentes con el mismo nombre base para usarlos como leyendas. El nodo también admite una estructura de carpetas específica donde las subcarpetas pueden nombrarse con un prefijo numérico (como `10_nombre_carpeta`) para indicar que las imágenes dentro deben repetirse varias veces en la salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `folder` | La carpeta desde la cual cargar las imágenes. Las opciones disponibles son los subdirectorios dentro del directorio de entrada de ComfyUI. | COMBO | Sí | *Cargado dinámicamente desde `folder_paths.get_input_subfolders()`* |

**Nota:** El nodo espera una estructura de archivos específica. Para cada archivo de imagen (`.png`, `.jpg`, `.jpeg`, `.webp`), buscará un archivo `.txt` con el mismo nombre para usarlo como leyenda. Si no se encuentra un archivo de leyenda, se utiliza una cadena vacía. El nodo también admite una estructura especial donde el nombre de una subcarpeta comienza con un número y un guion bajo (por ejemplo, `5_gatos`), lo que hará que todas las imágenes dentro de esa subcarpeta se repitan esa cantidad de veces en la lista de salida final.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `images` | Una lista de tensores de imágenes cargadas. | IMAGE |
| `texts` | Una lista de leyendas de texto correspondientes a cada imagen cargada. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `e176f35118f08ea397c63f5b6f347d9cdb3dc1a08db7ad7a5cc8255e1526e6ca`
