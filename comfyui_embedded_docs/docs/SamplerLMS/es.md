El nodo SamplerLMS crea un muestreador de Mínimos Cuadrados Medios (LMS) para su uso en modelos de difusión. Genera un objeto de muestreador que puede utilizarse en el proceso de muestreo, permitiéndole controlar el orden del algoritmo LMS para lograr estabilidad y precisión numérica.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `orden` | El parámetro de orden para el algoritmo del muestreador LMS, que controla la precisión y estabilidad del método numérico (valor predeterminado: 4) | INT | Sí | 1 a 100 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Un objeto de muestreador LMS configurado que puede utilizarse en el flujo de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/es.md)

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`
