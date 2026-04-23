> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/es.md)

El nodo LTXV Reference Audio se utiliza para la transferencia de identidad del hablante en la generación de audio. Codifica un clip de audio de referencia en el acondicionamiento para un modelo, permitiendo que el audio generado adopte las características de voz del hablante. También puede aplicar una guía de identidad, que ejecuta un paso de procesamiento adicional para amplificar el efecto de identidad del hablante.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo que se va a parchear con la guía de identidad. |
| `positive` | CONDITIONING | Sí | - | La entrada de acondicionamiento positivo. |
| `negative` | CONDITIONING | Sí | - | La entrada de acondicionamiento negativo. |
| `reference_audio` | AUDIO | Sí | - | Clip de audio de referencia cuya identidad de hablante se va a transferir. Se recomiendan ~5 segundos (duración de entrenamiento). Clips más cortos o más largos pueden degradar la transferencia de identidad de voz. |
| `audio_vae` | VAE | Sí | - | VAE de audio LTXV para codificar el audio de referencia. |
| `identity_guidance_scale` | FLOAT | No | 0.0 - 100.0 | Intensidad de la guía de identidad. Ejecuta un paso de avance adicional sin referencia en cada paso para amplificar la identidad del hablante. Establecer en 0 para desactivar (sin paso adicional). (por defecto: 3.0) |
| `start_percent` | FLOAT | No | 0.0 - 1.0 | Inicio del rango de sigma donde la guía de identidad está activa. (por defecto: 0.0) |
| `end_percent` | FLOAT | No | 0.0 - 1.0 | Fin del rango de sigma donde la guía de identidad está activa. (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo parcheado con la función de guía de identidad. |
| `positive` | CONDITIONING | El acondicionamiento positivo, que ahora contiene los datos codificados del audio de referencia. |
| `negative` | CONDITIONING | El acondicionamiento negativo, que ahora contiene los datos codificados del audio de referencia. |