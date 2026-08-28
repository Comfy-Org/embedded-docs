# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio transfiere la identidad de voz de un hablante desde un clip de audio de referencia al audio generado. Codifica el audio de referencia en el condicionamiento y, opcionalmente, parchea el modelo con guía de identidad, que ejecuta una pasada adicional hacia adelante sin la referencia en cada paso para amplificar el efecto de identidad del hablante.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a parchear con la guía de identidad. | MODEL | Sí | - |
| `positivo` | La entrada de condicionamiento positiva. | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativa. | CONDITIONING | Sí | - |
| `audio_referencia` | Clip de audio de referencia cuya identidad de hablante se transferirá. Se recomiendan ~5 segundos (duración de entrenamiento). Clips más cortos o más largos pueden degradar la transferencia de identidad de voz. | AUDIO | Sí | - |
| `audio_vae` | VAE de audio LTXV para codificación. | VAE | Sí | - |
| `escala_guía_identidad` | Fuerza de la guía de identidad. Ejecuta una pasada adicional hacia adelante sin referencia en cada paso para amplificar la identidad del hablante. Establézcalo en 0 para desactivarla (sin pasada adicional). (por defecto: 3.0) | FLOAT | Sí | 0.0 - 100.0 |
| `porcentaje_inicio` | Inicio del rango sigma donde la guía de identidad está activa. (por defecto: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `porcentaje_fin` | Fin del rango sigma donde la guía de identidad está activa. (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

Nota: La guía de identidad solo se aplica cuando `identity_guidance_scale` es mayor que 0 y el paso de muestreo actual está dentro del rango definido por `start_percent` y `end_percent`. El audio de referencia se remuestrea a la frecuencia de muestreo del VAE de audio si difieren.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo parcheado con la función de guía de identidad. | MODEL |
| `positivo` | El condicionamiento positivo, ahora con los datos de audio de referencia codificados. | CONDITIONING |
| `negativo` | El condicionamiento negativo, ahora con los datos de audio de referencia codificados. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/es.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
