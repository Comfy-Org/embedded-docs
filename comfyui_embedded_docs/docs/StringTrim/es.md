> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/es.md)

El nodo `StringTrim` elimina los caracteres de espacio en blanco del inicio, final o ambos lados de una cadena de texto. Puedes elegir recortar desde el lado izquierdo, el lado derecho o ambos lados de la cadena. Esto es útil para limpiar entradas de texto eliminando espacios no deseados, tabulaciones o saltos de línea.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `cadena` | STRING | Sí | - | La cadena de texto a procesar. Admite entrada multilínea. |
| `modo` | COMBO | Sí | "Both"<br>"Left"<br>"Right" | Especifica qué lado(s) de la cadena recortar. "Both" elimina espacios en blanco de ambos extremos, "Left" solo del inicio, "Right" solo del final. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La cadena de texto recortada, con los espacios en blanco eliminados según el modo seleccionado. |

---
**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`
