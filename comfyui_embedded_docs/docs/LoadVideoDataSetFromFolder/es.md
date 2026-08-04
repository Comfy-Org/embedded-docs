# Cargar Video (desde Carpeta)

Carga todos los archivos de video compatibles desde una carpeta seleccionada dentro del directorio de entrada de ComfyUI y los devuelve como una lista de referencias de video. Este nodo devuelve referencias perezosas de video, por lo que los fotogramas se decodifican solo cuando otro nodo realmente los necesita.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `folder` | La carpeta que contiene los archivos de video. Seleccione entre las subcarpetas disponibles dentro del directorio de entrada de ComfyUI. | STRING | Sí | Todas las subcarpetas disponibles en el directorio de entrada de ComfyUI |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
**Nota:** La carpeta seleccionada debe contener al menos un archivo de video compatible. Las extensiones compatibles son MP4, AVI, MOV, WEBM, MKV y FLV. Si no se encuentran archivos de video compatibles, el nodo genera un error.
|------------------|-------------|---------------|
| `videos` | Una lista de referencias de video perezosas, una por cada archivo de video en la carpeta seleccionada. Los fotogramas de video se decodifican solo cuando la salida es consumida por otro nodo. | VIDEO (list) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
