# Kling Fotograma Inicial-Final a Video

Este nodo crea una secuencia de video que hace una transición entre las imágenes de inicio y fin proporcionadas. Genera todos los fotogramas intermedios para producir una transformación suave desde el primer fotograma hasta el último. Este nodo llama a la API de imagen a video, pero solo admite las opciones de entrada que funcionan con el campo de solicitud `image_tail`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `start_frame` | Imagen de referencia: cadena codificada en URL o Base64, no puede superar los 10MB, resolución no inferior a 300×300px, relación de aspecto entre 1:2.5 y 2.5:1. Base64 no debe incluir el prefijo `data:image`. | IMAGE | Sí | - |
| `end_frame` | Imagen de referencia: control del fotograma final. Cadena codificada en URL o Base64, no puede superar los 10MB, resolución no inferior a 300×300px. Base64 no debe incluir el prefijo `data:image`. | IMAGE | Sí | - |
| `prompt` | Indicación de texto positiva | STRING | Sí | - |
| `negative_prompt` | Indicación de texto negativa | STRING | Sí | - |
| `cfg_scale` | Controla la fuerza de la guía de la indicación (predeterminado: 0.5) | FLOAT | No | 0.0-1.0 |
| `aspect_ratio` | La relación de aspecto para el video generado (predeterminado: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuración a utilizar para la generación de video siguiendo el formato: modo / duración / nombre_del_modelo. (predeterminado: "pro mode / 5s duration / kling-v2-5-turbo"). Todas las opciones disponibles usan el modo pro con el modelo kling-v2-5-turbo y solo se diferencian en la duración del video. | COMBO | No | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Restricciones de imagen:**

- Tanto `start_frame` como `end_frame` deben proporcionarse y no pueden superar un tamaño de archivo de 10MB.
- Resolución mínima: 300×300 píxeles para ambas imágenes.
- La relación de aspecto de `start_frame` debe estar entre 1:2.5 y 2.5:1.
- Las imágenes codificadas en Base64 no deben incluir el prefijo "data:image".

**Restricciones de la indicación:**

- La indicación positiva no debe estar vacía.
- Tanto la indicación positiva como la negativa están limitadas a 500 caracteres.
- Si `negative_prompt` se deja vacío, se omite en la solicitud.

**Precios:**

- "pro mode / 5s duration / kling-v2-5-turbo": $0.35 USD por generación.
- "pro mode / 10s duration / kling-v2-5-turbo": $0.70 USD por generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|---------------|
| `output` | La secuencia de video generada | VIDEO |
| `video_id` | Identificador único del video generado | STRING |
| `duration` | Duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
