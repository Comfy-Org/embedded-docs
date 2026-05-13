> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/es.md)

El nodo LaplaceScheduler genera una secuencia de valores sigma que siguen una distribución de Laplace para su uso en el muestreo de difusión. Crea un programa de niveles de ruido que disminuye gradualmente desde un valor máximo hasta uno mínimo, utilizando parámetros de la distribución de Laplace para controlar la progresión. Este programador se utiliza comúnmente en flujos de trabajo de muestreo personalizados para definir el programa de ruido de los modelos de difusión.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pasos` | INT | Sí | 1 a 10000 | Número de pasos de muestreo en el programa (predeterminado: 20) |
| `sigma_max` | FLOAT | Sí | 0.0 a 5000.0 | Valor sigma máximo al inicio del programa (predeterminado: 14.614642) |
| `sigma_min` | FLOAT | Sí | 0.0 a 5000.0 | Valor sigma mínimo al final del programa (predeterminado: 0.0291675) |
| `mu` | FLOAT | Sí | -10.0 a 10.0 | Parámetro de media para la distribución de Laplace (predeterminado: 0.0) |
| `beta` | FLOAT | Sí | 0.0 a 10.0 | Parámetro de escala para la distribución de Laplace (predeterminado: 0.5) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Una secuencia de valores sigma que siguen un programa de distribución de Laplace |

---
**Source fingerprint (SHA-256):** `9d8cacb93d0bb1872a368821fd3cad5d6d373817a923436af9f62a7648d5d735`
