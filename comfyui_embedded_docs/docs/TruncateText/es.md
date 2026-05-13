> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/en.md)

Este nodo acorta texto cortándolo en una longitud máxima especificada. Toma cualquier texto de entrada y devuelve solo la primera parte, hasta la cantidad de caracteres que establezcas. Es una forma sencilla de garantizar que el texto no supere un tamaño determinado.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `text` | STRING | Sí | N/A | La cadena de texto que se truncará. |
| `max_length` | INT | Sí | 1 a 10000 | Longitud máxima del texto. El texto se cortará después de esta cantidad de caracteres (predeterminado: 77). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `string` | STRING | El texto truncado, que contiene solo los primeros `max_length` caracteres de la entrada. |

---
**Source fingerprint (SHA-256):** `271a77a910967c4fd86a07485449679fb8db89f6b3f2bf0a8fa2ff224ea2f7b2`
