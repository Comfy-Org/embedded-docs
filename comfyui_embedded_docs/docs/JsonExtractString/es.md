El nodo JsonExtractString lee una cadena de texto que contiene datos JSON y extrae el valor asociado a una clave específica. Convierte el valor extraído en una cadena. Si el JSON no es válido, no se encuentra la clave o el valor es nulo, el nodo devuelve una cadena vacía.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `json_string` | El texto que contiene los datos JSON a analizar. | STRING | Sí | N/A |
| `key` | La clave específica cuyo valor de cadena desea extraer del objeto JSON. | STRING | Sí | N/A |

**Nota:** El nodo solo extrae valores de objetos JSON (diccionarios). Si el JSON analizado no es un objeto o si la clave especificada no existe dentro de él, la salida será una cadena vacía.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El valor de cadena extraído del JSON para la clave especificada, o una cadena vacía si la extracción falla. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/es.md)

---
**Source fingerprint (SHA-256):** `f05e2d9fd4888870a844c85ac7543d6c38c1c56f2ef22a402fc93ee716743612`
