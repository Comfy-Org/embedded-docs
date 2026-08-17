# CLIPMergeAdd

El nodo CLIPMergeAdd combina dos modelos CLIP añadiendo parches del segundo modelo al primero. Crea una copia del primer modelo CLIP e incorpora selectivamente parches clave del segundo modelo, excluyendo los IDs de posición y los parámetros de escala logit. Esto le permite fusionar componentes de modelos CLIP preservando la estructura del modelo base.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip1` | El modelo CLIP base que se clonará y se utilizará como base para la fusión | CLIP | Sí | - |
| `clip2` | El modelo CLIP secundario que proporciona los parches clave que se añadirán al modelo base | CLIP | Sí | - |

Nota: Los parches clave de `clip2` se añaden con una fuerza de 1.0. Las claves que terminan en `.position_ids` o `.logit_scale` se excluyen de la fusión.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CLIP` | Un modelo CLIP fusionado que contiene la estructura del modelo base con los parches añadidos del modelo secundario | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/es.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
