# Escala de Ruido del Modelo

Este nodo ajusta la escala de ruido utilizada durante el muestreo del modelo. Permite establecer un valor específico de escala de ruido, que controla la cantidad de ruido aplicada al proceso de muestreo del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le aplicará el ajuste de escala de ruido. | MODEL | Sí | - |
| `escala_ruido` | Escala de ruido de entrenamiento absoluta. Por ejemplo, HiDream-O1 base: 8.0, dev: 7.5. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 64.0 (paso: 0.01) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `MODEL` | El modelo modificado con la nueva escala de ruido aplicada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/es.md)

---
**Source fingerprint (SHA-256):** `37b77a5d65fb872f45be8ffa4efb65037bc7459bb001babaaf6b526a9a735190`
