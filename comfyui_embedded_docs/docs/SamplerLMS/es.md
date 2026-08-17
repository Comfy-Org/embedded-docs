# SamplerLMS

El nodo SamplerLMS crea un muestreador de Mínimos Cuadrados Medios (LMS) para su uso en modelos de difusión. Genera un objeto de muestreador que puede utilizarse en el proceso de muestreo, lo que le permite controlar el orden del algoritmo LMS para lograr estabilidad y precisión numéricas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `order` | El parámetro de orden para el algoritmo del muestreador LMS, que controla la precisión y estabilidad del método numérico (valor predeterminado: 4; parámetro avanzado) | INT | Sí | 1 a 100 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Un objeto de muestreador LMS configurado que puede utilizarse en el proceso de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/es.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
