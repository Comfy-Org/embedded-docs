> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/es.md)

Este nodo genera un video con una persona u objeto basado en materiales de referencia proporcionados. Utiliza el modelo Wan 2.7 para crear videos a partir de un prompt de texto, compatible con actuaciones de un solo personaje e interacciones de múltiples personajes. Debes proporcionar al menos un video o imagen de referencia para que la generación funcione.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"wan2.7-r2v"` | El modelo específico a utilizar para la generación de video. |
| `model.prompt` | STRING | Sí | - | Prompt que describe el video. Usa identificadores como 'character1' y 'character2' para referirte a los personajes de referencia. |
| `model.negative_prompt` | STRING | No | - | Prompt negativo que describe lo que se debe evitar en el video generado (predeterminado: vacío). |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. |
| `model.ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video de salida. |
| `model.duration` | INT | Sí | 2 a 10 | La duración del video generado en segundos (predeterminado: 5). |
| `model.reference_videos` | VIDEO | No | - | Una lista de videos de referencia. Puedes agregar hasta 3 videos. |
| `model.reference_images` | IMAGE | No | - | Una lista de imágenes de referencia. Puedes agregar hasta 5 imágenes. |
| `semilla` | INT | No | 0 a 2147483647 | Semilla a utilizar para la generación, que ayuda a controlar la aleatoriedad del resultado (predeterminado: 0). |
| `marca_de_agua` | BOOLEAN | No | - | Si se debe agregar una marca de agua generada por IA al resultado (predeterminado: False). Esta es una configuración avanzada. |

**Restricciones importantes:**
*   Debes proporcionar al menos un video de referencia o una imagen de referencia en las entradas `model.reference_videos` o `model.reference_images`.
*   El número total combinado de videos e imágenes de referencia no puede exceder de 5.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`
