# Stablezero123Conditioning

Este nodo está diseñado para procesar y acondicionar datos para su uso en modelos StableZero123, enfocándose en preparar la entrada en un formato específico que sea compatible y esté optimizado para estos modelos.

## Entradas

| Parámetro | Descripción | Tipo Comfy |
| --- | --- | --- |
| `clip_vision` | Procesa datos visuales para alinearlos con los requisitos del modelo, mejorando la comprensión del contexto visual por parte del modelo. | `CLIP_VISION` |
| `init_image` | Sirve como imagen de entrada inicial para el modelo, estableciendo la línea base para operaciones posteriores basadas en imágenes. | `IMAGE` |
| `vae` | Integra las salidas del autoencoder variacional, facilitando la capacidad del modelo para generar o modificar imágenes. | `VAE` |
| `width` | Especifica el ancho de la imagen de salida, permitiendo un redimensionamiento dinámico según las necesidades del modelo. | `INT` |
| `height` | Determina la altura de la imagen de salida, permitiendo personalizar las dimensiones de salida. | `INT` |
| `batch_size` | Controla la cantidad de imágenes procesadas en un solo lote, optimizando la eficiencia computacional. | `INT` |
| `elevation` | Ajusta el ángulo de elevación para el renderizado de modelos 3D, mejorando la comprensión espacial del modelo. | `FLOAT` |
| `azimuth` | Modifica el ángulo acimutal para la visualización de modelos 3D, mejorando la percepción de orientación del modelo. | `FLOAT` |

## Salidas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | Genera vectores de acondicionamiento positivo, ayudando al refuerzo de características positivas del modelo. | `CONDITIONING` |
| `negative` | Produce vectores de acondicionamiento negativo, asistiendo al modelo en la evitación de ciertas características. | `CONDITIONING` |
| `latent` | Crea representaciones latentes, facilitando una comprensión más profunda de los datos por parte del modelo. | `LATENT` |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/es.md)
