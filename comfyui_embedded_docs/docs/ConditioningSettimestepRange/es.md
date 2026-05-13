> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/es.md)

Este nodo está diseñado para ajustar el aspecto temporal del condicionamiento estableciendo un rango específico de pasos de tiempo. Permite un control preciso sobre los puntos de inicio y finalización del proceso de condicionamiento, posibilitando una generación más dirigida y eficiente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | La entrada de condicionamiento representa el estado actual del proceso de generación, que este nodo modifica al establecer un rango específico de pasos de tiempo. |
| `inicio` | `FLOAT` | El parámetro de inicio especifica el comienzo del rango de pasos de tiempo como un porcentaje del proceso total de generación, permitiendo un control preciso sobre cuándo comienzan los efectos del condicionamiento. |
| `fin` | `FLOAT` | El parámetro de finalización define el punto final del rango de pasos de tiempo como un porcentaje, habilitando un control preciso sobre la duración y la conclusión de los efectos del condicionamiento. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | La salida es el condicionamiento modificado con el rango de pasos de tiempo especificado aplicado, listo para su posterior procesamiento o generación. |