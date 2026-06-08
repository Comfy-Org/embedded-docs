El nodo ComboOptionTestNode es un nodo lógico diseñado para probar y transmitir selecciones de cuadros combinados. Toma dos entradas de cuadro combinado, cada una con un conjunto predefinido de opciones, y genera los valores seleccionados directamente sin modificaciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `combo` | La primera selección de un conjunto de tres opciones de prueba. | COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La segunda selección de un conjunto diferente de tres opciones de prueba. | COMBO | Sí | `"option4"`<br>`"option5"`<br>`"option6"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output_1` | Genera el valor seleccionado del primer cuadro combinado (`combo`). | COMBO |
| `output_2` | Genera el valor seleccionado del segundo cuadro combinado (`combo2`). | COMBO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/es.md)

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`
