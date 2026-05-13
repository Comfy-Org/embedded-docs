> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/es.md)

El nodo StringCompare compara dos cadenas de texto utilizando diferentes métodos de comparación. Puede verificar si una cadena comienza con otra, termina con otra, o si ambas cadenas son exactamente iguales. La comparación puede realizarse considerando o ignorando las diferencias entre mayúsculas y minúsculas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `string_a` | STRING | Sí | - | La primera cadena a comparar |
| `string_b` | STRING | Sí | - | La segunda cadena contra la que se compara |
| `mode` | COMBO | Sí | "Comienza Con"<br>"Termina Con"<br>"Igual" | El método de comparación a utilizar (predeterminado: "Comienza Con") |
| `case_sensitive` | BOOLEAN | No | - | Si se deben considerar las diferencias entre mayúsculas y minúsculas durante la comparación (predeterminado: verdadero) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | BOOLEAN | Devuelve verdadero si se cumple la condición de comparación, falso en caso contrario |

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
