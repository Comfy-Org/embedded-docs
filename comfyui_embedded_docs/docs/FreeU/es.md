# FreeU

El nodo FreeU aplica modificaciones en el dominio de la frecuencia a los bloques de salida de un modelo para mejorar la calidad de generación de imágenes. Funciona escalando diferentes grupos de canales y aplicando filtrado de Fourier a mapas de características específicos, lo que permite un control fino sobre el comportamiento del modelo durante el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le aplicarán las modificaciones de FreeU | MODEL | Sí | - |
| `b1` | Factor de escalado del backbone para características de model_channels × 4 (por defecto: 1.1) | FLOAT | Sí | 0.0 - 10.0 |
| `b2` | Factor de escalado del backbone para características de model_channels × 2 (por defecto: 1.2) | FLOAT | Sí | 0.0 - 10.0 |
| `s1` | Factor de escalado de la conexión de salto para características de model_channels × 4 (por defecto: 0.9) | FLOAT | Sí | 0.0 - 10.0 |
| `s2` | Factor de escalado de la conexión de salto para características de model_channels × 2 (por defecto: 0.2) | FLOAT | Sí | 0.0 - 10.0 |

Nota: Los ajustes de FreeU se aplican únicamente a los mapas de características cuyo número de canales sea igual a model_channels × 4 (usando `b1` y `s1`) o model_channels × 2 (usando `b2` y `s2`). El filtro de Fourier escala solo la región central de baja frecuencia de los mapas de características de las conexiones de salto; todos los demás componentes de frecuencia permanecen sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con los parches de FreeU aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/es.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
