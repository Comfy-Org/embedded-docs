> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/es.md)

El nodo StringSubstring extrae una porción de texto de una cadena más larga. Toma una posición inicial y una posición final para definir la sección que deseas extraer, luego devuelve el texto entre esas dos posiciones.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada de la cual extraer |
| `start` | INT | Sí | - | La posición inicial del índice para la subcadena |
| `end` | INT | Sí | - | La posición final del índice para la subcadena |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La subcadena extraída del texto de entrada |