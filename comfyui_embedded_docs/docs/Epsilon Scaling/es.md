> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/es.md)

Implementa el método Epsilon Scaling del artículo de investigación "Elucidating the Exposure Bias in Diffusion Models". Este método mejora la calidad de las muestras escalando el ruido predicho durante el proceso de muestreo. Utiliza un programa uniforme para mitigar el sesgo de exposición en los modelos de difusión.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar el escalado épsilon |
| `scaling_factor` | FLOAT | No | 0.5 - 1.5 | El factor utilizado para escalar el ruido predicho (por defecto: 1.005) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con escalado épsilon aplicado |