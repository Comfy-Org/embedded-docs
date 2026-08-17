# SplitSigmasDenoise

El nodo SplitSigmasDenoise divide una secuencia de valores sigma en dos partes según un parámetro de fuerza de eliminación de ruido. Divide los sigmas de entrada en secuencias sigma altas y bajas, donde el punto de división se determina multiplicando los pasos totales por el factor de denoise. Esto permite separar el programa de ruido en diferentes rangos de intensidad para un procesamiento especializado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de entrada de valores sigma que representa el programa de ruido | SIGMAS | Sí | - |
| `denoise` | El factor de intensidad de eliminación de ruido que determina dónde dividir la secuencia sigma (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

Nota: El número total de pasos es el número de valores sigma menos 1. Las dos secuencias de salida comparten un valor sigma en el punto de división. Con `denoise` = 0.0, `high_sigmas` está vacía; con `denoise` = 1.0, `high_sigmas` contiene solo el primer valor sigma y `low_sigmas` contiene la secuencia completa.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `high_sigmas` | La primera parte de la secuencia sigma que contiene valores sigma más altos | SIGMAS |
| `low_sigmas` | La segunda parte de la secuencia sigma que contiene valores sigma más bajos | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/es.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
