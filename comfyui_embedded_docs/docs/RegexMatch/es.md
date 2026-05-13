> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/es.md)

El nodo RegexMatch verifica si una cadena de texto contiene una coincidencia con un patrón de expresión regular determinado. Busca en la cadena de entrada y devuelve un resultado simple de sí/no que indica si el patrón se encontró en alguna parte del texto. Puedes ajustar cómo funciona la búsqueda habilitando opciones como la coincidencia sin distinción de mayúsculas/minúsculas o el modo multilínea.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `cadena` | STRING | Sí | - | La cadena de texto en la que buscar coincidencias |
| `patrón_regex` | STRING | Sí | - | El patrón de expresión regular para comparar con la cadena |
| `insensible_a_mayúsculas` | BOOLEAN | No | - | Si se debe ignorar mayúsculas/minúsculas al coincidir (valor predeterminado: True) |
| `multilínea` | BOOLEAN | No | - | Si se debe habilitar el modo multilínea para la coincidencia de expresiones regulares (valor predeterminado: False) |
| `dotall` | BOOLEAN | No | - | Si se debe habilitar el modo dotall para la coincidencia de expresiones regulares (valor predeterminado: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `matches` | BOOLEAN | Devuelve True si el patrón de expresión regular coincide con alguna parte de la cadena de entrada, False en caso contrario |

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
