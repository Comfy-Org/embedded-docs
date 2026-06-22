# Wan 2.7 Referencia a Video

Este nodo genera un video con una persona u objeto basado en materiales de referencia proporcionados. Utiliza el modelo Wan 2.7 para crear videos a partir de un prompt de texto, compatible con actuaciones de un solo personaje e interacciones de múltiples personajes. Debes proporcionar al menos un video o imagen de referencia para que la generación funcione.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo específico a utilizar para la generación de video. | COMBO | Sí | `"wan2.7-r2v"` |
| `model.prompt` | Prompt que describe el video. Usa identificadores como 'character1' y 'character2' para referirte a los personajes de referencia. | STRING | Sí | - |
| `model.negative_prompt` | Prompt negativo que describe lo que se debe evitar en el video generado (predeterminado: vacío). | STRING | No | - |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La duración del video generado en segundos (predeterminado: 5). | INT | Sí | 2 a 10 |
| `model.reference_videos` | Una lista de videos de referencia. Puedes agregar hasta 3 videos. | VIDEO | No | - |
| `model.reference_images` | Una lista de imágenes de referencia. Puedes agregar hasta 5 imágenes. | IMAGE | No | - |
| `semilla` | Semilla a utilizar para la generación, que ayuda a controlar la aleatoriedad del resultado (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `marca_de_agua` | Si se debe agregar una marca de agua generada por IA al resultado (predeterminado: False). Esta es una configuración avanzada. | BOOLEAN | No | - |

**Restricciones importantes:**
*   Debes proporcionar al menos un video de referencia o una imagen de referencia en las entradas `model.reference_videos` o `model.reference_images`.
*   El número total combinado de videos e imágenes de referencia no puede exceder de 5.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`
