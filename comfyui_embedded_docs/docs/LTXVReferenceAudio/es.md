> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/es.md)

El nodo **LTXV Reference Audio** se utiliza para la transferencia de identidad del hablante en la generación de audio. Codifica un clip de audio de referencia en el condicionamiento de un modelo, permitiendo que el audio generado adopte las características vocales del hablante. También puede aplicar guía de identidad, que ejecuta un paso de procesamiento adicional para amplificar el efecto de la identidad del hablante.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se le aplicará la guía de identidad. |
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo. |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo. |
| `reference_audio` | AUDIO | Sí | - | Clip de audio de referencia cuya identidad de hablante se transferirá. Se recomiendan ~5 segundos (duración de entrenamiento). Clips más cortos o más largos pueden degradar la transferencia de identidad de voz. |
| `audio_vae` | VAE | Sí | - | VAE de audio LTXV para codificar el audio de referencia. |
| `identity_guidance_scale` | FLOAT | No | 0.0 - 100.0 | Intensidad de la guía de identidad. Ejecuta un pase directo adicional sin referencia en cada paso para amplificar la identidad del hablante. Establecer en 0 para deshabilitar (sin pase adicional). (valor predeterminado: 3.0) |
| `start_percent` | FLOAT | No | 0.0 - 1.0 | Inicio del rango sigma donde la guía de identidad está activa. (valor predeterminado: 0.0) |
| `end_percent` | FLOAT | No | 0.0 - 1.0 | Fin del rango sigma donde la guía de identidad está activa. (valor predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con la función de guía de identidad. |
| `positive` | CONDITIONING | El condicionamiento positivo, que ahora contiene los datos de audio de referencia codificados. |
| `negative` | CONDITIONING | El condicionamiento negativo, que ahora contiene los datos de audio de referencia codificados. |

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`
