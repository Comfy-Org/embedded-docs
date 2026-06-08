# Descripción general

Genera ruido con correlación temporal para la segunda pasada del proceso de refinamiento de video VOID. Toma el video de salida de la Pasada 1 y distorsiona el ruido gaussiano siguiendo los vectores de flujo óptico, creando ruido que se mueve de forma coherente con el contenido del video. Este ruido distorsionado se utiliza como latente inicial para la Pasada 2, lo que mejora la consistencia temporal en el resultado final.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de flujo óptico proveniente de OpticalFlowLoader (RAFT-large). | MODEL | Sí | - |
| `video` | Fotogramas del video de salida de la Pasada 1 [T, A, L, 3]. | IMAGE | Sí | - |
| `width` | Ancho del latente de salida (predeterminado: 672). | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `height` | Alto del latente de salida (predeterminado: 384). | INT | Sí | 16 a MAX_RESOLUTION (paso 8) |
| `length` | Número de fotogramas de píxeles. Se redondea hacia abajo para que latent_t sea par (requisito de patch_size_t=2), ej. 49 → 45 (predeterminado: 45). | INT | Sí | 1 a MAX_RESOLUTION (paso 1) |
| `batch_size` | Número de secuencias de ruido idénticas a generar (predeterminado: 1). | INT | Sí | 1 a 64 |

**Nota sobre el parámetro `length`:** El valor de `length` se redondea automáticamente hacia abajo al valor válido más cercano que produzca una dimensión `latent_t` par. Esto es requerido por la restricción `patch_size_t=2` del modelo CogVideoX-Fun-V1.5. Se registra una advertencia cuando ocurre el redondeo.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `warped_noise` | Un tensor 5D (B, C, T, A, L) que contiene ruido gaussiano distorsionado por flujo óptico, listo para usarse como latente inicial en la Pasada 2 de VOID. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/es.md)

---
**Source fingerprint (SHA-256):** `a0f986e54bcc6c455220f89f5d840585a9eae081e522ea11e0ce37ab46821bd9`
