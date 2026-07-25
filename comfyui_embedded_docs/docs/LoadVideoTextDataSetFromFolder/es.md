# Cargar Video-Texto (desde Carpeta)

Este nodo carga un conjunto de datos de archivos de video y sus correspondientes leyendas de texto desde una subcarpeta especificada dentro del directorio de entrada de ComfyUI. Devuelve dos listas: referencias de video perezosas (los fotogramas se decodifican solo cuando se necesitan en nodos posteriores) y sus leyendas asociadas. El nodo admite formatos de video comunes como MP4, AVI, MOV, WEBM, MKV y FLV, y también puede manejar estructuras de carpetas anidadas con prefijos de recuento de repetición (por ejemplo, `5_classname/`) utilizados por herramientas como kohya‑ss/sd‑scripts.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `folder` | La subcarpeta que contiene archivos de video y archivos de leyendas `.txt`. Seleccione entre las subcarpetas disponibles en el directorio de entrada de ComfyUI. | STRING | Sí | Combo: lista dinámica de todos los subdirectorios dentro de la carpeta de entrada de ComfyUI |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `videos` | Referencias perezosas a los archivos de video cargados. Los fotogramas se decodifican solo cuando están conectados a un nodo posterior que los procesa. Cada elemento corresponde a un video de la carpeta de entrada. | VIDEO (list) |
| `texts` | Lista de leyendas de texto, una por video. Si un video no tiene un archivo `.txt` correspondiente, su leyenda es una cadena vacía. | STRING (list) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
