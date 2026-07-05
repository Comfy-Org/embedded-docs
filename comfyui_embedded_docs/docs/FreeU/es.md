# FreeU

El nodo FreeU aplica modificaciones en el dominio de la frecuencia a los bloques de salida de un modelo para mejorar la calidad de generación de imágenes. Funciona escalando diferentes grupos de canales y aplicando filtrado de Fourier a mapas de características específicos, lo que permite un control preciso sobre el comportamiento del modelo durante el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le aplicarán las modificaciones FreeU | MODEL | Sí | - |
| `b1` | Factor de escala del backbone para características de model_channels × 4 (predeterminado: 1.1) | FLOAT | Sí | 0.0 - 10.0 |
| `b2` | Factor de escala del backbone para características de model_channels × 2 (predeterminado: 1.2) | FLOAT | Sí | 0.0 - 10.0 |
| `s1` | Factor de escala de conexión de salto para características de model_channels × 4 (predeterminado: 0.9) | FLOAT | Sí | 0.0 - 10.0 |
| `s2` | Factor de escala de conexión de salto para características de model_channels × 2 (predeterminado: 0.2) | FLOAT | Sí | 0.0 - 10.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo modificado con los parches FreeU aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/es.md)

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
