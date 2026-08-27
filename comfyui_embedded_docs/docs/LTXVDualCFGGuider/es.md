# LTXV Dual CFG Guider

Este nodo crea un objeto de muestreo guiado (guía CFG) para los modelos LTXV-AV. Aplica una escala de guía separada a la parte de video y a la parte de audio del latent empaquetado, lo que permite controlar la influencia del condicionamiento en cada modalidad de forma independiente. Si las dos escalas son iguales, o si el latent no contiene componentes de video y audio separados, se utiliza una única escala general.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo que se usará al muestrear. | MODEL | Sí | - |
| `positivo` | Condicionamiento positivo para guiar la generación. | CONDITIONING | Sí | - |
| `negativo` | Condicionamiento negativo para alejar la generación. | CONDITIONING | Sí | - |
| `video_cfg` | Intensidad de guía aplicada a la modalidad de video del latent (por defecto: 3.0). | FLOAT | Sí | 0.0 a 100.0 |
| `audio_cfg` | Intensidad de guía aplicada a la modalidad de audio del latent (por defecto: 7.0). | FLOAT | Sí | 0.0 a 100.0 |

Nota: Cuando `video_cfg` y `audio_cfg` son iguales o muy cercanos en valor, la guía utiliza ese valor como una única escala CFG para todo el latent. Si el latent no es un latent LTXV-AV empaquetado, solo se utiliza el valor de `video_cfg`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `guider` | La guía CFG configurada para pasarse a un nodo de muestreo. | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/es.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
