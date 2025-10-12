> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/es.md)

El nodo ChromaRadianceOptions permite configurar ajustes avanzados para el modelo Chroma Radiance. Envuelve un modelo existente y aplica opciones específicas durante el proceso de eliminación de ruido basándose en valores sigma, permitiendo un control afinado sobre el tamaño de tile NeRF y otros parámetros relacionados con la radiancia.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Requerido | - | - | El modelo al que aplicar las opciones de Chroma Radiance |
| `preserve_wrapper` | BOOLEAN | Opcional | True | - | Cuando está habilitado, delegará a un envoltorio de función de modelo existente si existe. Generalmente debería dejarse habilitado. |
| `start_sigma` | FLOAT | Opcional | 1.0 | 0.0 - 1.0 | Primer sigma en el que estas opciones estarán en efecto. |
| `end_sigma` | FLOAT | Opcional | 0.0 | 0.0 - 1.0 | Último sigma en el que estas opciones estarán en efecto. |
| `nerf_tile_size` | INT | Opcional | -1 | -1 y superior | Permite anular el tamaño de tile NeRF por defecto. -1 significa usar el valor por defecto (32). 0 significa usar modo sin tiles (puede requerir mucha VRAM). |

**Nota:** Las opciones de Chroma Radiance solo tienen efecto cuando el valor sigma actual se encuentra entre `end_sigma` y `start_sigma` (inclusive). El parámetro `nerf_tile_size` solo se aplica cuando se establece en 0 o valores superiores.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con las opciones de Chroma Radiance aplicadas |
