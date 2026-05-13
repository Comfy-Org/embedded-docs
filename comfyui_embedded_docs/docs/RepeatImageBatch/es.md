> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/es.md)

El nodo RepeatImageBatch está diseñado para replicar una imagen determinada un número específico de veces, creando un lote de imágenes idénticas. Esta funcionalidad es útil para operaciones que requieren múltiples instancias de la misma imagen, como el procesamiento por lotes o el aumento de datos.

## Entradas

| Campo   | Tipo de Dato | Descripción                                                                 |
|---------|--------------|-----------------------------------------------------------------------------|
| `image` | `IMAGE`      | El parámetro 'image' representa la imagen que se va a replicar. Es fundamental para definir el contenido que se duplicará en el lote. |
| `amount`| `INT`        | El parámetro 'amount' especifica el número de veces que se debe replicar la imagen de entrada. Influye directamente en el tamaño del lote de salida, permitiendo una creación flexible de lotes. |

## Salidas

| Campo | Tipo de Dato | Descripción                                                              |
|-------|--------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`      | La salida es un lote de imágenes, cada una idéntica a la imagen de entrada, replicadas según el 'amount' especificado. |