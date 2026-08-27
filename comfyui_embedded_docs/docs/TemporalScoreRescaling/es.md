# TSR - Reajuste de Puntuación Temporal

Este nodo aplica el reescalado de puntuación temporal (TSR, por sus siglas en inglés) a un modelo de difusión. Modifica el comportamiento de muestreo del modelo reescalando el ruido o puntuación predicho durante el proceso de eliminación de ruido, lo que puede orientar la diversidad de la salida generada. Esto se implementa como una función post-CFG (Classifier-Free Guidance).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión que se va a parchear con la función TSR. | MODEL | Sí | - |
| `tsr_k` | Controla la fuerza del reescalado. Un valor de k más bajo produce resultados más detallados; un valor de k más alto produce resultados más suaves en la generación de imágenes. Establecer k = 1 desactiva el reescalado. (predeterminado: 0.95) | FLOAT | Sí | 0.01 - 100.0 |
| `tsr_sigma` | Controla qué tan temprano surte efecto el reescalado. Los valores más grandes surten efecto antes. (predeterminado: 1.0) | FLOAT | Sí | 0.01 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `modelo_modificado` | El modelo de entrada, ahora parcheado con la función de reescalado de puntuación temporal aplicada a su proceso de muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/es.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
