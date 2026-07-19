# ModelSamplingAuraFlow

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a modelos de difusión, diseñada específicamente para arquitecturas de modelo AuraFlow. Modifica el comportamiento de muestreo del modelo aplicando un parámetro de desplazamiento que ajusta la distribución de muestreo. Este nodo hereda del marco de muestreo de modelos SD3 y proporciona un control preciso sobre el proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplicará la configuración de muestreo AuraFlow | MODEL | Sí | - |
| `shift` | El valor de desplazamiento que se aplicará a la distribución de muestreo (predeterminado: 1.73) | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con la configuración de muestreo AuraFlow aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/es.md)

---
**Source fingerprint (SHA-256):** `f49367534032fb2d697d16e8197c16dc761678a5e39990993bdc864bfccea314`
