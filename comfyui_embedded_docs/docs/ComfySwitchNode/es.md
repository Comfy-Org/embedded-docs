> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/es.md)

El nodo Switch selecciona entre dos posibles entradas según una condición booleana. Genera la entrada `on_true` cuando el `switch` está activado, y la entrada `on_false` cuando el `switch` está desactivado. Esto permite crear lógica condicional y elegir diferentes rutas de datos en tu flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `interruptor` | BOOLEAN | Sí | | Una condición booleana que determina qué entrada se debe pasar. Cuando está activado (verdadero), se selecciona la entrada `en_verdadero`. Cuando está desactivado (falso), se selecciona la entrada `en_falso`. |
| `en_falso` | MATCH_TYPE | No | | Los datos que se pasarán a la salida cuando el `interruptor` esté desactivado (falso). Esta entrada solo es obligatoria cuando el `interruptor` es falso. |
| `en_verdadero` | MATCH_TYPE | No | | Los datos que se pasarán a la salida cuando el `interruptor` esté activado (verdadero). Esta entrada solo es obligatoria cuando el `interruptor` es verdadero. |

**Nota sobre los requisitos de entrada:** Las entradas `on_false` y `on_true` son condicionalmente obligatorias. El nodo solicitará la entrada `on_true` solo cuando el `switch` sea verdadero, y la entrada `on_false` solo cuando el `switch` sea falso. Ambas entradas deben ser del mismo tipo de dato.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | MATCH_TYPE | Los datos seleccionados. Será el valor de la entrada `en_verdadero` si el `interruptor` es verdadero, o el valor de la entrada `en_falso` si el `interruptor` es falso. |

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
