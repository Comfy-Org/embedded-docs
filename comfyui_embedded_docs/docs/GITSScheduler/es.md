# GITSScheduler

El nodo GITSScheduler genera sigmas de programación de ruido para el método de muestreo GITS (Generative Iterative Time Steps). Calcula los valores de sigma basándose en un parámetro de coeficiente y el número de pasos, con un factor de denoising opcional que puede reducir el número total de pasos utilizados. El nodo utiliza niveles de ruido predefinidos e interpolación para crear la programación final de sigmas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `coef` | El valor del coeficiente que controla la curva de la programación de ruido (por defecto: 1.20). El valor se redondea a dos decimales y selecciona qué tabla de niveles de ruido predefinida se utiliza. | FLOAT | Sí | 0.80 - 1.50 (paso 0.05) |
| `pasos` | El número total de pasos de muestreo para generar los sigmas (por defecto: 10) | INT | Sí | 2 - 1000 |
| `denoise` | Factor de denoising que reduce el número de pasos utilizados (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Cuando `denoise` es 0.0 o menor, el nodo devuelve un tensor vacío. Cuando `denoise` es menor que 1.0, el número real de pasos utilizados se calcula como `round(steps * denoise)`, y solo se conserva la última parte correspondiente de la programación. Para pasos entre 2 y 20, el nodo selecciona una programación de ruido predefinida coincidente. Para pasos mayores de 20, el nodo utiliza interpolación log-lineal para extender los niveles de ruido predefinidos al número deseado de pasos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `sigmas` | Los valores de sigma generados para la programación de ruido. Para N pasos, se devuelven N+1 valores de sigma, y el último sigma se establece en 0. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/es.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
