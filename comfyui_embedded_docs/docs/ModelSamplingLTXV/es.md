> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/es.md)

El nodo ModelSamplingLTXV aplica parámetros de muestreo avanzados a un modelo basándose en el recuento de tokens. Calcula un valor de desplazamiento utilizando una interpolación lineal entre los valores de desplazamiento base y máximo, donde el cálculo depende del número de tokens en el latente de entrada. Luego, el nodo crea una configuración de muestreo de modelo especializada y la aplica al modelo de entrada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de entrada al que se aplicarán los parámetros de muestreo |
| `max_shift` | FLOAT | No | 0.0 a 100.0 | El valor de desplazamiento máximo utilizado en el cálculo (por defecto: 2.05) |
| `base_shift` | FLOAT | No | 0.0 a 100.0 | El valor de desplazamiento base utilizado en el cálculo (por defecto: 0.95) |
| `latent` | LATENT | No | - | Entrada latente opcional utilizada para determinar el recuento de tokens para el cálculo de desplazamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con los parámetros de muestreo aplicados |