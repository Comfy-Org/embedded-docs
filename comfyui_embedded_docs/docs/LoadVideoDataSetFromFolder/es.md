# Cargar Video (desde Carpeta)

Carga un conjunto de datos de videos desde una carpeta seleccionada dentro del directorio de entrada de ComfyUI y los devuelve como una lista de referencias de video diferidas. Este nodo carga un conjunto de datos de videos: los fotogramas se decodifican solo cuando otro nodo realmente los necesita. Los formatos admitidos son MP4, AVI, MOV, WEBM, MKV y FLV.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `folder` | La carpeta que contiene los archivos de video. | COMBO | Sí | Todas las subcarpetas disponibles en el directorio de entrada de ComfyUI (se completa dinámicamente) |

**Nota:** La carpeta seleccionada debe ser una subcarpeta del directorio de entrada de ComfyUI y debe contener al menos un archivo de video compatible. Las extensiones admitidas son MP4, AVI, MOV, WEBM, MKV y FLV. Si no se encuentran archivos de video compatibles, o si la ruta de la carpeta se resuelve fuera del directorio de entrada, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `videos` | Una lista de referencias de video diferidas, una por cada archivo de video compatible en la carpeta seleccionada, ordenadas alfabéticamente por nombre de archivo. Los fotogramas de video se decodifican solo cuando otro nodo consume la salida. | VIDEO (lista) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
