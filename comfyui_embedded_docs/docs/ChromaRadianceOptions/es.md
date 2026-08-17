# Opciones de Croma Radiance

El nodo ChromaRadianceOptions le permite configurar ajustes avanzados para el modelo Chroma Radiance. Envuelve un modelo existente y aplica opciones específicas durante el proceso de eliminación de ruido basadas en los valores sigma, lo que permite un control fino sobre el tamaño de tesela NeRF y otros parámetros relacionados con la radiancia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo al que aplicar las opciones de Chroma Radiance. | MODEL | Sí | - |
| `preserve_wrapper` | Cuando está habilitado, delegará en un envoltorio de función de modelo existente si lo hay. En general, debe dejarse habilitado. (predeterminado: True) | BOOLEAN | No | - |
| `start_sigma` | Primer sigma en el que estas opciones estarán en vigor. (predeterminado: 1.0) | FLOAT | No | 0.0 to 1.0 |
| `end_sigma` | Último sigma en el que estas opciones estarán en vigor. (predeterminado: 0.0) | FLOAT | No | 0.0 to 1.0 |
| `nerf_tile_size` | Permite anular el tamaño de tesela NeRF predeterminado. -1 significa usar el valor predeterminado (32). 0 significa usar el modo sin teselado (puede requerir mucha VRAM). (predeterminado: -1) | INT | No | -1 and above |
| `force_sequential_txt_ids` | Fuerza el uso de identificadores de token de texto secuenciales en lugar de ceros. Debe usarse para checkpoints del 22/05/2026 al 01/06/2026 que se hayan entrenado de esta manera pero que no contengan la clave `__sequential__` en el state dict. (predeterminado: False) | BOOLEAN | No | - |

**Nota:** Las opciones de Chroma Radiance solo tienen efecto cuando el valor sigma actual se encuentra entre `end_sigma` y `start_sigma` (inclusive). El parámetro `nerf_tile_size` solo se aplica cuando se establece en 0 o valores superiores. El parámetro `force_sequential_txt_ids` solo se aplica cuando se establece en True.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model` | El modelo modificado con las opciones de Chroma Radiance aplicadas. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/es.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
