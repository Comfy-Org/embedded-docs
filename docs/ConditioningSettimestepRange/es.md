Este nodo está diseñado para ajustar el aspecto temporal del condicionamiento al establecer un rango específico de tiempos. Permite un control preciso sobre los puntos de inicio y fin del proceso de condicionamiento, habilitando una generación más dirigida y eficiente.

## Tipos de entrada de ConditioningSetTimestepRange

| Parámetro | Tipo Comfy | Descripción |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | La entrada de condicionamiento representa el estado actual del proceso de generación, que este nodo modifica al establecer un rango específico de tiempos. |
| `start` | `FLOAT` | El parámetro de inicio especifica el comienzo del rango de tiempos como un porcentaje del proceso total de generación, permitiendo un control fino sobre cuándo comienzan los efectos de condicionamiento. |
| `end` | `FLOAT` | El parámetro de fin define el punto final del rango de tiempos como un porcentaje, habilitando un control preciso sobre la duración y conclusión de los efectos de condicionamiento. |

## Tipos de salida de ConditioningSetTimestepRange

| Parámetro | Tipo Comfy | Descripción |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | La salida es el condicionamiento modificado con el rango de tiempos especificado aplicado, listo para un procesamiento o generación adicional. 
