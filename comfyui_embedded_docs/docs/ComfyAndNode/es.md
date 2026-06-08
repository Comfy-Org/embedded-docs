# Descripción General

El nodo Y realiza una operación lógica AND sobre un conjunto de valores de entrada. Devuelve `true` solo si todos los valores proporcionados se consideran verdaderos según las reglas de veracidad de Python. Este nodo es útil para verificar que se cumplan múltiples condiciones antes de continuar.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `valores` | Una lista de valores a evaluar. El nodo acepta al menos un valor, y puedes agregar más haciendo clic en el botón "+" del nodo. | ANY | Sí | 1 o más valores |

**Nota:** El nodo utiliza las reglas de veracidad de Python para determinar si un valor es `true` o `false`. Por ejemplo, una cadena vacía, el número 0, una lista vacía y `None` se consideran `false`. Todos los demás valores se consideran `true`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `BOOLEAN` | Devuelve `true` si todos los valores de entrada son verdaderos, de lo contrario devuelve `false`. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/es.md)

---
**Source fingerprint (SHA-256):** `fd9d18ce698472a7e35ad3082f2ccff8ae264b11bd887a498f929cd877ff38c4`
