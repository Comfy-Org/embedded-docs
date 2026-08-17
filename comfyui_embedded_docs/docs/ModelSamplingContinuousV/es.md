# ModelSamplingContinuousV

El nodo ModelSamplingContinuousV modifica el comportamiento de muestreo de un modelo aplicando parámetros de muestreo continuo de predicción V. Crea un clon del modelo de entrada y lo configura con ajustes personalizados de rango sigma para un control avanzado del muestreo. Esto permite a los usuarios ajustar finamente el proceso de muestreo con valores sigma mínimos y máximos específicos.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de entrada que se modificará con el muestreo continuo de predicción V | MODEL | Sí | - |
| `sampling` | El método de muestreo a aplicar. Actualmente solo se admite la predicción V. | COMBO | Sí | `"v_prediction"` |
| `sigma_max` | El valor sigma máximo para el muestreo (predeterminado: 500.0) | FLOAT | Sí | 0.0 – 1000.0 (paso 0.001) |
| `sigma_min` | El valor sigma mínimo para el muestreo (predeterminado: 0.03) | FLOAT | Sí | 0.0 – 1000.0 (paso 0.001) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el muestreo continuo de predicción V aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/es.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
