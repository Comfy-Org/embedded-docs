El nodo WanSCAILToVideo prepara el condicionamiento y un espacio latente vacío para la generación de video. Procesa entradas opcionales como imágenes de referencia, videos de pose y salidas de CLIP vision, incrustándolas en el condicionamiento positivo y negativo para un modelo de video. El nodo genera el condicionamiento modificado y un tensor latente en blanco con las dimensiones de video especificadas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo. | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar imágenes y fotogramas de video. | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 512). Debe ser divisible por 8. | INT | Sí | 32 a MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles (predeterminado: 896). Debe ser divisible por 8. | INT | Sí | 32 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas en el video (predeterminado: 81). Debe ser divisible por 4. | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | El número de videos a generar en un lote (predeterminado: 1). | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida opcional de CLIP vision para el condicionamiento. | CLIP_VISION_OUTPUT | No | - |
| `imagen_referencia` | Una imagen de referencia opcional para el condicionamiento. | IMAGE | No | - |
| `video_pose` | Video utilizado para el condicionamiento de pose. Se reducirá a la mitad de la resolución del video principal. | IMAGE | No | - |
| `fuerza_pose` | Intensidad del latente de pose (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 10.0 |
| `inicio_pose` | Paso inicial para usar el condicionamiento de pose (predeterminado: 0.0). | FLOAT | Sí | 0.0 a 1.0 |
| `fin_pose` | Paso final para usar el condicionamiento de pose (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** La entrada `pose_video` se procesa solo para los primeros `length` fotogramas. La `reference_image` se procesa solo para la primera imagen del lote. Cuando se proporciona `reference_image`, se utiliza un latente relleno de ceros del mismo tamaño para el condicionamiento negativo. Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | El condicionamiento positivo modificado, que potencialmente contiene latentes de imagen de referencia incrustados, salida de CLIP vision o latentes de video de pose. | CONDITIONING |
| `latente` | El condicionamiento negativo modificado, que potencialmente contiene latentes de imagen de referencia incrustados, salida de CLIP vision o latentes de video de pose. | CONDITIONING |
| `latent` | Un tensor latente vacío de forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/es.md)

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
