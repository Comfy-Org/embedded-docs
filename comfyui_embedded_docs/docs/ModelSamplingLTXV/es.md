# MuestreoDeModeloLTXV

El nodo ModelSamplingLTXV aplica parámetros de muestreo avanzados a un modelo según el número de tokens. Calcula un valor de desplazamiento mediante una interpolación lineal entre los valores de desplazamiento base y máximo, y el cálculo depende del número de tokens en el latente de entrada. A continuación, el nodo crea una configuración especializada de muestreo del modelo y la aplica al modelo de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de entrada al que se le aplicarán los parámetros de muestreo | MODEL | Sí | - |
| `desplazamiento_max` | El valor de desplazamiento máximo utilizado en el cálculo de interpolación lineal (valor predeterminado: 2.05) | FLOAT | Sí | 0.0 a 100.0 (paso: 0.01) |
| `desplazamiento_base` | El valor de desplazamiento base utilizado en el cálculo de interpolación lineal (valor predeterminado: 0.95) | FLOAT | Sí | 0.0 a 100.0 (paso: 0.01) |
| `latente` | Entrada latente opcional utilizada para determinar el número de tokens para el cálculo del desplazamiento. Si no se proporciona, se usa un número de tokens predeterminado de 4096 | LATENT | No | - |

El valor de desplazamiento se calcula interpolando entre `base_shift` y `max_shift` en un rango de tokens de 1024 a 4096. Cuando se suministra un `latent`, el número de tokens se calcula a partir del producto de sus dimensiones espaciales (como alto y ancho). Si no se proporciona ningún `latent`, el número de tokens se establece en 4096 de forma predeterminada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con los parámetros de muestreo aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/es.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
