
Este nodo está diseñado para generar datos de condicionamiento para tareas de generación de video, específicamente adaptado para su uso con modelos SVD_img2vid. Toma varias entradas, incluyendo imágenes iniciales, parámetros de video y un modelo VAE para producir datos de condicionamiento que pueden ser utilizados para guiar la generación de fotogramas de video.

## Entradas

| Parameter             | Comfy dtype        | Description (Descripción) |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Representa el modelo de visión CLIP utilizado para codificar características visuales de la imagen inicial, desempeñando un papel crucial en la comprensión del contenido y contexto de la imagen para la generación de video. |
| `init_image`          | `IMAGE`            | La imagen inicial a partir de la cual se generará el video, sirviendo como punto de partida para el proceso de generación de video. |
| `vae`                 | `VAE`              | Un modelo de Autoencoder Variacional (VAE) utilizado para codificar la imagen inicial en un espacio latente, facilitando la generación de fotogramas de video coherentes y continuos. |
| `width`               | `INT`              | El ancho deseado de los fotogramas de video a generar, permitiendo la personalización de la resolución del video. |
| `height`              | `INT`              | La altura deseada de los fotogramas de video, permitiendo el control sobre la relación de aspecto y resolución del video. |
| `video_frames`        | `INT`              | Especifica el número de fotogramas a generar para el video, determinando la longitud del video. |
| `motion_bucket_id`    | `INT`              | Un identificador para categorizar el tipo de movimiento que se aplicará en la generación de video, ayudando en la creación de videos dinámicos y atractivos. |
| `fps`                 | `INT`              | La tasa de fotogramas por segundo (fps) para el video, influyendo en la suavidad y realismo del video generado. |
| `augmentation_level`  | `FLOAT`            | Un parámetro que controla el nivel de aumento aplicado a la imagen inicial, afectando la diversidad y variabilidad de los fotogramas de video generados. |

## Salidas

| Parameter     | Comfy dtype        | Description (Descripción) |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Los datos de condicionamiento positivos, que consisten en características codificadas y parámetros para guiar el proceso de generación de video en una dirección deseada. |
| `negative`    | `CONDITIONING`     | Los datos de condicionamiento negativos, que proporcionan un contraste con el condicionamiento positivo, que puede ser utilizado para evitar ciertos patrones o características en el video generado. |
| `latent`      | `LATENT`           | Representaciones latentes generadas para cada fotograma del video, sirviendo como un componente fundamental para el proceso de generación de video. |
