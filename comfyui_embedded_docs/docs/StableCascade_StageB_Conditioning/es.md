# StableCascade_StageB_Conditioning

El nodo `StableCascade_StageB_Conditioning` prepara los datos de condicionamiento para la generación de la Etapa B de Stable Cascade, combinando la información de condicionamiento existente con representaciones latentes previas de la Etapa C. Modifica los datos de condicionamiento para incluir las muestras latentes de la Etapa C, lo que permite que el proceso de generación aproveche la información previa para obtener resultados más coherentes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento que se modificarán con la información previa de la Etapa C | CONDITIONING | Sí | - |
| `etapa_c` | La representación latente de la Etapa C que contiene muestras previas para el condicionamiento | LATENT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento modificados con la información previa de la Etapa C integrada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
