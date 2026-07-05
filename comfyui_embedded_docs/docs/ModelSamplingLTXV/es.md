# MuestreoDeModeloLTXV

El nodo ModelSamplingLTXV aplica parámetros de muestreo avanzados a un modelo basándose en el recuento de tokens. Calcula un valor de desplazamiento mediante una interpolación lineal entre valores de desplazamiento base y máximo, donde el cálculo depende del número de tokens en el latente de entrada. Luego, el nodo crea una configuración de muestreo de modelo especializada y la aplica al modelo de entrada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de entrada al que se aplicarán los parámetros de muestreo | MODEL | Sí | - |
| `desplazamiento_max` | El valor máximo de desplazamiento utilizado en el cálculo de interpolación lineal (predeterminado: 2.05) | FLOAT | Sí | 0.0 a 100.0 |
| `desplazamiento_base` | El valor base de desplazamiento utilizado en el cálculo de interpolación lineal (predeterminado: 0.95) | FLOAT | Sí | 0.0 a 100.0 |
| `latente` | Entrada latente opcional utilizada para determinar el recuento de tokens para el cálculo de desplazamiento. Si no se proporciona, se utiliza un recuento de tokens predeterminado de 4096 | LATENT | No | - |


| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con los parámetros de muestreo aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/es.md)

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
