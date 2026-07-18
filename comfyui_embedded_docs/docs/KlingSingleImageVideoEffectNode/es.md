El Nodo de Efecto de Video a partir de una Imagen Única de Kling crea videos con diferentes efectos especiales basados en una sola imagen de referencia. Aplica diversos efectos visuales y escenas para transformar imágenes estáticas en contenido de video dinámico. El nodo admite diferentes escenas de efectos, opciones de modelo y duraciones de video para lograr el resultado visual deseado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Imagen de referencia. URL o cadena codificada en Base64 (sin el prefijo data:image). El tamaño del archivo no puede superar los 10 MB, la resolución no debe ser inferior a 300x300 px y la relación de aspecto debe estar entre 1:2.5 y 2.5:1 | IMAGE | Sí | - |
| `effect_scene` | El tipo de escena de efecto especial que se aplicará a la generación del video. Algunos efectos pueden tener precios diferentes. | COMBO | Sí | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | La versión específica del modelo que se utilizará para generar el efecto de video. | COMBO | Sí | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duración` | La duración del video generado en segundos. | COMBO | Sí | `"5"`<br>`"10"` |

**Nota:** El parámetro `effect_scene` afecta el precio del nodo. Los efectos `dizzydizzy` y `bloombloom` cuestan $0.49 USD por generación, mientras que todos los demás efectos cuestan $0.28 USD por generación.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | El video generado con los efectos aplicados | VIDEO |
| `video_id` | El identificador único del video generado | STRING |
| `duración` | La duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/es.md)

---
**Source fingerprint (SHA-256):** `519db2f7185f200140c746bdebf89383523e0342bbfb61538adac063295d365d`
