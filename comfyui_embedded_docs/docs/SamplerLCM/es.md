# SamplerLCM

El nodo SamplerLCM proporciona un muestreador LCM (Modelo de Consistencia Latente) con ajustes de ruido configurables por paso. El parámetro `s_noise` actúa como un multiplicador de la escala de ruido de entrenamiento del modelo, lo que permite un control preciso del ruido aplicado en cada paso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicador de ruido por paso en el primer paso (1.0 = coincide con el entrenamiento). Predeterminado: 1.0. | FLOAT | Sí | 0.0 a 64.0 (paso: 0.01) |
| `s_noise_end` | Multiplicador de ruido por paso en el último paso. Establézcalo igual a `s_noise` para un programa constante. Predeterminado: 1.0. | FLOAT | Sí | 0.0 a 64.0 (paso: 0.01) |
| `noise_clip_std` | Limita el ruido por paso a ± N*std. 0 lo desactiva. Predeterminado: 0.0. | FLOAT | Sí | 0.0 a 10.0 (paso: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `SAMPLER` | El objeto muestreador LCM configurado, listo para usarse en un flujo de trabajo de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/es.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
