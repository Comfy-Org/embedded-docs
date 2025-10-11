> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/es.md)

El nodo RegexMatch verifica si una cadena de texto coincide con un patrón de expresión regular especificado. Busca en la cadena de entrada cualquier ocurrencia del patrón regex y devuelve si se encontró una coincidencia. Puedes configurar varios indicadores regex como sensibilidad a mayúsculas y minúsculas, modo multilínea y modo dotall para controlar cómo se comporta la coincidencia de patrones.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto en la que buscar coincidencias |
| `regex_pattern` | STRING | Sí | - | El patrón de expresión regular con el que comparar la cadena |
| `case_insensitive` | BOOLEAN | No | - | Si se debe ignorar mayúsculas y minúsculas al hacer la coincidencia (valor por defecto: True) |
| `multiline` | BOOLEAN | No | - | Si se debe habilitar el modo multilínea para la coincidencia regex (valor por defecto: False) |
| `dotall` | BOOLEAN | No | - | Si se debe habilitar el modo dotall para la coincidencia regex (valor por defecto: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | Devuelve True si el patrón regex coincide con cualquier parte de la cadena de entrada, False en caso contrario |