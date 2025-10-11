> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/es.md)

El nodo Case Converter transforma cadenas de texto a diferentes formatos de mayúsculas y minúsculas. Toma una cadena de entrada y la convierte según el modo seleccionado, produciendo una cadena de salida con el formato de mayúsculas y minúsculas especificado aplicado. El nodo admite cuatro opciones diferentes de conversión de mayúsculas y minúsculas para modificar la capitalización de su texto.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | String | - | - | La cadena de texto que se convertirá a un formato de mayúsculas y minúsculas diferente |
| `mode` | STRING | Combo | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | El modo de conversión de mayúsculas y minúsculas a aplicar: UPPERCASE convierte todas las letras a mayúsculas, lowercase convierte todas las letras a minúsculas, Capitalize capitaliza solo la primera letra, Title Case capitaliza la primera letra de cada palabra |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena de entrada convertida al formato de mayúsculas y minúsculas especificado |