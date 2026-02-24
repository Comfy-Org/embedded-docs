> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/es.md)

Este nodo fusiona múltiples listas de texto en una única lista combinada. Está diseñado para recibir entradas de texto como listas y concatenarlas. El nodo registra el número total de textos en la lista fusionada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `texts` | STRING | Sí | N/A | Las listas de texto que se van a fusionar. Se pueden conectar múltiples listas a la entrada, y estas se concatenarán en una sola. |

**Nota:** Este nodo está configurado como un proceso de grupo (`is_group_process = True`), lo que significa que maneja automáticamente múltiples entradas de lista concatenándolas antes de que se ejecute la función principal de procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `texts` | STRING | La lista única y fusionada que contiene todos los textos de entrada. |
