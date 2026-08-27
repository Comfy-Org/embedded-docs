# ProgramadorAlineaTusPasos

El nodo AlignYourStepsScheduler genera valores sigma para el proceso de eliminación de ruido según diferentes tipos de modelo. Calcula los niveles de ruido apropiados para cada paso del proceso de muestreo y ajusta el número total de pasos de acuerdo con el parámetro `denoise`. Esto ayuda a alinear los pasos de muestreo con los requisitos específicos de los diferentes modelos de difusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `tipo_modelo` | Especifica el tipo de modelo a utilizar para el cálculo de sigma (predeterminado: "SD1") | COMBO | Sí | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `pasos` | El número total de pasos de muestreo a generar (predeterminado: 10) | INT | Sí | 1 a 10000 |
| `desruido` | Controla cuánto eliminar el ruido de la imagen, donde 1.0 utiliza todos los pasos y los valores más bajos utilizan menos pasos (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

Nota: Cada tipo de modelo tiene un cronograma de niveles de ruido integrado que contiene 11 valores sigma (para 10 pasos). Cuando `denoise` es 0.0, el nodo devuelve un tensor de sigma vacío. Cuando `denoise` está entre 0.0 y 1.0, el número efectivo de pasos se calcula como `round(steps × denoise)`, y solo se utiliza la última parte correspondiente del cronograma de sigma. Si el valor de `steps` solicitado no coincide con la longitud del cronograma integrado, los niveles de ruido se interpolan log-linealmente para que coincidan con el número de pasos solicitado. El valor final de sigma siempre se establece en 0.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | Devuelve los valores sigma calculados para el proceso de eliminación de ruido | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/es.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
