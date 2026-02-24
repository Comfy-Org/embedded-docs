> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/es.md)

El nodo Switch selecciona entre dos entradas posibles basándose en una condición booleana. Emite la entrada `on_true` cuando el `switch` está habilitado, y la entrada `on_false` cuando el `switch` está deshabilitado. Esto permite crear lógica condicional y elegir diferentes rutas de datos en tu flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Sí | | Una condición booleana que determina qué entrada pasar a la salida. Cuando está habilitado (true), se selecciona la entrada `on_true`. Cuando está deshabilitado (false), se selecciona la entrada `on_false`. |
| `on_false` | MATCH_TYPE | No | | Los datos que se pasarán a la salida cuando el `switch` esté deshabilitado (false). Esta entrada solo es necesaria cuando el `switch` es false. |
| `on_true` | MATCH_TYPE | No | | Los datos que se pasarán a la salida cuando el `switch` esté habilitado (true). Esta entrada solo es necesaria cuando el `switch` es true. |

**Nota sobre los requisitos de entrada:** Las entradas `on_false` y `on_true` son condicionalmente obligatorias. El nodo solicitará la entrada `on_true` solo cuando el `switch` sea true, y la entrada `on_false` solo cuando el `switch` sea false. Ambas entradas deben ser del mismo tipo de dato.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | Los datos seleccionados. Será el valor de la entrada `on_true` si el `switch` es true, o el valor de la entrada `on_false` si el `switch` es false. |
