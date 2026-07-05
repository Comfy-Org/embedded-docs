# SplitSigmasDenoise

El nodo SplitSigmasDenoise divide una secuencia de valores sigma en dos partes basándose en un parámetro de fuerza de eliminación de ruido. Divide los sigmas de entrada en secuencias de sigma altas y bajas, donde el punto de división se determina multiplicando el total de pasos por el factor de eliminación de ruido. Esto permite separar el programa de ruido en diferentes rangos de intensidad para un procesamiento especializado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de entrada de valores sigma que representa el programa de ruido | SIGMAS | Sí | - |
| `denoise` | El factor de fuerza de eliminación de ruido que determina dónde dividir la secuencia sigma (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas_altos` | La primera parte de la secuencia sigma que contiene valores sigma más altos | SIGMAS |
| `sigmas_bajos` | La segunda parte de la secuencia sigma que contiene valores sigma más bajos | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/es.md)

---
**Source fingerprint (SHA-256):** `fda53efe2fcaed9244376b7360d8b0b76ce7395d594de4c2ecc48a8f243d7ca6`
