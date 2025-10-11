> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/es.md)

El nodo StringReplace realiza operaciones de reemplazo de texto en cadenas de entrada. Busca una subcadena específica dentro del texto de entrada y reemplaza todas sus ocurrencias con una subcadena diferente. Este nodo devuelve la cadena modificada con todos los reemplazos aplicados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada donde se realizarán los reemplazos |
| `find` | STRING | Sí | - | La subcadena a buscar dentro del texto de entrada |
| `replace` | STRING | Sí | - | El texto de reemplazo que sustituirá todas las ocurrencias encontradas |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena modificada con todas las ocurrencias del texto de búsqueda reemplazadas por el texto de reemplazo |