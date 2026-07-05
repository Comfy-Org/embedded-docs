# WanImageToVideo

El nodo WanImageToVideo prepara representaciones de condicionamiento y latentes para tareas de generación de video. Crea un espacio latente vacío para la generación de video y puede incorporar opcionalmente imágenes iniciales y salidas de CLIP vision para guiar el proceso de generación de video. El nodo modifica tanto las entradas de condicionamiento positivo como negativo según la imagen y los datos de visión proporcionados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes al espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | Alto del video de salida (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | Número de videos a generar en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_de_vision_clip` | Salida opcional de CLIP vision para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicial` | Imagen inicial opcional para inicializar la generación de video | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imágenes y aplica enmascaramiento a las entradas de condicionamiento. El parámetro `clip_vision_output`, cuando se proporciona, agrega condicionamiento basado en visión tanto a las entradas positivas como negativas.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con datos de imagen y visión incorporados | CONDITIONING |
| `negative` | Condicionamiento negativo modificado con datos de imagen y visión incorporados | CONDITIONING |
| `latent` | Tensor de espacio latente vacío listo para la generación de video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
