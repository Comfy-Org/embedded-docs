> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/es.md)

El nodo ModelSamplingContinuousV modifica el comportamiento de muestreo de un modelo aplicando parámetros de muestreo de predicción V continua. Crea un clon del modelo de entrada y lo configura con rangos de sigma personalizados para un control avanzado del muestreo. Esto permite a los usuarios ajustar el proceso de muestreo con valores mínimo y máximo de sigma específicos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada que se modificará con muestreo de predicción V continua |
| `sampling` | STRING | Sí | `"v_prediction"` | El método de muestreo a aplicar (actualmente solo se admite predicción V) |
| `sigma_max` | FLOAT | Sí | 0.0 - 1000.0 | El valor máximo de sigma para el muestreo (predeterminado: 500.0) |
| `sigma_min` | FLOAT | Sí | 0.0 - 1000.0 | El valor mínimo de sigma para el muestreo (predeterminado: 0.03) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo modificado con muestreo de predicción V continua aplicado |

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
