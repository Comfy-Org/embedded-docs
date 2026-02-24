> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/es.md)

Este nodo acorta texto recortándolo a una longitud máxima especificada. Toma cualquier texto de entrada y devuelve solo la primera parte, hasta el número de caracteres que establezcas. Es una forma sencilla de asegurar que el texto no exceda un tamaño determinado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sí | N/A | La cadena de texto que se va a truncar. |
| `max_length` | INT | No | 1 a 10000 | Longitud máxima del texto. El texto se cortará después de esta cantidad de caracteres (por defecto: 77). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `string` | STRING | El texto truncado, que contiene solo los primeros `max_length` caracteres de la entrada. |
