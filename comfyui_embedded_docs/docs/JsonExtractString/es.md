> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/es.md)

El nodo JsonExtractString lee una cadena de texto que contiene datos JSON y extrae el valor asociado a una clave específica. Convierte el valor extraído en una cadena de texto. Si el JSON no es válido, no se encuentra la clave o el valor es nulo, el nodo devuelve una cadena vacía.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | Sí | N/A | El texto que contiene los datos JSON que se van a analizar. |
| `key` | STRING | Sí | N/A | La clave específica cuyo valor de cadena de texto se desea extraer del objeto JSON. |

**Nota:** El nodo solo extrae valores de objetos JSON (diccionarios). Si el JSON analizado no es un objeto o si la clave especificada no existe dentro de él, la salida será una cadena vacía.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | El valor de cadena de texto extraído del JSON para la clave especificada, o una cadena vacía si falla la extracción. |