> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/es.md)

El nodo Kling Omni Editar Video (Pro) utiliza un modelo de IA para editar un video existente basándose en una descripción textual. Proporcionas un video de origen y un prompt, y el nodo genera un nuevo video de la misma duración con los cambios solicitados. Opcionalmente, puede usar imágenes de referencia para guiar el estilo y conservar el audio original del video de origen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` | El modelo de IA a utilizar para la edición de video (predeterminado: `"kling-v3-omni"`). |
| `prompt` | STRING | Sí | | Una descripción textual del contenido del video. Puede incluir tanto descripciones positivas como negativas. |
| `video` | VIDEO | Sí | | Video para editar. La duración del video de salida será la misma. |
| `mantener_sonido_original` | BOOLEAN | Sí | | Determina si se conserva el audio original del video de entrada en la salida (predeterminado: True). |
| `imágenes_referencia` | IMAGE | No | | Hasta 4 imágenes de referencia adicionales. |
| `resolución` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución del video de salida (predeterminado: `"1080p"`). |
| `semilla` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). |

**Restricciones y limitaciones:**

* El `prompt` debe tener entre 1 y 2500 caracteres de longitud.
* El `video` de entrada debe tener una duración de entre 3.0 y 10.05 segundos.
* Las dimensiones del `video` de entrada deben estar entre 720x720 y 2160x2160 píxeles.
* Se puede proporcionar un máximo de 4 `reference_images` cuando se utiliza un video.
* Cada `reference_image` debe tener al menos 300x300 píxeles.
* Cada `reference_image` debe tener una relación de aspecto entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El video editado generado por el modelo de IA. |

---
**Source fingerprint (SHA-256):** `ddc3fdc8c97cdcdd34f16a0916b13ffe6adeb46e58e2933516c9a6aef7c36730`
