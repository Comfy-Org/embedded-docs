Este nodo genera un video a partir de una descripción textual utilizando el modelo Wan 2.7. Envía tu solicitud a una API externa, que procesa el prompt y devuelve un archivo de video. Opcionalmente, puedes proporcionar un clip de audio para influir en el movimiento y la sincronización del video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo específico a utilizar para la generación de video. | COMBO | Sí | `"wan2.7-t2v"` |
| `model.prompt` | Una descripción de los elementos y características visuales que deseas en el video. Compatible con inglés y chino. | STRING | Sí | - |
| `model.negative_prompt` | Una descripción de elementos o características que deseas evitar en el video generado. | STRING | No | - |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La duración del video en segundos (predeterminado: 5). | INT | Sí | 2 a 15 |
| `audio` | Un archivo de audio para guiar la generación del video, como para sincronización de labios o movimiento al ritmo. Si no se proporciona, el modelo generará música de fondo o efectos de sonido coincidentes. La duración del audio debe estar entre 1.5 y 60 segundos. | AUDIO | No | - |
| `semilla` | Un número utilizado para controlar la aleatoriedad de la generación, asegurando resultados reproducibles (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `extender_prompt` | Cuando está habilitado, el prompt se mejorará con asistencia de IA (predeterminado: True). | BOOLEAN | No | - |
| `marca de agua` | Cuando está habilitado, se agregará una marca de agua generada por IA al resultado (predeterminado: False). | BOOLEAN | No | - |

**Nota:** El parámetro `audio` es opcional. Si se proporciona, su duración debe estar entre 1.5 y 60 segundos. Si se omite, el modelo generará audio automáticamente.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `ce8a2f4e53b2bce879f143c66f6078fd81c6308e2822cb486b1cf8e178a6f58c`
