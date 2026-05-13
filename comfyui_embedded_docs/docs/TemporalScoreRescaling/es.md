> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/es.md)

Este nodo aplica Re-escalado de Puntuación Temporal (TSR) a un modelo de difusión. Modifica el comportamiento de muestreo del modelo re-escalando el ruido o la puntuación predicha durante el proceso de eliminación de ruido, lo que puede dirigir la diversidad del resultado generado. Se implementa como una función posterior a CFG (Guía Libre de Clasificador).

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión al que se le aplicará el parche con la función TSR. |
| `tsr_k` | FLOAT | No | 0.01 - 100.0 | Controla la intensidad del re-escalado. Un valor k más bajo produce resultados más detallados; un valor k más alto produce resultados más suaves en la generación de imágenes. Establecer k = 1 desactiva el re-escalado. (valor predeterminado: 0.95) |
| `tsr_sigma` | FLOAT | No | 0.01 - 100.0 | Controla qué tan temprano surte efecto el re-escalado. Los valores más grandes surten efecto más temprano. (valor predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `patched_model` | MODEL | El modelo de entrada, ahora parcheado con la función de Re-escalado de Puntuación Temporal aplicada a su proceso de muestreo. |

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`
