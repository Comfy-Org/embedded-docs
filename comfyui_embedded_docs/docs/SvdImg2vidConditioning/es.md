> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/es.md)

Este nodo está diseñado para generar datos de condicionamiento para tareas de generación de video, específicamente adaptado para su uso con modelos SVD_img2vid. Toma diversas entradas, incluyendo imágenes iniciales, parámetros de video y un modelo VAE, para producir datos de condicionamiento que pueden utilizarse para guiar la generación de fotogramas de video.

## Entradas

| Parámetro             | Tipo Comfy        | Descripción |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Representa el modelo de visión CLIP utilizado para codificar características visuales a partir de la imagen inicial, desempeñando un papel crucial en la comprensión del contenido y contexto de la imagen para la generación de video. |
| `init_image`          | `IMAGE`            | La imagen inicial a partir de la cual se generará el video, sirviendo como punto de partida para el proceso de generación de video. |
| `vae`                 | `VAE`              | Un modelo de Autoencoder Variacional (VAE) utilizado para codificar la imagen inicial en un espacio latente, facilitando la generación de fotogramas de video coherentes y continuos. |
| `width`               | `INT`              | El ancho deseado de los fotogramas de video a generar, permitiendo personalizar la resolución del video. |
| `height`              | `INT`              | La altura deseada de los fotogramas de video, permitiendo controlar la relación de aspecto y la resolución del video. |
| `video_frames`        | `INT`              | Especifica el número de fotogramas que se generarán para el video, determinando la duración del mismo. |
| `motion_bucket_id`    | `INT`              | Un identificador para categorizar el tipo de movimiento que se aplicará en la generación del video, ayudando en la creación de videos dinámicos y atractivos. |
| `fps`                 | `INT`              | La tasa de fotogramas por segundo (fps) para el video, influyendo en la fluidez y el realismo del video generado. |
| `augmentation_level`  | `FLOAT`            | Un parámetro que controla el nivel de aumento aplicado a la imagen inicial, afectando la diversidad y variabilidad de los fotogramas de video generados. |

## Salidas

| Parámetro     | Tipo Comfy        | Descripción |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Los datos de condicionamiento positivo, que consisten en características y parámetros codificados para guiar el proceso de generación de video en una dirección deseada. |
| `negative`    | `CONDITIONING`     | Los datos de condicionamiento negativo, que proporcionan un contraste con el condicionamiento positivo, y pueden utilizarse para evitar ciertos patrones o características en el video generado. |
| `latent`      | `LATENT`           | Representaciones latentes generadas para cada fotograma del video, que sirven como componente fundamental para el proceso de generación de video. |