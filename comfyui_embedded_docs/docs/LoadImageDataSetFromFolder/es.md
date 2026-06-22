# Cargar conjunto de imágenes desde carpeta

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/en.md)

Este nodo carga múltiples imágenes desde una subcarpeta específica dentro del directorio de entrada de ComfyUI. Escanea la carpeta seleccionada en busca de tipos de archivos de imagen comunes y los devuelve como una lista, lo que resulta útil para procesamiento por lotes o preparación de conjuntos de datos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `folder` | La carpeta desde la cual cargar imágenes. Las opciones son las subcarpetas presentes en el directorio de entrada principal de ComfyUI. | STRING | Sí | *Múltiples opciones disponibles* |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `images` | Lista de imágenes cargadas. El nodo carga todos los archivos de imagen válidos (PNG, JPG, JPEG, WEBP) encontrados en la carpeta seleccionada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `0f6e1b3d159f7d7c0c9530350ee057118a2618796f149586bae925253ecc8cf0`
