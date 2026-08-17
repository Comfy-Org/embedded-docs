# MuestreoDeModeloStableCascade

El nodo ModelSamplingStableCascade aplica el muestreo Stable Cascade a un modelo ajustando los parámetros de muestreo con un valor de desplazamiento. Crea un clon modificado del modelo de entrada con una configuración de muestreo personalizada para la generación Stable Cascade.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de entrada al que se le aplica el muestreo Stable Cascade | MODEL | Sí | - |
| `shift` | El valor de desplazamiento para aplicar a los parámetros de muestreo (predeterminado: 2.0) | FLOAT | Sí | 0.0 - 100.0 (step: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el muestreo Stable Cascade aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/es.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
