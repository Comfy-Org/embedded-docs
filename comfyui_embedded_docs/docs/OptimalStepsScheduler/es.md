# OptimalStepsScheduler

El nodo OptimalStepsScheduler calcula los sigmas del programa de ruido para modelos de difusión según el tipo de modelo seleccionado y la configuración de pasos. Ajusta el número total de pasos de acuerdo con el parámetro de denoising e interpola los niveles de ruido para que coincidan con la cantidad de pasos solicitada. El nodo devuelve una secuencia de valores sigma que determinan los niveles de ruido utilizados durante el proceso de muestreo de difusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_type` | El tipo de modelo de difusión a utilizar para el cálculo de los niveles de ruido | COMBO | Sí | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | El número total de pasos de muestreo a calcular (predeterminado: 20) | INT | Sí | 3-1000 |
| `denoise` | Controla la fuerza de eliminación de ruido, que ajusta el número efectivo de pasos (predeterminado: 1.0) | FLOAT | Sí | 0.0-1.0 |

**Nota:** Cuando `denoise` se establece en un valor menor que 1.0, el nodo calcula los pasos efectivos como `steps * denoise`. Si `denoise` se establece en 0.0, el nodo devuelve un tensor vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | Una secuencia de valores sigma que representan el programa de ruido para el muestreo de difusión | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/es.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
