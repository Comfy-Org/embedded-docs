> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/es.md)

El nodo SetClipHooks permite aplicar hooks personalizados a un modelo CLIP, permitiendo modificaciones avanzadas a su comportamiento. Puede aplicar hooks a las salidas de acondicionamiento y opcionalmente habilitar la funcionalidad de programación de clip. Este nodo crea una copia clonada del modelo CLIP de entrada con las configuraciones de hook especificadas aplicadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP al que aplicar los hooks |
| `aplicar_a_conds` | BOOLEAN | Sí | - | Si aplicar hooks a las salidas de acondicionamiento (por defecto: True) |
| `programar_clip` | BOOLEAN | Sí | - | Si habilitar la programación de clip (por defecto: False) |
| `ganchos` | HOOKS | No | - | Grupo de hooks opcional para aplicar al modelo CLIP |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `clip` | CLIP | Un modelo CLIP clonado con los hooks especificados aplicados |
