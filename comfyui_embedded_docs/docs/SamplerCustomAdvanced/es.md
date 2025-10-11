> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/es.md)

El nodo SamplerCustomAdvanced realiza un muestreo avanzado en el espacio latente utilizando configuraciones personalizadas de ruido, guía y muestreo. Procesa una imagen latente a través de un proceso de muestreo guiado con generación de ruido y programaciones de sigma personalizables, produciendo tanto la salida muestreada final como una versión sin ruido cuando está disponible.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `noise` | NOISE | Sí | - | El generador de ruido que proporciona el patrón de ruido inicial y la semilla para el proceso de muestreo |
| `guider` | GUIDER | Sí | - | El modelo de guía que dirige el proceso de muestreo hacia las salidas deseadas |
| `sampler` | SAMPLER | Sí | - | El algoritmo de muestreo que define cómo se recorre el espacio latente durante la generación |
| `sigmas` | SIGMAS | Sí | - | La programación de sigma que controla los niveles de ruido a lo largo de los pasos de muestreo |
| `latent_image` | LATENT | Sí | - | La representación latente inicial que sirve como punto de partida para el muestreo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | La representación latente muestreada final después de completar el proceso de muestreo |
| `denoised_output` | LATENT | Una versión sin ruido de la salida cuando está disponible, de lo contrario devuelve lo mismo que la salida |