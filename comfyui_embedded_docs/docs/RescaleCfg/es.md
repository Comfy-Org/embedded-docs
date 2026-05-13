> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/es.md)

El nodo RescaleCFG está diseñado para ajustar las escalas de condicionamiento y no condicionamiento de la salida de un modelo en función de un multiplicador especificado, con el objetivo de lograr un proceso de generación más equilibrado y controlado. Funciona reescalando la salida del modelo para modificar la influencia de los componentes condicionados y no condicionados, mejorando potencialmente el rendimiento o la calidad de la salida del modelo.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `modelo`   | MODEL     | El parámetro `modelo` representa el modelo generativo que se va a ajustar. Es crucial, ya que el nodo aplica una función de reescalado a la salida del modelo, influyendo directamente en el proceso de generación. |
| `multiplicador` | `FLOAT` | El parámetro `multiplicador` controla el grado de reescalado aplicado a la salida del modelo. Determina el equilibrio entre los componentes originales y reescalados, afectando las características finales de la salida. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `modelo`   | MODEL     | El modelo modificado con escalas de condicionamiento y no condicionamiento ajustadas. Se espera que este modelo produzca salidas con características potencialmente mejoradas debido al reescalado aplicado. |