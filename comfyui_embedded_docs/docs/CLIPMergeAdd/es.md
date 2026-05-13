> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/es.md)

El nodo CLIPMergeAdd combina dos modelos CLIP añadiendo parches del segundo modelo al primero. Crea una copia del primer modelo CLIP e incorpora selectivamente parches clave del segundo modelo, excluyendo los ID de posición y los parámetros de escala logit. Esto permite fusionar componentes de modelos CLIP mientras se preserva la estructura del modelo base.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip1` | CLIP | Sí | - | El modelo CLIP base que será clonado y utilizado como base para la fusión |
| `clip2` | CLIP | Sí | - | El modelo CLIP secundario que proporciona los parches clave que se añadirán al modelo base |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CLIP` | CLIP | Un modelo CLIP fusionado que contiene la estructura del modelo base con parches añadidos del modelo secundario |

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`
