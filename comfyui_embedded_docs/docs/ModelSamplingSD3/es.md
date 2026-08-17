# MuestreoDeModeloSD3

El nodo ModelSamplingSD3 aplica parámetros de muestreo de Stable Diffusion 3 a un modelo. Modifica el comportamiento de muestreo del modelo ajustando el parámetro `shift`, que controla las características de la distribución de muestreo. El nodo crea una copia modificada del modelo de entrada con la configuración de muestreo especificada aplicada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de entrada al que se le aplican los parámetros de muestreo de SD3 | MODEL | Sí | - |
| `shift` | Controla el parámetro de desplazamiento de muestreo (predeterminado: 3.0) | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con los parámetros de muestreo de SD3 aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/es.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
