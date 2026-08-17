# Kling Imagen a Video

El nodo Kling Image to Video genera un video a partir de una imagen de referencia inicial utilizando indicaciones de texto. Usa la imagen como primer fotograma y crea una secuencia de video basada en descripciones de texto positivas y negativas, con opciones configurables para modelo, duración, modo de generación y relación de aspecto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `start_frame` | La imagen de referencia utilizada para generar el video. Debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1. | IMAGE | Sí | - |
| `prompt` | Indicación de texto positiva. Máximo 500 caracteres. | STRING | Sí | - |
| `negative_prompt` | Indicación de texto negativa. Máximo 500 caracteres. Puede dejarse vacía. | STRING | Sí | - |
| `model_name` | El modelo utilizado para la generación de video (predeterminado: `"kling-v2-5-turbo"`). | COMBO | Sí | `"kling-v2-5-turbo"` |
| `cfg_scale` | Controla cuán fielmente el video sigue la indicación. Los valores más altos significan una adherencia más fuerte (predeterminado: 0.8). | FLOAT | Sí | 0.0 a 1.0 |
| `mode` | El modo de generación (predeterminado: `"pro"`). | COMBO | Sí | `"pro"` |
| `aspect_ratio` | La relación de aspecto del video generado (predeterminado: `"16:9"`). | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La duración del video generado en segundos (predeterminado: `"5"`). | COMBO | Sí | `"5"`<br>`"10"` |

Nota: La indicación positiva no debe estar vacía. Tanto la indicación positiva como la negativa están limitadas a 500 caracteres. La imagen de entrada debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado. | VIDEO |
| `video_id` | Identificador único del video generado. | STRING |
| `duration` | Duración del video generado. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
