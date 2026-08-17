# TSR - Reajuste de Puntuación Temporal

Este nodo aplica el reescalado temporal de puntuaciones (TSR) a un modelo de difusión. Modifica el comportamiento de muestreo del modelo reescalando el ruido o la puntuación predichos durante el proceso de eliminación de ruido, lo que puede dirigir la diversidad de la salida generada. Esto se implementa como una función posterior a CFG (Classifier-Free Guidance).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión que se va a parchear con la función TSR. | MODEL | Sí | - |
| `tsr_k` | Controla la fuerza del reescalado. Un valor más bajo de k produce resultados más detallados; un valor más alto produce resultados más suaves en la generación de imágenes. Establecer k = 1 desactiva el reescalado. (por defecto: 0.95) | FLOAT | No | 0.01 - 100.0 |
| `tsr_sigma` | Controla la anticipación con la que el reescalado surte efecto. Los valores más grandes surten efecto antes. (por defecto: 1.0) | FLOAT | No | 0.01 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `patched_model` | El modelo de entrada, ahora parcheado con la función de reescalado temporal de puntuaciones aplicada a su proceso de muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/es.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
