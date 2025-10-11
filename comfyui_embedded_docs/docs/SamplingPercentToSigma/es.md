> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/es.md)

El nodo SamplingPercentToSigma convierte un valor de porcentaje de muestreo a un valor sigma correspondiente utilizando los parámetros de muestreo del modelo. Toma un valor porcentual entre 0.0 y 1.0 y lo asigna al valor sigma apropiado en el programa de ruido del modelo, con opciones para devolver ya sea el sigma calculado o los valores sigma máximo/mínimo reales en los límites.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo que contiene los parámetros de muestreo utilizados para la conversión |
| `sampling_percent` | FLOAT | Sí | 0.0 a 1.0 | El porcentaje de muestreo a convertir a sigma (valor por defecto: 0.0) |
| `return_actual_sigma` | BOOLEAN | Sí | - | Devuelve el valor sigma real en lugar del valor utilizado para comprobaciones de intervalo. Esto solo afecta los resultados en 0.0 y 1.0. (valor por defecto: False) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | El valor sigma convertido correspondiente al porcentaje de muestreo de entrada |