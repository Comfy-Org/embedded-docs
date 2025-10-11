> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/es.md)

El nodo StringCompare compara dos cadenas de texto utilizando diferentes métodos de comparación. Puede verificar si una cadena comienza con otra, termina con otra, o si ambas cadenas son exactamente iguales. La comparación puede realizarse considerando o no las diferencias entre mayúsculas y minúsculas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Sí | - | La primera cadena a comparar |
| `string_b` | STRING | Sí | - | La segunda cadena contra la que comparar |
| `mode` | COMBO | Sí | "Starts With"<br>"Ends With"<br>"Equal" | El método de comparación a utilizar |
| `case_sensitive` | BOOLEAN | No | - | Si se deben considerar las mayúsculas y minúsculas durante la comparación (por defecto: true) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Devuelve true si se cumple la condición de comparación, false en caso contrario |