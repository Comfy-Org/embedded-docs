# Wan22FunControlToVideo

El nodo Wan22FunControlToVideo prepara los datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo Wan de video. Codifica imágenes de referencia opcionales y videos de control en el espacio latente, los adjunta al condicionamiento positivo y negativo, y crea un tensor latente relleno de ceros con las dimensiones espaciales y temporales correctas para el video solicitado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (por defecto: 832, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (por defecto: 480, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `duración` | Número de fotogramas en la secuencia de video (por defecto: 81, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `tamaño_lote` | Número de secuencias de video a generar (por defecto: 1) | INT | Sí | 1 a 4096 |
| `imagen_ref` | Imagen de referencia opcional que proporciona guía visual para la generación | IMAGE | No | - |
| `video_control` | Video de control opcional que guía el proceso de generación | IMAGE | No | - |

**Nota:** El parámetro `length` se procesa en pasos de 4 fotogramas, y el nodo aplica automáticamente un escalado temporal al construir el espacio latente. Cuando se proporciona `ref_image`, solo se codifica su primer fotograma y se adjunta al condicionamiento como latentes de referencia. Cuando se proporciona `control_video`, este se recorta a `length` fotogramas, se codifica y se coloca en el latente concatenado utilizado por el condicionamiento. El parámetro `start_image` se menciona en la lógica de ejecución, pero no está expuesto en el esquema de entradas del nodo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo con datos latentes específicos del video añadidos, incluidos el latente concatenado, la máscara y los latentes de referencia opcionales | CONDITIONING |
| `negativo` | Condicionamiento negativo con datos latentes específicos del video añadidos, incluidos el latente concatenado, la máscara y los latentes de referencia opcionales | CONDITIONING |
| `latente` | Tensor latente vacío preparado para la generación de video, con dimensiones según el tamaño del lote, los canales latentes, la longitud, la altura y el ancho | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/es.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
