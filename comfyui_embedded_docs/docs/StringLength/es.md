> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringLength/es.md)

El nodo StringLength calcula el número de caracteres en una cadena de texto. Toma cualquier entrada de texto y devuelve el recuento total de caracteres, incluyendo espacios y puntuación. Esto es útil para medir la longitud del texto o validar requisitos de tamaño de cadena.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | N/A | La cadena de texto de la cual medir la longitud. Admite entrada multilínea. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `length` | INT | El número total de caracteres en la cadena de entrada, incluyendo espacios y caracteres especiales. |