# Wan 2.7 Imagen a Video

El nodo Wan 2.7 Image to Video genera un video a partir de una imagen de primer fotograma. Opcionalmente, puedes proporcionar una imagen de último fotograma para crear una transición entre ambos, o proporcionar un archivo de audio para guiar el movimiento y la sincronización del video. El nodo utiliza un modelo de IA para animar la escena según tu descripción de texto.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA que se usará para la generación de video. | DYNAMIC_COMBO | Sí | `"wan2.7-i2v"` |
| `primer_fotograma` | Imagen del primer fotograma. La relación de aspecto de salida se deriva de esta imagen. | IMAGE | Sí | - |
| `último_fotograma` | Imagen del último fotograma. El modelo genera un video que hace la transición del primer al último fotograma. | IMAGE | No | - |
| `audio` | Audio para guiar la generación del video (p. ej., sincronización de labios, movimiento sincronizado con el ritmo). Duración: 2s-30s. Si no se proporciona, el modelo genera automáticamente música de fondo o efectos de sonido acordes. | AUDIO | No | - |
| `semilla` | Semilla para usar en la generación (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `extender_prompt` | Si se debe mejorar el prompt con asistencia de IA (predeterminado: True). Esta es una configuración avanzada. | BOOLEAN | Sí | True<br>False |
| `marca_de_agua` | Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False). Esta es una configuración avanzada. | BOOLEAN | Sí | True<br>False |

### Entradas de wan2.7-i2v

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. | STRING | Sí | - |
| `negative_prompt` | Prompt negativo que describe lo que se debe evitar. | STRING | Sí | - |
| `resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `duration` | La duración del video generado en segundos (predeterminado: 5). | INT | Sí | 2 a 15 |

**Nota:** La entrada `audio` tiene una restricción de duración. Si se proporciona, el archivo de audio debe tener entre 2 y 30 segundos de duración.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
