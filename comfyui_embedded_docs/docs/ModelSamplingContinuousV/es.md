> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/es.md)

El nodo ModelSamplingContinuousV modifica el comportamiento de muestreo de un modelo aplicando parámetros de muestreo continuo de predicción-V. Crea un clon del modelo de entrada y lo configura con ajustes personalizados de rango sigma para un control avanzado del muestreo. Esto permite a los usuarios ajustar finamente el proceso de muestreo con valores sigma mínimos y máximos específicos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada que será modificado con muestreo continuo de predicción-V |
| `sampling` | STRING | Sí | "v_prediction" | El método de muestreo a aplicar (actualmente solo se admite predicción-V) |
| `sigma_max` | FLOAT | Sí | 0.0 - 1000.0 | El valor sigma máximo para el muestreo (por defecto: 500.0) |
| `sigma_min` | FLOAT | Sí | 0.0 - 1000.0 | El valor sigma mínimo para el muestreo (por defecto: 0.03) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con muestreo continuo de predicción-V aplicado |