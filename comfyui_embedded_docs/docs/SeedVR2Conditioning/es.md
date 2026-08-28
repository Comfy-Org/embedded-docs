# Aplicar Condicionamiento SeedVR2

Este nodo construye un condicionamiento positivo y negativo a partir de un latent de VAE para usarlo con el modelo SeedVR2. Valida la forma del latent de entrada y la estructura del modelo, y luego produce tanto el condicionamiento positivo como el negativo que guían el muestreo de imágenes o vídeos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo SeedVR2. | MODEL | Sí | - |
| `vae_conditioning` | El latent de VAE de SeedVR2 a partir del cual construir el condicionamiento (nombre mostrado: latent). | LATENT | Sí | - |

Nota: el latent `vae_conditioning` debe ser un tensor de 5 dimensiones en el diseño de canales primero de Comfy (B, C, T, H, W), donde C es el número de canales esperado para el VAE de SeedVR2. El nodo genera un error si el latent no tiene 5 dimensiones, si su número de canales no coincide, o si parece estar en un diseño de canales al final. La entrada `model` debe ser un modelo con la estructura esperada de SeedVR2. Internamente, el nodo añade un canal de máscara constante al latent y adjunta la condición resultante a los grupos de condicionamiento positivo y negativo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | El condicionamiento positivo para el muestreo. | CONDITIONING |
| `negative` | El condicionamiento negativo para el muestreo. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
