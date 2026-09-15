# KlingSingleImageVideoEffectNode

El nodo Kling Single Image Video Effect crea videos con diferentes efectos especiales basados en una única imagen de referencia. Aplica diversos efectos visuales y escenas para transformar imágenes estáticas en contenido de video dinámico. El nodo admite diferentes escenas de efectos, opciones de modelo y duraciones de video para lograr el resultado visual deseado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | Imagen de referencia. URL o cadena codificada en Base64 (sin el prefijo data:image). El tamaño del archivo no puede exceder 10MB, la resolución no debe ser inferior a 300x300px, la relación de aspecto debe estar entre 1:2.5 y 2.5:1 | IMAGE | Sí | - |
| `effect_scene` | El tipo de escena de efecto especial que se aplicará a la generación del video. Algunos efectos pueden tener diferentes precios. | COMBO | Sí | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | La versión específica del modelo que se usará para generar el efecto de video. | COMBO | Sí | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | La duración del video generado en segundos. | COMBO | Sí | `"5"`<br>`"10"` |

**Nota:** El parámetro `effect_scene` afecta el precio del nodo. Los efectos `dizzydizzy` y `bloombloom` cuestan $0.49 USD por generación, mientras que todos los demás efectos cuestan $0.28 USD por generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado con los efectos aplicados | VIDEO |
| `video_id` | El identificador único del video generado | STRING |
| `duration` | La duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/es.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
