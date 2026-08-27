# LTXVModalityGuidance

Este nodo aplica guía multimodal (audio-video) a un modelo LTXV-AV. Durante el muestreo, ejecuta una pasada adicional hacia adelante por paso con las conexiones de atención cruzada de audio a video y de video a audio deshabilitadas, y luego empuja el resultado hacia la predicción acoplada. Esto fortalece la sincronización audiovisual, como la sincronización de labios. El valor predeterminado de referencia para `modality_scale` es 3.0; configurarlo en 1.0 desactiva la pasada adicional.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo base al que se le aplicará la guía multimodal. Se clona internamente, dejando el modelo original sin cambios. | MODEL | Sí | - |
| `modality_scale` | Fuerza de la guía de acoplamiento audio-video. El valor predeterminado es 3.0. Configúrelo en 1.0 para desactivar la pasada adicional hacia adelante. | FLOAT | Sí | 1.0 a 100.0 (default: 3.0) |
| `porcentaje_inicio` | El punto del proceso de muestreo, como porcentaje de 0.0 a 1.0, en el que comienza la guía multimodal. El valor predeterminado es 0.0. | FLOAT | Sí | 0.0 a 1.0 (default: 0.0) |
| `porcentaje_fin` | El punto del proceso de muestreo, como porcentaje de 0.0 a 1.0, en el que termina la guía multimodal. El valor predeterminado es 1.0. | FLOAT | Sí | 0.0 a 1.0 (default: 1.0) |

La guía se aplica solo para los pasos de muestreo cuyos valores de sigma se encuentran dentro del rango definido por `start_percent` y `end_percent`. Fuera de este rango, el nodo devuelve el resultado denoizado sin cambios. Un `modality_scale` de 1.0 también desactiva por completo la pasada adicional hacia adelante.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `model` | El modelo clonado con una función de guía post-CFG adjunta. Este modelo modificado aplica guía multimodal durante el muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/es.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
