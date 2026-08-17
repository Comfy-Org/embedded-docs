# MuestreoDeModeloLTXV

El nodo ModelSamplingLTXV aplica parámetros de muestreo avanzados a un modelo según el recuento de tokens. Calcula un valor de desplazamiento mediante una interpolación lineal entre los valores de desplazamiento base y máximo, dependiendo el cálculo del número de tokens en el latent de entrada. A continuación, el nodo crea una configuración de muestreo de modelo especializada y la aplica al modelo de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de entrada al que se le aplicarán los parámetros de muestreo | MODEL | Sí | - |
| `max_shift` | El valor de desplazamiento máximo utilizado en el cálculo de interpolación lineal. El valor de desplazamiento es igual a este máximo en 4096 tokens (por defecto: 2.05) | FLOAT | Sí | 0.0 to 100.0 |
| `base_shift` | El valor de desplazamiento base utilizado en el cálculo de interpolación lineal. El valor de desplazamiento es igual a esta base en 1024 tokens (por defecto: 0.95) | FLOAT | Sí | 0.0 to 100.0 |
| `latent` | Entrada latente opcional utilizada para determinar el recuento de tokens para el cálculo del desplazamiento. El recuento de tokens es el producto de las dimensiones espaciales de las muestras latentes. Si no se proporciona, se utiliza un recuento de tokens predeterminado de 4096 | LATENT | No | - |

Nota: El valor de desplazamiento se calcula mediante interpolación lineal entre `base_shift` en 1024 tokens y `max_shift` en 4096 tokens. Cuando no se proporciona `latent`, el recuento de tokens predeterminado de 4096 hace que el desplazamiento sea igual a `max_shift`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con los parámetros de muestreo aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/es.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
