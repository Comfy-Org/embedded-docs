# O

El nodo ComfyOrNode realiza una operación OR lógica sobre un conjunto de valores de entrada. Devuelve `true` si cualquiera de los valores proporcionados se considera verdadero según las reglas estándar de veracidad de Python.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `value` | Valor que se evalúa para determinar su veracidad. Se pueden proporcionar varios valores añadiendo más entradas. El nodo devuelve `true` si cualquiera de estos valores es verdadero. | ANY | Sí | Mínimo 1 valor; se aceptan múltiples valores |

**Nota:** El nodo acepta un mínimo de 1 valor de entrada. Se pueden añadir más entradas según sea necesario mediante la función de crecimiento automático.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `BOOLEAN` | Devuelve `true` si cualquiera de los valores de entrada es verdadero; devuelve `false` si todos los valores de entrada son falsos. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/es.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
