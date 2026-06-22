# ComfySoftSwitchNode

El nodo Soft Switch selecciona entre dos posibles valores de entrada según una condición booleana. Genera el valor de la entrada `on_true` cuando el `switch` es verdadero, y el valor de la entrada `on_false` cuando el `switch` es falso. Este nodo está diseñado para ser perezoso, lo que significa que solo evalúa la entrada necesaria según el estado del interruptor.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `switch` | La condición booleana que determina qué entrada se debe pasar. Cuando es verdadera, se selecciona la entrada `on_true`. Cuando es falsa, se selecciona la entrada `on_false`. | BOOLEAN | Sí |  |
| `on_false` | El valor a generar cuando la condición del `switch` es falsa. Esta entrada es opcional, pero al menos una de las entradas `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No |  |
| `on_true` | El valor a generar cuando la condición del `switch` es verdadera. Esta entrada es opcional, pero al menos una de las entradas `on_false` o `on_true` debe estar conectada. | MATCH_TYPE | No |  |

**Nota:** Las entradas `on_false` y `on_true` deben ser del mismo tipo de dato, según lo definido por la plantilla interna del nodo. Al menos una de estas dos entradas debe estar conectada para que el nodo funcione.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El valor seleccionado. Coincidirá con el tipo de dato de la entrada `on_false` o `on_true` conectada. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `f5e40e7f43948b81b5442c885c3e1ff15e38f8f7ddda00ef3be42225765bfd1c`
