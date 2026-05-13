> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/es.md)

El nodo SamplingPercentToSigma convierte un valor de porcentaje de muestreo en un valor sigma correspondiente utilizando los parámetros de muestreo del modelo. Toma un valor porcentual entre 0.0 y 1.0 y lo asigna al valor sigma adecuado dentro del programa de ruido del modelo, con opciones para devolver el sigma calculado o los valores sigma máximos/mínimos reales en los límites.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que contiene los parámetros de muestreo utilizados para la conversión |
| `porcentaje_muestreo` | FLOAT | Sí | 0.0 a 1.0 | El porcentaje de muestreo a convertir a sigma (predeterminado: 0.0) |
| `devolver_sigma_real` | BOOLEAN | Sí | - | Devuelve el valor sigma real en lugar del valor utilizado para comprobaciones de intervalo. Esto solo afecta los resultados en 0.0 y 1.0. (predeterminado: Falso) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `sigma_value` | FLOAT | El valor sigma convertido correspondiente al porcentaje de muestreo de entrada |

---
**Source fingerprint (SHA-256):** `88ecea0528dfeff75248a8dfee8381e1f73d1a2d9ee3e7f8e37fef0f2b2499ec`
