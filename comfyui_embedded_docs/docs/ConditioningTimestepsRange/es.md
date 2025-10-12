> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/es.md)

El nodo ConditioningTimestepsRange crea tres rangos de pasos temporales distintos para controlar cuándo se aplican los efectos de condicionamiento durante el proceso de generación. Toma valores de porcentaje de inicio y fin y divide el rango completo de pasos temporales (0.0 a 1.0) en tres segmentos: el rango principal entre los porcentajes especificados, el rango anterior al porcentaje de inicio y el rango posterior al porcentaje de fin.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `porcentaje_inicio` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje de inicio del rango de pasos temporales (por defecto: 0.0) |
| `porcentaje_fin` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje de fin del rango de pasos temporales (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ANTES_DE_RANGO` | TIMESTEPS_RANGE | El rango principal de pasos temporales definido por start_percent y end_percent |
| `DESPUÉS_DE_RANGO` | TIMESTEPS_RANGE | El rango de pasos temporales desde 0.0 hasta start_percent |
| `AFTER_RANGE` | TIMESTEPS_RANGE | El rango de pasos temporales desde end_percent hasta 1.0 |