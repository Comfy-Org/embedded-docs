# Cargar conjunto de imágenes desde carpeta

Este nodo carga un conjunto de imágenes desde una carpeta seleccionada y las devuelve como una lista. La carpeta debe ser una subcarpeta dentro del directorio principal de entrada de ComfyUI. Los formatos de imagen admitidos son PNG, JPG, JPEG y WEBP.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `folder` | La carpeta desde la que cargar las imágenes. Las opciones disponibles son las subcarpetas presentes en el directorio principal de entrada de ComfyUI. Se rechazan los valores que resuelvan fuera de este directorio (por ejemplo, usando ".."). | COMBO | Sí | *Varias opciones disponibles* — las subcarpetas presentes en el directorio de entrada de ComfyUI |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `images` | Lista de imágenes cargadas. El nodo carga todos los archivos de imagen válidos (PNG, JPG, JPEG, WEBP) que se encuentren en la carpeta seleccionada y los devuelve como una lista. Si la carpeta no contiene archivos de imagen admitidos, se genera un error. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
