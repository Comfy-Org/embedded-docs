# Wan 2.7 Referencia a Video

Este nodo genera un video de una persona u objeto basado en los materiales de referencia proporcionados. Utiliza el modelo Wan 2.7 para crear videos a partir de una instrucción de texto, con soporte para actuaciones de un solo personaje e interacciones de múltiples personajes. Debe proporcionar al menos un video de referencia o una imagen de referencia para que la generación funcione.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo específico a utilizar para la generación de video. | DYNAMIC_COMBO | Sí | "wan2.7-r2v" |
| `semilla` | Semilla a utilizar para la generación, que ayuda a controlar la aleatoriedad de la salida (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `marca_de_agua` | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False). Esta es una configuración avanzada. | BOOLEAN | No | True<br>False |

### Entradas de wan2.7-r2v

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Instrucción que describe el video. Use identificadores como 'character1' y 'character2' para referirse a los personajes de referencia. Debe contener al menos un personaje. | STRING | Sí | - |
| `prompt_negativo` | Instrucción negativa que describe qué evitar (predeterminado: vacío). | STRING | No | - |
| `resolución` | La resolución del video de salida. | COMBO | Sí | "720P"<br>"1080P" |
| `relación` | La relación de aspecto del video de salida. | COMBO | Sí | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duración` | La duración del video generado en segundos (predeterminado: 5). | INT | Sí | 2 a 10 |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model.reference_videos` | Ranura ampliable: conecte hasta 3 videos de referencia (slots `video1` a `video3`). Se requiere al menos un video de referencia o imagen en total. | VIDEO | No | 0 a 3 elementos |
| `model.reference_images` | Ranura ampliable: conecte hasta 5 imágenes de referencia (slots `image1` a `image5`). Se requiere al menos un video de referencia o imagen en total. | IMAGE | No | 0 a 5 elementos |

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
