> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/es.md)

El nodo RegexReplace busca y reemplaza texto en cadenas utilizando patrones de expresiones regulares. Permite buscar patrones de texto y reemplazarlos con nuevo texto, con opciones para controlar cómo funciona la coincidencia de patrones, incluyendo sensibilidad a mayúsculas y minúsculas, coincidencia multilínea y limitación del número de reemplazos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada en la que buscar y reemplazar |
| `regex_pattern` | STRING | Sí | - | El patrón de expresión regular a buscar en la cadena de entrada |
| `replace` | STRING | Sí | - | El texto de reemplazo para sustituir los patrones coincidentes |
| `case_insensitive` | BOOLEAN | No | - | Cuando está activado, hace que la coincidencia de patrones ignore las diferencias entre mayúsculas y minúsculas (valor por defecto: True) |
| `multiline` | BOOLEAN | No | - | Cuando está activado, cambia el comportamiento de ^ y $ para que coincidan al inicio/final de cada línea en lugar de solo al inicio/final de toda la cadena (valor por defecto: False) |
| `dotall` | BOOLEAN | No | - | Cuando está activado, el carácter punto (.) coincidirá con cualquier carácter incluyendo caracteres de nueva línea. Cuando está desactivado, los puntos no coincidirán con saltos de línea (valor por defecto: False) |
| `count` | INT | No | 0-100 | Número máximo de reemplazos a realizar. Establecer en 0 para reemplazar todas las ocurrencias (valor por defecto). Establecer en 1 para reemplazar solo la primera coincidencia, 2 para las dos primeras coincidencias, etc. (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena modificada con los reemplazos especificados aplicados |
