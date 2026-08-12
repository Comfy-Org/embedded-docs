# MiniMax H3 Imagen a Video

Este nodo prepara el condicionamiento y el latente vacío necesarios para generar un video con el modelo MiniMax H3. Toma un prompt de texto y, opcionalmente, imágenes para el primer y/o último fotograma del video, y los convierte en entradas del modelo. Las imágenes clave se redimensionan, se codifican y se adjuntan al condicionamiento al inicio y al final del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Range |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar las imágenes clave en el condicionamiento. | CLIP | Sí |  |
| `vae` | Modelo VAE utilizado para codificar las imágenes clave al espacio latente cuando se proporcionan imágenes clave. | VAE | Sí |  |
| `prompt` | Prompt de texto que describe el video a generar. Admite múltiples líneas y prompts dinámicos. | STRING | Sí |  |
| `ancho` | Ancho del video en píxeles (predeterminado: 1344). | INT | Sí | 32 a MAX_RESOLUTION (paso 32) |
| `alto` | Alto del video en píxeles (predeterminado: 768). | INT | Sí | 32 a MAX_RESOLUTION (paso 32) |
| `duración` | Número de fotogramas a 24 fps, ajustado al alza a la cuadrícula 17k+5 del modelo (124 = ~5s; el rango entrenado es ~124-362, más largo no está probado) (predeterminado: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `primer_fotograma` | Imagen opcional utilizada como primer fotograma del video. Se estira al tamaño completo del lienzo, por lo que no se conserva su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |
| `último_fotograma` | Imagen opcional utilizada como último fotograma del video. Se recorta para cubrir el lienzo conservando su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |

Cuando se proporcionan `first_frame` y/o `last_frame`, las imágenes clave se codifican con el VAE y se adjuntan al condicionamiento en el fotograma 0 y en el último fotograma, respectivamente. Cuando no se proporciona ninguno, el nodo funciona únicamente con el prompt.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | Condicionamiento que contiene el prompt codificado y, cuando se proporcionan imágenes clave, las imágenes clave codificadas y el número de fotogramas para el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vacío que representa el video a generar, con el ancho, alto y número de fotogramas solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `46efc87bd46f4a86cb6df37c75f960419a2a98b34480e7dc0023c9d87903870b`
