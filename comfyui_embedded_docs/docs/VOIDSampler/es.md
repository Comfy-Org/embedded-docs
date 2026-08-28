# VOIDSampler

VOIDSampler es un muestreador DDIM especializado para modelos de inpainting VOID. Implementa el mismo proceso de eliminación de ruido con el que fue entrenado VOID, sin la escala de ruido que aplican los KSampler estándar. Use este nodo con SamplerCustom o SamplerCustomAdvanced, junto con RandomNoise o VOIDWarpedNoiseSource.

## Entradas

Este nodo no tiene parámetros de entrada configurables. Es un muestreador autónomo que aplica un algoritmo de muestreo DDIM fijo.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| *Sin entradas* | Este nodo no acepta ningún parámetro de entrada. | - | - | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `SAMPLER` | Un objeto de muestreador que implementa el algoritmo DDIM de VOID, listo para conectarse a los nodos SamplerCustom o SamplerCustomAdvanced. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/es.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
