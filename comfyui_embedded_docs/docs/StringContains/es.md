> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/es.md)

El nodo StringContains verifica si una cadena de texto determinada contiene una subcadena especificada. Puede realizar esta verificación con coincidencia sensible a mayúsculas/minúsculas o insensible, devolviendo un resultado booleano que indica si la subcadena fue encontrada dentro de la cadena principal.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `cadena` | STRING | Sí | - | La cadena de texto principal en la que buscar |
| `subcadena` | STRING | Sí | - | El texto a buscar dentro de la cadena principal |
| `distingue mayúsculas y minúsculas` | BOOLEAN | No | - | Determina si la búsqueda debe ser sensible a mayúsculas/minúsculas (valor predeterminado: true) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `contains` | BOOLEAN | Devuelve true si la subcadena se encuentra en la cadena, false en caso contrario |

---
**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`
