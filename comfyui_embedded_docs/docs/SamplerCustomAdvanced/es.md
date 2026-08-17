# SamplerCustomAdvanced

El nodo SamplerCustomAdvanced realiza un muestreo avanzado del espacio latente utilizando configuraciones personalizadas de ruido, guía y muestreo. Procesa una imagen latente mediante un proceso de muestreo guiado con generación de ruido personalizable y programaciones de sigma, produciendo tanto la salida muestreada final como una versión denoizada cuando esté disponible.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `noise` | El generador de ruido que proporciona el patrón de ruido inicial y la semilla para el proceso de muestreo. | NOISE | Sí | - |
| `guider` | El modelo de guía que dirige el proceso de muestreo hacia las salidas deseadas. | GUIDER | Sí | - |
| `sampler` | El algoritmo de muestreo que define cómo se recorre el espacio latente durante la generación. | SAMPLER | Sí | - |
| `sigmas` | La programación de sigmas que controla los niveles de ruido a lo largo de los pasos de muestreo. | SIGMAS | Sí | - |
| `latent_image` | La representación latente inicial que sirve como punto de partida para el muestreo. Admite un `noise_mask` opcional para el denoizado selectivo, y claves opcionales `downscale_ratio_spacial` y `downscale_ratio_temporal` para el manejo avanzado de latentes. | LATENT | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | La representación latente muestreada final después de completar el proceso de muestreo. Las claves `downscale_ratio_spacial` o `downscale_ratio_temporal` del latente de entrada se eliminan de esta salida. | LATENT |
| `denoised_output` | Una versión denoizada de la salida cuando el proceso de muestreo produce una predicción limpia intermedia (x0); de lo contrario, devuelve lo mismo que la salida. Cuando está disponible, representa la mejor estimación del modelo del latente limpio en cada paso. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
