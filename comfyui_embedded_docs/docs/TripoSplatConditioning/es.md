# Condicionamiento TripoSplat

Este nodo codifica una imagen de entrada utilizando el codificador visual DINOv3 y el VAE de Flux2 para crear datos de condicionamiento positivos y negativos para el modelo TripoSplat. También genera un objetivo de ruido de tamaño fijo (una secuencia latente más un token de cámara) que sirve como punto de partida para el KSampler.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip_vision` | Codificador de imagen DINOv3 ViT-H/16+ | CLIP_VISION | Sí | - |
| `vae` | VAE de Flux2 | VAE | Sí | - |
| `image` | La imagen de entrada a codificar | IMAGE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | Datos de condicionamiento positivos que contienen las características de imagen de DINOv3 y el latente del VAE de Flux2 de la imagen de entrada | CONDITIONING |
| `negative` | Datos de condicionamiento negativos que contienen características de DINOv3 rellenas con ceros y un latente del VAE de Flux2 relleno con ceros | CONDITIONING |
| `latent` | El objetivo de ruido de tamaño fijo (latente + cámara) para el KSampler | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/es.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
