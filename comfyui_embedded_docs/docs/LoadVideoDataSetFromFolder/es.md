# Cargar Video (desde Carpeta)

Carga todos los archivos de video compatibles desde una carpeta seleccionada dentro del directorio de entrada de ComfyUI y los devuelve como una lista de referencias de video. Este nodo devuelve referencias de video diferidas, por lo que los fotogramas se decodifican solo cuando otro nodo realmente los necesita. Formatos compatibles: MP4, AVI, MOV, WEBM, MKV y FLV.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `folder` | La carpeta que contiene los archivos de video. Seleccione entre las subcarpetas disponibles dentro del directorio de entrada de ComfyUI. | COMBO | Sí | Todas las subcarpetas disponibles en el directorio de entrada de ComfyUI |

**Nota:** La carpeta seleccionada debe contener al menos un archivo de video compatible. Las extensiones admitidas son MP4, AVI, MOV, WEBM, MKV y FLV. Si no se encuentran archivos de video compatibles, el nodo genera un error. La carpeta debe resolverse a una ubicación dentro del directorio de entrada de ComfyUI; los nombres de carpeta que intenten escapar de él (por ejemplo, con "..") se rechazan con un error.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `videos` | Una lista de referencias de video diferidas, una para cada archivo de video en la carpeta seleccionada. Los fotogramas se decodifican solo cuando la salida es consumida por otro nodo. | VIDEO (lista) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
