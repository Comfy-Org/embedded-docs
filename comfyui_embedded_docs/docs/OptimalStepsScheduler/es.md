> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/es.md)

El nodo OptimalStepsScheduler calcula los sigmas del programa de ruido para modelos de difusión según el tipo de modelo seleccionado y la configuración de pasos. Ajusta el número total de pasos de acuerdo con el parámetro de eliminación de ruido (`denoise`) e interpola los niveles de ruido para que coincidan con la cantidad de pasos solicitada. El nodo devuelve una secuencia de valores sigma que determinan los niveles de ruido utilizados durante el proceso de muestreo de difusión.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_type` | COMBO | Sí | "FLUX"<br>"Wan"<br>"Chroma" | El tipo de modelo de difusión a utilizar para el cálculo del nivel de ruido |
| `pasos` | INT | Sí | 3-1000 | El número total de pasos de muestreo a calcular (predeterminado: 20) |
| `eliminar ruido` | FLOAT | No | 0.0-1.0 | Controla la intensidad de eliminación de ruido, que ajusta el número efectivo de pasos (predeterminado: 1.0) |

**Nota:** Cuando `denoise` se establece en un valor menor a 1.0, el nodo calcula los pasos efectivos como `steps * denoise`. Si `denoise` se establece en 0.0, el nodo devuelve un tensor vacío.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `sigmas` | SIGMAS | Una secuencia de valores sigma que representa el programa de ruido para el muestreo de difusión |

---
**Source fingerprint (SHA-256):** `4379171dc6d525a1ece514fdd11a95bfd92ed0c8b301f69ca718c1a3256b9590`
