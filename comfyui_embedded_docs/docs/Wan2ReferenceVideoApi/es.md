# Wan 2.7 Referencia a Video

Este nodo genera un video que presenta a una persona u objeto basado en los materiales de referencia proporcionados. Utiliza el modelo Wan 2.7 para crear videos a partir de un prompt de texto, admitiendo actuaciones de un solo personaje e interacciones de múltiples personajes. Debe proporcionar al menos un video de referencia o imagen de referencia para que la generación funcione.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo específico a utilizar para la generación de videos. | DYNAMIC_COMBO | Sí | "wan2.7-r2v" |
| `seed` | Semilla para usar en la generación, que ayuda a controlar la aleatoriedad del resultado (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False). Esta es una configuración avanzada. | BOOLEAN | Sí | True<br>False |

### wan2.7-r2v Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt que describe el video. Use identificadores como 'character1' y 'character2' para referirse a los personajes de referencia. Debe contener al menos un personaje. | STRING | Sí | - |
| `negative_prompt` | Prompt negativo que describe lo que se debe evitar (predeterminado: vacío). | STRING | No | - |
| `resolution` | La resolución del video de salida. | COMBO | Sí | "720P"<br>"1080P" |
| `ratio` | La relación de aspecto del video de salida. | COMBO | Sí | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | La duración del video generado en segundos (predeterminado: 5). | INT | Sí | 2 a 10 |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `reference_videos` | Ranura ampliable: conecte hasta 3 videos de referencia (ranuras `video1` a `video3`). Se requiere al menos un video o imagen de referencia en total. | VIDEO | No | 0 a 3 elementos |
| `reference_images` | Ranura ampliable: conecte hasta 5 imágenes de referencia (ranuras `image1` a `image5`). Se requiere al menos un video o imagen de referencia en total. | IMAGE | No | 0 a 5 elementos |

**Restricciones importantes:**

* Debe proporcionar al menos un video de referencia o imagen de referencia en las entradas `model.reference_videos` o `model.reference_images`.
* El número total combinado de videos e imágenes de referencia no puede superar 5.
* La entrada `model.prompt` debe contener al menos un personaje.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
