# SamplerLCM

El nodo SamplerLCM proporciona un muestreador LCM (Modelo de Consistencia Latente) con parámetros de ruido ajustables por paso. Permite controlar el ruido aplicado en cada paso de muestreo, lo que posibilita un ajuste detallado del proceso de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicador de ruido por paso en el primer paso. Un valor de 1.0 coincide con la escala de ruido de entrenamiento del modelo. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 64.0 (incremento: 0.01) |
| `s_noise_end` | Multiplicador de ruido por paso en el último paso. Establecer igual a `s_noise` para una programación de ruido constante. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 64.0 (incremento: 0.01) |
| `noise_clip_std` | Limita el ruido por paso a un rango de +/- N desviaciones estándar. Un valor de 0 desactiva la limitación. (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 10.0 (incremento: 0.01) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `SAMPLER` | El objeto muestreador LCM configurado, listo para ser utilizado en un flujo de trabajo de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/es.md)

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
