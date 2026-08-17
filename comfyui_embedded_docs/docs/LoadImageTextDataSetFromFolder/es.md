# Cargar conjunto de imágenes y texto desde carpeta

Este nodo carga un conjunto de datos de pares de imágenes y descripciones de texto desde una carpeta especificada y los devuelve como una lista. Formatos admitidos: PNG, JPG, JPEG, WEBP. Para cada archivo de imagen, el nodo busca automáticamente un archivo `.txt` con el mismo nombre base para usarlo como su descripción. El nodo también admite una estructura de carpetas donde los nombres de las subcarpetas comienzan con un prefijo numérico (como `10_folder_name`), lo que hace que las imágenes dentro de esa subcarpeta se repitan esa cantidad de veces en la salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `folder` | La carpeta desde la que se cargan las imágenes y las descripciones de texto. Las opciones disponibles son los subdirectorios dentro del directorio de entrada de ComfyUI. | COMBO | Sí | *Cargado dinámicamente desde `folder_paths.get_input_subfolders()`* |

**Nota:** El nodo espera una estructura de archivos específica. Para cada archivo de imagen (`.png`, `.jpg`, `.jpeg`, `.webp`), buscará un archivo `.txt` con el mismo nombre para usarlo como descripción. Si no se encuentra un archivo de descripción, se utiliza una cadena vacía. El nodo también admite una estructura especial donde el nombre de una subcarpeta comienza con un número y un guion bajo (p. ej., `5_cats`), lo que hará que todas las imágenes dentro de esa subcarpeta se repitan esa cantidad de veces en la lista final de salida. La carpeta seleccionada debe estar dentro del directorio de entrada de ComfyUI; los nombres de carpeta que se resuelvan fuera de él son rechazados.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `images` | Una lista de tensores de imagen cargados. | IMAGE |
| `texts` | Una lista de descripciones de texto correspondientes a cada imagen cargada. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
