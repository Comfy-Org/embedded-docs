> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/es.md)

Este nodo está diseñado para procesar información de condicionamiento de forma por lotes, específicamente adaptada para el modelo StableZero123. Se enfoca en manejar eficientemente múltiples conjuntos de datos de condicionamiento simultáneamente, optimizando el flujo de trabajo en escenarios donde el procesamiento por lotes es crucial.

## Entradas

| Parámetro             | Tipo de Dato | Descripción |
|----------------------|--------------|-------------|
| `clip_vision`         | `CLIP_VISION` | Las incrustaciones visuales de CLIP que proporcionan contexto visual para el proceso de condicionamiento. |
| `init_image`          | `IMAGE`      | La imagen inicial sobre la cual se aplica el condicionamiento, sirviendo como punto de partida para el proceso de generación. |
| `vae`                 | `VAE`        | El autoencoder variacional utilizado para codificar y decodificar imágenes en el proceso de condicionamiento. |
| `width`               | `INT`        | El ancho de la imagen de salida. |
| `height`              | `INT`        | La altura de la imagen de salida. |
| `batch_size`          | `INT`        | El número de conjuntos de condicionamiento a procesar en un solo lote. |
| `elevation`           | `FLOAT`      | El ángulo de elevación para el condicionamiento de modelos 3D, afectando la perspectiva de la imagen generada. |
| `azimuth`             | `FLOAT`      | El ángulo azimutal para el condicionamiento de modelos 3D, afectando la orientación de la imagen generada. |
| `elevation_batch_increment` | `FLOAT` | El cambio incremental en el ángulo de elevación a lo largo del lote, permitiendo perspectivas variadas. |
| `azimuth_batch_increment` | `FLOAT` | El cambio incremental en el ángulo azimutal a lo largo del lote, permitiendo orientaciones variadas. |

## Salidas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | La salida de condicionamiento positivo, adaptada para promover ciertas características o aspectos en el contenido generado. |
| `negative`    | `CONDITIONING` | La salida de condicionamiento negativo, adaptada para desalentar ciertas características o aspectos en el contenido generado. |
| `latent`      | `LATENT`     | La representación latente derivada del proceso de condicionamiento, lista para pasos adicionales de procesamiento o generación. |