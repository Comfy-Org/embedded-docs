> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/es.md)

El nodo GITSScheduler genera programaciones de ruido sigmas para el método de muestreo GITS (Generative Iterative Time Steps). Calcula los valores sigma basándose en un parámetro de coeficiente y número de pasos, con un factor de eliminación de ruido opcional que puede reducir el total de pasos utilizados. El nodo utiliza niveles de ruido predefinidos e interpolación para crear la programación sigma final.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `coef` | FLOAT | Sí | 0.80 - 1.50 | El valor del coeficiente que controla la curva de la programación de ruido (valor por defecto: 1.20) |
| `pasos` | INT | Sí | 2 - 1000 | El número total de pasos de muestreo para los cuales generar sigmas (valor por defecto: 10) |
| `denoise` | FLOAT | Sí | 0.0 - 1.0 | Factor de eliminación de ruido que reduce el número de pasos utilizados (valor por defecto: 1.0) |

**Nota:** Cuando `denoise` se establece en 0.0, el nodo devuelve un tensor vacío. Cuando `denoise` es menor que 1.0, el número real de pasos utilizados se calcula como `round(steps * denoise)`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Los valores sigma generados para la programación de ruido |
