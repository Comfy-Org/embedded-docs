# ComfySoftSwitchNode

El nodo Soft Switch selecciona entre dos posibles valores de entrada basándose en una condición booleana. Genera el valor de la entrada `on_true` cuando el `switch` es verdadero, y el valor de la entrada `on_false` cuando el `switch` es falso. Este nodo está diseñado con evaluación perezosa, lo que significa que solo evalúa la entrada que se necesita según el estado del `switch`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `switch` | La condición booleana que determina qué entrada se debe pasar. Cuando es verdadero, se selecciona la entrada `on_true`. Cuando es falso, se selecciona la entrada `on_false`. | BOOLEAN | Sí | true<br>false |
| `on_false` | El valor a emitir cuando la condición `switch` es falsa. Esta entrada es opcional, pero al menos una de `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No |  |
| `on_true` | El valor a emitir cuando la condición `switch` es verdadera. Esta entrada es opcional, pero al menos una de `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No |  |

**Nota:** Las entradas `on_false` y `on_true` deben ser del mismo tipo de datos, según lo definido por la plantilla interna del nodo. Al menos una de estas dos entradas debe estar conectada para que el nodo funcione. Si solo está conectada una entrada, ese valor se pasa a la salida independientemente del estado del `switch`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El valor seleccionado. Coincidirá con el tipo de datos de la entrada `on_false` o `on_true` conectada. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
