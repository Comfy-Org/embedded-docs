> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/es.md)

El nodo GITSScheduler genera sigmas de programación de ruido para el método de muestreo GITS (Pasos de Tiempo Iterativos Generativos). Calcula valores sigma basados en un parámetro de coeficiente y número de pasos, con un factor de eliminación de ruido opcional que puede reducir los pasos totales utilizados. El nodo utiliza niveles de ruido predefinidos e interpolación para crear la programación sigma final.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `coeff` | FLOAT | Sí | 0.80 - 1.50 | El valor del coeficiente que controla la curva de programación de ruido (predeterminado: 1.20) |
| `steps` | INT | Sí | 2 - 1000 | El número total de pasos de muestreo para generar sigmas (predeterminado: 10) |
| `denoise` | FLOAT | Sí | 0.0 - 1.0 | Factor de eliminación de ruido que reduce el número de pasos utilizados (predeterminado: 1.0) |

**Nota:** Cuando `denoise` se establece en 0.0, el nodo devuelve un tensor vacío. Cuando `denoise` es menor que 1.0, el número real de pasos utilizados se calcula como `round(steps * denoise)`. Para pasos mayores a 20, el nodo utiliza interpolación log-lineal para extender los niveles de ruido predefinidos al número deseado de pasos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `sigmas` | SIGMAS | Los valores sigma generados para la programación de ruido |

---
**Source fingerprint (SHA-256):** `b81b85f95236276822429ec7cbc90204c6f4f86ea3e89ed8b7c2aea40597fea9`
