> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon> Scaling/es.md)

Este nodo implementa el método de Escalado de Épsilon del artículo de investigación "Elucidating the Exposure Bias in Diffusion Models". Funciona escalando el ruido predicho durante el proceso de muestreo para ayudar a reducir el sesgo de exposición, lo que puede conducir a una mejora en la calidad de las imágenes generadas. Esta implementación utiliza el "programación uniforme" recomendada por el artículo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará el parche de escalado de épsilon. |
| `scaling_factor` | FLOAT | No | 0.5 - 1.5 | El factor por el cual se escala el ruido predicho. Un valor mayor que 1.0 reduce el ruido, mientras que un valor menor que 1.0 lo aumenta (valor por defecto: 1.005). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | Una versión parcheada del modelo de entrada con la función de escalado de épsilon aplicada a su proceso de muestreo. |
