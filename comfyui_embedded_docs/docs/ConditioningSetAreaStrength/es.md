> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/es.md)

Este nodo está diseñado para modificar el atributo de intensidad de un conjunto de condicionamiento dado, permitiendo ajustar la influencia o intensidad del condicionamiento en el proceso de generación.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | El conjunto de condicionamiento a modificar, que representa el estado actual del condicionamiento que influye en el proceso de generación. |
| `fuerza` | `FLOAT` | El valor de intensidad que se aplicará al conjunto de condicionamiento, determinando la intensidad de su influencia. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | El conjunto de condicionamiento modificado con valores de intensidad actualizados para cada elemento. |