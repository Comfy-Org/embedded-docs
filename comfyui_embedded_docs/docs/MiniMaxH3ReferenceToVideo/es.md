# MiniMax H3 Referencia a Video

MiniMax H3 Reference to Video crea el condicionamiento de texto y el latente de audio-video vacío necesarios para la generación de referencia a video con MiniMax H3. Se proporciona un prompt junto con imágenes, videos y clips de audio de referencia opcionales, y el nodo codifica estas referencias en tokens que el modelo puede usar durante la generación. El prompt se refiere a las referencias con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>`.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar los medios de referencia en tokens de condicionamiento. | CLIP | Sí | |
| `vae` | VAE utilizado para codificar las imágenes de referencia y los fotogramas de video de referencia en el espacio latente. | VAE | Sí | |
| `audio_vae` | VAE utilizado para codificar el audio de referencia en el espacio latente (frecuencia de muestreo de audio de 32 kHz). | VAE | Sí | |
| `prompt` | Prompt de texto para el video. Los medios de referencia se pueden invocar con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>` (índice basado en 1 por tipo). Admite prompts de varias líneas y dinámicos. | STRING | Sí | |
| `width` | Ancho del video generado en píxeles (por defecto: 1344). | INT | Sí | 32 a 16384 (paso 32) |
| `height` | Alto del video generado en píxeles (por defecto: 768). | INT | Sí | 32 a 16384 (paso 32) |
| `length` | Número de fotogramas a 24 fps; 124 = ~5 s, el rango entrenado es de ~124-362 (por defecto: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `ref_image_size` | Modo de tamaño de la imagen de referencia. `match` solo reduce la escala de cada imagen de referencia, manteniendo la relación de aspecto, hasta el área de píxeles de la generación; `max` utiliza el borde corto de 2048 píxeles de la canalización de referencia para obtener la mejor fidelidad de identidad. Los tokens de referencia viajan a través de cada paso de muestreo, por lo que `max` puede ser varias veces más lento (por defecto: `match`). | COMBO | Sí | `"match"`<br>`"max"` |
| `ref_images` | Imágenes de referencia opcionales. Cada imagen se reduce a un borde corto de 2048 píxeles si es más grande y nunca se amplía. Se pueden proporcionar varias imágenes. | IMAGE | No | 0 a 9 |
| `ref_videos` | Fotogramas de video de referencia opcionales a 24 fps (2-15 s). Se pueden proporcionar varios videos. | IMAGE | No | 0 a 3 |
| `ref_video_audios` | Bandas sonoras opcionales emparejadas con los videos de referencia por índice; `ref_video_audio_N` es la banda sonora del `ref_video_N` con el mismo número. | AUDIO | No | 0 a 3 |
| `ref_audios` | Clips de audio de referencia independientes opcionales. | AUDIO | No | 0 a 3 |

Notas:
- El prompt se refiere a los medios de referencia con etiquetas basadas en 1 por tipo: `<Picture i>` para imágenes, `<Video k>` para videos y `<Audio j>` para audio. Las referencias se presentan al modelo en un orden fijo: imágenes, luego videos (con la etiqueta `<Audio j>` de cada banda sonora justo antes de su `<Video k>`), y luego el audio independiente.
- Los videos de referencia deben contener al menos 5 fotogramas (~0,2 segundos a 24 fps); de lo contrario, el nodo genera un error. Los fotogramas de video se limitan al `length` seleccionado y se recortan a un número de fotogramas compatible.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `positive` | Condicionamiento que contiene el prompt codificado junto con los tokens codificados de imagen, video y audio de referencia que usa el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente de audio-video vacío con el `width`, `height` y `length` (número de fotogramas) solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
