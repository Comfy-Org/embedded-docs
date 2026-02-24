> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/es.md)

El nodo Soft Switch selecciona entre dos valores de entrada posibles según una condición booleana. Emite el valor de la entrada `on_true` cuando el `switch` es verdadero, y el valor de la entrada `on_false` cuando el `switch` es falso. Este nodo está diseñado para ser perezoso (lazy), lo que significa que solo evalúa la entrada que se necesita según el estado del interruptor.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Sí | | La condición booleana que determina qué entrada pasar. Cuando es verdadera, se selecciona la entrada `on_true`. Cuando es falsa, se selecciona la entrada `on_false`. |
| `on_false` | MATCH_TYPE | No | | El valor a emitir cuando la condición `switch` es falsa. Esta entrada es opcional, pero al menos una de las entradas `on_false` o `on_true` debe estar conectada. |
| `on_true` | MATCH_TYPE | No | | El valor a emitir cuando la condición `switch` es verdadera. Esta entrada es opcional, pero al menos una de las entradas `on_false` o `on_true` debe estar conectada. |

**Nota:** Las entradas `on_false` y `on_true` deben ser del mismo tipo de dato, según lo define la plantilla interna del nodo. Al menos una de estas dos entradas debe estar conectada para que el nodo funcione.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | El valor seleccionado. Coincidirá con el tipo de dato de la entrada `on_false` o `on_true` conectada. |
