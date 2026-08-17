# StableCascade_StageB_Conditioning

El nodo `StableCascade_StageB_Conditioning` prepara datos de condicionamiento para la generación de Stable Cascade Stage B, combinando la información de condicionamiento existente con representaciones latentes previas de la Etapa C. Modifica cada entrada de condicionamiento para incluir las muestras latentes de la Etapa C, lo que permite que el proceso de generación aproveche la información previa para obtener resultados más coherentes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `conditioning` | Los datos de condicionamiento que se modificarán con la información previa de la Etapa C. | CONDITIONING | Sí | - |
| `stage_c` | La representación latente de la Etapa C que contiene muestras previas para el condicionamiento. | LATENT | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento modificados con la información previa de la Etapa C integrada. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
