# Interruptor

El nodo Switch selecciona entre dos entradas posibles según una condición booleana. Genera en la salida la entrada `on_true` cuando el `switch` está habilitado, y la entrada `on_false` cuando el `switch` está deshabilitado, lo que permite crear lógica condicional y elegir diferentes rutas de datos en su flujo de trabajo. Este nodo está actualmente marcado como experimental.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `switch` | Una condición booleana que determina qué entrada se debe pasar. Cuando está habilitado (true), se selecciona la entrada `on_true`. Cuando está deshabilitado (false), se selecciona la entrada `on_false`. | BOOLEAN | Sí |  |
| `on_false` | Los datos que se pasarán a la salida cuando el `switch` esté deshabilitado (false). Esta entrada solo es necesaria cuando el `switch` es false. | MATCH_TYPE | No |  |
| `on_true` | Los datos que se pasarán a la salida cuando el `switch` esté habilitado (true). Esta entrada solo es necesaria cuando el `switch` es true. | MATCH_TYPE | No |  |

**Nota sobre los requisitos de entrada:** Las entradas `on_false` y `on_true` son necesarias de forma condicional. El nodo solicitará la entrada `on_true` solo cuando el `switch` sea true, y la entrada `on_false` solo cuando el `switch` sea false. Ambas entradas deben ser del mismo tipo de datos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Los datos seleccionados. Será el valor de la entrada `on_true` si el `switch` es true, o el valor de la entrada `on_false` si el `switch` es false. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
