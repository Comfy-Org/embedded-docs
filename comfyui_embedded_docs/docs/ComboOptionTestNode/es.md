# ComboOptionTestNode

El nodo ComboOptionTestNode es un nodo lógico diseñado para probar y transmitir selecciones de cuadros combinados. Recibe dos entradas de cuadro combinado, cada una con un conjunto predefinido de opciones, y emite los valores seleccionados directamente sin modificarlos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `combo` | La primera selección de un conjunto de tres opciones de prueba. | COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La segunda selección de un conjunto diferente de tres opciones de prueba. | COMBO | Sí | `"option4"`<br>`"option5"`<br>`"option6"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output_1` | Emite el valor seleccionado en el primer cuadro combinado (`combo`). | COMBO |
| `output_2` | Emite el valor seleccionado en el segundo cuadro combinado (`combo2`). | COMBO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/es.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
