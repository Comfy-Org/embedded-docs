
Este nodo está diseñado para procesar y condicionar datos para su uso en modelos StableZero123, centrándose en preparar la entrada en un formato específico que es compatible y optimizado para estos modelos.

## Entradas

| Parámetro             | Tipo Comfy        | Descripción |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Procesa datos visuales para alinearlos con los requisitos del modelo, mejorando la comprensión del contexto visual por parte del modelo. |
| `init_image`          | `IMAGE`            | Sirve como la entrada de imagen inicial para el modelo, estableciendo la base para operaciones basadas en imágenes posteriores. |
| `vae`                 | `VAE`              | Integra salidas de autoencoders variacionales, facilitando la capacidad del modelo para generar o modificar imágenes. |
| `width`               | `INT`              | Especifica el ancho de la imagen de salida, permitiendo un redimensionamiento dinámico según las necesidades del modelo. |
| `height`              | `INT`              | Determina la altura de la imagen de salida, permitiendo la personalización de las dimensiones de salida. |
| `batch_size`          | `INT`              | Controla el número de imágenes procesadas en un solo lote, optimizando la eficiencia computacional. |
| `elevation`           | `FLOAT`            | Ajusta el ángulo de elevación para el renderizado del modelo 3D, mejorando la comprensión espacial del modelo. |
| `azimuth`             | `FLOAT`            | Modifica el ángulo de acimut para la visualización del modelo 3D, mejorando la percepción de orientación del modelo. |

## Salidas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Genera vectores de condicionamiento positivos, ayudando en el refuerzo de características positivas del modelo. |
| `negative`    | `CONDITIONING` | Produce vectores de condicionamiento negativos, asistiendo en la evitación de ciertas características por parte del modelo. |
| `latent`      | `LATENT`     | Crea representaciones latentes, facilitando una comprensión más profunda del modelo sobre los datos.
