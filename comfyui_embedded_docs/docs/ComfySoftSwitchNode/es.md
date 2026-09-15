# ComfySoftSwitchNode

El nodo Soft Switch selecciona entre dos posibles valores de entrada según una condición booleana. Devuelve el valor de la entrada `on_true` cuando `switch` es verdadero, y el valor de la entrada `on_false` cuando `switch` es falso. Este nodo está diseñado para ser perezoso (lazy), lo que significa que solo evalúa la entrada que realmente se necesita según el estado de `switch`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `switch` | La condición booleana que determina qué entrada se deja pasar. Cuando es verdadera, se selecciona la entrada `on_true`. Cuando es falsa, se selecciona la entrada `on_false`. | BOOLEAN | Sí | True or False |
| `on_false` | El valor que se debe devolver cuando la condición `switch` es falsa. Esta entrada es opcional, pero al menos una de `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No | Mismo tipo de datos que `on_true` |
| `on_true` | El valor que se debe devolver cuando la condición `switch` es verdadera. Esta entrada es opcional, pero al menos una de `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No | Mismo tipo de datos que `on_false` |

**Nota:** Las entradas `on_false` y `on_true` deben ser del mismo tipo de datos, tal como lo define la plantilla interna del nodo. Al menos una de estas dos entradas debe estar conectada; de lo contrario, el nodo devuelve el mensaje de validación "At least one of on_false or on_true must be connected to Switch node". Debido a que el nodo es perezoso (lazy), cuando solo se conecta una entrada, el nodo siempre devuelve el valor de esa entrada independientemente del estado de `switch`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El valor seleccionado. Coincide con el tipo de datos de la entrada conectada `on_false` o `on_true`. Cuando ambas entradas están conectadas, devuelve `on_true` si `switch` es verdadero, y `on_false` si `switch` es falso. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
