> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/es.md)

El ComboOptionTestNode es un nodo lógico diseñado para probar y transmitir selecciones de cuadros combinados. Toma dos entradas de cuadros combinados, cada una con un conjunto predefinido de opciones, y emite los valores seleccionados directamente sin modificación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"` | La primera selección de un conjunto de tres opciones de prueba. |
| `combo2` | COMBO | Sí | `"option4"`<br>`"option5"`<br>`"option6"` | La segunda selección de un conjunto diferente de tres opciones de prueba. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_1` | COMBO | Emite el valor seleccionado del primer cuadro combinado (`combo`). |
| `output_2` | COMBO | Emite el valor seleccionado del segundo cuadro combinado (`combo2`). |
