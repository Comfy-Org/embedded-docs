# OptimalStepsScheduler

El nodo OptimalStepsScheduler crea un programa de ruido (una secuencia de valores sigma) para usarse durante el muestreo de difusión. Selecciona los niveles de ruido base según el tipo de modelo elegido, ajusta el programa cuando el denoising se aplica parcialmente e interpola los niveles para que los sigmas devueltos coincidan con el número de pasos solicitado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_type` | El tipo de modelo de difusión que se usará para el cálculo del nivel de ruido. | COMBO | Sí | "FLUX"<br>"Wan"<br>"Chroma" |
| `pasos` | El número total de pasos de muestreo a calcular (predeterminado: 20). | INT | Sí | 3 a 1000 |
| `eliminar ruido` | Controla la intensidad del denoising, lo que ajusta el número efectivo de pasos (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

**Nota:** Cuando `denoise` es menor que 1.0, el nodo usa `round(steps * denoise)` como el número total de pasos efectivos. Si `denoise` es 0.0, el nodo devuelve un tensor vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | Una secuencia de valores sigma que representa el programa de ruido para el muestreo de difusión. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/es.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
