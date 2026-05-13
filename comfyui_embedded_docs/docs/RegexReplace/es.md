> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/es.md)

El nodo RegexReplace busca y reemplaza texto en cadenas utilizando patrones de expresiones regulares. Permite buscar patrones de texto y reemplazarlos con texto nuevo, con opciones para controlar cómo funciona la coincidencia de patrones, incluyendo sensibilidad a mayúsculas/minúsculas, coincidencia multilínea y limitación del número de reemplazos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada en la que buscar y reemplazar |
| `regex_pattern` | STRING | Sí | - | El patrón de expresión regular para buscar en la cadena de entrada |
| `replace` | STRING | Sí | - | El texto de reemplazo para sustituir los patrones coincidentes |
| `case_insensitive` | BOOLEAN | No | - | Cuando está habilitado, hace que la coincidencia de patrones ignore diferencias de mayúsculas/minúsculas (predeterminado: Verdadero) |
| `multiline` | BOOLEAN | No | - | Cuando está habilitado, cambia el comportamiento de ^ y $ para que coincidan al inicio/final de cada línea en lugar de solo al inicio/final de toda la cadena (predeterminado: Falso) |
| `dotall` | BOOLEAN | No | - | Cuando está habilitado, el carácter punto (.) coincidirá con cualquier carácter, incluidos los caracteres de nueva línea. Cuando está deshabilitado, los puntos no coincidirán con nuevas líneas (predeterminado: Falso) |
| `count` | INT | No | 0-100 | Número máximo de reemplazos a realizar. Establecer en 0 para reemplazar todas las ocurrencias (predeterminado). Establecer en 1 para reemplazar solo la primera coincidencia, 2 para las dos primeras coincidencias, etc. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La cadena modificada con los reemplazos especificados aplicados |

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
