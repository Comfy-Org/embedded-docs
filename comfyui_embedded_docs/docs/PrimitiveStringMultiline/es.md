> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/es.md)

El nodo PrimitiveStringMultiline proporciona un campo de entrada de texto multilínea para ingresar y pasar valores de cadena a través de su flujo de trabajo. Acepta entrada de texto con múltiples líneas y emite el mismo valor de cadena sin cambios. Este nodo es útil cuando necesita ingresar contenido de texto más largo o texto formateado que abarca varias líneas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Sí | N/A | El valor de entrada de texto que puede abarcar múltiples líneas |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | El mismo valor de cadena que se proporcionó como entrada |