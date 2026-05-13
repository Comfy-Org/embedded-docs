> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/es.md)

El nodo StringReplace realiza operaciones de reemplazo de texto en cadenas de entrada. Busca una subcadena específica dentro del texto de entrada y reemplaza todas sus apariciones con una subcadena diferente. Este nodo devuelve la cadena modificada con todos los reemplazos aplicados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada donde se realizarán los reemplazos |
| `find` | STRING | Sí | - | La subcadena a buscar dentro del texto de entrada |
| `replace` | STRING | Sí | - | El texto de reemplazo que sustituirá todas las apariciones encontradas |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La cadena modificada con todas las apariciones del texto buscado reemplazadas por el texto de reemplazo |

---
**Source fingerprint (SHA-256):** `72159dba72261efe9df283c1ea3f789651eade923efdaeb108bacc1d0da663f8`
