# Aplicar Condicionamiento SeedVR2

Este nodo construye el condicionamiento positivo y negativo a partir de un latent de VAE para su uso con el modelo SeedVR2. Añade un canal de máscara al latent y luego lo combina con los embeddings de condicionamiento positivo y negativo integrados del modelo para producir los valores de condicionamiento necesarios para el muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo SeedVR2. | MODEL | Sí | - |
| `vae_conditioning` | El latent de VAE a partir del cual se construye el condicionamiento. Nombre mostrado: latent. | LATENT | Sí | - |

El latent `vae_conditioning` debe ser un tensor 5-D en el diseño de Comfy de canales primero (B, C, T, H, W) con el número de canales esperado por el VAE de SeedVR2. Los latents con canales al final se rechazan con un error. La entrada `model` debe ser un modelo SeedVR2 válido con la estructura interna esperada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | El condicionamiento positivo para el muestreo. | CONDITIONING |
| `negative` | El condicionamiento negativo para el muestreo. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
