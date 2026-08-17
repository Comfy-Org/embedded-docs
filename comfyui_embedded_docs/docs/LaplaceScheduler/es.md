# LaplaceScheduler

El nodo LaplaceScheduler genera una secuencia de valores sigma que sigue una distribución de Laplace para usar en el muestreo de difusión. Crea un programa de niveles de ruido que disminuyen gradualmente desde un valor máximo hasta un mínimo, utilizando parámetros de la distribución de Laplace para controlar la progresión. Este programador se utiliza comúnmente en flujos de trabajo de muestreo personalizados para definir el programa de ruido para modelos de difusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `steps` | Número de pasos de muestreo en el programa (por defecto: 20) | INT | Sí | 1 a 10000 |
| `sigma_max` | Valor sigma máximo al inicio del programa (por defecto: 14.614642) | FLOAT | Sí | 0.0 a 5000.0 |
| `sigma_min` | Valor sigma mínimo al final del programa (por defecto: 0.0291675) | FLOAT | Sí | 0.0 a 5000.0 |
| `mu` | Parámetro de media para la distribución de Laplace (por defecto: 0.0) | FLOAT | Sí | -10.0 a 10.0 |
| `beta` | Parámetro de escala para la distribución de Laplace (por defecto: 0.5) | FLOAT | Sí | 0.0 a 10.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `SIGMAS` | Una secuencia de valores sigma que sigue un programa de distribución de Laplace | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/es.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
