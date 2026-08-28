# Cargar Video-Texto (desde Carpeta)

Este nodo carga archivos de video y sus leyendas de texto asociadas desde una subcarpeta seleccionada en el directorio de entrada de ComfyUI, y los devuelve como dos listas: videos y leyendas. Las entradas de video son referencias diferidas, por lo que los fotogramas se decodifican solo cuando un nodo posterior los necesita. Los formatos admitidos son MP4, AVI, MOV, WEBM, MKV y FLV. También se admiten subcarpetas anidadas con un prefijo de recuento de repeticiones (por ejemplo `5_classname/`, como usan herramientas como kohya-ss/sd-scripts).

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `folder` | La carpeta que contiene los archivos de video y las leyendas .txt. | COMBO | Sí | Múltiples opciones disponibles: lista dinámicamente todas las subcarpetas dentro del directorio de entrada de ComfyUI |

La carpeta seleccionada debe ser una subcarpeta del directorio de entrada de ComfyUI; un nombre de carpeta que se resuelva fuera de ese directorio genera un error. Si la carpeta seleccionada no contiene archivos con una extensión de video admitida (MP4, AVI, MOV, WEBM, MKV, FLV), el nodo genera un error. Para subcarpetas anidadas cuyo nombre comienza con un número seguido de un guion bajo (por ejemplo `5_classname`), cada video dentro de esa carpeta se incluye en el conjunto de datos tantas veces como indique ese prefijo. La leyenda de cada video se lee de un archivo `.txt` con el mismo nombre base; si no existe un archivo `.txt` correspondiente, la leyenda es una cadena vacía.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `videos` | Referencias diferidas de video; los fotogramas se decodifican solo cuando se necesitan más adelante. Una entrada por cada archivo de video encontrado en la carpeta. | VIDEO (lista) |
| `texts` | Lista de leyendas de texto. Una leyenda por video; si un video no tiene un archivo `.txt` correspondiente, su leyenda es una cadena vacía. | STRING (lista) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
