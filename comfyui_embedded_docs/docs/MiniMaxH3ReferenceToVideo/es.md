# MiniMax H3 Referencia a Video

MiniMax H3 Reference to Video crea el condicionamiento de texto y el latent de video vacío necesarios para la generación de video con referencia a MiniMax H3. Debe proporcionar un prompt junto con imágenes, videos y clips de audio de referencia opcionales, y el nodo codifica estas referencias en tokens que el modelo puede usar durante la generación. El prompt se refiere a las referencias con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar los medios de referencia en tokens de condicionamiento. | CLIP | Sí | |
| `vae` | VAE utilizado para codificar imágenes de referencia y fotogramas de video de referencia en el espacio latente. | VAE | Sí | |
| `audio_vae` | VAE utilizado para codificar el audio de referencia en el espacio latente (frecuencia de muestreo de audio de 32 kHz). | VAE | Sí | |
| `prompt` | Prompt de texto para el video. Los medios de referencia se pueden referenciar con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>` (indexadas desde 1 por tipo). Admite prompts multilínea y dinámicos. | STRING | Sí | |
| `ancho` | Ancho del video generado en píxeles (predeterminado: 1344). | INT | Sí | 32 a 16384 (paso 32) |
| `alto` | Alto del video generado en píxeles (predeterminado: 768). | INT | Sí | 32 a 16384 (paso 32) |
| `duración` | Número de fotogramas a 24 fps; 124 = ~5s, el rango entrenado es ~124-362 (predeterminado: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `tamaño_imagen_ref` | Modo de dimensionamiento de la imagen de referencia. `match` reduce la escala de cada imagen de referencia únicamente, manteniendo la relación de aspecto, al área de píxeles de la generación; `max` utiliza el borde corto de 2048px del pipeline de referencia para una mejor fidelidad de identidad. Los tokens de referencia viajan a través de cada paso de muestreo, por lo que `max` puede ser varias veces más lento (predeterminado: `match`). | COMBO | Sí | `"match"`<br>`"max"` |
| `imágenes_ref` | Imágenes de referencia opcionales. Cada imagen se reduce a un borde corto de 2048px si es más grande y nunca se aumenta de escala. Se pueden proporcionar múltiples imágenes. | IMAGE | No | 0 a 9 |
| `videos_ref` | Fotogramas de video de referencia opcionales a 24 fps (2-15s). Se pueden proporcionar múltiples videos. | IMAGE | No | 0 a 3 |
| `audios_video_ref` | Bandas sonoras opcionales emparejadas con los videos de referencia por índice; `ref_video_audio_N` es la banda sonora del `ref_video_N` del mismo número. | AUDIO | No | 0 a 3 |
| `audios_ref` | Clips de audio de referencia independientes opcionales. | AUDIO | No | 0 a 3 |

Notas:
- El prompt se refiere a los medios de referencia con etiquetas indexadas desde 1 por tipo: `<Picture i>` para imágenes, `<Video k>` para videos y `<Audio j>` para audio. Las referencias se presentan al modelo en un orden fijo: imágenes, luego videos (con la etiqueta `<Audio j>` de cada banda sonora justo antes de su `<Video k>`), y luego audio independiente.
- Los videos de referencia deben contener al menos 5 fotogramas (~0.2 segundos a 24 fps); de lo contrario, el nodo genera un error. Los fotogramas de video también se limitan al `length` seleccionado y se recortan a un número de fotogramas compatible.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | Condicionamiento que contiene el prompt codificado junto con los tokens codificados de imagen, video y audio de referencia utilizados por el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latent de audio-video vacío en el `ancho`, `alto` y `duración` solicitados (número de fotogramas). | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `529e51c5c9c63a94176a15851f40ac42f7bd93e7d7c6ad334ed22aa29d04dfde`
