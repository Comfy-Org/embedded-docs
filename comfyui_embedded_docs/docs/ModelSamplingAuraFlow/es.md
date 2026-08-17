# ModelSamplingAuraFlow

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a los modelos de difusión, diseñada específicamente para arquitecturas de modelos AuraFlow. Modifica el comportamiento de muestreo del modelo aplicando un parámetro `shift` que ajusta la distribución de muestreo. Este nodo hereda del marco de muestreo de modelos SD3 y proporciona un control fino sobre el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de difusión al que aplicar la configuración de muestreo AuraFlow. | MODEL | Sí | - |
| `shift` | El valor de desplazamiento que se aplica a la distribución de muestreo. Predeterminado: 1.73. Paso: 0.01. | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model` | El modelo modificado con la configuración de muestreo AuraFlow aplicada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/es.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
