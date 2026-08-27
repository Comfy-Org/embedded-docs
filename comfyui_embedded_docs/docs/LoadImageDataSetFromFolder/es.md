# Cargar conjunto de imágenes desde carpeta

Este nodo carga múltiples imágenes desde una subcarpeta seleccionada dentro del directorio principal de entrada de ComfyUI y las devuelve como una lista. Escanea la carpeta elegida en busca de archivos de imagen en formato PNG, JPG, JPEG o WEBP, lo que resulta útil para procesamiento por lotes o preparación de conjuntos de datos de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `folder` | La carpeta desde la que se cargan las imágenes. Las opciones son las subcarpetas presentes en el directorio principal de entrada de ComfyUI. | COMBO | Sí | Múltiples opciones disponibles |

Nota: La carpeta seleccionada debe ser una subcarpeta del directorio principal de entrada de ComfyUI; cualquier valor que se resuelva fuera de este directorio es rechazado. Solo se cargan los archivos con las extensiones .png, .jpg, .jpeg o .webp, y la verificación de extensión no distingue entre mayúsculas y minúsculas. Si la carpeta seleccionada no contiene archivos de imagen válidos, el nodo genera un error. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `images` | Lista de imágenes cargadas. El nodo carga todos los archivos de imagen válidos (PNG, JPG, JPEG, WEBP) que se encuentren en la carpeta seleccionada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
