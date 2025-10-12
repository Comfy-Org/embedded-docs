> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/es.md)

El nodo CLIPMergeSubtract realiza una fusión de modelos restando los pesos de un modelo CLIP de otro. Crea un nuevo modelo CLIP clonando el primer modelo y luego restando los parches clave del segundo modelo, con un multiplicador ajustable para controlar la intensidad de la resta. Esto permite una mezcla de modelos afinada mediante la eliminación de características específicas del modelo base.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Sí | - | El modelo CLIP base que será clonado y modificado |
| `clip2` | CLIP | Sí | - | El modelo CLIP cuyos parches clave serán restados del modelo base |
| `multiplicador` | FLOAT | Sí | -10.0 a 10.0 | Controla la intensidad de la operación de resta (valor por defecto: 1.0) |

**Nota:** El nodo excluye los parámetros `.position_ids` y `.logit_scale` de la operación de resta, independientemente del valor del multiplicador.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `clip` | CLIP | El modelo CLIP resultante después de restar los pesos del segundo modelo del primero |
