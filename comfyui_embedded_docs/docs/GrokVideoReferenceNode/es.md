El nodo Grock Referencia a Video genera un video basado en un prompt de texto, utilizando hasta siete imágenes de referencia para guiar el estilo y contenido del resultado. Se conecta a una API externa para crear el video, el cual luego se descarga y se devuelve.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Descripción textual del video deseado. | STRING | Sí | N/A |
| `modelo` | El modelo a utilizar para la generación del video. | COMBO | Sí | `"grok-imagine-video"` |
| `model.reference_images` | Hasta 7 imágenes de referencia para guiar la generación del video. | IMAGE | Sí | 1 a 7 imágenes |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `model.aspect_ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `model.duration` | La duración del video de salida en segundos (predeterminado: 6). | INT | Sí | 2 a 10 |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

**Nota:** El parámetro `model` es un grupo que contiene `reference_images`, `resolution`, `aspect_ratio` y `duration`. Debes proporcionar al menos una imagen de referencia y puedes proporcionar hasta siete.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
