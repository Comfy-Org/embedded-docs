# MiniMax H3 Referencia a Video

El nodo MiniMax H3 Reference to Video crea el condicionamiento de texto y el latent de audio-video vacío necesarios para la generación de video con referencia de MiniMax H3. Proporcionas un prompt más imágenes, videos y clips de audio de referencia opcionales, y el nodo codifica estas referencias en tokens que el modelo puede usar durante la generación. El prompt hace referencia a los medios de referencia con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar los medios de referencia en tokens de condicionamiento. | CLIP | Sí | |
| `vae` | VAE utilizado para codificar imágenes de referencia y fotogramas de video de referencia en el espacio latente. | VAE | Sí | |
| `audio_vae` | VAE utilizado para codificar audio de referencia en el espacio latente. El audio se vuelve a muestrear a la tasa de muestreo del VAE de audio (32 kHz por defecto). | VAE | Sí | |
| `prompt` | Prompt de texto para el video. Los medios de referencia se pueden direccionar con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>` (basadas en 1 por tipo). Admite prompts multilínea y dinámicos. | STRING | Sí | |
| `ancho` | Ancho del video generado en píxeles (predeterminado: 1344). | INT | Sí | 32 a 16384 (paso 32) |
| `alto` | Alto del video generado en píxeles (predeterminado: 768). | INT | Sí | 32 a 16384 (paso 32) |
| `duración` | Número de fotogramas a 24 fps; 124 = ~5 s, el rango entrenado es ~124-362 (predeterminado: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `tamaño_imagen_ref` | Ajuste de tamaño de las imágenes de referencia. `match` reduce cada imagen de referencia solo si es necesario, manteniendo la relación de aspecto, al área de píxeles de la generación; `max` utiliza el borde corto de 2048 px del pipeline de referencia para una mayor fidelidad de identidad. Los tokens de referencia permanecen durante cada paso de muestreo, por lo que `max` puede ser varias veces más lento (predeterminado: `match`). | COMBO | Sí | `"match"`<br>`"max"` |
| `imágenes_ref` | Ranura ampliable: conecta de 1 a 9 imágenes de referencia (`ref_image_1` ... `ref_image_9`). Cada imagen se reduce a un borde corto de 2048 px si es más grande y nunca se amplía. | IMAGE | No | 0 a 9 |
| `videos_ref` | Ranura ampliable: conecta de 1 a 3 videos de referencia (`ref_video_1` ... `ref_video_3`). Fotogramas de video de referencia a 24 fps (2-15 s). | IMAGE | No | 0 a 3 |
| `audios_video_ref` | Ranura ampliable: conecta de 1 a 3 bandas sonoras (`ref_video_audio_1` ... `ref_video_audio_3`). Banda sonora del video de referencia del mismo número. | AUDIO | No | 0 a 3 |
| `audios_ref` | Ranura ampliable: conecta de 1 a 3 clips de audio de referencia independientes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | No | 0 a 3 |

Notas:

- El prompt hace referencia a los medios de referencia con etiquetas basadas en 1 por tipo: `<Picture i>` para imágenes, `<Video k>` para videos y `<Audio j>` para audio. Las referencias se presentan al modelo en un orden fijo: primero las imágenes, luego los videos (con la etiqueta `<Audio j>` de cada banda sonora justo antes de su `<Video k>`), y finalmente el audio independiente.
- Los videos de referencia deben contener al menos 5 fotogramas (~0,2 segundos a 24 fps); de lo contrario, el nodo genera un error. Los fotogramas de video también se limitan al `length` seleccionado y se recortan a un número de fotogramas admitido.
- El `length` solicitado se alinea a un número de fotogramas admitido antes de que se cree el latent.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | Condicionamiento que contiene el prompt codificado junto con los tokens de imagen, video y audio de referencia codificados utilizados por el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latent de audio-video vacío con el `width`, `height` y `length` (número de fotogramas) solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
