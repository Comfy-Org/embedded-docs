# GITSScheduler

El nodo GITSScheduler genera el cronograma de sigma (nivel de ruido) utilizado por el método de muestreo GITS. Selecciona una tabla de niveles de ruido predefinida según el parámetro `coeff` y el número de `steps`, recortando opcionalmente el cronograma cuando se usa un valor de `denoise` inferior a 1.0.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `coeff` | El coeficiente que selecciona qué tabla de niveles de ruido predefinida se utiliza para construir el cronograma. El valor se redondea a 2 decimales (por defecto: 1.20) | FLOAT | Sí | 0.80 - 1.50 |
| `steps` | El número total de pasos de muestreo para generar sigmas (por defecto: 10) | INT | Sí | 2 - 1000 |
| `denoise` | Factor de denoising que reduce el número de pasos utilizados (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Cuando `denoise` se establece en 0.0, el nodo devuelve un tensor vacío. Cuando `denoise` es menor que 1.0, el número real de pasos utilizados se calcula como `round(steps * denoise)`. Para pasos hasta 20, el nodo usa niveles de ruido predefinidos directamente; para pasos mayores de 20, usa interpolación log-lineal para extender los niveles de ruido predefinidos al número deseado de pasos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `sigmas` | Los valores sigma generados para el cronograma de ruido | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/es.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
