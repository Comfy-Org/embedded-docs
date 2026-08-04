# Cargar Video-Texto (desde Carpeta)

Este nodo carga archivos de video y sus leyendas de texto asociadas desde una subcarpeta seleccionada en el directorio de entrada de ComfyUI y los devuelve como dos listas: videos y leyendas. Las entradas de video son referencias perezosas, por lo que los fotogramas solo se decodifican cuando un nodo posterior los necesita. Los formatos compatibles son MP4, AVI, MOV, WEBM, MKV y FLV. También se admiten carpetas anidadas con prefijo de recuento de repeticiones (por ejemplo, `5_classname/`, como usan herramientas como kohya-ss/sd-scripts).

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `folder` | La carpeta que contiene archivos de video y leyendas .txt. | STRING | Sí | Combo: lista dinámica de todas las subcarpetas dentro del directorio de entrada de ComfyUI |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
Si la carpeta seleccionada no contiene archivos con una extensión de video compatible, el nodo genera un error. Para carpetas anidadas cuyo nombre comienza con un número seguido de un guion bajo (por ejemplo, `5_classname`), cada video dentro de esa carpeta se incluye en el conjunto de datos tantas veces como indique ese prefijo.
|------------------|-------------|---------------|
| `videos` | Referencias de video perezosas; los fotogramas solo se decodifican cuando se necesitan posteriormente. Una entrada por cada archivo de video encontrado en la carpeta. | VIDEO (list) |
| `texts` | Lista de leyendas de texto. Una leyenda por video; si un video no tiene un archivo `.txt` correspondiente, su leyenda es una cadena vacía. | STRING (list) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
