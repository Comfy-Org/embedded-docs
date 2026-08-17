# WanDancerEncodeAudio

Este nodo procesa una entrada de audio para extraer características que pueden usarse para guiar un modelo de generación de video. Analiza el audio para detectar el tempo, los ritmos y otras características musicales, y luego empaqueta esta información en un formato adecuado para condicionar un modelo de video, lo que permite que el video generado se sincronice con el audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio` | La entrada de audio que se analizará y codificará. | AUDIO | Sí | - |
| `video_frames` | El número de fotogramas del video de destino. Se utiliza para calcular la velocidad de fotogramas para la sincronización (por defecto: 149). | INT | Sí | Min: 1, Max: 268435456 (MAX_RESOLUTION), Step: 4 |
| `audio_inject_scale` | La escala de las características de audio cuando se inyectan en el modelo de video (por defecto: 1.0). | FLOAT | Sí | Min: 0.0, Max: 10.0, Step: 0.01 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio_encoder_output` | Un diccionario que contiene las características de audio procesadas, la velocidad de fotogramas calculada (fps) y la escala de inyección de audio. Esta salida se utiliza para condicionar el modelo de generación de video. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Una cadena de texto que describe la velocidad de fotogramas calculada (fps) según la duración del audio y el número de fotogramas de video. Esta cadena está diseñada para usarse en el prompt del modelo de video. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/es.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
