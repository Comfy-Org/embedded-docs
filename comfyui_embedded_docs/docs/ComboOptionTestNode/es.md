# ComboOptionTestNode

Este nodo toma dos selecciones de cuadros combinados y las pasa directamente a sus salidas sin modificarlas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `combo` | La primera selección, elegida de un conjunto de tres opciones de prueba. | COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La segunda selección, elegida de un conjunto diferente de tres opciones de prueba. | COMBO | Sí | `"option4"`<br>`"option5"`<br>`"option6"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output_1` | Devuelve el valor seleccionado en el primer cuadro combinado (`combo`), sin cambios. | COMBO |
| `output_2` | Devuelve el valor seleccionado en el segundo cuadro combinado (`combo2`), sin cambios. | COMBO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/es.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
