# FreeU

El nodo FreeU aplica modificaciones en el dominio de la frecuencia a los bloques de salida de un modelo para mejorar la calidad de generación de imágenes. Funciona escalando diferentes grupos de canales y aplicando filtrado de Fourier a mapas de características específicos, lo que permite un control preciso sobre el comportamiento del modelo durante el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le aplicarán las modificaciones FreeU | MODEL | Sí | - |
| `b1` | Factor de escalado del backbone para características de model_channels × 4 (predeterminado: 1.1) | FLOAT | Sí | 0.0 - 10.0 |
| `b2` | Factor de escalado del backbone para características de model_channels × 2 (predeterminado: 1.2) | FLOAT | Sí | 0.0 - 10.0 |
| `s1` | Factor de escalado de la conexión de salto para características de model_channels × 4 (predeterminado: 0.9) | FLOAT | Sí | 0.0 - 10.0 |
| `s2` | Factor de escalado de la conexión de salto para características de model_channels × 2 (predeterminado: 0.2) | FLOAT | Sí | 0.0 - 10.0 |

Nota: Las modificaciones se aplican solo a los mapas de características con canales model_channels × 4 y model_channels × 2; `b1`/`s1` afectan a los primeros y `b2`/`s2` a los últimos. Los demás mapas de características no se modifican.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con los parches FreeU aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/es.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
