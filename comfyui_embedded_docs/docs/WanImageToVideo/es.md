# WanImageToVideo

El nodo WanImageToVideo prepara las representaciones de condicionamiento y las representaciones latentes para tareas de generación de video. Crea un espacio latente vacío para la generación de video y puede incorporar opcionalmente imágenes iniciales y salidas de visión de CLIP para guiar el proceso de generación de video. El nodo modifica tanto las entradas de condicionamiento positivo como negativo según la imagen y los datos de visión proporcionados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positivo para guiar la generación | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativo para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes en el espacio latente | VAE | Sí | - |
| `width` | Ancho del video de salida (por defecto: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Altura del video de salida (por defecto: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas del video (por defecto: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida de visión de CLIP opcional para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Imagen inicial opcional para inicializar la generación de video. Cuando se proporciona, la imagen se redimensiona para ajustarse al ancho y la altura especificados, y los primeros fotogramas del video se inicializan a partir de esta imagen. Los fotogramas restantes se rellenan con valores de gris neutro (0.5). Solo se utilizan los primeros `length` fotogramas de la imagen. | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imágenes utilizando el VAE y aplica una máscara a las entradas de condicionamiento. La máscara cubre todos los fotogramas excepto los inicializados por la imagen inicial, lo que permite que la generación se base en la imagen proporcionada. El parámetro `clip_vision_output`, cuando se proporciona, añade condicionamiento basado en visión tanto a las entradas positivas como negativas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con los datos de imagen y visión incorporados | CONDITIONING |
| `negative` | Condicionamiento negativo modificado con los datos de imagen y visión incorporados | CONDITIONING |
| `latent` | Tensor del espacio latente vacío listo para la generación de video, con forma [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
