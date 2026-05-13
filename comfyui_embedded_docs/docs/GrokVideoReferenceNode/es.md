> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/es.md)

El nodo Grock Referencia a Video genera un video basado en un prompt de texto, utilizando hasta siete imágenes de referencia para guiar el estilo y contenido del resultado. Se conecta a una API externa para crear el video, el cual luego se descarga y se devuelve.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción textual del video deseado. |
| `model` | COMBO | Sí | `"grok-imagine-video"` | El modelo a utilizar para la generación del video. |
| `model.reference_images` | IMAGE | Sí | 1 a 7 imágenes | Hasta 7 imágenes de referencia para guiar la generación del video. |
| `model.resolution` | COMBO | Sí | `"480p"`<br>`"720p"` | La resolución del video de salida. |
| `model.aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | La relación de aspecto del video de salida. |
| `model.duration` | INT | Sí | 2 a 10 | La duración del video de salida en segundos (predeterminado: 6). |
| `seed` | INT | No | 0 a 2147483647 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). |

**Nota:** El parámetro `model` es un grupo que contiene `reference_images`, `resolution`, `aspect_ratio` y `duration`. Debes proporcionar al menos una imagen de referencia y puedes proporcionar hasta siete.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
