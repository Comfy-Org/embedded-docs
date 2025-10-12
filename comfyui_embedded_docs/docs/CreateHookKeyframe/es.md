> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/es.md)

El nodo Create Hook Keyframe permite definir puntos específicos en un proceso de generación donde el comportamiento de los hooks cambia. Crea keyframes que modifican la intensidad de los hooks en porcentajes particulares del progreso de generación, y estos keyframes pueden encadenarse para crear patrones de programación complejos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `multiplicador_fuerza` | FLOAT | Sí | -20.0 a 20.0 | Multiplicador para la intensidad del hook en este keyframe (valor por defecto: 1.0) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 | El punto porcentual en el proceso de generación donde este keyframe entra en efecto (valor por defecto: 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Grupo opcional de keyframes de hook anterior al que añadir este keyframe |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un grupo de keyframes de hook que incluye el keyframe recién creado |
