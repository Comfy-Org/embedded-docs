# CLIPMergeSubtract

El nodo CLIPMergeSubtract fusiona dos modelos CLIP restando los pesos de un modelo del otro. Crea un nuevo modelo CLIP clonando el primer modelo y luego restando los parches clave del segundo modelo, con un multiplicador ajustable para controlar la intensidad de la resta. Esto permite una combinación de modelos finamente ajustada al eliminar características específicas del modelo base.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip1` | El modelo CLIP base que se clonará y modificará | CLIP | Sí | - |
| `clip2` | El modelo CLIP cuyos parches clave se restarán del modelo base | CLIP | Sí | - |
| `multiplier` | Controla la intensidad de la operación de resta (predeterminado: 1.0) | FLOAT | Sí | -10.0 to 10.0 (step: 0.01) |

**Nota:** El nodo excluye los parámetros `.position_ids` y `.logit_scale` de la operación de resta, independientemente del valor del multiplicador.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `clip` | El modelo CLIP resultante después de restar los pesos del segundo modelo del primero | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/es.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
