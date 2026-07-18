# Acondicionamiento TripoSplat

Este nodo codifica una imagen de entrada utilizando DINOv3 y el VAE Flux2 para crear datos de acondicionamiento positivo y negativo para el modelo TripoSplat. También genera un objetivo de ruido de tamaño fijo (latente más datos de cámara) que sirve como punto de partida para el KSampler.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `clip_vision` | Codificador de imágenes DINOv3 ViT-H/16+ | CLIP_VISION | Sí | - |
| `vae` | VAE Flux2 | VAE | Sí | - |
| `imagen` | La imagen de entrada a codificar | IMAGE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `positivo` | Datos de acondicionamiento positivo que contienen características DINOv3 y latente del VAE Flux2 | CONDITIONING |
| `negativo` | Datos de acondicionamiento negativo que contienen características DINOv3 rellenas con ceros y latente del VAE Flux2 relleno con ceros | CONDITIONING |
| `latente` | Objetivo de ruido de tamaño fijo (secuencia latente más token de cámara) para el KSampler | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/es.md)

---
**Source fingerprint (SHA-256):** `9187a4a020818b9adc762eb41e913086b59d62c47abe92d4bafdb14bc8779f51`
