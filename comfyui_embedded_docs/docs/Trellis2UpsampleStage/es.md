# Trellis2UpsampleStage

Este nodo toma el latente de forma de resolución 512 producido por la primera pasada de muestreo de la etapa de forma, lo amplía a una resolución objetivo superior y prepara el condicionamiento y el latente necesarios para la segunda pasada de muestreo de la etapa de forma. Adjunta metadatos por etapa al condicionamiento para que el modelo pueda usarlos durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `positive` | El condicionamiento positivo al que se adjuntan los metadatos de forma de la etapa de ampliación. | CONDITIONING | Sí | |
| `negative` | El condicionamiento negativo al que se adjuntan los metadatos de forma de la etapa de ampliación. | CONDITIONING | Sí | |
| `shape_latent` | El latente de forma de resolución 512 que sale del primer KSampler de la etapa de forma. | LATENT | Sí | |
| `vae` | El VAE Trellis2 utilizado para decodificar el latente de forma en coordenadas dispersas de alta resolución. | VAE | Sí | |
| `target_resolution` | Resolución de vóxeles de la forma ampliada. Mayor = más detalle, más VRAM. Por defecto: 1024. | INT | Sí | 1024 - 2048 (step 128) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `positive` | Condicionamiento positivo con los metadatos de forma de la etapa de ampliación adjuntos. | CONDITIONING |
| `negative` | Condicionamiento negativo con los metadatos de forma de la etapa de ampliación adjuntos. | CONDITIONING |
| `latent` | Latente relleno de ceros preparado para la segunda pasada de muestreo de la etapa de forma en la resolución objetivo, que contiene las coordenadas ampliadas y los metadatos de resolución. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/es.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
