> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/es.md)

El nodo LaplaceScheduler genera una secuencia de valores sigma que sigue una distribución de Laplace para su uso en el muestreo de difusión. Crea un programa de niveles de ruido que disminuyen gradualmente desde un valor máximo hasta un valor mínimo, utilizando parámetros de distribución de Laplace para controlar la progresión. Este programador se utiliza comúnmente en flujos de trabajo de muestreo personalizados para definir el programa de ruido para modelos de difusión.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pasos` | INT | Sí | 1 a 10000 | Número de pasos de muestreo en el programa (valor por defecto: 20) |
| `sigma_max` | FLOAT | Sí | 0.0 a 5000.0 | Valor sigma máximo al inicio del programa (valor por defecto: 14.614642) |
| `sigma_min` | FLOAT | Sí | 0.0 a 5000.0 | Valor sigma mínimo al final del programa (valor por defecto: 0.0291675) |
| `mu` | FLOAT | Sí | -10.0 a 10.0 | Parámetro de media para la distribución de Laplace (valor por defecto: 0.0) |
| `beta` | FLOAT | Sí | 0.0 a 10.0 | Parámetro de escala para la distribución de Laplace (valor por defecto: 0.5) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Una secuencia de valores sigma que sigue un programa de distribución de Laplace |
