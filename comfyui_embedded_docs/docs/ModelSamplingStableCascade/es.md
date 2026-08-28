# MuestreoDeModeloStableCascade

El nodo ModelSamplingStableCascade aplica un muestreo en cascada estable a un modelo ajustando los parámetros de muestreo con un valor de desplazamiento. Crea una copia parcheada del modelo de entrada con una configuración personalizada de muestreo en cascada estable, dejando el modelo original sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de entrada al que se aplica el muestreo en cascada estable. | MODEL | Sí | - |
| `desplazamiento` | El valor de desplazamiento que se aplica a los parámetros de muestreo (por defecto: 2.0). | FLOAT | Sí | 0.0 - 100.0 (step 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con el muestreo en cascada estable aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/es.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
