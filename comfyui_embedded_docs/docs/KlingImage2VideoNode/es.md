# Kling Imagen a Video

El nodo Kling Imagen a Video genera un video a partir de una imagen de referencia inicial utilizando indicaciones de texto. Toma una imagen como primer fotograma y crea una secuencia de video basada en descripciones de texto positivas y negativas, con opciones configurables para modelo, duración, relación de aspecto y modo de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `start_frame` | La imagen de referencia utilizada para generar el video. | IMAGE | Sí | - |
| `prompt` | Indicación de texto positiva. | STRING | Sí | - |
| `negative_prompt` | Indicación de texto negativa. | STRING | Sí | - |
| `model_name` | El modelo utilizado para la generación de video (predeterminado: `"kling-v2-master"`). | COMBO | Sí | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` |
| `cfg_scale` | Controla qué tan fielmente el video sigue la indicación. Valores más altos significan mayor adherencia (predeterminado: 0.8). | FLOAT | Sí | 0.0 a 1.0 |
| `mode` | El modo de generación. `"std"` es calidad estándar, `"pro"` es mayor calidad (predeterminado: `"std"`). | COMBO | Sí | `"std"`<br>`"pro"` |
| `aspect_ratio` | La relación de aspecto del video generado (predeterminado: `"16:9"`). | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La duración del video generado en segundos (predeterminado: `"5"`). | COMBO | Sí | `"5"`<br>`"10"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | El video generado como salida. | VIDEO |
| `duration` | Identificador único para el video generado. | STRING |
| `duration` | Información de duración del video generado. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/es.md)

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
