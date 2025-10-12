> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/es.md)

El nodo StringTrim elimina caracteres de espacio en blanco del principio, final o ambos lados de una cadena de texto. Puedes elegir recortar del lado izquierdo, derecho o ambos lados de la cadena. Esto es útil para limpiar entradas de texto eliminando espacios, tabulaciones o caracteres de nueva línea no deseados.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Sí | - | La cadena de texto a procesar. Admite entrada multilínea. |
| `mode` | COMBO | Sí | "Both"<br>"Left"<br>"Right" | Especifica qué lado(s) de la cadena recortar. "Both" elimina espacios en blanco de ambos extremos, "Left" elimina solo del principio, "Right" elimina solo del final. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena de texto recortada con espacios en blanco eliminados según el modo seleccionado. |
