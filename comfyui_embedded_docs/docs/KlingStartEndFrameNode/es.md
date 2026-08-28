# Kling Fotograma Inicial-Final a Video

Este nodo crea una secuencia de video que hace la transición entre las imágenes de inicio y fin proporcionadas. Genera todos los fotogramas intermedios para producir una transformación suave del primer al último fotograma. Este nodo llama a la API de imagen a video, pero solo admite las opciones de entrada que funcionan con el campo de solicitud `image_tail`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Imagen de referencia: URL o cadena codificada en Base64, no puede superar los 10 MB, resolución no inferior a 300×300 píxeles, relación de aspecto entre 1:2.5 y 2.5:1. El Base64 no debe incluir el prefijo data:image. | IMAGE | Sí | - |
| `end_frame` | Imagen de referencia: control del fotograma final. URL o cadena codificada en Base64, no puede superar los 10 MB, resolución no inferior a 300×300 píxeles. El Base64 no debe incluir el prefijo data:image. | IMAGE | Sí | - |
| `prompt` | Indicación de texto positiva. No debe estar vacía y no puede superar los 500 caracteres. | STRING | Sí | - |
| `negative_prompt` | Indicación de texto negativa. No puede superar los 500 caracteres. Si se deja vacía, se omite de la solicitud. | STRING | Sí | - |
| `cfg_scale` | Controla la intensidad de la guía de la indicación (valor por defecto: 0.5) | FLOAT | Sí | 0.0-1.0 |
| `aspect_ratio` | La relación de aspecto del video generado (valor por defecto: "16:9") | COMBO | Sí | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuración a utilizar para la generación de video, con el formato: modo / duración / nombre del modelo. (Valor por defecto: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Sí | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Restricciones de las imágenes:**

- Tanto `start_frame` como `end_frame` son obligatorios y no pueden superar los 10 MB de tamaño de archivo.
- Resolución mínima: 300×300 píxeles para ambas imágenes.
- La relación de aspecto de `start_frame` debe estar entre 1:2.5 y 2.5:1.
- Las imágenes codificadas en Base64 no deben incluir el prefijo "data:image".

**Restricciones de las indicaciones:**

- `prompt` no debe estar vacío y no puede superar los 500 caracteres.
- `negative_prompt` no puede superar los 500 caracteres; cuando está vacío, no se envía con la solicitud.

**Notas sobre el modo:**

- Ambas opciones de modo utilizan el modo pro con el modelo kling-v2-5-turbo y solo difieren en la duración (5 segundos o 10 segundos).
- Precio por generación, como se muestra en la insignia de precio del nodo: el modo de 5s cuesta $0.35 USD y el modo de 10s cuesta $0.70 USD.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La secuencia de video generada | VIDEO |
| `video_id` | Identificador único del video generado | STRING |
| `duration` | Duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
