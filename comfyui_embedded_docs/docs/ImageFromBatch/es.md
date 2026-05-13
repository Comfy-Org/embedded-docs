> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/es.md)

El nodo `ImageFromBatch` está diseñado para extraer un segmento específico de imágenes de un lote, basándose en el índice y la longitud proporcionados. Permite un control más detallado sobre las imágenes agrupadas, facilitando operaciones en imágenes individuales o subconjuntos dentro de un lote más grande.

## Entradas

| Campo           | Tipo de Dato | Descripción                                                                           |
|-----------------|--------------|---------------------------------------------------------------------------------------|
| `imagen`         | `IMAGE`      | El lote de imágenes del cual se extraerá un segmento. Este parámetro es crucial para especificar el lote de origen. |
| `indice_lote`   | `INT`        | El índice inicial dentro del lote desde el cual comienza la extracción. Determina la posición inicial del segmento a extraer del lote. |
| `longitud`        | `INT`        | La cantidad de imágenes a extraer del lote a partir de `indice_lote`. Este parámetro define el tamaño del segmento a extraer. |

## Salidas

| Campo  | Tipo de Dato | Descripción                                                                                   |
|--------|--------------|-----------------------------------------------------------------------------------------------|
| `imagen`| `IMAGE`      | El segmento extraído de imágenes del lote especificado. Esta salida representa un subconjunto del lote original, determinado por los parámetros `indice_lote` y `longitud`. |