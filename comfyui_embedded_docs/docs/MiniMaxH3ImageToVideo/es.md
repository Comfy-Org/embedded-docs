# MiniMax H3 Imagen a Video

Este nodo prepara el condicionamiento y el latente vacío necesarios para generar un video con el modelo MiniMax H3. Toma un prompt de texto y, opcionalmente, imágenes para el primer y/o último fotograma del video, y los convierte en entradas del modelo. Las imágenes de los fotogramas clave se redimensionan, se codifican y se adjuntan al condicionamiento al inicio y al final del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar las imágenes de los fotogramas clave en el condicionamiento. | CLIP | Sí |  |
| `vae` | Modelo VAE utilizado para codificar las imágenes de los fotogramas clave en el espacio latente cuando se proporcionan imágenes de fotogramas clave. | VAE | Sí |  |
| `prompt` | Prompt de texto que describe el video a generar. Admite múltiples líneas y prompts dinámicos. | STRING | Sí |  |
| `ancho` | Ancho del video en píxeles (predeterminado: 1344). | INT | Sí | 32 a MAX_RESOLUTION (paso 32) |
| `alto` | Altura del video en píxeles (predeterminado: 768). | INT | Sí | 32 a MAX_RESOLUTION (paso 32) |
| `duración` | Número de fotogramas a 24 fps, redondeado hacia arriba a la cuadrícula 17k+5 del modelo (124 = ~5 s; el rango entrenado es ~124-362, las duraciones mayores no han sido probadas) (predeterminado: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `primer_fotograma` | Imagen opcional utilizada como primer fotograma del video. Se estira al tamaño completo del lienzo, por lo que no se conserva su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |
| `último_fotograma` | Imagen opcional utilizada como último fotograma del video. Se recorta para cubrir el lienzo conservando su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |

Cuando se proporcionan `first_frame` y/o `last_frame`, las imágenes de los fotogramas clave se codifican con el VAE y se adjuntan al condicionamiento en el fotograma 0 y en el fotograma final, respectivamente. Cuando no se proporciona ninguno, el nodo trabaja solamente con el prompt. El `length` solicitado se redondea hacia arriba al número de fotogramas válido más cercano (17k + 5), por lo que el número efectivo de fotogramas puede ser ligeramente superior al solicitado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | Condicionamiento que contiene el prompt codificado y, cuando se proporcionan imágenes de fotogramas clave, los fotogramas clave codificados y el número de fotogramas para el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente de audio-video vacío que representa el contenido a generar, con el ancho, la altura y el número de fotogramas solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
