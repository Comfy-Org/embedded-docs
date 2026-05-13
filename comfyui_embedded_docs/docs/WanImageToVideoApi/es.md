> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/en.md)

El nodo Wan Image to Video genera un video a partir de una sola imagen de entrada y un prompt de texto. Utiliza la imagen proporcionada como primer fotograma y crea una secuencia de video basada en la descripción, con opciones para resolución, duración, audio y otras configuraciones avanzadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-i2v-preview"<br>"wan2.6-i2v" | Modelo a utilizar (predeterminado: "wan2.6-i2v") |
| `image` | IMAGE | Sí | - | Imagen de entrada que sirve como primer fotograma para la generación del video. Se requiere exactamente una imagen. |
| `prompt` | STRING | Sí | - | Prompt que describe los elementos y las características visuales. Admite inglés y chino (predeterminado: vacío). |
| `negative_prompt` | STRING | No | - | Prompt negativo que describe lo que se debe evitar (predeterminado: vacío). |
| `resolution` | COMBO | No | "480P"<br>"720P"<br>"1080P" | Calidad de resolución del video (predeterminado: "720P"). El modelo Wan 2.6 no admite 480P. |
| `duration` | INT | No | 5-15 (paso: 5) | Duración del video generado en segundos. Una duración de 15 segundos solo es compatible con el modelo Wan 2.6 (predeterminado: 5). |
| `audio` | AUDIO | No | - | El audio debe contener una voz clara y fuerte, sin ruidos extraños ni música de fondo. Cuando se proporciona, la duración del audio debe estar entre 3.0 y 29.0 segundos. |
| `seed` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (predeterminado: 0). |
| `generate_audio` | BOOLEAN | No | - | Si no se proporciona una entrada de audio, generar audio automáticamente (predeterminado: False). |
| `prompt_extend` | BOOLEAN | No | - | Si se debe mejorar el prompt con asistencia de IA (predeterminado: True). |
| `watermark` | BOOLEAN | No | - | Si se debe agregar una marca de agua generada por IA al resultado (predeterminado: False). |
| `shot_type` | COMBO | No | "single"<br>"multi" | Especifica el tipo de toma para el video generado, es decir, si el video es una sola toma continua o múltiples tomas con cortes. Este parámetro solo tiene efecto cuando prompt_extend es True (predeterminado: "single"). |

**Restricciones:**

- Se requiere exactamente una imagen de entrada para la generación del video.
- El modelo Wan 2.6 (`wan2.6-i2v`) no admite la resolución 480P.
- Una duración de 15 segundos solo es compatible con el modelo Wan 2.6 (`wan2.6-i2v`).
- Cuando se proporciona audio, su duración debe estar entre 3.0 y 29.0 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | Video generado basado en la imagen de entrada y el prompt. |

---
**Source fingerprint (SHA-256):** `ad4947dbb9c12ebb97ace99cd447431ba6db88a3b74239099fcbea501cff71f0`
