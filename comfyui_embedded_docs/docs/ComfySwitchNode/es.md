# Interruptor

El nodo Switch selecciona entre dos entradas posibles según una condición booleana. Genera la entrada `on_true` cuando el `switch` está habilitado y la entrada `on_false` cuando el `switch` está deshabilitado. Solo se evalúa la rama seleccionada, por lo que la otra entrada no es necesaria. Esto permite crear lógica condicional y elegir diferentes rutas de datos en su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `interruptor` | Una condición booleana que determina qué entrada se debe pasar. Cuando está habilitado (true), se selecciona la entrada `on_true`. Cuando está deshabilitado (false), se selecciona la entrada `on_false`. | BOOLEAN | Sí |  |
| `en_falso` | Los datos que se pasarán a la salida cuando el `switch` esté deshabilitado (false). Esta entrada solo es necesaria cuando el `switch` es false. | MATCH_TYPE | No |  |
| `en_verdadero` | Los datos que se pasarán a la salida cuando el `switch` esté habilitado (true). Esta entrada solo es necesaria cuando el `switch` es true. | MATCH_TYPE | No |  |

**Nota sobre los requisitos de entrada:** Las entradas `on_false` y `on_true` son requeridas condicionalmente. El nodo solicitará la entrada `on_true` solo cuando el `switch` sea true, y la entrada `on_false` solo cuando el `switch` sea false. Ambas entradas deben ser del mismo tipo de datos y deben coincidir con el tipo de datos de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `salida` | Los datos seleccionados. Será el valor de la entrada `on_true` si el `switch` es true, o el valor de la entrada `on_false` si el `switch` es false. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
