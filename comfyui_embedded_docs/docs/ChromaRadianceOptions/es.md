# Opciones de Croma Radiance

El nodo ChromaRadianceOptions le permite configurar ajustes avanzados para el modelo Chroma Radiance. Envuelve un modelo existente y aplica opciones específicas durante el proceso de eliminación de ruido basándose en valores sigma, lo que permite un control fino sobre el tamaño de tesela NeRF y otros parámetros relacionados con la radiancia.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo al que se le aplicarán las opciones de Chroma Radiance | MODEL | Sí | - |
| `preservar_envoltorio` | Cuando está habilitado, delegará en un envoltorio de función del modelo existente si lo hay. Generalmente debería dejarse habilitado. (por defecto: True) | BOOLEAN | No | - |
| `sigma_inicial` | Primer sigma en el que estas opciones estarán en vigor. (por defecto: 1.0) | FLOAT | No | 0.0 a 1.0 |
| `sigma_final` | Último sigma en el que estas opciones estarán en vigor. (por defecto: 0.0) | FLOAT | No | 0.0 a 1.0 |
| `tamaño_mosaico_nerf` | Permite anular el tamaño de tesela NeRF predeterminado. -1 significa usar el predeterminado (32). 0 significa usar el modo sin teselas (puede requerir mucha VRAM). (por defecto: -1) | INT | No | -1 y superiores |
| `forzar_ids_de_texto_secuenciales` | Fuerza el uso de identificadores de token de texto secuenciales en lugar de ceros. Debe usarse para checkpoints desde 2026-05-22 hasta 2026-06-01 que se entrenaron de esta manera pero que no contienen la clave `__sequential__` en el diccionario de estado. (por defecto: False) | BOOLEAN | No | - |

**Nota:** Las opciones de Chroma Radiance solo tienen efecto cuando el valor sigma actual se encuentra entre `end_sigma` y `start_sigma` (inclusive). El parámetro `nerf_tile_size` solo se aplica cuando se establece en 0 o en valores superiores. El parámetro `force_sequential_txt_ids` solo se aplica cuando se establece en True. Cuando `nerf_tile_size` es -1 y `force_sequential_txt_ids` es False, no se configura ninguna opción y el modelo se devuelve sin cambios sin aplicar ningún envoltorio.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `model` | El modelo con las opciones de Chroma Radiance aplicadas, o el modelo sin cambios si no hay opciones activas | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/es.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
