# StableCascade_StageB_Conditioning

El nodo StableCascade_StageB_Conditioning prepara los datos de condicionamiento para la generación de Stable Cascade Stage B al combinar la información de condicionamiento existente con las representaciones latentes previas de Stage C. Copia cada entrada de condicionamiento y añade las muestras latentes de Stage C, lo que permite que el proceso de generación aproveche la información previa para obtener resultados más coherentes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento que se modificarán con la información previa de Stage C | CONDITIONING | Sí | - |
| `etapa_c` | La representación latente de Stage C que contiene muestras previas para el condicionamiento | LATENT | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento modificados con la información previa de Stage C integrada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
