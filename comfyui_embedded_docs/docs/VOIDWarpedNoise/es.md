# VOIDWarpedNoise

Genera ruido temporalmente correlacionado para la segunda pasada del proceso de refinamiento de video VOID. Toma el video de salida de la Pasada 1 y deforma el ruido gaussiano a lo largo de los vectores de flujo óptico, creando ruido que se mueve de manera coherente con el contenido del video. Este ruido deformado se utiliza como latente inicial para la Pasada 2, lo que mejora la consistencia temporal en el resultado final.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de flujo óptico de OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Sí | - |
| `video` | Fotogramas de video de salida de la Pasada 1 [T, H, W, 3]. | IMAGE | Sí | - |
| `width` | Ancho del latente de salida (por defecto: 672). | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `height` | Alto del latente de salida (por defecto: 384). | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `length` | Número de fotogramas de píxeles. Se redondea hacia abajo para que `latent_t` sea par (requisito de `patch_size_t=2`), p. ej. 49 → 45 (por defecto: 45). | INT | Sí | 1 a MAX_RESOLUTION (paso 1) |
| `batch_size` | Número de secuencias de ruido idénticas a generar (por defecto: 1). | INT | Sí | 1 a 64 |

**Nota sobre el parámetro `length`:** El valor de `length` se redondea automáticamente hacia abajo al valor válido más cercano que produzca una dimensión `latent_t` par. Esto es requerido por la restricción `patch_size_t=2` del modelo CogVideoX-Fun-V1.5. Se registra una advertencia cuando se produce el redondeo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `warped_noise` | Un tensor 5D (B, C, T, H, W) que contiene ruido gaussiano deformado por flujo óptico, listo para usarse como latente inicial en la Pasada 2 de VOID. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/es.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
