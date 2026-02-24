> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/es.md)

Este nodo carga múltiples imágenes desde una subcarpeta específica dentro del directorio de entrada de ComfyUI. Escanea la carpeta seleccionada en busca de tipos de archivo de imagen comunes y los devuelve como una lista, lo que resulta útil para procesamiento por lotes o preparación de conjuntos de datos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sí | *Múltiples opciones disponibles* | La carpeta desde la cual cargar las imágenes. Las opciones son las subcarpetas presentes en el directorio de entrada principal de ComfyUI. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | Lista de imágenes cargadas. El nodo carga todos los archivos de imagen válidos (PNG, JPG, JPEG, WEBP) encontrados en la carpeta seleccionada. |
