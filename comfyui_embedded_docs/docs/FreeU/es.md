> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/es.md)

El nodo FreeU aplica modificaciones en el dominio de la frecuencia a los bloques de salida de un modelo para mejorar la calidad de generación de imágenes. Funciona escalando diferentes grupos de canales y aplicando filtrado de Fourier a mapas de características específicos, lo que permite un control preciso sobre el comportamiento del modelo durante el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que se le aplicarán las modificaciones FreeU |
| `b1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala del backbone para características de model_channels × 4 (predeterminado: 1.1) |
| `b2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala del backbone para características de model_channels × 2 (predeterminado: 1.2) |
| `s1` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de conexión de salto para características de model_channels × 4 (predeterminado: 0.9) |
| `s2` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de conexión de salto para características de model_channels × 2 (predeterminado: 0.2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `modelo` | MODEL | El modelo modificado con los parches FreeU aplicados |

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
