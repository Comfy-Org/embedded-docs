> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/es.md)

Este nodo combina múltiples listas de texto en una única lista combinada. Está diseñado para recibir entradas de texto como listas y concatenarlas. El nodo registra el número total de textos en la lista combinada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `textos` | STRING | Sí | N/A | Las listas de texto que se van a combinar. Se pueden conectar múltiples listas a la entrada, y se concatenarán en una sola. |

**Nota:** Este nodo está configurado como un proceso grupal (`is_group_process = True`), lo que significa que maneja automáticamente múltiples entradas de lista concatenándolas antes de que se ejecute la función de procesamiento principal.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `textos` | STRING | La única lista combinada que contiene todos los textos de entrada. |

---
**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`
