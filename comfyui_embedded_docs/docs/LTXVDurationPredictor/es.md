# LTXV Duration Predictor

Este nodo predice la duración natural de la toma para un prompt utilizando una cabeza de duración LTX 2.4. Convierte la duración predicha en un número de fotogramas que se ajusta a la cuadrícula de fotogramas de la VAE, utilizando la velocidad de fotogramas proporcionada y los límites de duración mínima/máxima.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo utilizado para preprocesar las incrustaciones de texto y ejecutar la cabeza de duración. | MODEL | Sí | N/A |
| `positivo` | El condicionamiento que proporciona las incrustaciones de texto del prompt y los metadatos para la predicción de duración. | CONDITIONING | Sí | N/A |
| `duration_head` | Cabeza de duración LTX 2.4 cargada con ModelPatchLoader. Debe ser una cabeza de duración LTX. | MODEL_PATCH | Sí | N/A |
| `frecuencia_de_fotogramas` | Velocidad de fotogramas en fotogramas por segundo utilizada para convertir segundos a fotogramas (predeterminado: 24.0). | FLOAT | Sí | 1.0 a 120.0 |
| `segundos_mínimos` | Duración mínima en segundos utilizada al convertir la predicción a un número de fotogramas (predeterminado: 1.0). | FLOAT | Sí | 0.5 a 120.0 |
| `segundos_máximos` | Duración máxima en segundos utilizada al convertir la predicción a un número de fotogramas (predeterminado: 20.0). | FLOAT | Sí | 0.5 a 120.0 |

Nota: La entrada `duration_head` debe ser una cabeza de duración LTX 2.4 cargada con ModelPatchLoader. Si el parche de modelo conectado no es una cabeza de duración LTX, el nodo lanza un ValueError.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `num_frames` | La duración predicha convertida a un número de fotogramas y ajustada a la cuadrícula de fotogramas 8k+1 de la VAE. | INT |
| `segundos` | Duración predicha en bruto (sin limitar). Este es el valor antes de ajustarse a la cuadrícula de fotogramas. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/es.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
