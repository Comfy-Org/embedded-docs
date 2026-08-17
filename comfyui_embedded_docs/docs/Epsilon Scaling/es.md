# Escalado Épsilon

Este nodo implementa el método de escalado de épsilon (Epsilon Scaling) del artículo de investigación "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). Funciona escalando el ruido predicho durante el proceso de muestreo para ayudar a reducir el sesgo de exposición, lo que puede conducir a una mejora en la calidad de las imágenes generadas. Esta implementación utiliza el «programa uniforme» (uniform schedule) recomendado por el artículo por su practicidad y efectividad.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le aplicará el parche de escalado de épsilon. | MODEL | Sí | - |
| `scaling_factor` | El factor por el cual se escala el ruido predicho. Un valor mayor que 1.0 reduce el ruido predicho, mientras que un valor menor que 1.0 lo aumenta (por defecto: 1.005). | FLOAT | Sí | 0.5 - 1.5 (paso: 0.001) |

Nota: El `scaling_factor` está protegido contra un valor de cero para evitar la división por cero. La interfaz de usuario impone un mínimo de 0.5, por lo que esto no puede ocurrir mediante el uso normal.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | Una copia parcheada del modelo de entrada con la función de escalado de épsilon aplicada a su proceso de muestreo. El modelo original queda sin modificaciones. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/es.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
