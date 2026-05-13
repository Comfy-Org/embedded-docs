> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/es.md)

Implementa el método de Escalado Epsilon del artículo de investigación "Elucidating the Exposure Bias in Diffusion Models". Este método mejora la calidad de las muestras al escalar el ruido predicho durante el proceso de muestreo. Utiliza un programa uniforme para mitigar el sesgo de exposición en los modelos de difusión.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se le aplicará el escalado epsilon |
| `scaling_factor` | FLOAT | No | 0.5 - 1.5 | Factor utilizado para escalar el ruido predicho (predeterminado: 1.005) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo con el escalado epsilon aplicado |