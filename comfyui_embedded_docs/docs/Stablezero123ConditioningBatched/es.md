# Stablezero123ConditioningBatched

Este nodo está diseñado para procesar información de condicionamiento de forma por lotes, específicamente adaptada para el modelo StableZero123. Se enfoca en manejar eficientemente múltiples conjuntos de datos de condicionamiento simultáneamente, optimizando el flujo de trabajo en escenarios donde el procesamiento por lotes es crucial.

## Entradas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `clip_vision` | Las incrustaciones visuales de CLIP que proporcionan contexto visual para el proceso de condicionamiento. | `CLIP_VISION` |
| `init_image` | La imagen inicial sobre la cual se aplica el condicionamiento, sirviendo como punto de partida para el proceso de generación. | `IMAGE` |
| `vae` | El autoencoder variacional utilizado para codificar y decodificar imágenes en el proceso de condicionamiento. | `VAE` |
| `width` | El ancho de la imagen de salida. | `INT` |
| `height` | La altura de la imagen de salida. | `INT` |
| `batch_size` | El número de conjuntos de condicionamiento a procesar en un solo lote. | `INT` |
| `elevation` | El ángulo de elevación para el condicionamiento de modelos 3D, afectando la perspectiva de la imagen generada. | `FLOAT` |
| `azimuth` | El ángulo azimutal para el condicionamiento de modelos 3D, afectando la orientación de la imagen generada. | `FLOAT` |
| `elevation_batch_increment` | El cambio incremental en el ángulo de elevación a lo largo del lote, permitiendo perspectivas variadas. | `FLOAT` |
| `azimuth_batch_increment` | El cambio incremental en el ángulo azimutal a lo largo del lote, permitiendo orientaciones variadas. | `FLOAT` |

## Salidas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | La salida de condicionamiento positivo, adaptada para promover ciertas características o aspectos en el contenido generado. | `CONDITIONING` |
| `negative` | La salida de condicionamiento negativo, adaptada para desalentar ciertas características o aspectos en el contenido generado. | `CONDITIONING` |
| `latent` | La representación latente derivada del proceso de condicionamiento, lista para pasos adicionales de procesamiento o generación. | `LATENT` |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/es.md)
