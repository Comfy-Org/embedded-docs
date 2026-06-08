El nodo ChromaRadianceOptions permite configurar ajustes avanzados para el modelo Chroma Radiance. Envuelve un modelo existente y aplica opciones específicas durante el proceso de eliminación de ruido basándose en valores sigma, lo que permite un control preciso sobre el tamaño del mosaico NeRF y otros parámetros relacionados con la radiancia.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se aplicarán las opciones de Chroma Radiance | MODEL | Sí | - |
| `preservar_envoltorio` | Cuando está habilitado, delegará en un envoltorio de función de modelo existente si existe. Generalmente debe dejarse habilitado. (predeterminado: True) | BOOLEAN | No | - |
| `sigma_inicial` | Primer sigma en el que estas opciones estarán activas. (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |
| `sigma_final` | Último sigma en el que estas opciones estarán activas. (predeterminado: 0.0) | FLOAT | No | 0.0 a 1.0 |
| `tamaño_mosaico_nerf` | Permite sobrescribir el tamaño predeterminado del mosaico NeRF. -1 significa usar el valor predeterminado (32). 0 significa usar el modo sin mosaico (puede requerir mucha VRAM). (predeterminado: -1) | INT | No | -1 y superior |

**Nota:** Las opciones de Chroma Radiance solo surten efecto cuando el valor sigma actual se encuentra entre `end_sigma` y `start_sigma` (inclusive). El parámetro `nerf_tile_size` solo se aplica cuando se establece en 0 o valores superiores.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con las opciones de Chroma Radiance aplicadas | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/es.md)

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`
