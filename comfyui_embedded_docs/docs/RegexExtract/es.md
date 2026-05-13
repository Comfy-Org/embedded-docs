> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/es.md)

El nodo RegexExtract busca patrones en texto utilizando expresiones regulares. Puede encontrar la primera coincidencia, todas las coincidencias, grupos específicos de las coincidencias, o todos los grupos en múltiples coincidencias. El nodo admite varias banderas de expresiones regulares para sensibilidad a mayúsculas/minúsculas, coincidencia multilínea y comportamiento dotall.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `string` | STRING | Sí | - | El texto de entrada en el que buscar patrones |
| `regex_pattern` | STRING | Sí | - | El patrón de expresión regular a buscar |
| `mode` | COMBO | Sí | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | El modo de extracción determina qué partes de las coincidencias se devuelven (predeterminado: "First Match") |
| `case_insensitive` | BOOLEAN | No | - | Si se ignora mayúsculas/minúsculas al coincidir (predeterminado: True) |
| `multiline` | BOOLEAN | No | - | Si se trata la cadena como múltiples líneas (predeterminado: False) |
| `dotall` | BOOLEAN | No | - | Si el punto (.) coincide con saltos de línea (predeterminado: False) |
| `group_index` | INT | No | 0-100 | El índice del grupo de captura a extraer al usar modos de grupo (predeterminado: 1) |

**Nota:** Al usar los modos "First Group" o "All Groups", el parámetro `group_index` especifica qué grupo de captura extraer. El grupo 0 representa la coincidencia completa, mientras que los grupos 1+ representan los grupos de captura numerados en tu patrón de expresión regular.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | STRING | El texto extraído según el modo y los parámetros seleccionados |

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
