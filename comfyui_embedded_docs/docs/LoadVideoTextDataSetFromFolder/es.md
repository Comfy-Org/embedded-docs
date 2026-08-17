# Cargar Video-Texto (desde Carpeta)

Este nodo carga un conjunto de datos de pares video-texto desde una subcarpeta seleccionada en el directorio de entrada de ComfyUI y los devuelve como dos listas: videos y descripciones de texto. Las entradas de video son referencias diferidas (lazy), por lo que los fotogramas se decodifican solo cuando un nodo posterior los necesita. Los formatos admitidos son MP4, AVI, MOV, WEBM, MKV y FLV. Las descripciones se leen de archivos `.txt` que comparten el mismo nombre que cada archivo de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `folder` | La carpeta que contiene los archivos de video y las descripciones `.txt`. | COMBO | Sí | Todas las subcarpetas dentro del directorio de entrada de ComfyUI (lista dinámica) |

Notas:
- La carpeta seleccionada debe ser una subcarpeta del directorio de entrada de ComfyUI; las rutas que se resuelvan fuera de él son rechazadas.
- Si la carpeta no contiene ningún archivo con una extensión de video admitida, el nodo genera un error.
- Las subcarpetas cuyo nombre comienza con un número seguido de un guion bajo (por ejemplo `5_classname/`, como se usa en herramientas como kohya-ss/sd-scripts) también son compatibles: cada video dentro de esa carpeta se incluye en el conjunto de datos el número de veces indicado por ese prefijo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `videos` | Referencias de video diferidas; los fotogramas se decodifican solo cuando se necesitan más adelante. Una entrada por cada archivo de video encontrado en la carpeta. | VIDEO (lista) |
| `texts` | Lista de descripciones de texto. Una descripción por video; si un video no tiene un archivo `.txt` correspondiente, su descripción es una cadena vacía. | STRING (lista) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
