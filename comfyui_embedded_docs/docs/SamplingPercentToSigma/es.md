# SamplingPercentToSigma

El nodo SamplingPercentToSigma convierte un valor de porcentaje de muestreo a un valor sigma correspondiente utilizando los parámetros de muestreo del modelo. Toma un valor de porcentaje entre 0.0 y 1.0 y lo asigna al valor sigma apropiado en el programa de ruido del modelo, con opciones para devolver el sigma calculado o los valores sigma máximo/mínimo reales en los límites.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que contiene los parámetros de muestreo utilizados para la conversión | MODEL | Sí | - |
| `porcentaje_muestreo` | El porcentaje de muestreo a convertir a sigma (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 (paso: 0.0001) |
| `devolver_sigma_real` | Devuelve el valor sigma real en lugar del valor utilizado para las comprobaciones de intervalo. Esto solo afecta los resultados en 0.0 y 1.0. (por defecto: False) | BOOLEAN | Sí | - |

Cuando `return_actual_sigma` está habilitado, un `sampling_percent` de 0.0 devuelve el valor sigma máximo del modelo (sigma_max), y un `sampling_percent` de 1.0 devuelve el valor sigma mínimo (sigma_min). Para todos los demás porcentajes, el resultado es el mismo esté o no habilitada la opción.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `valor_sigma` | El valor sigma convertido correspondiente al porcentaje de muestreo de entrada | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/es.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
