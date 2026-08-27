# Condicionamiento TripoSplat

Este nodo codifica una imagen de entrada utilizando el codificador de imagen DINOv3 y el VAE Flux2 para crear datos de condicionamiento positivo y negativo para el modelo TripoSplat. También genera un objetivo de ruido de tamaño fijo (latente más datos de cámara) que sirve como punto de partida para el KSampler.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip_vision` | Codificador de imagen DINOv3 ViT-H/16+ | CLIP_VISION | Sí | - |
| `vae` | VAE Flux2 | VAE | Sí | - |
| `imagen` | La imagen de entrada a codificar | IMAGE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | Datos de condicionamiento positivo que contienen características DINOv3 y latente del VAE Flux2 | CONDITIONING |
| `negativo` | Datos de condicionamiento negativo que contienen características DINOv3 rellenas de ceros y latente del VAE Flux2 relleno de ceros | CONDITIONING |
| `latente` | El objetivo de ruido de tamaño fijo (latente + cámara) para el KSampler | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/es.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
