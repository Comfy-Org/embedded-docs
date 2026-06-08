El nodo AlignYourStepsScheduler genera valores sigma para el proceso de eliminación de ruido basándose en diferentes tipos de modelo. Calcula los niveles de ruido apropiados para cada paso del proceso de muestreo y ajusta el número total de pasos según el parámetro de eliminación de ruido. Esto ayuda a alinear los pasos de muestreo con los requisitos específicos de diferentes modelos de difusión.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tipo_modelo` | Especifica el tipo de modelo a utilizar para el cálculo de sigma (predeterminado: "SD1") | STRING | Sí | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `pasos` | El número total de pasos de muestreo a generar (predeterminado: 10) | INT | Sí | 1 a 10000 |
| `desruido` | Controla cuánto eliminar el ruido de la imagen, donde 1.0 utiliza todos los pasos y valores más bajos utilizan menos pasos (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas` | Devuelve los valores sigma calculados para el proceso de eliminación de ruido | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/es.md)

---
**Source fingerprint (SHA-256):** `112535f9c100ca4e13dcd733e7a371c00c203b38d77bd10beb4355ba3512ec66`
