# SeedVR2Conditioning

Este nodo construye condicionamiento positivo y negativo a partir de un latente VAE para su uso con el modelo SeedVR2. Prepara los datos de condicionamiento que guían el proceso de generación de imágenes o videos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | El modelo SeedVR2. | MODEL | Sí | - |
| `vae_conditioning` | El latente VAE a partir del cual construir el condicionamiento. | LATENT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model` | El modelo SeedVR2. | MODEL |
| `positive` | El condicionamiento positivo para guiar la generación. | CONDITIONING |
| `negative` | El condicionamiento negativo para guiar la generación. | CONDITIONING |
| `latent` | Las muestras latentes procesadas. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `8f99c0e712c5c6fc76261d6d72c5c08b7202c77827ecf2549240fc530c1b65bd`
