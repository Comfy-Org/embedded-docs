> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/es.md)

El nodo StringContains verifica si una cadena dada contiene una subcadena específica. Puede realizar esta verificación con coincidencias que distinguen entre mayúsculas y minúsculas o que no distinguen, devolviendo un resultado booleano que indica si se encontró la subcadena dentro de la cadena principal.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto principal en la que se va a buscar |
| `substring` | STRING | Sí | - | El texto que se va a buscar dentro de la cadena principal |
| `case_sensitive` | BOOLEAN | No | - | Determina si la búsqueda debe distinguir entre mayúsculas y minúsculas (valor por defecto: true) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | Devuelve true si se encuentra la subcadena en la cadena, false en caso contrario |
