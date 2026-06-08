# ComfyOrNode

El nodo ComfyOrNode realiza una operación lógica OR sobre un conjunto de valores de entrada. Devuelve `true` si alguno de los valores proporcionados se considera verdadero según las reglas estándar de veracidad de Python.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `value` | Un valor a evaluar para determinar su veracidad. Puede proporcionar múltiples valores agregando más entradas. El nodo devuelve `true` si alguno de estos valores es verdadero. | ANY | Sí | Se aceptan múltiples valores |

**Nota:** El nodo acepta un mínimo de 1 valor de entrada. Puede agregar más entradas según sea necesario utilizando la función de crecimiento automático.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `BOOLEAN` | Devuelve `true` si alguno de los valores de entrada es verdadero; devuelve `false` si todos los valores de entrada son falsos. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/es.md)

---
**Source fingerprint (SHA-256):** `00c60d5c80bbddc993af0bcd92e35dc77f153731329c23a6e4e9a980709111b1`
