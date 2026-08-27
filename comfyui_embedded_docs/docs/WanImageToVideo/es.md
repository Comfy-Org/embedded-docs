# WanImageToVideo

El nodo WanImageToVideo prepara representaciones de condicionamiento y latentes para tareas de generación de video. Crea un espacio latente vacío para la generación de video y puede incorporar opcionalmente imágenes iniciales y salidas de visión CLIP para guiar el proceso de generación. El nodo modifica tanto las entradas de condicionamiento positivas como negativas según la imagen y los datos de visión proporcionados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes al espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida (predeterminado: 832, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `altura` | Altura del video de salida (predeterminado: 480, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video (predeterminado: 81, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `tamaño_del_lote` | Número de videos a generar en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_de_vision_clip` | Salida de visión CLIP opcional para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicial` | Imagen inicial opcional para iniciar la generación del video. Cuando se proporciona, la imagen se redimensiona para ajustarse al ancho y alto especificados, y los primeros fotogramas del video se inicializan a partir de esta imagen. Los fotogramas restantes se rellenan con valores de gris neutro (0.5). Los fotogramas más allá de `length` se ignoran. | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imágenes utilizando el VAE y aplica una máscara a las entradas de condicionamiento. La máscara cubre todos los fotogramas excepto los inicializados por la imagen inicial, lo que permite que la generación se base en la imagen proporcionada. Solo se utilizan los primeros tres canales de color (RGB) de la imagen al codificar. El parámetro `clip_vision_output`, cuando se proporciona, añade condicionamiento basado en visión tanto a las entradas positivas como a las negativas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo modificado con datos de imagen y visión incorporados | CONDITIONING |
| `negativo` | Condicionamiento negativo modificado con datos de imagen y visión incorporados | CONDITIONING |
| `latente` | Tensor de espacio latente vacío listo para la generación de video, con forma [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
