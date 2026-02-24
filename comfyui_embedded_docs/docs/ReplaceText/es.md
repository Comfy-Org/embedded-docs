> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/es.md)

El nodo Replace Text realiza una sustitución de texto simple. Busca un fragmento de texto específico dentro de la entrada y reemplaza cada ocurrencia con un nuevo fragmento de texto. La operación se aplica a todas las entradas de texto proporcionadas al nodo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sí | - | El texto a procesar. |
| `find` | STRING | No | - | El texto a buscar y reemplazar (valor por defecto: cadena vacía). |
| `replace` | STRING | No | - | El texto con el que reemplazar el texto encontrado (valor por defecto: cadena vacía). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `text` | STRING | El texto procesado, con todas las ocurrencias del texto `find` reemplazadas por el texto `replace`. |
