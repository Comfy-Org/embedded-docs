# VOIDWarpedNoiseSource

## Resumen

Este nodo convierte un LATENT (como la salida del nodo VOIDWarpedNoise) en una fuente de NOISE. Esto le permite usar el ruido deformado con el nodo SamplerCustomAdvanced para una generación de imágenes más controlada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `warped_noise` | Ruido deformado latente de VOIDWarpedNoise | LATENT | Sí | N/D |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `NOISE` | Una fuente de ruido que se puede usar con SamplerCustomAdvanced | NOISE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/es.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
