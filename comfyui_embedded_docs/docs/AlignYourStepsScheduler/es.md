# ProgramadorAlineaTusPasos

El nodo AlignYourStepsScheduler crea los valores sigma utilizados durante el proceso de eliminación de ruido (denoising) para diferentes tipos de modelos de difusión. Selecciona los niveles de ruido base para el modelo elegido, ajusta el número de pasos según el ajuste `denoise` y devuelve un tensor de valores sigma que termina en 0.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_type` | El tipo de modelo utilizado para seleccionar los niveles de ruido base (predeterminado: "SD1") | COMBO | Sí | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | El número total de pasos de muestreo a generar (predeterminado: 10) | INT | Sí | 1 a 10000 |
| `denoise` | Controla cuánto del proceso de muestreo se utiliza: 1.0 usa todos los pasos, los valores más bajos usan menos pasos, y 0.0 devuelve un tensor sigma vacío (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | Los valores sigma calculados para el proceso de eliminación de ruido. Si `denoise` es 0.0, se devuelve un tensor vacío. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/es.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
