> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/es.md)

El nodo StringSubstring extrae una porción de texto de una cadena más grande. Toma una posición inicial y una posición final para definir la sección que se desea extraer, y luego devuelve el texto comprendido entre esas dos posiciones.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto de entrada de la que se extraerá. Admite texto de varias líneas. |
| `start` | INT | Sí | - | El índice de la posición inicial para la subcadena. El primer carácter se encuentra en el índice 0. |
| `end` | INT | Sí | - | El índice de la posición final para la subcadena. El carácter en este índice no se incluye en el resultado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La subcadena extraída del texto de entrada, que contiene todos los caracteres desde la posición `start` hasta (sin incluir) la posición `end`. |

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`
