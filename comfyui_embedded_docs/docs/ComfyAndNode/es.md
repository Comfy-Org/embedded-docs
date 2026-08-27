# Y

El nodo And realiza una operación lógica AND sobre un conjunto de valores de entrada. Devuelve `true` solo si todos los valores proporcionados se consideran verdaderos según las reglas de veracidad de Python. Este nodo es útil para comprobar que se cumplen varias condiciones antes de continuar.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `valores` | Un valor a evaluar. El nodo acepta al menos un valor, y puedes añadir más haciendo clic en el botón "+" del nodo. Acepta cualquier tipo de dato. | ANY | Sí | 1 o más (sin máximo) |

**Nota:** El nodo utiliza las reglas de veracidad de Python para determinar si un valor es `true` o `false`. Por ejemplo, una cadena vacía, el número 0, una lista vacía y `None` se consideran `false`. Todos los demás valores se consideran `true`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `BOOLEAN` | Devuelve `true` si todos los valores de entrada son verdaderos; de lo contrario, devuelve `false`. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/es.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
