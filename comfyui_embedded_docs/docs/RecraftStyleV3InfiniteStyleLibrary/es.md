> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/es.md)

Este nodo permite seleccionar un estilo de la Biblioteca de Estilos Infinitos de Recraft utilizando un UUID preexistente. Recupera la información del estilo basándose en el identificador proporcionado y la devuelve para su uso en otros nodos de Recraft.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | Sí | Cualquier UUID válido | UUID del estilo de la Biblioteca de Estilos Infinitos. |

**Nota:** La entrada `style_id` no puede estar vacía. Si se proporciona una cadena vacía, el nodo generará una excepción.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | El objeto de estilo seleccionado de la Biblioteca de Estilos Infinitos de Recraft |