# MiniMaxH3AddGuide

Este nodo fija una imagen, un clip corto, audio o un clip con su banda sonora en cualquier fotograma elegido de un video MiniMax H3. Añade un fotograma clave guía al condicionamiento en el índice de fotograma especificado, y puede encadenar varios de estos nodos para fijar varios fotogramas en el mismo video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `positive` | El condicionamiento al que se adjunta el fotograma clave guía. | CONDITIONING | Sí | - |
| `latent` | El latent de audio-video MiniMax H3 que define el video objetivo. Debe ser un latent AV MiniMax H3 (anidado, con dos tensores 5D de 24 canales cada uno). | LATENT | Sí | - |
| `frame_idx` | Índice de fotograma en el que anclar la imagen o el primer fotograma del clip. Los valores negativos se cuentan desde el final del video. (por defecto: 0) | INT | Sí | -9999 a 9999 |
| `vae` | VAE de video, necesario cuando se conecta una imagen. | VAE | No | - |
| `audio_vae` | VAE de audio, necesario cuando se conecta un audio. | VAE | No | - |
| `image` | Imagen o fotogramas de video para anclar. Los lotes de múltiples fotogramas se anclan como un clip y se recortan a las longitudes de clip válidas del modelo: 5, 22, 39... (17k + 5) fotogramas. Los lotes de menos de 5 fotogramas usan solo la primera imagen. | IMAGE | No | - |
| `audio` | Banda sonora para anclar a partir del mismo índice de fotograma, recortada a la duración restante del video. | AUDIO | No | - |

**Restricciones:**
- Debe proporcionarse al menos uno de `image` o `audio`; de lo contrario, el nodo genera un error.
- `vae` es obligatorio cuando se conecta `image`.
- `audio_vae` es obligatorio cuando se conecta `audio`.
- Los lotes de `image` con menos de 5 fotogramas usan solo la primera imagen; los lotes de 5 o más fotogramas se recortan a una longitud de clip válida (5, 22, 39, etc.).
- `frame_idx` debe colocar la guía dentro del rango de fotogramas del video, y un clip de múltiples fotogramas debe caber completamente en el video; de lo contrario, el nodo genera un error.
- Cuando se conecta audio, el índice de fotograma no debe estar más allá del final de la pista de audio del video.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | El condicionamiento con el fotograma clave guía añadido, que contiene el índice de fotograma resuelto y, cuando se proporcionan, los latents codificados de imagen o audio. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/es.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
