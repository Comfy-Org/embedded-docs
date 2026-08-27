# ModelSamplingAuraFlow

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a los modelos de difusión, diseñada específicamente para las arquitecturas de modelo AuraFlow. Modifica el comportamiento de muestreo del modelo aplicando un valor de shift que ajusta la distribución de muestreo. Este nodo hereda del marco de muestreo de modelos SD3 y proporciona un control fino sobre el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplicará la configuración de muestreo AuraFlow | MODEL | Sí | - |
| `shift` | El valor de shift que se aplicará a la distribución de muestreo (predeterminado: 1.73, paso: 0.01) | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con la configuración de muestreo AuraFlow aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/es.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
