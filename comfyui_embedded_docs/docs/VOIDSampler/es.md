> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/es.md)

# Descripción General

El nodo VOIDSampler proporciona un método de muestreo DDIM especializado diseñado específicamente para modelos de inpainting VOID. Implementa el mismo proceso de eliminación de ruido utilizado durante el entrenamiento del modelo VOID, sin el escalado de ruido que aplican los KSamplers estándar. Este nodo está diseñado para usarse con los nodos SamplerCustom o SamplerCustomAdvanced, y debe combinarse con RandomNoise o VOIDWarpedNoiseSource.

## Entradas

Este nodo no tiene parámetros de entrada configurables. Es un muestreador autocontenido que aplica un algoritmo de muestreo DDIM fijo.

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| *Sin entradas* | - | - | - | Este nodo no acepta ningún parámetro de entrada. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `SAMPLER` | SAMPLER | Un objeto muestreador que implementa el algoritmo VOID DDIM, listo para conectarse a los nodos SamplerCustom o SamplerCustomAdvanced. |