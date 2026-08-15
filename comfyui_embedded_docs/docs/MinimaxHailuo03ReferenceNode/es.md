# MiniMax H3 Referencia a Video

Este nodo genera un video utilizando el modelo MiniMax H3, empleando imágenes, videos y audio de referencia para condicionar el resultado. Las referencias se mencionan en la indicación según su orden de conexión: "Image 1", "Image 2", "Video 1", "Audio 1", y así sucesivamente.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | Modelo a utilizar para la generación de video (predeterminado: "MiniMax H3"). Al seleccionar "MiniMax H3" se proporcionan los ajustes `prompt`, `resolution`, `ratio`, `duration`, `reference_images`, `reference_videos` y `reference_audios` que aparecen a continuación. | DYNAMIC_COMBO | Sí | "MiniMax H3" |
| `semilla` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos (predeterminado: 42). | INT | Sí | 0 a 4294967295 |
| `marca de agua` | Indica si se debe añadir una marca de agua AIGC al video (predeterminado: false). | BOOLEAN | No | true<br>false |

### Entradas de MiniMax H3

Estas entradas aparecen cuando se selecciona "MiniMax H3" como modelo.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Indicación de texto para la generación de video. Se puede hacer referencia a los medios de referencia por su orden, por ejemplo, "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sí | Longitud mínima: 1 carácter |
| `resolution` | Resolución del video de salida (predeterminado: "768P"). | STRING | Sí | "768P"<br>"2K" |
| `ratio` | Relación de aspecto del video de salida (predeterminado: "adaptive"). | STRING | Sí | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duración del video de salida en segundos (predeterminado: 5). | INT | Sí | 4 a 15 |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `reference_images` | Ranura ampliable: conecte de 1 a 9 elementos (`image_1`...`image_9`). Imágenes de referencia de sujeto o estilo, a las que se hace referencia en la indicación como "Image 1".."Image 9" en orden de conexión. Hasta 9 imágenes. | IMAGE | No | 0 a 9 imágenes |
| `reference_videos` | Ranura ampliable: conecte de 1 a 3 elementos (`video_1`...`video_3`). Videos de referencia de movimiento o escena, a los que se hace referencia en la indicación como "Video 1".."Video 3" en orden de conexión. Hasta 3 videos, de 2 a 15 segundos cada uno, 15 segundos en total. | VIDEO | No | 0 a 3 videos |
| `reference_audios` | Ranura ampliable: conecte de 1 a 3 elementos (`audio_1`...`audio_3`). Referencias de audio, a las que se hace referencia en la indicación como "Audio 1".."Audio 3" en orden de conexión. Hasta 3 clips, de 2 a 15 segundos cada uno, 15 segundos en total. No se puede utilizar sin una imagen o video de referencia. | AUDIO | No | 0 a 3 clips |

### Restricciones de parámetros

- Se requiere al menos una imagen de referencia o un video de referencia. No se acepta audio de referencia por sí solo.
- Cada imagen de referencia debe tener una relación de aspecto entre aproximadamente 0.4 y 2.5 (2:5 a 5:2) y un ancho y alto mínimos de 256 píxeles.
- Cada video de referencia debe tener una duración de entre 2 y 15 segundos, con una frecuencia de cuadros entre 23.976 y 60 FPS. La duración total de todos los videos de referencia no puede superar los 15 segundos.
- Cada clip de audio de referencia debe tener una duración de entre 2 y 15 segundos. La duración total de todos los clips de audio de referencia no puede superar los 15 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `f7e9c68addda6b48a2366139ecfa28ee57e6cda4aa5cd775c2d769517366573f`
