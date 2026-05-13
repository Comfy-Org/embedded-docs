> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/es.md)

Este nodo está diseñado para procesar y acondicionar datos para su uso en modelos StableZero123, enfocándose en preparar la entrada en un formato específico que sea compatible y esté optimizado para estos modelos.

## Entradas

| Parámetro             | Tipo Comfy         | Descripción |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Procesa datos visuales para alinearlos con los requisitos del modelo, mejorando la comprensión del contexto visual por parte del modelo. |
| `init_image`          | `IMAGE`            | Sirve como imagen de entrada inicial para el modelo, estableciendo la línea base para operaciones posteriores basadas en imágenes. |
| `vae`                 | `VAE`              | Integra las salidas del autoencoder variacional, facilitando la capacidad del modelo para generar o modificar imágenes. |
| `width`               | `INT`              | Especifica el ancho de la imagen de salida, permitiendo un redimensionamiento dinámico según las necesidades del modelo. |
| `height`              | `INT`              | Determina la altura de la imagen de salida, permitiendo personalizar las dimensiones de salida. |
| `batch_size`          | `INT`              | Controla la cantidad de imágenes procesadas en un solo lote, optimizando la eficiencia computacional. |
| `elevation`           | `FLOAT`            | Ajusta el ángulo de elevación para el renderizado de modelos 3D, mejorando la comprensión espacial del modelo. |
| `azimuth`             | `FLOAT`            | Modifica el ángulo acimutal para la visualización de modelos 3D, mejorando la percepción de orientación del modelo. |

## Salidas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Genera vectores de acondicionamiento positivo, ayudando al refuerzo de características positivas del modelo. |
| `negative`    | `CONDITIONING` | Produce vectores de acondicionamiento negativo, asistiendo al modelo en la evitación de ciertas características. |
| `latent`      | `LATENT`     | Crea representaciones latentes, facilitando una comprensión más profunda de los datos por parte del modelo. |