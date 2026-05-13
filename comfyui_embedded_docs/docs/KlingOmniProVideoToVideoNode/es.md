> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/es.md)

Este nodo utiliza el modelo Kling AI para generar un nuevo video basado en un video de entrada e imágenes de referencia opcionales. Proporcionas un prompt de texto que describe el contenido deseado, y el nodo transforma el video de referencia en consecuencia. También puede incorporar hasta cuatro imágenes de referencia adicionales para guiar el estilo y el contenido del resultado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` | El modelo Kling específico a utilizar para la generación de video (predeterminado: "kling-v3-omni"). |
| `prompt` | STRING | Sí | N/A | Un prompt de texto que describe el contenido del video. Puede incluir descripciones tanto positivas como negativas. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación de aspecto deseada para el video generado. |
| `duration` | INT | Sí | 3 a 10 | La duración del video generado en segundos (predeterminado: 3). |
| `reference_video` | VIDEO | Sí | N/A | Video a utilizar como referencia. |
| `keep_original_sound` | BOOLEAN | Sí | N/A | Determina si se conserva el audio del video de referencia en la salida (predeterminado: True). |
| `reference_images` | IMAGE | No | N/A | Hasta 4 imágenes de referencia adicionales. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución para el video generado (predeterminado: "1080p"). |
| `semilla` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). |

**Restricciones de los Parámetros:**

* El `prompt` debe tener entre 1 y 2500 caracteres de longitud.
* El `reference_video` debe tener una duración entre 3.0 y 10.05 segundos.
* El `reference_video` debe tener dimensiones entre 720x720 y 2160x2160 píxeles.
* Se puede proporcionar un máximo de 4 `reference_images`. Cada imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video recién generado. |

---
**Source fingerprint (SHA-256):** `1bed976530603bcf7db67048e89ad6adac218fba8597744f8ece3e16a2ee4993`
