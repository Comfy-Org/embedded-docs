> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/es.md)

El nodo Convertir Cadena a Combo toma una cadena de texto como entrada y la convierte en un tipo de datos Combo. Esto permite utilizar un valor de texto como selección para otros nodos que requieren una entrada de tipo Combo. Simplemente pasa el valor de la cadena sin cambios, pero altera su tipo de datos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | N/A | La cadena de texto que se convertirá en un tipo Combo. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | COMBO | La cadena de entrada, ahora formateada como un tipo de datos Combo. |
