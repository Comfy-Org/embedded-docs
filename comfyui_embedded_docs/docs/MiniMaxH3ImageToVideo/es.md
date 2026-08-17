# MiniMax H3 Imagen a Video

MiniMax H3 Image to Video prepara el condicionamiento y el latente vacío necesarios para generar un video con el modelo MiniMax H3. Toma un prompt de texto y, opcionalmente, imágenes para el primer y/o último fotograma del video, y los convierte en entradas del modelo. Las imágenes de fotograma clave se redimensionan, codifican y se adjuntan al condicionamiento al inicio y al final del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
|-----------|-------------|---------------|-------------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar las imágenes de fotograma clave en condicionamiento. | CLIP | Sí |  |
| `vae` | Modelo VAE utilizado para codificar las imágenes de fotograma clave en el espacio latente cuando se proporcionan imágenes de fotograma clave. | VAE | Sí |  |
| `prompt` | Prompt de texto que describe el video a generar. Admite múltiples líneas y prompts dinámicos. | STRING | Sí |  |
| `width` | Ancho del video en píxeles (por defecto: 1344). | INT | Sí | 32 to MAX_RESOLUTION (step 32) |
| `height` | Alto del video en píxeles (por defecto: 768). | INT | Sí | 32 to MAX_RESOLUTION (step 32) |
| `length` | Número de fotogramas a 24 fps, redondeado hacia arriba a la cuadrícula 17k+5 del modelo (124 = ~5s; el rango entrenado es de ~124 a 362, no se ha probado con valores más largos) (por defecto: 124). | INT | Sí | 5 to 3600 (step 17) |
| `first_frame` | Imagen opcional utilizada como primer fotograma del video. Se estira al tamaño completo del lienzo, por lo que no se conserva su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |
| `last_frame` | Imagen opcional utilizada como último fotograma del video. Se recorta para cubrir el lienzo conservando su relación de aspecto. Solo se utiliza la primera imagen del lote de entrada. | IMAGE | No |  |

Cuando se proporcionan `first_frame` y/o `last_frame`, las imágenes de fotograma clave se codifican con el VAE y se adjuntan al condicionamiento en el fotograma 0 y en el fotograma final, respectivamente. Cuando no se proporciona ninguna, el nodo funciona únicamente a partir del prompt.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | Condicionamiento que contiene el prompt codificado y, cuando se proporcionan imágenes de fotograma clave, los fotogramas clave codificados ubicados en el primer y último fotograma del video para el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vacío que representa el video y su pista de audio correspondiente a generar, con el ancho, alto y número de fotogramas solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
