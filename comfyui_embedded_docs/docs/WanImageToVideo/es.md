# WanImageToVideo

El nodo WanImageToVideo prepara representaciones de condicionamiento y latentes para la generación de video. Crea un espacio latente vacío para el video y puede incorporar opcionalmente una imagen inicial y una salida de visión CLIP para guiar la generación. Tanto las entradas de condicionamiento `positive` como `negative` se actualizan con la imagen y los datos de visión proporcionados.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positiva utilizada para guiar la generación | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativa utilizada para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `width` | Ancho del video generado (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video generado (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas del video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos que se generarán en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida de visión CLIP opcional añadida como condicionamiento adicional tanto a las entradas positiva como negativa | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Imagen inicial opcional utilizada para inicializar el video. Cuando se proporciona, se redimensiona al `width` y `height` especificados y se coloca al principio de la secuencia de fotogramas; los fotogramas más allá de `length` se ignoran. Los fotogramas restantes se rellenan con valores de gris neutro (0.5). | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, la secuencia de fotogramas se codifica con el VAE y se aplica una máscara al condicionamiento. La máscara se establece en 0 para los fotogramas cubiertos por la imagen inicial y en 1 para los fotogramas restantes, de modo que la generación continúa desde la imagen proporcionada. Durante la codificación solo se utilizan los primeros tres canales de color (RGB) de la imagen. Tanto el condicionamiento positivo como el negativo reciben la misma imagen latente concatenada, la máscara y (si se proporciona) la salida de visión CLIP.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo, actualizado con la imagen y los datos de visión | CONDITIONING |
| `negative` | Condicionamiento negativo, actualizado con la imagen y los datos de visión | CONDITIONING |
| `latent` | Tensor latente vacío listo para la generación de video, con forma [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
