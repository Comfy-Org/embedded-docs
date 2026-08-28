# SamplerCustomAdvanced

El nodo SamplerCustomAdvanced realiza un muestreo avanzado del espacio latente utilizando configuraciones personalizadas de ruido, guía y muestreo. Procesa una imagen latente a través de un proceso de muestreo guiado con generación de ruido y programaciones sigma personalizables, produciendo tanto la salida muestreada final como una versión sin ruido cuando esté disponible.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ruido` | El generador de ruido que proporciona el patrón de ruido inicial y la semilla para el proceso de muestreo | NOISE | Sí | - |
| `guía` | El modelo de guía que dirige el proceso de muestreo hacia las salidas deseadas | GUIDER | Sí | - |
| `muestreador` | El algoritmo de muestreo que define cómo se recorre el espacio latente durante la generación | SAMPLER | Sí | - |
| `sigmas` | La programación sigma que controla los niveles de ruido a lo largo de los pasos de muestreo | SIGMAS | Sí | - |
| `imagen_latente` | La representación latente inicial que sirve como punto de partida para el muestreo. Admite un `noise_mask` opcional para la eliminación selectiva de ruido, y claves opcionales `downscale_ratio_spacial` y `downscale_ratio_temporal` para el manejo avanzado de latentes | LATENT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
| --- | --- | --- |
| `salida` | La representación latente muestreada final después de completar el proceso de muestreo. Cualquier clave `downscale_ratio_spacial` o `downscale_ratio_temporal` del latente de entrada se elimina de esta salida | LATENT |
| `salida_sin_ruido` | Una versión sin ruido de la salida cuando el proceso de muestreo produce una predicción limpia intermedia (x0); de lo contrario, devuelve lo mismo que la salida. Cuando está disponible, representa la mejor estimación del modelo del latente limpio en cada paso | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
