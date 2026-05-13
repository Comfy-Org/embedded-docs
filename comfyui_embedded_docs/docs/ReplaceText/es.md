> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/es.md)

El nodo Reemplazar Texto realiza una sustitución de texto simple. Busca un fragmento de texto específico dentro de la entrada y reemplaza cada aparición con un nuevo fragmento de texto. La operación se aplica a todas las entradas de texto proporcionadas al nodo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `text` | STRING | Sí | - | El texto a procesar. |
| `find` | STRING | Sí | - | Texto a buscar (predeterminado: cadena vacía). |
| `replace` | STRING | Sí | - | Texto con el que reemplazar (predeterminado: cadena vacía). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `text` | STRING | El texto procesado con todas las apariciones del texto `find` reemplazadas por el texto `replace`. |

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
