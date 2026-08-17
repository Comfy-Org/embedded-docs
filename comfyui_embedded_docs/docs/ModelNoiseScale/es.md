# Escala de Ruido del Modelo

Este nodo ajusta la escala de ruido utilizada durante el muestreo del modelo. Permite establecer un valor específico de escala de ruido, que controla la cantidad de ruido aplicado al proceso de muestreo del modelo. El nodo clona el modelo y actualiza su configuración de muestreo con la nueva escala de ruido, manteniendo la configuración de desplazamiento y multiplicador existente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le aplica el ajuste de escala de ruido. | MODEL | Sí | - |
| `noise_scale` | Escala de ruido de entrenamiento absoluta. Por ejemplo, HiDream-O1 base: 8.0, dev: 7.5. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 64.0 (paso: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL` | El modelo modificado con la nueva escala de ruido aplicada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/es.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
