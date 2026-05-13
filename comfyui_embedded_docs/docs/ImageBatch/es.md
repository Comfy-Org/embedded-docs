> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/es.md)

El nodo `ImageBatch` está diseñado para combinar dos imágenes en un solo lote. Si las dimensiones de las imágenes no coinciden, reescala automáticamente la segunda imagen para que coincida con las dimensiones de la primera antes de combinarlas.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image1`  | `IMAGE`     | La primera imagen que se combinará en el lote. Sirve como referencia para las dimensiones a las que se ajustará la segunda imagen si es necesario. |
| `image2`  | `IMAGE`     | La segunda imagen que se combinará en el lote. Se reescala automáticamente para que coincida con las dimensiones de la primera imagen si son diferentes. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El lote combinado de imágenes, con la segunda imagen reescalada para que coincida con las dimensiones de la primera si es necesario. |