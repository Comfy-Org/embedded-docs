
Este nodo se especializa en mejorar la resolución de las imágenes a través de un proceso de aumento de 4x, incorporando elementos de condicionamiento para refinar la salida. Aprovecha técnicas de difusión para aumentar la resolución de las imágenes, permitiendo ajustes en la relación de escala y la augmentación de ruido para afinar el proceso de mejora.

## Entradas

| Parámetro            | Tipo Comfy        | Descripción |
|----------------------|--------------------|-------------|
| `images`             | `IMAGE`            | Las imágenes de entrada que se van a aumentar. Este parámetro es crucial ya que influye directamente en la calidad y resolución de las imágenes de salida. |
| `positive`           | `CONDITIONING`     | Elementos de condicionamiento positivos que guían el proceso de aumento hacia atributos o características deseadas en las imágenes de salida. |
| `negative`           | `CONDITIONING`     | Elementos de condicionamiento negativos que el proceso de aumento debe evitar, ayudando a dirigir la salida lejos de atributos o características no deseadas. |
| `scale_ratio`        | `FLOAT`            | Determina el factor por el cual se aumenta la resolución de la imagen. Una relación de escala más alta resulta en una imagen de salida más grande, permitiendo mayor detalle y claridad. |
| `noise_augmentation` | `FLOAT`            | Controla el nivel de augmentación de ruido aplicado durante el proceso de aumento. Esto puede usarse para introducir variabilidad y mejorar la robustez de las imágenes de salida. |

## Salidas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Los elementos de condicionamiento positivo refinados resultantes del proceso de aumento. |
| `negative`    | `CONDITIONING` | Los elementos de condicionamiento negativo refinados resultantes del proceso de aumento. |
| `latent`      | `LATENT`     | Una representación latente generada durante el proceso de aumento, que puede ser utilizada en procesamiento adicional o entrenamiento de modelos.
