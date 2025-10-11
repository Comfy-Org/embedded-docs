> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

El nodo WanImageToVideo prepara las representaciones de condicionamiento y latentes para tareas de generación de video. Crea un espacio latente vacío para la generación de video y puede incorporar opcionalmente imágenes de inicio y salidas de visión CLIP para guiar el proceso de generación de video. El nodo modifica tanto las entradas de condicionamiento positivas como negativas en función de los datos de imagen y visión proporcionados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo para guiar la generación |
| `negative` | CONDITIONING | Sí | - | Entrada de condicionamiento negativo para guiar la generación |
| `vae` | VAE | Sí | - | Modelo VAE para codificar imágenes al espacio latente |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida (por defecto: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida (por defecto: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video (por defecto: 81, paso: 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar en un lote (por defecto: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para condicionamiento adicional |
| `start_image` | IMAGE | No | - | Imagen de inicio opcional para inicializar la generación del video |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imágenes y aplica enmascaramiento a las entradas de condicionamiento. El parámetro `clip_vision_output`, cuando se proporciona, añade condicionamiento basado en visión tanto a las entradas positivas como negativas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con datos de imagen y visión incorporados |
| `negative` | CONDITIONING | Condicionamiento negativo modificado con datos de imagen y visión incorporados |
| `latent` | LATENT | Tensor de espacio latente vacío listo para la generación de video |