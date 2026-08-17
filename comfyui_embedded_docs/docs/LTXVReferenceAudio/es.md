# LTXV Reference Audio (ID-LoRA)

El nodo LTXV Reference Audio establece un clip de audio de referencia para la transferencia de identidad del hablante con ID-LoRA en la generación de audio. Codifica el clip en el condicionamiento para que el audio generado adopte las características de voz del hablante y, opcionalmente, parchea el modelo con guía de identidad, lo que ejecuta una pasada directa adicional sin la referencia para amplificar el efecto de identidad del hablante.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo a parchear con la guía de identidad. | MODEL | Sí | - |
| `positive` | La entrada de condicionamiento positivo. | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo. | CONDITIONING | Sí | - |
| `reference_audio` | Clip de audio de referencia cuya identidad de hablante se transferirá. Se recomiendan ~5 segundos (duración de entrenamiento). Los clips más cortos o más largos pueden degradar la transferencia de identidad de voz. | AUDIO | Sí | - |
| `audio_vae` | LTXV Audio VAE para la codificación. | VAE | Sí | - |
| `identity_guidance_scale` | Fuerza de la guía de identidad. Ejecuta en cada paso una pasada directa adicional sin la referencia para amplificar la identidad del hablante. Configúrelo en 0 para desactivarlo (sin pasada adicional). (predeterminado: 3.0) | FLOAT | No | 0.0 - 100.0 |
| `start_percent` | Inicio del rango sigma donde la guía de identidad está activa. (predeterminado: 0.0) | FLOAT | No | 0.0 - 1.0 |
| `end_percent` | Fin del rango sigma donde la guía de identidad está activa. (predeterminado: 1.0) | FLOAT | No | 0.0 - 1.0 |

Nota: La guía de identidad solo está activa para valores sigma dentro del rango definido por `start_percent` y `end_percent`; fuera de ese rango, la salida denoizada se deja sin cambios. El audio de referencia se agrega tanto al condicionamiento positivo como al negativo. Si la frecuencia de muestreo del audio de referencia difiere de la del VAE de audio, el audio se remuestrea automáticamente para que coincida con el VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo parcheado con la función de guía de identidad. | MODEL |
| `positive` | El condicionamiento positivo, que ahora contiene los datos de audio de referencia codificados. | CONDITIONING |
| `negative` | El condicionamiento negativo, que ahora contiene los datos de audio de referencia codificados. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/es.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
