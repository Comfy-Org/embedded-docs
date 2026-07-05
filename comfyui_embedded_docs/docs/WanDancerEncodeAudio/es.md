# WanDancerEncodeAudio

Este nodo procesa una entrada de audio para extraer características que pueden utilizarse para guiar un modelo de generación de video. Analiza el audio para detectar tempo, ritmos y otras características musicales, luego empaqueta esta información en un formato adecuado para condicionar un modelo de video, permitiendo que el video generado se sincronice con el audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `audio` | La entrada de audio que se analizará y codificará. | AUDIO | Sí | - |
| `video_frames` | El número de fotogramas en el video de destino. Se utiliza para calcular la velocidad de fotogramas para la sincronización (valor predeterminado: 149). | INT | Sí | Mín: 1, Máx: 268435456 (MAX_RESOLUTION), Paso: 4 |
| `audio_inject_scale` | La escala para las características de audio cuando se inyectan en el modelo de video (valor predeterminado: 1.0). | FLOAT | Sí | Mín: 0.0, Máx: 10.0, Paso: 0.01 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio_encoder_output` | Un diccionario que contiene las características de audio procesadas, la velocidad de fotogramas calculada (fps) y la escala de inyección de audio. Esta salida se utiliza para condicionar el modelo de generación de video. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Una cadena de texto que describe la velocidad de fotogramas calculada (fps) basada en la duración del audio y el número de fotogramas de video. Esta cadena está diseñada para usarse en el prompt del modelo de video. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/es.md)

---
**Source fingerprint (SHA-256):** `ef230c92b23a04369708041b2e5d03c1b2928edf746dc43020bae777f9f0b589`
