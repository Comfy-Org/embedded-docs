# VOIDSampler

## Resumen

El nodo VOIDSampler proporciona un método de muestreo DDIM especializado diseñado específicamente para modelos de inpainting VOID. Implementa el mismo proceso de eliminación de ruido (denoising) utilizado durante el entrenamiento de los modelos VOID, sin el escalado de ruido que aplican los KSamplers estándar. Este nodo está diseñado para usarse con los nodos SamplerCustom o SamplerCustomAdvanced, y debe combinarse con RandomNoise o VOIDWarpedNoiseSource.

## Entradas

Este nodo no tiene parámetros de entrada configurables. Es un sampler autocontenido que aplica un algoritmo de muestreo DDIM fijo.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| *Sin entradas* | Este nodo no acepta ningún parámetro de entrada. | - | - | - |

Nota: Los modelos VOID se entrenaron con el diffusers CogVideoXDDIMScheduler, que opera en el espacio alfa donde la desviación estándar de entrada es aproximadamente 1. El KSampler estándar aplica un escalado de ruido que multiplica por aproximadamente 4500x, lo cual es incompatible con este entrenamiento. El VOIDSampler omite ese escalado e implementa la regla de actualización DDIM directamente mediante la conversión de sigma a alfa.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `SAMPLER` | Un objeto sampler que implementa el algoritmo DDIM de VOID, listo para conectarse a los nodos SamplerCustom o SamplerCustomAdvanced. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/es.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
