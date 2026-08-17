# SamplingPercentToSigma

El nodo SamplingPercentToSigma convierte un valor de porcentaje de muestreo en el valor sigma correspondiente utilizando los parámetros de muestreo del modelo. Toma un valor porcentual entre 0.0 y 1.0 y lo asigna al valor sigma adecuado en el programa de ruido del modelo, con opciones para devolver tanto el sigma calculado como los valores sigma máximo/mínimo reales en los límites.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo que contiene los parámetros de muestreo utilizados para la conversión | MODEL | Sí | - |
| `sampling_percent` | El porcentaje de muestreo a convertir en sigma (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1.0 (paso: 0.0001) |
| `return_actual_sigma` | Devuelve el valor sigma real en lugar del valor utilizado para las comprobaciones de intervalo. Esto solo afecta los resultados en 0.0 y 1.0. (predeterminado: False) | BOOLEAN | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigma_value` | El valor sigma convertido correspondiente al porcentaje de muestreo de entrada | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/es.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
