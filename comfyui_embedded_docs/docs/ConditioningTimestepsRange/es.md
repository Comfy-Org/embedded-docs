> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/es.md)

El nodo `ConditioningTimestepsRange` crea tres rangos de pasos de tiempo distintos para controlar cuándo se aplican los efectos de condicionamiento durante el proceso de generación. Toma valores de porcentaje de inicio y fin y divide el rango completo de pasos de tiempo (0.0 a 1.0) en tres segmentos: el rango principal entre los porcentajes especificados, el rango anterior al porcentaje de inicio y el rango posterior al porcentaje de fin.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `porcentaje_inicio` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje inicial del rango de pasos de tiempo (predeterminado: 0.0) |
| `porcentaje_fin` | FLOAT | Sí | 0.0 - 1.0 | El porcentaje final del rango de pasos de tiempo (predeterminado: 1.0) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `ANTES_DE_RANGO` | TIMESTEPS_RANGE | El rango principal de pasos de tiempo definido por start_percent y end_percent |
| `DESPUÉS_DE_RANGO` | TIMESTEPS_RANGE | El rango de pasos de tiempo desde 0.0 hasta start_percent |
| `AFTER_RANGE` | TIMESTEPS_RANGE | El rango de pasos de tiempo desde end_percent hasta 1.0 |

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
