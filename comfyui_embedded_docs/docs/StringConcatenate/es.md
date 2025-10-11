> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/es.md)

El nodo StringConcatenate combina dos cadenas de texto en una uniéndolas con un delimitador especificado. Toma dos cadenas de entrada y un carácter o cadena delimitador, luego produce una única cadena donde las dos entradas están conectadas con el delimitador colocado entre ellas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Sí | - | La primera cadena de texto a concatenar |
| `string_b` | STRING | Sí | - | La segunda cadena de texto a concatenar |
| `delimiter` | STRING | No | - | El carácter o cadena a insertar entre las dos cadenas de entrada (valor por defecto: cadena vacía) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena combinada con el delimitador insertado entre string_a y string_b |