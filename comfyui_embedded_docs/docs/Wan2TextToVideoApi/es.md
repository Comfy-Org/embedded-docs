# Wan 2.7 Texto a Video

Este nodo genera un video a partir de una descripción de texto utilizando el modelo Wan 2.7. Envía tu solicitud a una API externa, que procesa el prompt y devuelve un archivo de video. Opcionalmente, puedes proporcionar un clip de audio para influir en el movimiento y la sincronización del video.

## Entradas

Las entradas incluyen configuraciones comunes y configuraciones específicas del modelo que aparecen cuando se selecciona el modelo `wan2.7-t2v`.

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model` | El modelo específico a utilizar para la generación de video. | COMBO | Sí | `"wan2.7-t2v"` |
| `audio` | Audio para impulsar la generación de video (por ejemplo, sincronización de labios, movimiento ajustado al ritmo). Duración: 3s-30s. Si no se proporciona, el modelo genera automáticamente música de fondo o efectos de sonido a juego. | AUDIO | No | - |
| `seed` | Semilla a utilizar para la generación (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `prompt_extend` | Si se debe mejorar el prompt con asistencia de IA (predeterminado: True). | BOOLEAN | No | - |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False). | BOOLEAN | No | - |

### Entradas de wan2.7-t2v

Estas configuraciones aparecen cuando se selecciona el modelo `wan2.7-t2v`.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. | STRING | Sí | - |
| `negative_prompt` | Prompt negativo que describe lo que se debe evitar. | STRING | No | - |
| `resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La duración del video en segundos (predeterminado: 5). | INT | Sí | 2 a 15 |

**Nota:** La entrada `prompt` no debe estar vacía. La entrada `audio` es opcional; si se proporciona, su duración debe estar entre 1.5 y 60 segundos. Si se omite, el modelo genera automáticamente audio a juego. Cuando `negative_prompt` se deja vacío, no se envía a la API. `prompt_extend` y `watermark` son opciones avanzadas.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
